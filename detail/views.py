from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from glom import glom, Coalesce

import store


require_http_methods(["GET"])
def lemma_details_page(request, lemma_id):
    lemma = store.get('wlist', lemma_id)
    bibl = glom(lemma,
            Coalesce(
                (
                    ('passport.bibliography.bibliographical_text_field',
                        lambda x:x.split(';')),
                    [str.strip]),
                default=[])
            )
    return render(request, 'details/l.html', {
        'lemma': lemma,
        'bibl': bibl,
        })


