from django.http import Http404
from django.http import JsonResponse
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
def details(request, obj_id):
    obj = store.get('object', obj_id)
    return render(request, 'object/details.html', {
        'object': obj,
        'revision_date': store.obj_revision_date(obj)
        })


@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    size = int(param_pop(params, 'size', 100))
    page = int(param_pop(params, 'page', 1))

    query = store.lucenify(params)
    hits = store.search('object', query, size=size, offset=(page-1)*size)
    
    return render(request, 'object/search.html', {
        'name': params.get('name', ''),
        'hits': store.hits_contents(hits),
        'pagination': store.pagination(page, size, hits.get('total')),
        'parameters': '&'.join(['{}={}'.format(k, v) for k, v in params.items()])
        })



