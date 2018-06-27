from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


import store


def resolve_name(lemma_id=None, lemma=None):
    lemma = lemma or store.get_lemma(lemma_id)
    if lemma:
        return lemma.get('name')
    else:
        print('lemma id does not exist: {}'.format(lemma_id))
        return lemma_id

def word_glyphs(lemma):
    word_glyphs = []
    for word in lemma.get('words', []):
        word_glyphs.append(
                '-'.join([e.get('code') for e in word.get('graphics', [])]))
    return word_glyphs


def revision_date(lemma):
    return lemma.get('revisions', [])[-1].split('@')[1]


def lemma_bibliography(lemma):
    return [bibentry.get('value')
            for entry_group in lemma.get('passport', {}).get('children', [])
            for bibentry in entry_group.get('children', [])
            if entry_group.get('type') == 'bibliography']

def lemma_relations(lemma):
    res = {}
    for relation in lemma.get('relations', []):
        object_id = relation.get('objectId')
        predicate = relation.get('type')
        objects = res.get(predicate, [])
        obj = store.get_lemma(object_id)
        objects.append({
            "id": object_id,
            "name": resolve_name(lemma=obj),
            "glyphs": word_glyphs(obj)})
        res[predicate] = objects
    return res



@require_http_methods(["GET"])
def details(request, lemma_id):
    lemma = store.get_lemma(lemma_id)
    return render(request, 'lemma/detail.html', {
                'lemma': lemma,
                'word_glyphs': word_glyphs(lemma),
                'revision_date': revision_date(lemma),
                'lemma_bibliography': lemma_bibliography(lemma),
                'lemma_relations': lemma_relations(lemma),
                })


@require_http_methods(["GET"])
def search(request):
    query=' '.join(['{}:{}'.format(k, v) for k, v in request.GET.items()])
    print(query)
    hits = store.search_lemma(query)
    for hit in hits:
        hit.get('_source')['score'] = hit.get('_score')
        hit.get('_source')['word_glyphs'] = word_glyphs(hit.get('_source'))
        hit.get('_source')['bib'] = lemma_bibliography(hit.get('_source'))
    hits = [hit.get('_source') for hit in hits]

    print(hits)
    return render(request, 'lemma/search.html', {
        'name': request.GET.get('name'),
        'hits': hits
        })

