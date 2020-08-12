import os
import re
import json
from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from glom import glom, Coalesce, flatten

import store

try:
    with open(
        os.path.join(
            settings.MEDIA_ROOT,
            'link-formatters.json'
        ), 'r'
    ) as f:
        EXT_REF_FORMATTERS = json.load(f)
except Exception:
    print(
        'Could not find external reference link formatters config file {}!'.format(
            os.path.join(
                settings.MEDIA_ROOT,
                'link-formatters.json',
            )
        )
    )
    EXT_REF_FORMATTERS = {}


def tag_transcription(string):
    return re.sub(
        r'\$([^$]*)\$',
        r'<span class="bbaw-libertine">\1</span>',
        string
    )


def occurrence_count(lemma_id):
    count = store.es.count(
        index="sentence",
        body={
            "query": {
                        "term": {
                            "tokens.lemma.id": lemma_id,
                        }
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
        anno['body'] = mark_safe(tag_transcription(textcontent))
        anno['name'] = mark_safe(tag_transcription(anno.get('name', '')))
    return annos

tlaTitle = "Thesaurus Linguae Aegyptiae"
tlaVersion = "19"
tlaIssue = "beta"
tlaReleaseDate = "30.10.2019"
tlaEditor = "Berlin-Brandenburgische Akademie der Wissenschaften & Sächsische Akademie der Wissenschaften zu Leipzig"
tlaPublisher = "Berlin-Brandenburgische Akademie der Wissenschaften"
tlaBaseURL = "https://tla.bbaw.de"

def coins_openurl_kev(doc):
    # generate a contextobject referent
    # https://groups.niso.org/apps/group_public/download.php/14833/z39_88_2004_r2010.pdf
    ctx_rft = [
        ('ctx_ver', "Z39.88-2004"),
        ('ctx_enc', "info.ofi/enc:UTF-8"),
        ('ctx_tim', datetime.now().isoformat()),
        ('rft.language', "en-US"),
        ('rft.au', glom(doc, "editors.author")),
        ('rft.genre', "article"),
        ('rft.atitle', 'Lemma {} - {}'.format(
            doc.get("id"),
            doc.get("name"),
        )),
        ('rft.jtitle', tlaTitle),
        ('rft.stitle', "TLA"),
        ('rft.volume', tlaVersion),
        ('rft.issue', tlaIssue),
        ('rft.date', glom(doc, "editors.updated")),
        ('rft.place', 'Berlin'),
        ('rft.publisher', tlaPublisher),
        ('rft_val_fmt', 'info:ofi/fmt:kev:mtx:journal'),
        ('url_ver', "Z39.88-2004"),
    ]
    coins_kev = urlencode(ctx_rft)
    return coins_kev


def create_ext_ref_link(provider, url, text):
    if url:
        return '''
        <a href="{url}" target="_blank">
            <button type="button" class="btn btn-red text-left text-decoration-none">
                <span class="fas fa-arrow-circle-right"></span>
                {provider}&nbsp;
                <em>
                    {text}
                </em>
            </button>
        </a>
        '''.format(
            provider=provider,
            url=url,
            text=text,
        )
    else:
        return '''
        <span class="fas fa-arrow-circle-right"></span>{provider}&nbsp;<em>{text}</em> &emsp;
        '''.format(
            provider=provider,
            text=text,
        )


def format_ext_refs(provider, references):
    formatter = EXT_REF_FORMATTERS.get(provider)
    ext_refs = []
    for ref in references:
        if formatter:
            if 'type-formats' in formatter:
                variant = ref.get('type')
                if variant not in formatter['type-formats']:
                    variant = 'default'
                ext_refs += [
                    create_ext_ref_link(
                        provider,
                        formatter['type-formats'][variant].format(id=ref['id']),
                        ref['id']
                    )
                ]
            elif 'default-format' in formatter:
                ext_refs += [
                    create_ext_ref_link(
                        provider,
                        formatter['default-format'].format(id=ref['id']),
                        ref['id']
                    )
                ]
            else:
                ext_refs += [create_ext_ref_link(provider, None, ref['id'])]
        else:
            ext_refs += [create_ext_ref_link(provider, None, ref['id'])]
    return ext_refs


@require_http_methods(["GET"])
def lemma_details_page(request, lemma_id):
    lemma = store.get('lemma', lemma_id)
    bibl = glom(
        lemma,
        Coalesce(
            (
                (
                    'passport.bibliography.0.bibliographical_text_field.0',
                    lambda x: re.sub(r';\s*([A-Z])', r'|\1', x).split('|') # Workaround: splitten nur wenn nach ";" kein Großbuchstabe folgt
                    #lambda x: x.split(';')
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
        ] for predicate, relations in lemma.get('relations', {}).items()
    }
    return render(
        request,
        'details/lemma.html',
        {
            'lemma': lemma,
            'bibl': bibl,
            'ext': {
                provider: format_ext_refs(provider, refs)
                for provider, refs in lemma.get('externalReferences', {}).items()
            },
            'coins': coins_openurl_kev(lemma),
            'occurrences': {
                'corpus': occurrence_count(lemma_id),
            },
            'annotations': render_annotations(
                lemma_annotations(
                    lemma_id
                )
            ),
            'tlaVersion': tlaVersion,
            'tlaTitle': tlaTitle,
            'tlaVersion': tlaVersion,
            'tlaIssue': tlaIssue,
            'tlaReleaseDate': tlaReleaseDate,
            'tlaEditor': tlaEditor,
            'tlaBaseURL': tlaBaseURL,
            'dateToday': datetime.now().strftime("%d.%m.%Y"),
        }
    )
