from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from glom import glom, Coalesce

import store

def occurence_count(lemma_id):
    count = store.es.count(
        index="occurence",
        doc_type="occurence",
        body={
            "query": {
                "term": {
                    "lemma": lemma_id,
                },
            }
        }
    ).get('count', 0)
    return count


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
    return render(
        request,
        'details/l.html',
        {
            'lemma': lemma,
            'bibl': bibl,
            'occurences': {
                'corpus': occurence_count(lemma_id),
            }
        }
    )


