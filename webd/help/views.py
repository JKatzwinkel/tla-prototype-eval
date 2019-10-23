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
tlaBaseURL = "http://tla.bbaw.de"
testHiero = "A1*-A2-<h3-Q3:X1-V28-D28-h0>-\"lb\"-<h0-Q3:X1:\"var\"-V28-D28-\"var\"-h3>-[(-A1-)]-<h1-Q3:X1-V28-['-D28-']-h0>-<h1-Q3:X1-V28-D28-h0>-\"lb\"-<0-2>-<0-2>-<1-0>-<h0-h3>-\"dtr\"-<h1-h0>-<h0-h1>-<h1-h0>-I9-\"mutil\"-I9"
#"<h3-p:t-H-kA-h0>-\"lb\"-<h0-p:t:\"var\"-H-kA-\"var\"-h3>-<h1-p:t-H-['-kA-']-h0>-<h1-p:t-H-kA-h0>-\"lb\"-<0->-<0-2>-<-0>-<1-0>-<h0-h3>-\"dtr\"-<h-h0>-<h0-h1>-<h1-h0>-f-\"mutil\"-f" #"g**f{{267,603,100}}-g:(d*t)-A1\\R230-A1\\50-A1\\r2-A1\\t3-<-G1->-<-A1->-[[-]]-[&-&]-[{-}]-['-']-o-O-A1-<1-ra-mn:n-//-0>-//-<0-mn:n-xpr-2>-<0-//-mn:n-//-0>-<1-0>-mn:n-xpr-<0-2>-<S-nTr-xpr-w->-<s1-nTr-xpr-w-s0>-//-//-<s0-xpr-w-s2>-<h-p:t-H-kA-h>-<h1-p:t-H-kA-h3>-<h1-p:t-H-kA-h>-<h3-p:t-H-kA-h1>-<h2-p:t-H-kA-h1>-<h-p:t-H-kA-h>-<h0-p:t-H-kA-h3>-<h0-p:t-H-kA-h>-<h0-p:t-H-kA-h1>-<h0-p:t-H-kA-h1>-<h-p:t-H-kA-h>-<h1-p:t-H-kA-h0>-<h1-p:t-H-kA-h0>-<h3-p:t-H-kA-h0>-<h2-p:t-H-kA-h0>"

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
def help(request):
    params = request.GET.copy()
    return render(
        request,
        'help/help.html',
        {
        'testHiero': testHiero,
        }
    )

@require_http_methods(["GET"])
def BTSglossings(request):
    params = request.GET.copy()
    return render(
        request,
        'help/BTS-glossings.html',
        {
        }
    )
    
@require_http_methods(["GET"])
def lingGlossings(request):
    params = request.GET.copy()
    return render(
        request,
        'help/ling-glossings.html',
        {
        }
    )
    
@require_http_methods(["GET"])
def helpSearch(request):
    params = request.GET.copy()
    return render(
        request,
        'help/help-search.html',
        {
        }
    )
    
@require_http_methods(["GET"])
def helpDict(request):
    params = request.GET.copy()
    return render(
        request,
        'help/help-dict.html',
        {
        }
    )
    
@require_http_methods(["GET"])
def helpLemma(request):
    params = request.GET.copy()
    return render(
        request,
        'help/help-lemma.html',
        {
        }
    )
    
@require_http_methods(["GET"])
def helpOccurences(request):
    params = request.GET.copy()
    return render(
        request,
        'help/help-occurences.html',
        {
        }
    )
    
    