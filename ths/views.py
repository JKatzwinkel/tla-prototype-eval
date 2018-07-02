from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

import store


@require_http_methods(["GET"])
def details(request, thsobj_id):
    thsobj = store.get('ths', thsobj_id)
    return render(request, 'ths/details.html', {
        'obj': thsobj
        })


@require_http_methods(["GET"])
def search(request):
    return render(request, 'ths/search.html', {})


