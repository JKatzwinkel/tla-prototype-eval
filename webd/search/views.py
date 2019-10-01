import re
import json
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils.http import urlencode

from glom import glom

from .forms import (
    DictSearchForm,
    TextWordSearchForm,
)

import store
from detail import views as detail_views


RESULTS_PER_PAGE = 24

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


def build_query(*clauses, fields=None):
    """ Generates an elasticsearch query in conjunctive normal form from the
    clauses passed as parameters. You can also whitelist the ``_source`` fields to be included
    in the results.

    Negate an atomic clause by giving it a ``predicate`` field with value ``must_not``.
    """
    query = {
        "query": {
            "bool": {
                "must": [],
                "must_not": [],
            }
        }
    }
    if fields is not None and type(fields) is list:
        query["_source"] = fields
    for clause in clauses:
        if type(clause) is dict:
            predicate = clause.pop('predicate', 'must')
            query['query']['bool'][predicate].append(clause)
        elif type(clause) is list:
            query['query']['bool']['must'].append(
                {
                    'bool': {
                        'should': clause
                    }
                }
            )
    return query


def dict_search_query(**params):
    """ generate elasticsearch query object with parameters as would be expected to come from
    the `dict-search` form in the `search/index.html` template. """
    q = {"query": {"bool": {"must": [], "must_not": [], "should": []}}}
    clauses = []
    if 'transcription' in params:
        transcription = params.get('transcription')[0] if type(
            params.get('transcription')) == list else params.get('transcription')
        if len(transcription.strip()) > 0:
            clauses.append(
                {
                    "match_phrase_prefix": {
                        "name": transcription,
                    }
                }
            )
            clauses.append(
                {
                    "term": {
                        "name": transcription,
                    }
                }
            )
    if 'script' in params:
        if ('h' in params.get('script')) ^ ('d' in params.get('script')):
            query = {
                "prefix": {
                    "id": "d"
                }
            }
            query['predicate'] = 'must' if 'd' in params.get('script') else 'must_not'
            clauses.append(query)
    if 'translation' in params:
        clauses.append(
            [
                {
                    "match": {
                        "translations.{}".format(lang): params.get('translation')[0]
                    }
                }
                for lang in params.get('lang', ['de'])
            ]
        )
    q = build_query(*clauses)
    print(q)
    return q


def textword_search_query(**params):
    """ generate elasticsearch query from parameters passed over by a
    :class:`forms.TextWordSearchForm`.
    """
    clauses = []
    if 'lemma' in params:
        clauses.append(
            [
                {
                    'term': {
                        'lemma': lemma
                    }
                }
                for lemma in params['lemma']
                if len(lemma.strip()) > 0
            ]
        )
    if 'translation' in params:
        if len(params.get('translation')[-1]) > 0:
            clauses.append(
                [
                    {
                        'match': {
                            'translations.{}'.format(lang): params.get('translation')[-1]
                        }
                    }
                    for lang in params.get('trans_lang', [])
                ]
            )
    if 'hieroglyphs' in params:
        if len(params.get('hieroglyphs')[-1]) > 0:
            glyphs = params.get('hieroglyphs')[-1]
            for glyph in re.split(r'[ :*-]', glyphs):
                clauses.append(
                    {
                        'match': {
                            'glyphs': glyph
                        }
                    }
                )
    q = build_query(*clauses)
    print(q)
    return q


def search_textword_occurrences(offset=1, size=RESULTS_PER_PAGE, **params):
    """ builds queries according to the parameters obtained from the :class:`forms.TextWordSearchForm` textword occurrence search form.
    Passes the final occurrence query to function :meth:`store.search` an returns the results.

    :rtype: list
    """
    passport_value = params.get('passport_0', [''])[-1]
    objects = None
    if passport_value is not None and len(passport_value.strip()) > 0:
        objects_query = build_query(
            {
                "match": {
                    params.get('passport_1')[-1]: passport_value,
                }
            },
            fields=['id'],
        )
        objects = [
            hit['_source']['id']
            for hit in store.scroll(
                'object',
                objects_query
            )
        ]
        if len(objects) < 1:
            print('no matching objects. so long!')
            return {}
    texts = None
    if objects is not None or len(params.get('textname', [''])[-1].strip()) > 0:
        clauses = []
        if params.get('textname') and len(params.get('textname')[-1].strip()) > 0:
            clauses.append(
                {
                    'match': {
                        'name': params.get('textname')[-1]
                    }
                }
            )
        if objects:
            clauses.append(
                {
                    'terms': {
                        'relations.partOf.id': list(map(str.lower, objects))
                    }
                }
            )
        texts_query = build_query(*clauses, fields=['id'])
        texts = [
            hit['_source']['id']
            for hit in store.scroll(
                'text',
                texts_query
            )
        ]
        with open('text_query.json', 'w+') as f:
            json.dump(texts_query, f, indent=1)
        if len(texts) < 1:
            print('no matching texts. bye!')
            return {}
    occurrences = []
    occurrences_query = textword_search_query(**params)
    if texts:
        occurrences_query['query']['bool']['must'].append(
            {
                'terms': {
                    'text': list(map(str.lower, texts))
                }
            }
        )
    with open('occurrence_query.json', 'w+') as f:
        json.dump(occurrences_query, f, ensure_ascii=False, indent=1)
    hits = store.search(
        'occurrence',
        occurrences_query,
        offset=offset,
        size=size,
    )
    return hits


def populate_textword_occurrences(hits, **params):
    """ take text word search results and the original search parameters and
    enrich the results with like highlighting and stuff.

    :rtype: list
    """
    occurrences = []
    filters = {
        k: params.get(k) for k in ["lemma", "transcription", "hieroglyphs"]
    }
    for hit in hits:
        sentence = store.get(
            'sentence',
            hit.get('sentence')
        )
        for i, token in enumerate(sentence['tokens']):
            if token.get('id') == hit['token']:
                token['highlight'] = 1
            else:
                match = True
                for k, vv in filters.items():
                    if vv:
                        match = match and any(
                            map(
                                lambda v: token.get(k) == v,
                                vv
                            )
                        )
                if 'translation' in filters:
                    match = match and any(
                        map(
                            lambda l: any(
                                map(
                                    lambda t: t in filters.get('translations').get(l, "").lower(),
                                    filters.get('trans_lang', [])
                                )
                            ),
                            filters.get('translation')
                        )
                    )
                if match:
                    token['highlight'] = 2
        text = store.get(
            'text',
            hit.get('text'),
        )
        if text:
            print('text id', text['id'])
            for path in text.get('paths', []):
                for node in path:
                    node["url"] = "/view/{}/{}".format(
                        {
                            "BTSTCObject": "object",
                            "BTSText": "text",
                        }.get(node.get('eclass')),
                        node['id']
                    )
            occurrences.append(
                {
                    "occurrence": hit,
                    "sentence": sentence,
                    "text": text,
                }
            )
        else:
            print('text not found: ', hit["text"])
    return occurrences


def hit_tree(hits):
    """ extracts the implicit hierarchical structure among the given objects """
    for hit in hits:
        hit["occurrences"] = detail_views.occurrence_count(
            hit.get('id')
        )
    structure = {
        h.get('id'): (hits.index(h), h)
        for h in hits
    }
    res = []

    def nest(hit, indent=0, pred=None):
        if hit.get('id') in structure:
            structure.pop(hit.get('id'))
        else:
            return
        hit['bibliography'] = glom(
            hit,
            'passport.bibliography.0.bibliographical_text_field.0',
            default=''
            )
        """ append hit to result list (represented as tuple containing indentation and rel type """
        res.append((indent, pred, hit))
        """ generate list of (id,relationtype) tuples representing the search results which
        are directly related to the current search result while preseving order """
        related_hit_ids = sorted([
            (hid.get('id'), pred)
            for pred in [
                'rootOf',
                'referencing',
                'successor',
                'referencedBy',
                'composedOf'
                'predecessor',
                'composes',
                'partOf'
            ]
            for hid in hit.get('relations', {}).get(pred, [])
            if hid.get('id') in structure],
            key=lambda t: structure.get(t[0])[0]
        )
        for hid, pred in related_hit_ids:
            if hid in structure:
                _, obj = structure.get(hid)
                nest(obj, indent=indent + 1, pred=pred)

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
            'passport_fields': filter(
                lambda property: property.startswith('passport') and property.endswith('id'),
                store.get_mappings('object')
            )
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
        if i < 3 or i > lastpageno - 2 or (i - page)**2 < 3:
            if len(pages) > 1:
                if type(pages[-1][0]) is int and pages[-1][0] < i - 1:
                    pages.append(('...', None))
            pages.append((i, href.format(i)))
    return pages


def request_url_without_page(request):
    url = request.get_full_path()
    page = int(request.GET.get('page', 1))
    if 'page=' in url:
        url = url.replace('page={}'.format(page), '')
    return url

#### Doppelung aus webd/details/views.py unschön
tlaTitle = "Thesaurus Linguae Aegyptiae"
tlaVersion = "19"
tlaIssue = "1"
tlaReleaseDate = "30.10.2019"
tlaEditor = "Berlin-Brandenburgische Akademie der Wissenschaften & Sächsische Akademie der Wissenschaften"
tlaPublisher = "Berlin-Brandenburgische Akademie der Wissenschaften"
tlaBaseURL = "http://tla.bbaw.de"


@require_http_methods(["GET"])
def search_dict(request):
    params = request.GET.copy()
    page = int(params.get('page', 1))
    offset = (page - 1) * RESULTS_PER_PAGE
    hits = store.search(
        'wlist',
        dict_search_query(**params),
        offset=offset,
        size=RESULTS_PER_PAGE,
    )
    count = hits.get('total')
    hits = store.hits_contents(hits)
    hits = hit_tree(hits)
    return render(
        request,
        'search/dict.html',
        {
            'params': params,
            'hits': hits,
            'hitcount': count,
            'page': page,
            'start': offset + 1,
            'end': min(count, offset + RESULTS_PER_PAGE),
            'pagination': pagination(request, count),
            'tlaVersion': tlaVersion,
            'tlaTitle': tlaTitle,
            'tlaVersion': tlaVersion,
            'tlaIssue': tlaIssue,
            'tlaReleaseDate': tlaReleaseDate,
            'tlaEditor': tlaEditor,
            'tlaBaseURL': tlaBaseURL,
            #'dateToday': datetime.now().strftime("%d.%m.%Y"),
        }
    )


@require_http_methods(["GET"])
def search_text_words(request):
    params = request.GET.copy()
    page = int(params.get('page', 1))
    offset = (page - 1) * RESULTS_PER_PAGE
    #form = TextWordSearchForm(request.GET)
    print(params)
    hits = search_textword_occurrences(
        offset=offset,
        size=RESULTS_PER_PAGE,
        **params,
    )
    count = hits.get('total', 0)
    hits = store.hits_contents(hits)
    hits = populate_textword_occurrences(hits, **params)
    return render(
        request,
        'search/occurrences.html',
        {
            'params': params,
            'hits': hits,
            'hitcount': count,
            'start': offset + 1,
            'end': min(count, offset + RESULTS_PER_PAGE),
            'pagination': pagination(request, count),
            'url': request_url_without_page(request),
            'tlaVersion': tlaVersion,
            'tlaTitle': tlaTitle,
            'tlaVersion': tlaVersion,
            'tlaIssue': tlaIssue,
            'tlaReleaseDate': tlaReleaseDate,
            'tlaEditor': tlaEditor,
            'tlaBaseURL': tlaBaseURL,
            #'dateToday': datetime.now().strftime("%d.%m.%Y"),
        }
    )
