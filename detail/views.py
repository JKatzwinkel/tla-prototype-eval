from django.shortcuts import render
from django.views.decorators.http import require_http_methods


import store


require_http_methods(["GET"])
def lemma_details_page(request, lemma_id):
    lemma = store.get('wlist', lemma_id)
    return render(request, 'details/lemma.html', {
        'lemma': lemma,
        })


