from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

import store


def param_pop(params, key, default):
    values = params.pop(key, [default])
    if len(values) < 2:
        return values[0]
    else:
        return values


@require_http_methods(["GET"])
def details(request, thsobj_id):
    thsobj = store.get('ths', thsobj_id)
    return render(request, 'ths/details.html', {
        'revision_date': store.obj_revision_date(thsobj),
        'obj': thsobj
        })


@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    size = int(param_pop(params, 'size', 100))
    page = int(param_pop(params, 'page', 1))
            
    query = store.lucenify(params)
    hits = store.search('ths', query, size=size, offset=(page-1)*size)

    for hit in hits.get('hits', []):
        hit.get('_source')['score'] = hit.get('_score')
    results = [hit.get('_source') for hit in hits.get('hits', [])]

    return render(request, 'ths/search.html', {
        'name': params.get('name', ''),
        'hits': results,
        'pagination': store.pagination(page, size, hits.get('total')),
        'parameters': '&'.join(['{}={}'.format(k, v) for k, v in params.items()])
        })


