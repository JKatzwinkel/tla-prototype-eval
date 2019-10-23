import re
from datetime import datetime

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils.http import urlencode

from glom import glom, Coalesce, flatten

import store
    
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
        ('rft.au', glom(doc, "edited.name")),
        ('rft.genre', "article"),
        ('rft.atitle', 'Lemma {} - {}'.format(
            doc.get("id"),
            doc.get("name"),
        )),
        ('rft.jtitle', tlaTitle),
        ('rft.stitle', "TLA"),
        ('rft.volume', tlaVersion),
        ('rft.issue', tlaIssue),
        ('rft.date', glom(doc, "edited.date")),
        ('rft.place', 'Berlin'),
        ('rft.publisher', tlaPublisher),
        ('rft_val_fmt', 'info:ofi/fmt:kev:mtx:journal'),
        ('url_ver', "Z39.88-2004"),
    ]
    coins_kev = urlencode(ctx_rft)
    return coins_kev

@require_http_methods(["GET"])
def introduction(request):
    params = request.GET.copy()
    return render(
        request,
        'info/introduction.html',
        {
        }
    )
    
@require_http_methods(["GET"])
def project(request):
    params = request.GET.copy()
    return render(
        request,
        'info/project.html',
        {
        }
    )
    
@require_http_methods(["GET"])
def collaboration(request):
    params = request.GET.copy()
    return render(
        request,
        'info/collaboration.html',
        {
        }
    )    
    
@require_http_methods(["GET"])
def licence(request):
    params = request.GET.copy()
    return render(
        request,
        'info/license.html',
        {
            'tlaVersion': tlaVersion,
            'tlaTitle': tlaTitle,
            'tlaVersion': tlaVersion,
            'tlaIssue': tlaIssue,
            'tlaReleaseDate': tlaReleaseDate,
            'tlaEditor': tlaEditor,
            'tlaBaseURL': tlaBaseURL
        }
    )
    
@require_http_methods(["GET"])
def dictionary(request):
    params = request.GET.copy()
    return render(
        request,
        'info/dictionary.html',
        {
        }
    )
        
@require_http_methods(["GET"])
def textCorpus(request):
    params = request.GET.copy()
    return render(
        request,
        'info/text-corpus.html',
        {
        }
    )
        
@require_http_methods(["GET"])
def extras(request):
    params = request.GET.copy()
    return render(
        request,
        'info/extras.html',
        {
        }
    ) 