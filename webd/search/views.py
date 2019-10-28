import re
import json
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils.http import urlencode

from glom import glom

from .forms import (
    DictSearchForm,
    TextWordSearchForm,
)

import store
from detail import views as detail_views

# zu Testzwecken erhöht
RESULTS_PER_PAGE = 100 # 24 

WORD_CLASSES = {
    "adjective": [
        "nisbe_adjective_preposition",
        "nisbe_adjective_substantive"],
    "adverb": [
        "prepositional_adverb"],
    "entity_name": [
        "artifact_name",
        "animal_name",
        "gods_name",
        "kings_name",
        "org_name",
        "person_name",
        "place_name"],
    "interjection": None,
    "substantive": [
        "substantive_masc",
        "substantive_fem"],
    "numeral": [
        "cardinal",
        "ordinal"],
    "particle": [
        "particle_enclitic",
        "particle_nonenclitic"],
    "preposition": None,
    "pronoun": [
        "demonstrative_pronoun",
        "interrogative_pronoun",
        "personal_pronoun",
        "relative_pronoun"],
    "root": None,
    "epitheton_title": [
        "title",
        "epith_god",
        "epith_king"],
    "verb": [
        "verb_2-lit",
        "verb_3-lit",
        "verb_4-lit",
        "verb_5-lit",
        "verb_6-lit",
        "verb_2-gem",
        "verb_3-gem",
        "verb_3-inf",
        "verb_4-inf",
        "verb_5-inf",
        "verb_caus_2-lit",
        "verb_caus_3-lit",
        "verb_caus_4-lit",
        "verb_caus_5-lit",
        "verb_caus_2-gem",
        "verb_caus_3-gem",
        "verb_caus_3-inf",
        "verb_caus_4-inf",
        "verb_irr"],
    "undefined": None,
    }

SORT_ORDERS = {
    "alph_asc": "Alphabetical (asc.)",
    "alph_desc": "Alphabetical (desc.)",
    "time_begin": "Attestation time, start",
    "time_end": "Attestation time, end",
    "root_asc": "Root",
}


def build_query(*clauses, fields=None):
    """ Generates an elasticsearch query in conjunctive normal form from the
    clauses passed as parameters. You can also whitelist the ``_source`` fields to be included
    in the results.

    Negate an atomic clause by giving it a ``predicate`` field with value ``must_not``.
    """
    query = {
        "query": {
            "bool": {
                "must": [],
                "must_not": [],
            } 
        }#,
       #"sort" : [
       #     {"name" : {"order" : "asc", "mode" : "avg"}}
       #     ]
    }
    if fields is not None and type(fields) is list:
        query["_source"] = fields
    for clause in clauses:
        if type(clause) is dict:
            predicate = clause.pop('predicate', 'must')
            query['query']['bool'][predicate].append(clause)
        elif type(clause) is list:
            query['query']['bool']['must'].append(
                {
                    'bool': {
                        'should': clause
                    }
                }
            )
    return query


def TLAWildcardToRegEx(expr):
    if expr:
        #expr = expr.replace('\\*', '\*') ## Test, nötig?
        #expr = expr.replace('\\[', '\[')
        #expr = expr.replace('\\]', '\]')
        #expr = expr.replace('\\?', '\?')
        expr = expr.replace('.', '\.')
        expr = expr.replace('-', '\-')
        expr = expr.replace('*', '.')
        expr = expr.replace('(', '\(') # Problem: elasticsearch Analyzer
        expr = expr.replace(')', '\)') 
        expr = expr.lower() # elasticsearch-Suche ist offenbar aktuell case-insensitive, daher muss auch die Suche in lowercase verwandelt werden
    return expr


def include_sort_order(query: dict, param: list) -> dict:
    """ takes an elasticsearch query DSL object and a list of parameter values,
    and puts a ``sort`` specification into the query before returning it.
    Only first element of the ``param`` list is used, tho. If ``param`` is empty,
    this defaults to ascending alphabetic order.

    :param param: list of sort order IDs like ``aleph_asc`` or ``time_begin``
    """
    sort_order = param[0] if len(param) > 0 else "alph_asc"
    qualifier = sort_order.split("_")[-1]
    if sort_order in ["alph_asc", "alph_desc"]:
        query["sort"] = [
            {
                "sort_string.keyword": {
                    "order": qualifier,
                }
            },
        ]
    elif sort_order in ["time_begin", "time_end"]:
        query["sort"] = [
            {
                "time_span.{}".format(qualifier): {
                    "order": {
                        "begin": "asc",
                        "end": "desc",
                    }.get(
                        qualifier,
                        "asc"
                    ),
                    "missing": "_last",
                }
            }
        ]
    elif sort_order in ["root_asc"]:
        query["sort"] = [
            {
                "id.keyword": {
                    "order": qualifier,
                    "missing": "_last",
                }
            }
        ]
    return query


def dict_search_query(**params):
    """ generate elasticsearch query object with parameters as would be expected to come from
    the `dict-search` form in the `search/index.html` template. """
    q = {"query": {"bool": {"must": [], "must_not": [], "should": []}}}
    clauses = []
    if 'transcription' in params:
        transcription = params.get('transcription')[0] if type(params.get('transcription')) == list else params.get('transcription')
        transcription = transcription.strip()
        if len(transcription) > 0:
            if 'transcription_enc' in params:
                transcription_enc = params.get('transcription_enc')[0] if type(params.get('transcription_enc')) == list else params.get('transcription_enc')
                if transcription_enc == 'manuel_de_codage':
                    translString = transcription.maketrans("'AaHxXSTDV", "ʾꜣꜥḥḫẖšṯḏṱ")
                    transcription = transcription.translate(translString)
                    transcription = transcription.replace("v", "h̭") 
                    transcription = transcription.replace("u", "u̯") 
                    #Problem, dass i zwei Bedeutungen hat; Darf man dann bei MdC-Kodierung nicht gleichzeitig in hierogl und demot suchen
                    #transcription = transcription.replace("i", "i̯") # Hieroglyphisch/Hieratisch
                    transcription = transcription.replace("i", "ı͗") # Demotisch
                    transcription = transcription.replace("'", "ı͗") # neue Empfehlung wäre i͗
            clauses.append(
                {
                    "regexp": {
                        "name": TLAWildcardToRegEx(transcription)+".*", # nur nach ".": '+"([\.].+)?",'
                    }
                }
            )
            # Roots von Suchergebnis ausnehmen; abhängig von Logik des root-Schlitzes
#            query = {
#                "term": {
#                    "type": "root"
#                }
#            }
#            query['predicate'] = 'must_not'
#            clauses.append(query) 
    if 'root' in params:
        root = params.get('root')[0] if type(params.get('root')) == list else params.get('root')
        root = root.strip()
        if len(root) > 0:
            if 'root_enc' in params:
                root_enc = params.get('root_enc')[0] if type(params.get('root_enc')) == list else params.get('root_enc')
                if root_enc == 'manuel_de_codage':
                    #nicht zusammengesetzte Unicode-Zeichen
                    translString = root.maketrans("'AaHxXSTDV", "ʾꜣꜥḥḫẖšṯḏṱ")
                    root = root.translate(translString)
                    #zusammengesetzte Unicode-Zeichen
                    root = root.replace("v", "h̭") 
                    root = root.replace("u", "u̯") 
                    #Problem, dass i zwei Bedeutungen hat; Darf man dann bei MdC-Kodierung nicht gleichzeitig in hierogl und demot suchen
                    #root = root.replace("i", "i̯") # Hieroglyphisch/Hieratisch
                    root = root.replace("i", "ı͗") # Demotisch
                    root = root.replace("'", "ı͗") # neue Empfehlung wäre i͗
#            # Logik: "Suche nach" root
#            clauses.append(
#                {
#                    "term": {
#                        "type": "root",
#                    }
#                }
#            )
#            clauses.append(
#                {
#                    "regexp": {
#                        "name": TLAWildcardToRegEx(root)+".*", 
#                    }
#                }
#            )
            # Logik: "Einschränkung durch" root
            clauses.append(
                {
                    "regexp": {
                        "relations.root.name": TLAWildcardToRegEx(root)+".*", 
                    }
                }
            )
    if 'script' in params:
        if ('hieroglyphic' in params.get('script')) ^ ('demotic' in params.get('script')): # XOR
            query = {
                "prefix": {
                    "id": "d"
                }
            }
            query['predicate'] = 'must' if 'demotic' in params.get('script') else 'must_not'
            clauses.append(query)
    if 'translation' in params:
        transl = params.get('translation')[0]
        transl = transl.strip()
        if transl != '':
            clauses.append(
                [
                    {
                        "match_phrase_prefix": {
                            "translations.{}".format(lang): transl,
                        }
                    }
                    for lang in params.get('lang', ['de'])
                ]
            )
    if 'pos_type' in params:
        pos_type = params.get('pos_type')[0]
        if pos_type != '' and pos_type != '(any)':
            if pos_type == '(any_but_names)':
                query = {
                    "term": {
                        "type": "entity_name"
                    }
                }
                query['predicate'] = 'must_not'
                clauses.append(query)                 
            else:
                clauses.append(
                    {
                        "term": {
                            "type": pos_type,
                        }
                    }
            )
    if 'pos_subtype' in params:
        pos_subtype = params.get('pos_subtype')[0]
        if pos_subtype != '' and pos_subtype != '(any)':
            clauses.append(
                {
                    "term": {
                        "subtype": pos_subtype,
                    }
                }
            )
    if 'bibliography' in params:
        bib = params.get('bibliography')[0]
        bib = bib.strip()
        if bib != '':
            clauses.append(
                {
                    "match_phrase_prefix": {
                        "passport.bibliography.bibliographical_text_field": bib,
                    }
                }
            )
    if 'lemma_id' in params:
        lemma_id = params.get('lemma_id')[0]
        lemma_id = lemma_id.strip()
        if lemma_id != '':
            clauses.append(
                {
                    "term": {
                        "id": lemma_id,
                    }
                }
            )
    q = include_sort_order(
            build_query(*clauses),
            params.get('sort_order', []),
    )
    #print(q)
    return q


def textword_search_query(**params):
    """ generate elasticsearch query from parameters passed over by a
    :class:`forms.TextWordSearchForm`.
    """
    clauses = []
    if 'lemma' in params:
        clauses.append(
            [
                {
                    'term': {
                        'lemma.id': lemma
                    }
                }
                for lemma in params['lemma']
                if len(lemma.strip()) > 0
            ]
        )
    if 'translation' in params:
        if len(params.get('translation')[-1]) > 0:
            clauses.append(
                [
                    {
                        'match': {
                            'translations.{}'.format(lang): params.get('translation')[-1]
                        }
                    }
                    for lang in params.get('trans_lang', [])
                ]
            )
    if 'hieroglyphs' in params:
        if len(params.get('hieroglyphs')[-1]) > 0:
            glyphs = params.get('hieroglyphs')[-1]
            for glyph in re.split(r'[ :*-]', glyphs):
                clauses.append(
                    {
                        'match': {
                            'glyphs': glyph
                        }
                    }
                )
    if 'sentence_id' in params:
        sentence_id = params.get('sentence_id')[0]
        print(sentence_id)
        sentence_id = sentence_id.strip()
        if sentence_id != '':
            clauses.append(
                {
                    "term": {
                        "id": sentence_id.lower(),
                    }
                }
            )
    q = build_query(*clauses)
    print(q)
    return q


def search_textword_occurrences(offset=1, size=RESULTS_PER_PAGE, **params):
    """ builds queries according to the parameters obtained from the :class:`forms.TextWordSearchForm` textword occurrence search form.
    Passes the final occurrence query to function :meth:`store.search` an returns the results.

    :rtype: list
    """
    passport_value = params.get('passport_0', [''])[-1]
    objects = None
    if passport_value is not None and len(passport_value.strip()) > 0:
        objects_query = build_query(
            {
                "match": {
                    params.get('passport_1')[-1]: passport_value,
                }
            },
            fields=['id'],
        )
        objects = [
            hit['_source']['id']
            for hit in store.scroll(
                'object',
                objects_query
            )
        ]
        if len(objects) < 1:
            print('no matching objects. so long!')
            return {}
    texts = None
    if objects is not None or len(params.get('textname', [''])[-1].strip()) > 0:
        clauses = []
        if params.get('textname') and len(params.get('textname')[-1].strip()) > 0:
            clauses.append(
                {
                    'match': {
                        'name': params.get('textname')[-1]
                    }
                }
            )
        if objects:
            clauses.append(
                {
                    'terms': {
                        'relations.partOf.id': list(map(str.lower, objects))
                    }
                }
            )
        texts_query = build_query(*clauses, fields=['id'])
        texts = [
            hit['_source']['id']
            for hit in store.scroll(
                'text',
                texts_query
            )
        ]
        if len(texts) < 1:
            print('no matching texts. bye!')
            return {}
    occurrences = []
    occurrences_query = textword_search_query(**params)
    if texts:
        occurrences_query['query']['bool']['must'].append(
            {
                'terms': {
                    'text': list(map(str.lower, texts))
                }
            }
        )
    hits = store.search(
        'occurrence',
        occurrences_query,
        offset=offset,
        size=size,
    )
    print(hits)
    return hits


def populate_textword_occurrences(hits, **params):
    """ take text word search results and the original search parameters and
    enrich the results with like highlighting and stuff.

    :rtype: list
    """
    occurrences = []
    filters = {
        k: params.get(k) for k in ["lemma", "transcription", "hieroglyphs"]
    }
    for hit in hits:
        sentence = store.get(
            'sentence',
            hit.get('location', {}).get('sentence')
        )
        for i, token in enumerate(sentence['tokens']):
            if token.get('id') == hit['id']:
                token['highlight'] = 1
            else:
                match = True
                for k, vv in filters.items():
                    if vv:
                        match = match and any(
                            map(
                                lambda v: token.get(k) == v,
                                vv
                            )
                        )
                if 'translation' in filters:
                    match = match and any(
                        map(
                            lambda l: any(
                                map(
                                    lambda t: t in filters.get('translations').get(l, "").lower(),
                                    filters.get('trans_lang', [])
                                )
                            ),
                            filters.get('translation')
                        )
                    )
                if match:
                    token['highlight'] = 2
        text = store.get(
            'text',
            hit.get('location', {}).get('text'),
        )
        if text:
            print('text id', text['id'])
            for path in text.get('paths', []):
                for node in path:
                    #node["url"] = "/view/{}/{}".format(
                    node["url"] = "/{}/{}".format(
                        {
                            "BTSTCObject": "object",
                            "BTSText": "text",
                        }.get(node.get('eclass')),
                        node['id']
                    )
            try:
                editor = text['edited']['name']
            except: 
                editor = '(not edited)'
            try:
                dateEdited = text['edited']['date']
            except: 
                dateEdited = '(not edited)'
            try:
                date = text['passport']['date'][0]['date'][0]['date'][0]['name']
            except: 
                date = '(not edited)'
            occurrences.append(
                {
                    "occurrence": hit,
                    "sentence": sentence,
                    "text": text,
                    "editor": editor,
                    "date": date,
                    "dateEdited": dateEdited,
                }
            )
        else:
            print('text not found: ', hit.get('location', {}).get("text"))
    return occurrences


def hit_tree(hits):
    """ extracts the implicit hierarchical structure among the given objects """
    for hit in hits:
        hit["occurrences"] = detail_views.occurrence_count(
            hit.get('id')
        )
    structure = {
        h.get('id'): (hits.index(h), h)
        for h in hits
    }
    res = []

    def nest(hit, indent=0, pred=None):
        if hit.get('id') in structure:
            structure.pop(hit.get('id'))
        else:
            return
        hit['bibliography'] = glom(
            hit,
            'passport.bibliography.0.bibliographical_text_field.0',
            default=''
            )
        """ append hit to result list (represented as tuple containing indentation and rel type """
        res.append((indent, pred, hit))
        """ generate list of (id,relationtype) tuples representing the search results which
        are directly related to the current search result while preseving order """
        related_hit_ids = sorted([
            (hid.get('id'), pred)
            for pred in [
                #'rootOf',
                'referencing',
                'contains',
                #'successor',
                #'referencedBy',
                #'composedOf',
                #'predecessor',
                #'composes',
            ]
            for hid in hit.get('relations', {}).get(pred, [])
            if hid.get('id') in structure],
            key=lambda t: structure.get(t[0])[0]
        )
        for hid, pred in related_hit_ids:
            if hid in structure:
                _, obj = structure.get(hid)
                #nest(obj, indent=indent + 1, pred=pred) #nesting (de)aktiviert: funktioniert nur innerhalb des Datenseite, nicht über Gesamtergebnismenge             

    while len(hits) > 0:
        hit = hits.pop(0)
        nest(hit)

    return res


@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    return render(
        request,
        'search/index.html',
        {
            'word_classes': WORD_CLASSES,
            'dictform': DictSearchForm(),
            'textwordform': TextWordSearchForm(),
            'passport_fields': filter(
                lambda property: property.startswith('passport') and property.endswith('id'),
                store.get_mappings('object')
            )
        }
    )


def pagination(request, hitcount) -> list:
    page = int(request.GET.get('page', 1))
    if 'page' in request.get_full_path():
        href = request.get_full_path().replace('page={}'.format(page), 'page={}')
    else:
        href = request.get_full_path() + '&page={}'
    lastpageno = hitcount // RESULTS_PER_PAGE + 2
    pages = []
    for i in range(1, lastpageno):
        if i < 3 or i > lastpageno - 2 or (i - page)**2 < 3:
            if len(pages) > 1:
                if type(pages[-1][0]) is int and pages[-1][0] < i - 1:
                    pages.append(('...', None))
            pages.append((i, href.format(i)))
    return pages


def request_url_without_page(request):
    url = request.get_full_path()
    page = int(request.GET.get('page', 1))
    if 'page=' in url:
        url = url.replace('page={}'.format(page), '')
    return url

#### Doppelung aus webd/details/views.py unschön
tlaTitle = "Thesaurus Linguae Aegyptiae"
tlaVersion = "19"
tlaIssue = "beta"
tlaReleaseDate = "30.10.2019"
tlaEditor = "Berlin-Brandenburgische Akademie der Wissenschaften & Sächsische Akademie der Wissenschaften zu Leipzig"
tlaPublisher = "Berlin-Brandenburgische Akademie der Wissenschaften"
tlaBaseURL = "https://tla.bbaw.de"

def sortTranslitStr(sortString):
    # zusammengesetzte Großbuchstaben in Kleinbuchstaben verwandeln
    sortString = sortString.replace('H̱', 'ẖ') 
    sortString = sortString.replace('I͗', 'ı͗') 
    sortString = sortString.replace('H̭', 'h̭') # eigentlich redundant
    sortString = sortString.replace('Č̣', 'č̣') # eigentlich redundant
    # Groß- in Kleinbuchstaben verwandeln
    sortString = sortString.lower()
    # Transliterationsalphabet in Pseudoalphabet verwandeln, nur unzusammengesetzte
    translString = sortString.maketrans("*=.-ʾꜣaijïyꜥewbpfmnrlhḥḫẖzsśšqḳkgtṱṯčdṭḏ", "ABCDFHIJNOPQRTUWXYZabcdeghijklmnopqrstuv")
    sortString = sortString.translate(translString) 
    # restliche, zusammengesetzte Kleinbuchstaben in Pseudoalphabet verwandeln
    sortString = sortString.replace('i̯', 'L') 
    sortString = sortString.replace('ı͗', 'M') # i ohne Punkt + Haken
    sortString = sortString.replace('i͗', 'M') # normales "i" + Haken
    sortString = sortString.replace('u̯', 'S')
    sortString = sortString.replace('h̭', 'f')
    sortString = sortString.replace('č̣', 'w')
    # entspricht Sortierfolge 
    # '*' > '=' > '.' > '-' > 'ʾ' > 'ꜣ' > 'a' > 'i' > 'i̯' > 'ı͗' > 'j' > 'ï' > 'y' > 'ꜥ' > 'e' > 'u̯' > 'w' > 'b' > 'p' > 'f' > 'm' > 'n' > 'r' > 'l' > 'h' > 'ḥ' > 'ḫ' > 'h̭' > 'ẖ' > 'z' > 's' > 'ś' > 'š' > 'q' > 'ḳ' > 'k' > 'g' > 't' > 'ṱ' > 'ṯ' > 'č' > 'd' > 'ṭ' > 'ḏ' > 'č̣'
    return sortString

def unicodeSearchStr(unicodeTransliteration):
    searchStr = unicodeTransliteration
    # zusammengesetzte Großbuchstaben in Kleinbuchstaben verwandeln
    searchStr = searchStr.replace('H̱', 'ẖ') 
    searchStr = searchStr.replace('I͗', 'ı͗') 
    searchStr = searchStr.replace('H̭', 'h̭') # eigentlich redundant
    searchStr = searchStr.replace('Č̣', 'č̣') # eigentlich redundant
    # Groß- in Kleinbuchstaben verwandeln
    searchStr = searchStr.lower()
    # zusammengesetzte Kleinbuchstaben in Pseudoalphabet verwandeln
    searchStr = searchStr.replace('i̯', 'i') 
    searchStr = searchStr.replace('ı͗', 'I') # i ohne Punkt + Haken
    searchStr = searchStr.replace('i͗', 'I') # normales "i" + Haken
    searchStr = searchStr.replace('u̯', 'u')
    searchStr = searchStr.replace('h̭', 'H')
    searchStr = searchStr.replace('č̣', 'D') # sollte nicht vorkommen, aber zur Sicherheit
    return searchStr

@require_http_methods(["GET"])
def search_dict(request):
    params = request.GET.copy()
    page = int(params.get('page', 1))
    offset = (page - 1) * RESULTS_PER_PAGE
    sort_order = params.get('sort_order', 'alph_asc')
    hits = store.search(
        'wlist',
        dict_search_query(**params),
        offset=offset,
        size=RESULTS_PER_PAGE,
    )
    count = hits.get('total')
    hits = store.hits_contents(hits)
    hits = hit_tree(hits)
    return render(
        request,
        'search/dict.html',
        {
            'params': params,
            'sort_order': {
                'options': SORT_ORDERS,
                'selection': sort_order,
            },
            'hits': hits,
            'hitcount': count,
            'page': page,
            'start': offset + 1,
            'end': min(count, offset + RESULTS_PER_PAGE),
            'pagination': pagination(request, count),
            'tlaVersion': tlaVersion,
            'tlaTitle': tlaTitle,
            'tlaVersion': tlaVersion,
            'tlaIssue': tlaIssue,
            'tlaReleaseDate': tlaReleaseDate,
            'tlaEditor': tlaEditor,
            'tlaBaseURL': tlaBaseURL,
            #'dateToday': datetime.now().strftime("%d.%m.%Y"),
        }
    )


def search_lemma(lemma_id):
    q = {"query": {"bool": {"must": [], "must_not": [], "should": []}}}
    clauses = []

    lemma_id = lemma_id.strip()
    if lemma_id != '':
        clauses.append(
            {
                "term": {
                    "id": lemma_id,
                }
            }
        )
    q = build_query(*clauses)
    print(q)

    hit = store.search(
        'wlist',
        q,
        size=1,
    )
    
    print(hit)
    return hit

@require_http_methods(["GET"])
def search_text_words(request):
    params = request.GET.copy()
    page = int(params.get('page', 1))
    offset = (page - 1) * RESULTS_PER_PAGE
    #form = TextWordSearchForm(request.GET)
    #print(params)
    hits = search_textword_occurrences(
        offset=offset,
        size=RESULTS_PER_PAGE,
        **params,
    )
    count = hits.get('total', 0)
    hits = store.hits_contents(hits)
    hits = populate_textword_occurrences(hits, **params)
    return render(
        request,
        'search/occurrences.html',
        {
            'params': params,
            'hits': hits,
            'hitcount': count,
            'start': offset + 1,
            'end': min(count, offset + RESULTS_PER_PAGE),
            'pagination': pagination(request, count),
            'url': request_url_without_page(request),
            'tlaVersion': tlaVersion,
            'tlaTitle': tlaTitle,
            'tlaVersion': tlaVersion,
            'tlaIssue': tlaIssue,
            'tlaReleaseDate': tlaReleaseDate,
            'tlaEditor': tlaEditor,
            'tlaBaseURL': tlaBaseURL,
            #'dateToday': datetime.now().strftime("%d.%m.%Y"),
        }
    )
