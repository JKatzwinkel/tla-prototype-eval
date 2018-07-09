from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


import store




def word_glyphs(lemma):
    word_glyphs = []
    if lemma:
        for word in lemma.get('words', []):
            word_glyphs.append(
                    '-'.join([e.get('code') for e in word.get('graphics', [])]))
    return word_glyphs



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
        obj = store.get('lemma', object_id)
        objects.append({
            "id": object_id,
            "name": store.resolve_name('lemma', obj=obj),
            "glyphs": word_glyphs(obj)})
        res[predicate] = objects
    return res



@require_http_methods(["GET"])
def details(request, lemma_id):
    lemma = store.get('lemma', lemma_id)
    return render(request, 'lemma/details.html', {
                'lemma': lemma,
                'word_glyphs': word_glyphs(lemma),
                'revision_date': store.obj_revision_date(lemma),
                'lemma_bibliography': lemma_bibliography(lemma),
                'lemma_relations': lemma_relations(lemma),
                })


@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    size = int(params.pop('size', [100])[0])
    page = int(params.pop('page', [1])[0])

    query = store.lucenify(params)
    hits = store.search('lemma', query, size=size, offset=(page-1)*size)

    for hit in hits.get('hits', []):
        hit.get('_source')['score'] = hit.get('_score')
        hit.get('_source')['word_glyphs'] = word_glyphs(hit.get('_source'))
        hit.get('_source')['bib'] = lemma_bibliography(hit.get('_source'))
    results = [hit.get('_source') for hit in hits.get('hits', [])]

    return render(request, 'lemma/search.html', {
        'name': params.get('name', ''),
        'hits': results,
        'pagination': store.pagination(page, size, hits.get('total')),
        'parameters': '&'.join(['{}={}'.format(k, v) for k, v in params.items()])
        })

