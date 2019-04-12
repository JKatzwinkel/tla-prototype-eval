from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

import store

@require_http_methods(["GET"])
def index(request):
    return render(request, 'index.html')


@require_http_methods(["GET"])
def es_search(request, index, query):
    return JsonResponse(
            store.search(index, query),
            safe=False)


@require_http_methods(["GET"])
def es_get(request, index, _id):
    return JsonResponse(
            store.get(index, _id),
            safe=False)

