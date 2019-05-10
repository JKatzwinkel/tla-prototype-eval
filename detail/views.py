import re
from datetime import datetime

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils.http import urlencode

from glom import glom, Coalesce, flatten

import store


def tag_transcription(string):
    return re.sub(
        r'\$([^$]*)\$',
        r'<span class="bbaw-libertine">\1</span>',
        string
    )


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


def lemma_annotations(lemma_id):
    """ find a lemma's annotations in es """
    hits = store.search(
        'annotation',
        'relations.partOf.id:{}'.format(lemma_id),
        size=100,
    )
    return store.hits_contents(hits)


def render_annotations(annos):
    for anno in annos:
        textcontent = '\n'.join(
            glom(
                anno,
                Coalesce(
                    (
                        (
                            'passport.annotation',
                            [
                                'lemma',
                            ]
                        ),
                        flatten
                    ),
                    default=[],
                )
            )
        )
        textcontent = re.sub(
            r'\n',
            '<br/>',
            textcontent
        )
        anno['body'] = tag_transcription(textcontent)
        anno['title'] = tag_transcription(anno['title'])
    return annos


def coins_openurl_kev(doc):
    # generate a contextobject referent
    # https://groups.niso.org/apps/group_public/download.php/14833/z39_88_2004_r2010.pdf
    ctx_rft = [
        ('ctx_ver', "Z39.88-2004"),
        ('ctx_enc', "info.ofi/enc:UTF-8"),
        ('ctx_tim', datetime.now().isoformat()),
        ('rft.language', "en-US"),
        ('rft.au', glom(doc, "edited.name")),
        ('rft.genre', "article"),
        ('rft.atitle', 'Lemma {} - {}'.format(
            doc.get("id"),
            doc.get("name"),
        )),
        ('rft.jtitle', "Thesaurus Linguae Aegyptiae"),
        ('rft.stitle', "TLA"),
        ('rft.volume', "19"),
        ('rft.issue', "1"),
        ('rft.date', glom(doc, "edited.date")),
        ('rft.place', 'Berlin'),
        ('rft.publisher', 'Berlin-Brandenburgische Akademie der Wissenschaften'),
        ('rft_val_fmt', 'info:ofi/fmt:kev:mtx:journal'),
        ('url_ver', "Z39.88-2004"),
    ]
    coins_kev = urlencode(ctx_rft)
    return coins_kev


@require_http_methods(["GET"])
def lemma_details_page(request, lemma_id):
    lemma = store.get('wlist', lemma_id)
    bibl = glom(
        lemma,
        Coalesce(
            (
                (
                    'passport.bibliography.0.bibliographical_text_field.0',
                    lambda x: x.split(';')
                ),
                [str.strip]
            ),
            default=[]
        )
    )
    lemma['relations'] = {
        predicate: [
            relation
            for relation in relations
            if relation.get('eclass') == 'BTSLemmaEntry'
        ] for predicate, relations in lemma['relations'].items()
    }
    return render(
        request,
        'details/lemma.html',
        {
            'lemma': lemma,
            'bibl': bibl,
            'coins': coins_openurl_kev(lemma),
            'occurences': {
                'corpus': occurence_count(lemma_id),
            },
            'annotations': render_annotations(
                lemma_annotations(
                    lemma_id
                )
            ),
        }
    )
