from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

import store

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
    return JsonResponse(params, safe=False)



