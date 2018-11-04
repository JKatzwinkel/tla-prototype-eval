from django.shortcuts import render
from django.views.decorators.http import require_http_methods

import store

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
    q = {"query": {"bool": {"must": []}}}
    if 'transcription' in params:
        q['query']['bool']['must'].append(
            {
                "match": {
                    "name": params.get('transcription')[0]
                    }
                })
    return q


def hit_tree(hits):
    """ extracts the implicit hierarchical structure among the given objects """
    structure = {h.get('id'):h for h in hits}
    res = []
    while len(hits) > 0:
        h = hits.pop(0)
        res.append((range(0), None, h))
        for pred in ['rootOf', 'successor']:
            for rel in h.get('relations', {}).get(pred, []):
                if rel.get('id') in structure:
                    obj = hits.pop(
                            hits.index(
                                structure.get(rel.get('id'))
                                )
                            )
                    res.append((range(1), pred, obj))
    return res


@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    return render(request, 'search/index.html',
            {
                'word_classes': WORD_CLASSES,
                }
            )


@require_http_methods(["GET"])
def search_dict(request):
    params = request.GET.copy()
    hits = store.search('wlist',
            dict_search_query(**params),
            offset=params.get('start', 1)-1,
            size=15
            )
    count = hits.get('total')
    hits = store.hits_contents(hits)
    hits = hit_tree(hits)
    return render(request, 'search/dict.html',
            {
                'hits': hits,
                'hitcount': count,
                'start': params.get('start', 1),
                'end': min(count, params.get('start', 1)+14),
                })


# Create your views here.
