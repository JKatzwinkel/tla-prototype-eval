from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import (
    DictSearchForm,
    TextWordSearchForm,
)

import store

RESULTS_PER_PAGE = 15

WORD_CLASSES = {
        "substantive": [
          "substantive_masc",
          "substantive_fem"],
        "particle": [
          "particle_enclitic",
          "particle_nonenclitic"],
        "root": [
          "substantive_fem"],
        "pronoun": [
          "personal_pronoun",
          "demonstrative_pronoun",
          "interrogative_pronoun",
          "relative_pronoun"],
        "numeral": [
          "cardinal",
          "ordinal"],
        "adverb": [
          "prepositional_adverb"],
        "preposition": None,
        "adjective": [
          "nisbe_adjective_preposition",
          "nisbe_adjective_substantive"],
        "epitheton_title": [
          "epith_king",
          "epith_god",
          "title"],
        "entity_name": [
          "place_name",
          "org_name",
          "person_name",
          "animal_name",
          "gods_name",
          "artifact_name",
          "kings_name"],
        "undefined": [
          "gods_name",
          "substantive_masc"],
        "verb": [
          "verb_caus_3-inf",
          "verb_5-inf",
          "verb_3-lit",
          "verb_3-inf",
          "verb_6-lit",
          "verb_caus_3-gem",
          "verb_5-lit",
          "verb_2-gem",
          "verb_caus_4-lit",
          "verb_caus_2-gem",
          "verb_4-lit",
          "verb_caus_5-lit",
          "verb_caus_3-lit",
          "verb_3-gem",
          "verb_caus_2-lit",
          "verb_irr",
          "verb_4-inf",
          "verb_caus_4-inf",
          "verb_2-lit"],
        "interjection": None}


def dict_search_query(**params):
    """ generate elasticsearch query object with parameters as would be expected to come from
    the `dict-search` form in the `search/index.html` template. """
    q = {"query": {"bool": {"must": [], "must_not": [], "should": []}}}
    if 'transcription' in params:
        transcription = params.get('transcription')[0] if type(
                params.get('transcription')) == list else params.get('transcription')
        q['query']['bool']['must'].extend([
            {
                "match_phrase_prefix": {
                    "name": transcription,
                    }
                },
            ])
        q['query']['bool']['should'].extend([
            {
                "term": {
                    "name": transcription,
                    }
                }
            ])
    if 'script' in params:
        if ('h' in params.get('script')) ^ ('d' in params.get('script')):
            query = {
                        "prefix": {
                            "id": "d"
                            }
                        }
            pred = 'must' if 'd' in params.get('script') else 'must_not'
            q['query']['bool'][pred].append(query)
    if 'translation' in params:
        for lang in params.get('lang', ['de']):
            q['query']['bool']['must'].append(
                    {
                        "match": {
                            "translations.{}".format(lang): params.get('translation')[0]
                            }
                        })


    return q


def hit_tree(hits):
    """ extracts the implicit hierarchical structure among the given objects """
    structure = {h.get('id'): (hits.index(h), h)
            for h in hits}
    res = []
    def nest(hit, indent=0, pred=None):
        if hit.get('id') in structure:
            structure.pop(hit.get('id'))
        else:
            return
        """ append hit to result list (represented as tuple containing indentation and rel type """
        res.append((range(indent), pred, hit))
        """ generate list of (id,relationtype) tuples representing the search results which
        are directly related to the current search result while preseving order """
        related_hit_ids = sorted([
                (hid.get('id'),
                    pred) for pred in [
                    'rootOf', 'successor', 'referencedBy', 'composedOf'
                    ] for hid in hit.get('relations', {}).get(
                        pred, []) if hid.get('id') in structure],
                    key = lambda t: structure.get(t[0])[0])
        for hid, pred in related_hit_ids:
            if hid in structure:
                _, obj = structure.get(hid)
                nest(obj, indent=indent+1, pred=pred)

    while len(hits) > 0:
        hit = hits.pop(0)
        nest(hit)

    return res


@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    return render(
        request,
        'search/index.html',
        {
            'word_classes': WORD_CLASSES,
            'dictform': DictSearchForm(),
            'textwordform': TextWordSearchForm(),
        }
    )


def pagination(request, hitcount):
    page = int(request.GET.get('page', 1))
    if 'page' in request.get_full_path():
        href = request.get_full_path().replace('page={}'.format(page), 'page={}')
    else:
        href = request.get_full_path() + '&page={}'
    lastpageno = hitcount // RESULTS_PER_PAGE + 2
    pages = []
    for i in range(1, lastpageno):
        if i < 3 or i > lastpageno-2 or (i-page)**2<3:
            if len(pages) > 1:
                if type(pages[-1][0]) is int and pages[-1][0] < i - 1:
                    pages.append(('...', None))
            pages.append((i, href.format(i)))
    return pages



@require_http_methods(["GET"])
def search_dict(request):
    params = request.GET.copy()
    page = int(params.get('page', 1))
    offset = (page - 1) * RESULTS_PER_PAGE
    hits = store.search('wlist',
            dict_search_query(**params),
            offset=offset,
            size=RESULTS_PER_PAGE,
            )
    count = hits.get('total')
    hits = store.hits_contents(hits)
    hits = hit_tree(hits)
    return render(request, 'search/dict.html',
            {
                'hits': hits,
                'hitcount': count,
                'page': page,
                'start': offset+1,
                'end': min(count, offset+RESULTS_PER_PAGE),
                'pagination': pagination(request, count),
                })


# Create your views here.
