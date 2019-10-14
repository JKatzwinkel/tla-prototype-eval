from django.utils.safestring import mark_safe
from django.template import Library
#from django.utils.http import urlencode
import re

import json

register = Library()

@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))
    
@register.filter(is_safe=True)
def subdictionaryFromLemmaID(lemmaID):
    subdict = '(error)'
    if lemmaID[0] == 'd':
        subdict = "Demotic"
    elif lemmaID[0] >= '1' and lemmaID[0] <= '9':
        subdict = "Hieroglyphic/Hieratic"
    return subdict 
    
@register.filter(is_safe=True)
def niceLineCount(lcStr):
    if lcStr:
        lcStr = lcStr.replace('lc', 'line')
    return lcStr 
    
@register.filter(is_safe=True)
def niceCorpus(corpus):
    if corpus:
        corpus = corpus.replace('corpus', 'Digital BTS corpus')
    return corpus 
    
@register.filter(is_safe=True)
def fixForRES(mdc):
    if mdc:
        mdc = mdc.replace('[', 'empty[shade]') # temporary workaround
        #mdc = mdc.replace(']', '"]"') # darf nicht nochmal getauscht werden, sonst zerstört es die Ersetzung von "["
        mdc = mdc.replace('..', 'empty')
        mdc = mdc.replace('.', 'empty[width=0.5,height=0.5]')
        mdc = mdc.replace('//', 'empty[shade]')
        mdc = mdc.replace('h/', 'empty[t]')
        mdc = mdc.replace('v/', 'empty[s]')
        mdc = mdc.replace('/', 'empty[ts]')
        mdc = re.sub(r'([0-9])([A-Z])', lambda m: m.group(0).lower(), mdc.rstrip()) #replace alphanumerical glyph index by lowercase
    return mdc 

@register.filter(is_safe=True)
def niceTransliteration(transl):
    if transl:
        transl = transl.replace('≡', '=')
        transl = transl.replace(',', '.')
        transl = transl.replace('.du', ':DU')
        transl = transl.replace('.pl', ':PL')
    return transl
    
@register.filter(is_safe=True)
def niceRelationName(name):
    if name == 'root':
        name = 'Root'
    elif name == 'rootOf':
        name = 'Root of'
    elif name == 'predecessor':
        name = 'Historical predecessors'
    elif name == 'successor':
        name = 'Historical successors'
    elif name == 'referencing':
        name = 'Substituted by'        
    elif name == 'referencedBy':
        name = 'Substitutes for following obsolete lemmata'        
    elif name == 'composedOf':
        name = 'Parts'        
    elif name == 'composes':
        name = 'Part of'        
    elif name == 'contains':
        name = 'Subordinates'        
    elif name == 'partOf':
        name = 'Superordinates'      
    return name
        
@register.filter(is_safe=True)
def niceQueryData(name):
    dict = {
        'script': 'Sub-dictionary',
        'hieroglyphic': 'Hieroglyphic/Hieratic',
        'demotic': 'Demotic',
        'coptic': 'Coptic',
        'transcription': 'Transliteration',
        'transcription_enc': 'Encoding',
        'unicode': 'Unicode',
        'manuel_de_codage': 'Manuel de Codage',
        'pos_type': 'Part of Speech', 
        'pos_subtype': 'POS subtype', 
        'lemma_id': 'Lemma ID'
        }
    newName = dict.get(name)
    if newName:
        return newName
    else:
        return name
        
@register.filter(is_safe=True)
def niceReviewState(name):
    dict = {
        'published': 'reviewed',
        'plublished-awaiting-review': 'yet to be reviewed',
        'published-obsolete': 'obsolete' }
    newName = dict.get(name)
    if newName:
        return newName
    else:
        return name
        
@register.filter(is_safe=True)
def nicePOS(name):
    dict = {
        "adjective": "adjective",
        "adverb": "adverb",
        "entity_name": "entity name",
        "epitheton_title": "title / epithet",
        "interjection": "interjection",
        "numeral": "numeral",
        "particle": "particle",
        "preposition": "preposition",
        "pronoun": "pronoun",
        "root": "root",
        "substantive": "noun",
        "undefined": "(undefined)",
        "verb": "verb" }
    newName = dict.get(name)
    if newName:
        return newName
    else:
        return name

@register.filter(is_safe=True)
def niceSubPOS(name):
    dict = {
        "animal_name": "animal",
        "artifact_name": "artifact",
        "cardinal": "cardinal",
        "demonstrative_pronoun": "demonstrative",
        "epith_god": "divine",
        "epith_king": "royal",
        "gods_name": "divine",
        "interrogative_pronoun": "interrogative",
        "kings_name": "royal",
        "nisbe_adjective_preposition": "de-prepositional nisbe",
        "nisbe_adjective_substantive": "de-nominal nisbe",
        "ordinal": "ordinal",
        "org_name": "organization",
        "particle_enclitic": "enclitic",
        "particle_nonenclitic": "nonenclitic",
        "person_name": "personal",
        "personal_pronoun": "personal",
        "place_name": "place",
        "prepositional_adverb": "de-prepositional",
        "relative_pronoun": "relative",
        "substantive_fem": "fem.",
        "substantive_masc": "masc.",
        "title": "title",
        "verb_2-gem": "II gem.",
        "verb_2-lit": "2 lit.",
        "verb_3-gem": "III gem.",
        "verb_3-inf": "III inf.",
        "verb_3-lit": "3 lit.",
        "verb_4-inf": "IV inf.",
        "verb_4-lit": "4 lit.",
        "verb_5-inf": "V inf.",
        "verb_5-lit": "5 lit.",
        "verb_6-lit": "6 lit.",
        "verb_caus_2-gem": "caus. II gem.",
        "verb_caus_2-lit": "caus. 2 lit.",
        "verb_caus_3-gem": "caus. III gem.",
        "verb_caus_3-inf": "caus. III inf.",
        "verb_caus_3-lit": "caus. 3 lit.",
        "verb_caus_4-inf": "caus. IV inf.",
        "verb_caus_4-lit": "caus. 4 lit.",
        "verb_caus_5-lit": "caus. 5 lit.",
        "verb_irr": "irregular" }
    newName = dict.get(name)
    if newName:
        return newName
    else:
        return name
    
@register.filter(is_safe=True)
def isURL(ref):       
    if ref[0:4] == 'http': 
        return True
    return False   
    
# obsolete
@register.filter(is_safe=True)
def linkFromExternalReference(ref, where):
    if where == 'aaew_wcn':
        if int(ref) >= 0: # ##: Problem: nicht Demotisch oder Demotisch
            ref = 'http://aaew.bbaw.de/tla/servlet/GetWcnDetails?u=guest&f=0&l=0&wn='+str(ref)+'&db=0'
            #DZA: ref = 'http://aaew.bbaw.de/tla/servlet/DzaBrowser?u=guest&f=0&l=0&wn='+str(ref)
        elif int(ref) < 0: # Demotisch
            ref = 'http://aaew.bbaw.de/tla/servlet/GetWcnDetails?u=guest&f=0&l=0&wn='+str(ref)+'&db=1'

    # ## weitere hinzufügen
        
    if ref[0:4] != 'http': # falls nun keine URL, dann '' zurückgeben
        ref = ''
    return ref   
# obsolete

@register.filter(is_safe=True)
def encodeEMail(text): 
    #text = urlencode(text) 
    return text
    
    
############################
##### temporär / Mockup ####
############################

@register.filter(is_safe=True)
def verbalFlexcode(flexcode):
    dict = {
        "0": "(unedited)",
        "1": "(?)",
        "2": "(unknown)",
        "3": "(not specified)",
        "4": "(unclear)",
        "5": "(probematic)",
        "9": "(to be reviewed)",
        "10000": "SC.unspec",
        "100000": "SC.unspec_Neg.n",
        "110000": "SC.unspec_Neg.n",
        "210000": "SC.unspec_Neg.nn",
        "10020": "SC.act.ngem.nom.subj",
        "110020": "SC.act.ngem.nom.subj_Neg.n",
        "210020": "SC.act.ngem.nom.subj_Neg.nn",
        "310020": "SC.act.ngem.nom.subj_Neg.n js",
        "410020": "SC.act.ngem.nom.subj_Neg.jmi",
        "510020": "SC.act.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610020": "SC.act.ngem.nom.subj_Neg.jwtj",
        "710020": "SC.act.ngem.nom.subj_Neg.jwt",
        "810020": "SC.act.ngem.nom.subj_Neg.w/ꜣ",
        "910020": "SC.act.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10021": "SC.act.ngem.1sg",
        "110021": "SC.act.ngem.1sg_Neg.n",
        "210021": "SC.act.ngem.1sg_Neg.nn",
        "310021": "SC.act.ngem.1sg_Neg.n js",
        "410021": "SC.act.ngem.1sg_Neg.jmi",
        "510021": "SC.act.ngem.1sg_Neg.n-zp/jwt-zp",
        "610021": "SC.act.ngem.1sg_Neg.jwtj",
        "710021": "SC.act.ngem.1sg_Neg.jwt",
        "810021": "SC.act.ngem.1sg_Neg.w/ꜣ",
        "910021": "SC.act.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10022": "SC.act.ngem.2sgm",
        "110022": "SC.act.ngem.2sgm_Neg.n",
        "210022": "SC.act.ngem.2sgm_Neg.nn",
        "310022": "SC.act.ngem.2sgm_Neg.n js",
        "410022": "SC.act.ngem.2sgm_Neg.jmi",
        "510022": "SC.act.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610022": "SC.act.ngem.2sgm_Neg.jwtj",
        "710022": "SC.act.ngem.2sgm_Neg.jwt",
        "810022": "SC.act.ngem.2sgm_Neg.w/ꜣ",
        "910022": "SC.act.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10023": "SC.act.ngem.2sgf",
        "110023": "SC.act.ngem.2sgf_Neg.n",
        "210023": "SC.act.ngem.2sgf_Neg.nn",
        "310023": "SC.act.ngem.2sgf_Neg.n js",
        "410023": "SC.act.ngem.2sgf_Neg.jmi",
        "510023": "SC.act.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610023": "SC.act.ngem.2sgf_Neg.jwtj",
        "710023": "SC.act.ngem.2sgf_Neg.jwt",
        "810023": "SC.act.ngem.2sgf_Neg.w/ꜣ",
        "910023": "SC.act.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10024": "SC.act.ngem.3sgm",
        "110024": "SC.act.ngem.3sgm_Neg.n",
        "210024": "SC.act.ngem.3sgm_Neg.nn",
        "310024": "SC.act.ngem.3sgm_Neg.n js",
        "410024": "SC.act.ngem.3sgm_Neg.jmi",
        "510024": "SC.act.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610024": "SC.act.ngem.3sgm_Neg.jwtj",
        "710024": "SC.act.ngem.3sgm_Neg.jwt",
        "810024": "SC.act.ngem.3sgm_Neg.w/ꜣ",
        "910024": "SC.act.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10025": "SC.act.ngem.3sgf",
        "110025": "SC.act.ngem.3sgf_Neg.n",
        "210025": "SC.act.ngem.3sgf_Neg.nn",
        "310025": "SC.act.ngem.3sgf_Neg.n js",
        "410025": "SC.act.ngem.3sgf_Neg.jmi",
        "510025": "SC.act.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610025": "SC.act.ngem.3sgf_Neg.jwtj",
        "710025": "SC.act.ngem.3sgf_Neg.jwt",
        "810025": "SC.act.ngem.3sgf_Neg.w/ꜣ",
        "910025": "SC.act.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10026": "SC.act.ngem.3sg",
        "110026": "SC.act.ngem.3sg_Neg.n",
        "210026": "SC.act.ngem.3sg_Neg.nn",
        "310026": "SC.act.ngem.3sg_Neg.n js",
        "410026": "SC.act.ngem.3sg_Neg.jmi",
        "510026": "SC.act.ngem.3sg_Neg.n-zp/jwt-zp",
        "610026": "SC.act.ngem.3sg_Neg.jwtj",
        "710026": "SC.act.ngem.3sg_Neg.jwt",
        "810026": "SC.act.ngem.3sg_Neg.w/ꜣ",
        "910026": "SC.act.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10027": "SC.act.ngem.1pl",
        "-10027": "SC.act.ngem.1du",
        "110027": "SC.act.ngem.1pl_Neg.n",
        "210027": "SC.act.ngem.1pl_Neg.nn",
        "-210027": "SC.act.ngem.1du_Neg.nn",
        "310027": "SC.act.ngem.1pl_Neg.n js",
        "-310027": "SC.act.ngem.1du_Neg.n js",
        "410027": "SC.act.ngem.1pl_Neg.jmi",
        "-410027": "SC.act.ngem.1du_Neg.jmi",
        "510027": "SC.act.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510027": "SC.act.ngem.1du_Neg.n-zp/jwt-zp",
        "610027": "SC.act.ngem.1pl_Neg.jwtj",
        "-610027": "SC.act.ngem.1du_Neg.jwtj",
        "710027": "SC.act.ngem.1pl_Neg.jwt",
        "-710027": "SC.act.ngem.1du_Neg.jwt",
        "810027": "SC.act.ngem.1pl_Neg.w/ꜣ",
        "-810027": "SC.act.ngem.1du_Neg.w/ꜣ",
        "910027": "SC.act.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910027": "SC.act.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10028": "SC.act.ngem.2pl",
        "-10028": "SC.act.ngem.2du",
        "110028": "SC.act.ngem.2pl_Neg.n",
        "210028": "SC.act.ngem.2pl_Neg.nn",
        "-210028": "SC.act.ngem.2du_Neg.nn",
        "310028": "SC.act.ngem.2pl_Neg.n js",
        "-310028": "SC.act.ngem.2du_Neg.n js",
        "410028": "SC.act.ngem.2pl_Neg.jmi",
        "-410028": "SC.act.ngem.2du_Neg.jmi",
        "510028": "SC.act.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510028": "SC.act.ngem.2du_Neg.n-zp/jwt-zp",
        "610028": "SC.act.ngem.2pl_Neg.jwtj",
        "-610028": "SC.act.ngem.2du_Neg.jwtj",
        "710028": "SC.act.ngem.2pl_Neg.jwt",
        "-710028": "SC.act.ngem.2du_Neg.jwt",
        "810028": "SC.act.ngem.2pl_Neg.w/ꜣ",
        "-810028": "SC.act.ngem.2du_Neg.w/ꜣ",
        "910028": "SC.act.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910028": "SC.act.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10029": "SC.act.ngem.3pl",
        "-10029": "SC.act.ngem.3du",
        "110029": "SC.act.ngem.3pl_Neg.n",
        "210029": "SC.act.ngem.3pl_Neg.nn",
        "-210029": "SC.act.ngem.3du_Neg.nn",
        "310029": "SC.act.ngem.3pl_Neg.n js",
        "-310029": "SC.act.ngem.3du_Neg.n js",
        "410029": "SC.act.ngem.3pl_Neg.jmi",
        "-410029": "SC.act.ngem.3du_Neg.jmi",
        "510029": "SC.act.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510029": "SC.act.ngem.3du_Neg.n-zp/jwt-zp",
        "610029": "SC.act.ngem.3pl_Neg.jwtj",
        "-610029": "SC.act.ngem.3du_Neg.jwtj",
        "710029": "SC.act.ngem.3pl_Neg.jwt",
        "-710029": "SC.act.ngem.3du_Neg.jwt",
        "810029": "SC.act.ngem.3pl_Neg.w/ꜣ",
        "-810029": "SC.act.ngem.3du_Neg.w/ꜣ",
        "910029": "SC.act.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910029": "SC.act.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "110030": "SC.act.ngem.1du_Neg.n",
        "110031": "SC.act.ngem.2du_Neg.n",
        "110032": "SC.act.ngem.3du_Neg.n",
        "10040": "SC.pass.ngem.nom.subj",
        "110040": "SC.pass.ngem.nom.subj_Neg.n",
        "210040": "SC.pass.ngem.nom.subj_Neg.nn",
        "310040": "SC.pass.ngem.nom.subj_Neg.n js",
        "410040": "SC.pass.ngem.nom.subj_Neg.jmi",
        "510040": "SC.pass.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610040": "SC.pass.ngem.nom.subj_Neg.jwtj",
        "710040": "SC.pass.ngem.nom.subj_Neg.jwt",
        "810040": "SC.pass.ngem.nom.subj_Neg.w/ꜣ",
        "910040": "SC.pass.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10041": "SC.pass.ngem.1sg",
        "110041": "SC.pass.ngem.1sg_Neg.n",
        "210041": "SC.pass.ngem.1sg_Neg.nn",
        "310041": "SC.pass.ngem.1sg_Neg.n js",
        "410041": "SC.pass.ngem.1sg_Neg.jmi",
        "510041": "SC.pass.ngem.1sg_Neg.n-zp/jwt-zp",
        "610041": "SC.pass.ngem.1sg_Neg.jwtj",
        "710041": "SC.pass.ngem.1sg_Neg.jwt",
        "810041": "SC.pass.ngem.1sg_Neg.w/ꜣ",
        "910041": "SC.pass.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10042": "SC.pass.ngem.2sgm",
        "110042": "SC.pass.ngem.2sgm_Neg.n",
        "210042": "SC.pass.ngem.2sgm_Neg.nn",
        "310042": "SC.pass.ngem.2sgm_Neg.n js",
        "410042": "SC.pass.ngem.2sgm_Neg.jmi",
        "510042": "SC.pass.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610042": "SC.pass.ngem.2sgm_Neg.jwtj",
        "710042": "SC.pass.ngem.2sgm_Neg.jwt",
        "810042": "SC.pass.ngem.2sgm_Neg.w/ꜣ",
        "910042": "SC.pass.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10043": "SC.pass.ngem.2sgf",
        "110043": "SC.pass.ngem.2sgf_Neg.n",
        "210043": "SC.pass.ngem.2sgf_Neg.nn",
        "310043": "SC.pass.ngem.2sgf_Neg.n js",
        "410043": "SC.pass.ngem.2sgf_Neg.jmi",
        "510043": "SC.pass.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610043": "SC.pass.ngem.2sgf_Neg.jwtj",
        "710043": "SC.pass.ngem.2sgf_Neg.jwt",
        "810043": "SC.pass.ngem.2sgf_Neg.w/ꜣ",
        "910043": "SC.pass.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10044": "SC.pass.ngem.3sgm",
        "110044": "SC.pass.ngem.3sgm_Neg.n",
        "210044": "SC.pass.ngem.3sgm_Neg.nn",
        "310044": "SC.pass.ngem.3sgm_Neg.n js",
        "410044": "SC.pass.ngem.3sgm_Neg.jmi",
        "510044": "SC.pass.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610044": "SC.pass.ngem.3sgm_Neg.jwtj",
        "710044": "SC.pass.ngem.3sgm_Neg.jwt",
        "810044": "SC.pass.ngem.3sgm_Neg.w/ꜣ",
        "910044": "SC.pass.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10045": "SC.pass.ngem.3sgf",
        "110045": "SC.pass.ngem.3sgf_Neg.n",
        "210045": "SC.pass.ngem.3sgf_Neg.nn",
        "310045": "SC.pass.ngem.3sgf_Neg.n js",
        "410045": "SC.pass.ngem.3sgf_Neg.jmi",
        "510045": "SC.pass.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610045": "SC.pass.ngem.3sgf_Neg.jwtj",
        "710045": "SC.pass.ngem.3sgf_Neg.jwt",
        "810045": "SC.pass.ngem.3sgf_Neg.w/ꜣ",
        "910045": "SC.pass.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10046": "SC.pass.ngem.3sg",
        "110046": "SC.pass.ngem.3sg_Neg.n",
        "210046": "SC.pass.ngem.3sg_Neg.nn",
        "310046": "SC.pass.ngem.3sg_Neg.n js",
        "410046": "SC.pass.ngem.3sg_Neg.jmi",
        "510046": "SC.pass.ngem.3sg_Neg.n-zp/jwt-zp",
        "610046": "SC.pass.ngem.3sg_Neg.jwtj",
        "710046": "SC.pass.ngem.3sg_Neg.jwt",
        "810046": "SC.pass.ngem.3sg_Neg.w/ꜣ",
        "910046": "SC.pass.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10047": "SC.pass.ngem.1pl",
        "-10047": "SC.pass.ngem.1du",
        "110047": "SC.pass.ngem.1pl_Neg.n",
        "-110047": "SC.pass.ngem.1du_Neg.n",
        "210047": "SC.pass.ngem.1pl_Neg.nn",
        "-210047": "SC.pass.ngem.1du_Neg.nn",
        "310047": "SC.pass.ngem.1pl_Neg.n js",
        "-310047": "SC.pass.ngem.1du_Neg.n js",
        "410047": "SC.pass.ngem.1pl_Neg.jmi",
        "-410047": "SC.pass.ngem.1du_Neg.jmi",
        "510047": "SC.pass.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510047": "SC.pass.ngem.1du_Neg.n-zp/jwt-zp",
        "610047": "SC.pass.ngem.1pl_Neg.jwtj",
        "-610047": "SC.pass.ngem.1du_Neg.jwtj",
        "710047": "SC.pass.ngem.1pl_Neg.jwt",
        "-710047": "SC.pass.ngem.1du_Neg.jwt",
        "810047": "SC.pass.ngem.1pl_Neg.w/ꜣ",
        "-810047": "SC.pass.ngem.1du_Neg.w/ꜣ",
        "910047": "SC.pass.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910047": "SC.pass.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10048": "SC.pass.ngem.2pl",
        "-10048": "SC.pass.ngem.2du",
        "110048": "SC.pass.ngem.2pl_Neg.n",
        "-110048": "SC.pass.ngem.2du_Neg.n",
        "210048": "SC.pass.ngem.2pl_Neg.nn",
        "-210048": "SC.pass.ngem.2du_Neg.nn",
        "310048": "SC.pass.ngem.2pl_Neg.n js",
        "-310048": "SC.pass.ngem.2du_Neg.n js",
        "410048": "SC.pass.ngem.2pl_Neg.jmi",
        "-410048": "SC.pass.ngem.2du_Neg.jmi",
        "510048": "SC.pass.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510048": "SC.pass.ngem.2du_Neg.n-zp/jwt-zp",
        "610048": "SC.pass.ngem.2pl_Neg.jwtj",
        "-610048": "SC.pass.ngem.2du_Neg.jwtj",
        "710048": "SC.pass.ngem.2pl_Neg.jwt",
        "-710048": "SC.pass.ngem.2du_Neg.jwt",
        "810048": "SC.pass.ngem.2pl_Neg.w/ꜣ",
        "-810048": "SC.pass.ngem.2du_Neg.w/ꜣ",
        "910048": "SC.pass.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910048": "SC.pass.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10049": "SC.pass.ngem.3pl",
        "-10049": "SC.pass.ngem.3du",
        "110049": "SC.pass.ngem.3pl_Neg.n",
        "-110049": "SC.pass.ngem.3du_Neg.n",
        "210049": "SC.pass.ngem.3pl_Neg.nn",
        "-210049": "SC.pass.ngem.3du_Neg.nn",
        "310049": "SC.pass.ngem.3pl_Neg.n js",
        "-310049": "SC.pass.ngem.3du_Neg.n js",
        "410049": "SC.pass.ngem.3pl_Neg.jmi",
        "-410049": "SC.pass.ngem.3du_Neg.jmi",
        "510049": "SC.pass.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510049": "SC.pass.ngem.3du_Neg.n-zp/jwt-zp",
        "610049": "SC.pass.ngem.3pl_Neg.jwtj",
        "-610049": "SC.pass.ngem.3du_Neg.jwtj",
        "710049": "SC.pass.ngem.3pl_Neg.jwt",
        "-710049": "SC.pass.ngem.3du_Neg.jwt",
        "810049": "SC.pass.ngem.3pl_Neg.w/ꜣ",
        "-810049": "SC.pass.ngem.3du_Neg.w/ꜣ",
        "910049": "SC.pass.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910049": "SC.pass.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10060": "",
        "10061": "",
        "10062": "",
        "10063": "",
        "10064": "",
        "10065": "",
        "10066": "",
        "10067": "",
        "10068": "",
        "10069": "",
        "10080": "",
        "10081": "",
        "10082": "",
        "10083": "",
        "10084": "",
        "10085": "",
        "10086": "",
        "10087": "",
        "10088": "",
        "10089": "",
        "10100": "SC.act.gem.nom.subj",
        "110100": "SC.act.gem.nom.subj_Neg.n",
        "210100": "SC.act.gem.nom.subj_Neg.nn",
        "310100": "SC.act.gem.nom.subj_Neg.n js",
        "410100": "SC.act.gem.nom.subj_Neg.jmi",
        "510100": "SC.act.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610100": "SC.act.gem.nom.subj_Neg.jwtj",
        "710100": "SC.act.gem.nom.subj_Neg.jwt",
        "810100": "SC.act.gem.nom.subj_Neg.w/ꜣ",
        "910100": "SC.act.gem.nom.subj/negated nfr/nfr-n/nfr-pw",
        "10101": "SC.act.gem.1sg",
        "110101": "SC.act.gem.1sg_Neg.n",
        "210101": "SC.act.gem.1sg_Neg.nn",
        "310101": "SC.act.gem.1sg_Neg.n js",
        "410101": "SC.act.gem.1sg_Neg.jmi",
        "510101": "SC.act.gem.1sg_Neg.n-zp/jwt-zp",
        "610101": "SC.act.gem.1sg_Neg.jwtj",
        "710101": "SC.act.gem.1sg_Neg.jwt",
        "810101": "SC.act.gem.1sg_Neg.w/ꜣ",
        "910101": "SC.act.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10102": "SC.act.gem.2sgm",
        "110102": "SC.act.gem.2sgm_Neg.n",
        "210102": "SC.act.gem.2sgm_Neg.nn",
        "310102": "SC.act.gem.2sgm_Neg.n js",
        "410102": "SC.act.gem.2sgm_Neg.jmi",
        "510102": "SC.act.gem.2sgm_Neg.n-zp/jwt-zp",
        "610102": "SC.act.gem.2sgm_Neg.jwtj",
        "710102": "SC.act.gem.2sgm_Neg.jwt",
        "810102": "SC.act.gem.2sgm_Neg.w/ꜣ",
        "910102": "SC.act.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10103": "SC.act.gem.2sgf",
        "110103": "SC.act.gem.2sgf_Neg.n",
        "210103": "SC.act.gem.2sgf_Neg.nn",
        "310103": "SC.act.gem.2sgf_Neg.n js",
        "410103": "SC.act.gem.2sgf_Neg.jmi",
        "510103": "SC.act.gem.2sgf_Neg.n-zp/jwt-zp",
        "610103": "SC.act.gem.2sgf_Neg.jwtj",
        "710103": "SC.act.gem.2sgf_Neg.jwt",
        "810103": "SC.act.gem.2sgf_Neg.w/ꜣ",
        "910103": "SC.act.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10104": "SC.act.gem.3sgm",
        "110104": "SC.act.gem.3sgm_Neg.n",
        "210104": "SC.act.gem.3sgm_Neg.nn",
        "310104": "SC.act.gem.3sgm_Neg.n js",
        "410104": "SC.act.gem.3sgm_Neg.jmi",
        "510104": "SC.act.gem.3sgm_Neg.n-zp/jwt-zp",
        "610104": "SC.act.gem.3sgm_Neg.jwtj",
        "710104": "SC.act.gem.3sgm_Neg.jwt",
        "810104": "SC.act.gem.3sgm_Neg.w/ꜣ",
        "910104": "SC.act.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10105": "SC.act.gem.3sgf",
        "110105": "SC.act.gem.3sgf_Neg.n",
        "210105": "SC.act.gem.3sgf_Neg.nn",
        "310105": "SC.act.gem.3sgf_Neg.n js",
        "410105": "SC.act.gem.3sgf_Neg.jmi",
        "510105": "SC.act.gem.3sgf_Neg.n-zp/jwt-zp",
        "610105": "SC.act.gem.3sgf_Neg.jwtj",
        "710105": "SC.act.gem.3sgf_Neg.jwt",
        "810105": "SC.act.gem.3sgf_Neg.w/ꜣ",
        "910105": "SC.act.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10106": "SC.act.gem.3sg",
        "110106": "SC.act.gem.3sg_Neg.n",
        "210106": "SC.act.gem.3sg_Neg.nn",
        "310106": "SC.act.gem.3sg_Neg.n js",
        "410106": "SC.act.gem.3sg_Neg.jmi",
        "510106": "SC.act.gem.3sg_Neg.n-zp/jwt-zp",
        "610106": "SC.act.gem.3sg_Neg.jwtj",
        "710106": "SC.act.gem.3sg_Neg.jwt",
        "810106": "SC.act.gem.3sg_Neg.w/ꜣ",
        "910106": "SC.act.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10107": "SC.act.gem.1pl",
        "-10107": "SC.act.gem.1du",
        "110107": "SC.act.gem.1pl_Neg.n",
        "-110107": "SC.act.gem.1du_Neg.n",
        "210107": "SC.act.gem.1pl_Neg.nn",
        "-210107": "SC.act.gem.1du_Neg.nn",
        "310107": "SC.act.gem.1pl_Neg.n js",
        "-310107": "SC.act.gem.1du_Neg.n js",
        "410107": "SC.act.gem.1pl_Neg.jmi",
        "-410107": "SC.act.gem.1du_Neg.jmi",
        "510107": "SC.act.gem.1pl_Neg.n-zp/jwt-zp",
        "-510107": "SC.act.gem.1du_Neg.n-zp/jwt-zp",
        "610107": "SC.act.gem.1pl_Neg.jwtj",
        "-610107": "SC.act.gem.1du_Neg.jwtj",
        "710107": "SC.act.gem.1pl_Neg.jwt",
        "-710107": "SC.act.gem.1du_Neg.jwt",
        "810107": "SC.act.gem.1pl_Neg.w/ꜣ",
        "-810107": "SC.act.gem.1du_Neg.w/ꜣ",
        "910107": "SC.act.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910107": "SC.act.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10108": "SC.act.gem.2pl",
        "-10108": "SC.act.gem.2du",
        "110108": "SC.act.gem.2pl_Neg.n",
        "-110108": "SC.act.gem.2du_Neg.n",
        "210108": "SC.act.gem.2pl_Neg.nn",
        "-210108": "SC.act.gem.2du_Neg.nn",
        "310108": "SC.act.gem.2pl_Neg.n js",
        "-310108": "SC.act.gem.2du_Neg.n js",
        "410108": "SC.act.gem.2pl_Neg.jmi",
        "-410108": "SC.act.gem.2du_Neg.jmi",
        "510108": "SC.act.gem.2pl_Neg.n-zp/jwt-zp",
        "-510108": "SC.act.gem.2du_Neg.n-zp/jwt-zp",
        "610108": "SC.act.gem.2pl_Neg.jwtj",
        "-610108": "SC.act.gem.2du_Neg.jwtj",
        "710108": "SC.act.gem.2pl_Neg.jwt",
        "-710108": "SC.act.gem.2du_Neg.jwt",
        "810108": "SC.act.gem.2pl_Neg.w/ꜣ",
        "-810108": "SC.act.gem.2du_Neg.w/ꜣ",
        "910108": "SC.act.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910108": "SC.act.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10109": "SC.act.gem.3pl",
        "-10109": "SC.act.gem.3du",
        "110109": "SC.act.gem.3pl_Neg.n",
        "-110109": "SC.act.gem.3du_Neg.n",
        "210109": "SC.act.gem.3pl_Neg.nn",
        "-210109": "SC.act.gem.3du_Neg.nn",
        "310109": "SC.act.gem.3pl_Neg.n js",
        "-310109": "SC.act.gem.3du_Neg.n js",
        "410109": "SC.act.gem.3pl_Neg.jmi",
        "-410109": "SC.act.gem.3du_Neg.jmi",
        "510109": "SC.act.gem.3pl_Neg.n-zp/jwt-zp",
        "-510109": "SC.act.gem.3du_Neg.n-zp/jwt-zp",
        "610109": "SC.act.gem.3pl_Neg.jwtj",
        "-610109": "SC.act.gem.3du_Neg.jwtj",
        "710109": "SC.act.gem.3pl_Neg.jwt",
        "-710109": "SC.act.gem.3du_Neg.jwt",
        "810109": "SC.act.gem.3pl_Neg.w/ꜣ",
        "-810109": "SC.act.gem.3du_Neg.w/ꜣ",
        "910109": "SC.act.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910109": "SC.act.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10120": "SC.pass.gem(redupl).nom.subj",
        "110120": "SC.pass.gem.nom.subj_Neg.n",
        "210120": "SC.pass.gem.nom.subj_Neg.nn",
        "310120": "SC.pass.gem.nom.subj_Neg.n js",
        "410120": "SC.pass.gem.nom.subj_Neg.jmi",
        "510120": "SC.pass.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610120": "SC.pass.gem.nom.subj_Neg.jwtj",
        "710120": "SC.pass.gem.nom.subj_Neg.jwt",
        "810120": "SC.pass.gem.nom.subj_Neg.w/ꜣ",
        "910120": "SC.pass.gem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10121": "SC.pass.gem(redupl).1sg",
        "110121": "SC.pass.gem.1sg_Neg.n",
        "210121": "SC.pass.gem.1sg_Neg.nn",
        "310121": "SC.pass.gem.1sg_Neg.n js",
        "410121": "SC.pass.gem.1sg_Neg.jmi",
        "510121": "SC.pass.gem.1sg_Neg.n-zp/jwt-zp",
        "610121": "SC.pass.gem.1sg_Neg.jwtj",
        "710121": "SC.pass.gem.1sg_Neg.jwt",
        "810121": "SC.pass.gem.1sg_Neg.w/ꜣ",
        "910121": "SC.pass.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10122": "SC.pass.gem(redupl).2sgm",
        "110122": "SC.pass.gem.2sgm_Neg.n",
        "210122": "SC.pass.gem.2sgm_Neg.nn",
        "310122": "SC.pass.gem.2sgm_Neg.n js",
        "410122": "SC.pass.gem.2sgm_Neg.jmi",
        "510122": "SC.pass.gem.2sgm_Neg.n-zp/jwt-zp",
        "610122": "SC.pass.gem.2sgm_Neg.jwtj",
        "710122": "SC.pass.gem.2sgm_Neg.jwt",
        "810122": "SC.pass.gem.2sgm_Neg.w/ꜣ",
        "910122": "SC.pass.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10123": "SC.pass.gem(redupl).sgf",
        "110123": "SC.pass.gem.2sgf_Neg.n",
        "210123": "SC.pass.gem.2sgf_Neg.nn",
        "310123": "SC.pass.gem.2sgf_Neg.n js",
        "410123": "SC.pass.gem.2sgf_Neg.jmi",
        "510123": "SC.pass.gem.2sgf_Neg.n-zp/jwt-zp",
        "610123": "SC.pass.gem.2sgf_Neg.jwtj",
        "710123": "SC.pass.gem.2sgf_Neg.jwt",
        "810123": "SC.pass.gem.2sgf_Neg.w/ꜣ",
        "910123": "SC.pass.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10124": "SC.pass.gem(redupl).3sgm",
        "110124": "SC.pass.gem.3sgm_Neg.n",
        "210124": "SC.pass.gem.3sgm_Neg.nn",
        "310124": "SC.pass.gem.3sgm_Neg.n js",
        "410124": "SC.pass.gem.3sgm_Neg.jmi",
        "510124": "SC.pass.gem.3sgm_Neg.n-zp/jwt-zp",
        "610124": "SC.pass.gem.3sgm_Neg.jwtj",
        "710124": "SC.pass.gem.3sgm_Neg.jwt",
        "810124": "SC.pass.gem.3sgm_Neg.w/ꜣ",
        "910124": "SC.pass.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10125": "SC.pass.gem(redupl).3sgf",
        "110125": "SC.pass.gem.3sgf_Neg.n",
        "210125": "SC.pass.gem.3sgf_Neg.nn",
        "310125": "SC.pass.gem.3sgf_Neg.n js",
        "410125": "SC.pass.gem.3sgf_Neg.jmi",
        "510125": "SC.pass.gem.3sgf_Neg.n-zp/jwt-zp",
        "610125": "SC.pass.gem.3sgf_Neg.jwtj",
        "710125": "SC.pass.gem.3sgf_Neg.jwt",
        "810125": "SC.pass.gem.3sgf_Neg.w/ꜣ",
        "910125": "SC.pass.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10126": "SC.pass.gem(redupl).3sg",
        "110126": "SC.pass.gem.3sg_Neg.n",
        "210126": "SC.pass.gem.3sg_Neg.nn",
        "310126": "SC.pass.gem.3sg_Neg.n js",
        "410126": "SC.pass.gem.3sg_Neg.jmi",
        "510126": "SC.pass.gem.3sg_Neg.n-zp/jwt-zp",
        "610126": "SC.pass.gem.3sg_Neg.jwtj",
        "710126": "SC.pass.gem.3sg_Neg.jwt",
        "810126": "SC.pass.gem.3sg_Neg.w/ꜣ",
        "910126": "SC.pass.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10127": "SC.pass.gem(redupl).1pl",
        "-10127": "SC.pass.gem(redupl).1du",
        "110127": "SC.pass.gem.1pl_Neg.n",
        "-110127": "SC.pass.gem.1du_Neg.n",
        "210127": "SC.pass.gem.1pl_Neg.nn",
        "-210127": "SC.pass.gem.1du_Neg.nn",
        "310127": "SC.pass.gem.1pl_Neg.n js",
        "-310127": "SC.pass.gem.1du_Neg.n js",
        "410127": "SC.pass.gem.1pl_Neg.jmi",
        "-410127": "SC.pass.gem.1du_Neg.jmi",
        "510127": "SC.pass.gem.1pl_Neg.n-zp/jwt-zp",
        "-510127": "SC.pass.gem.1du_Neg.n-zp/jwt-zp",
        "610127": "SC.pass.gem.1pl_Neg.jwtj",
        "-610127": "SC.pass.gem.1du_Neg.jwtj",
        "710127": "SC.pass.gem.1pl_Neg.jwt",
        "-710127": "SC.pass.gem.1du_Neg.jwt",
        "810127": "SC.pass.gem.1pl_Neg.w/ꜣ",
        "-810127": "SC.pass.gem.1du_Neg.w/ꜣ",
        "910127": "SC.pass.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910127": "SC.pass.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10128": "SC.pass.gem(redupl).2pl",
        "-10128": "SC.pass.gem(redupl).2du",
        "110128": "SC.pass.gem.2pl_Neg.n",
        "-110128": "SC.pass.gem.2du_Neg.n",
        "210128": "SC.pass.gem.2pl_Neg.nn",
        "-210128": "SC.pass.gem.2du_Neg.nn",
        "310128": "SC.pass.gem.2pl_Neg.n js",
        "-310128": "SC.pass.gem.2du_Neg.n js",
        "410128": "SC.pass.gem.2pl_Neg.jmi",
        "-410128": "SC.pass.gem.2du_Neg.jmi",
        "510128": "SC.pass.gem.2pl_Neg.n-zp/jwt-zp",
        "-510128": "SC.pass.gem.2du_Neg.n-zp/jwt-zp",
        "610128": "SC.pass.gem.2pl_Neg.jwtj",
        "-610128": "SC.pass.gem.2du_Neg.jwtj",
        "710128": "SC.pass.gem.2pl_Neg.jwt",
        "-710128": "SC.pass.gem.2du_Neg.jwt",
        "810128": "SC.pass.gem.2pl_Neg.w/ꜣ",
        "-810128": "SC.pass.gem.2du_Neg.w/ꜣ",
        "910128": "SC.pass.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910128": "SC.pass.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10129": "SC.pass.gem(redupl).3pl",
        "-10129": "SC.pass.gem(redupl).3du",
        "110129": "SC.pass.gem.3pl_Neg.n",
        "-110129": "SC.pass.gem.3du_Neg.n",
        "210129": "SC.pass.gem.3pl_Neg.nn",
        "-210129": "SC.pass.gem.3du_Neg.nn",
        "310129": "SC.pass.gem.3pl_Neg.n js",
        "-310129": "SC.pass.gem.3du_Neg.n js",
        "410129": "SC.pass.gem.3pl_Neg.jmi",
        "-410129": "SC.pass.gem.3du_Neg.jmi",
        "510129": "SC.pass.gem.3pl_Neg.n-zp/jwt-zp",
        "-510129": "SC.pass.gem.3du_Neg.n-zp/jwt-zp",
        "610129": "SC.pass.gem.3pl_Neg.jwtj",
        "-610129": "SC.pass.gem.3du_Neg.jwtj",
        "710129": "SC.pass.gem.3pl_Neg.jwt",
        "-710129": "SC.pass.gem.3du_Neg.jwt",
        "810129": "SC.pass.gem.3pl_Neg.w/ꜣ",
        "-810129": "SC.pass.gem.3du_Neg.w/ꜣ",
        "910129": "SC.pass.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910129": "SC.pass.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10140": "SC.act.spec",
        "110140": "SC.act.spec.nom.subj_Neg.n",
        "210140": "SC.act.spec.nom.subj_Neg.nn",
        "310140": "SC.act.spec.nom.subj_Neg.n js",
        "410140": "SC.act.spec.nom.subj_Neg.jmi",
        "510140": "SC.act.spec.nom.subj_Neg.n-zp/jwt-zp",
        "610140": "SC.act.spec.nom.subj_Neg.jwtj",
        "710140": "SC.act.spec.nom.subj_Neg.jwt",
        "810140": "SC.act.spec.nom.subj_Neg.w/ꜣ",
        "910140": "SC.act.spec.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10141": "SC.act.spec.1sg",
        "110141": "SC.act.spec.1sg_Neg.n",
        "210141": "SC.act.spec.1sg_Neg.nn",
        "310141": "SC.act.spec.1sg_Neg.n js",
        "410141": "SC.act.spec.1sg_Neg.jmi",
        "510141": "SC.act.spec.1sg_Neg.n-zp/jwt-zp",
        "610141": "SC.act.spec.1sg_Neg.jwtj",
        "710141": "SC.act.spec.1sg_Neg.jwt",
        "810141": "SC.act.spec.1sg_Neg.w/ꜣ",
        "910141": "SC.act.spec.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10142": "SC.act.spec.2sgm",
        "110142": "SC.act.spec.2sgm_Neg.n",
        "210142": "SC.act.spec.2sgm_Neg.nn",
        "310142": "SC.act.spec.2sgm_Neg.n js",
        "410142": "SC.act.spec.2sgm_Neg.jmi",
        "510142": "SC.act.spec.2sgm_Neg.n-zp/jwt-zp",
        "610142": "SC.act.spec.2sgm_Neg.jwtj",
        "710142": "SC.act.spec.2sgm_Neg.jwt",
        "810142": "SC.act.spec.2sgm_Neg.w/ꜣ",
        "910142": "SC.act.spec.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10143": "SC.act.spec.sgf",
        "110143": "SC.act.spec.2sgf_Neg.n",
        "210143": "SC.act.spec.2sgf_Neg.nn",
        "310143": "SC.act.spec.2sgf_Neg.n js",
        "410143": "SC.act.spec.2sgf_Neg.jmi",
        "510143": "SC.act.spec.2sgf_Neg.n-zp/jwt-zp",
        "610143": "SC.act.spec.2sgf_Neg.jwtj",
        "710143": "SC.act.spec.2sgf_Neg.jwt",
        "810143": "SC.act.spec.2sgf_Neg.w/ꜣ",
        "910143": "SC.act.spec.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10144": "SC.act.spec.3sgm",
        "110144": "SC.act.spec.3sgm_Neg.n",
        "210144": "SC.act.spec.3sgm_Neg.nn",
        "310144": "SC.act.spec.3sgm_Neg.n js",
        "410144": "SC.act.spec.3sgm_Neg.jmi",
        "510144": "SC.act.spec.3sgm_Neg.n-zp/jwt-zp",
        "610144": "SC.act.spec.3sgm_Neg.jwtj",
        "710144": "SC.act.spec.3sgm_Neg.jwt",
        "810144": "SC.act.spec.3sgm_Neg.w/ꜣ",
        "910144": "SC.act.spec.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10145": "SC.act.spec.3sgf",
        "110145": "SC.act.spec.3sgf_Neg.n",
        "210145": "SC.act.spec.3sgf_Neg.nn",
        "310145": "SC.act.spec.3sgf_Neg.n js",
        "410145": "SC.act.spec.3sgf_Neg.jmi",
        "510145": "SC.act.spec.3sgf_Neg.n-zp/jwt-zp",
        "610145": "SC.act.spec.3sgf_Neg.jwtj",
        "710145": "SC.act.spec.3sgf_Neg.jwt",
        "810145": "SC.act.spec.3sgf_Neg.w/ꜣ",
        "910145": "SC.act.spec.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10146": "SC.act.spec.3sg",
        "110146": "SC.act.spec.3sg_Neg.n",
        "210146": "SC.act.spec.3sg_Neg.nn",
        "310146": "SC.act.spec.3sg_Neg.n js",
        "410146": "SC.act.spec.3sg_Neg.jmi",
        "510146": "SC.act.spec.3sg_Neg.n-zp/jwt-zp",
        "610146": "SC.act.spec.3sg_Neg.jwtj",
        "710146": "SC.act.spec.3sg_Neg.jwt",
        "810146": "SC.act.spec.3sg_Neg.w/ꜣ",
        "910146": "SC.act.spec.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10147": "SC.act.spec.1pl",
        "-10147": "SC.act.spec.1du",
        "110147": "SC.act.spec.1pl_Neg.n",
        "-110147": "SC.act.spec.1du_Neg.n",
        "210147": "SC.act.spec.1pl_Neg.nn",
        "-210147": "SC.act.spec.1du_Neg.nn",
        "310147": "SC.act.spec.1pl_Neg.n js",
        "-310147": "SC.act.spec.1du_Neg.n js",
        "410147": "SC.act.spec.1pl_Neg.jmi",
        "-410147": "SC.act.spec.1du_Neg.jmi",
        "510147": "SC.act.spec.1pl_Neg.n-zp/jwt-zp",
        "-510147": "SC.act.spec.1du_Neg.n-zp/jwt-zp",
        "610147": "SC.act.spec.1pl_Neg.jwtj",
        "-610147": "SC.act.spec.1du_Neg.jwtj",
        "710147": "SC.act.spec.1pl_Neg.jwt",
        "-710147": "SC.act.spec.1du_Neg.jwt",
        "810147": "SC.act.spec.1pl_Neg.w/ꜣ",
        "-810147": "SC.act.spec.1du_Neg.w/ꜣ",
        "910147": "SC.act.spec.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910147": "SC.act.spec.1du_Neg.nfr/nfr-n/nfr-pw",
        "10148": "SC.act.spec.2pl",
        "-10148": "SC.act.spec.2du",
        "110148": "SC.act.spec.2pl_Neg.n",
        "-110148": "SC.act.spec.2du_Neg.n",
        "210148": "SC.act.spec.2pl_Neg.nn",
        "-210148": "SC.act.spec.2du_Neg.nn",
        "310148": "SC.act.spec.2pl_Neg.n js",
        "-310148": "SC.act.spec.2du_Neg.n js",
        "410148": "SC.act.spec.2pl_Neg.jmi",
        "-410148": "SC.act.spec.2du_Neg.jmi",
        "510148": "SC.act.spec.2pl_Neg.n-zp/jwt-zp",
        "-510148": "SC.act.spec.2du_Neg.n-zp/jwt-zp",
        "610148": "SC.act.spec.2pl_Neg.jwtj",
        "-610148": "SC.act.spec.2du_Neg.jwtj",
        "710148": "SC.act.spec.2pl_Neg.jwt",
        "-710148": "SC.act.spec.2du_Neg.jwt",
        "810148": "SC.act.spec.2pl_Neg.w/ꜣ",
        "-810148": "SC.act.spec.2du_Neg.w/ꜣ",
        "910148": "SC.act.spec.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910148": "SC.act.spec.2du_Neg.nfr/nfr-n/nfr-pw",
        "10149": "SC.act.spec.3pl",
        "-10149": "SC.act.spec.3du",
        "110149": "SC.act.spec.3pl_Neg.n",
        "-110149": "SC.act.spec.3du_Neg.n",
        "210149": "SC.act.spec.3pl_Neg.nn",
        "-210149": "SC.act.spec.3du_Neg.nn",
        "310149": "SC.act.spec.3pl_Neg.n js",
        "-310149": "SC.act.spec.3du_Neg.n js",
        "410149": "SC.act.spec.3pl_Neg.jmi",
        "-410149": "SC.act.spec.3du_Neg.jmi",
        "510149": "SC.act.spec.3pl_Neg.n-zp/jwt-zp",
        "-510149": "SC.act.spec.3du_Neg.n-zp/jwt-zp",
        "610149": "SC.act.spec.3pl_Neg.jwtj",
        "-610149": "SC.act.spec.3du_Neg.jwtj",
        "710149": "SC.act.spec.3pl_Neg.jwt",
        "-710149": "SC.act.spec.3du_Neg.jwt",
        "810149": "SC.act.spec.3pl_Neg.w/ꜣ",
        "-810149": "SC.act.spec.3du_Neg.w/ꜣ",
        "910149": "SC.act.spec.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910149": "SC.act.spec.3du_Neg.nfr/nfr-n/nfr-pw",
        "10160": "SC.pass.spec.nom.subj",
        "110160": "SC.pass.spec.nom.subj_Neg.n",
        "210160": "SC.pass.spec.nom.subj_Neg.nn",
        "310160": "SC.pass.spec.nom.subj_Neg.n js",
        "410160": "SC.pass.spec.nom.subj_Neg.jmi",
        "510160": "SC.pass.spec.nom.subj_Neg.n-zp/jwt-zp",
        "610160": "SC.pass.spec.nom.subj_Neg.jwtj",
        "710160": "SC.pass.spec.nom.subj_Neg.jwt",
        "810160": "SC.pass.spec.nom.subj_Neg.w/ꜣ",
        "910160": "SC.pass.spec.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10161": "SC.pass.spec.1sg",
        "110161": "SC.pass.spec.1sg_Neg.n",
        "210161": "SC.pass.spec.1sg_Neg.nn",
        "310161": "SC.pass.spec.1sg_Neg.n js",
        "410161": "SC.pass.spec.1sg_Neg.jmi",
        "510161": "SC.pass.spec.1sg_Neg.n-zp/jwt-zp",
        "610161": "SC.pass.spec.1sg_Neg.jwtj",
        "710161": "SC.pass.spec.1sg_Neg.jwt",
        "810161": "SC.pass.spec.1sg_Neg.w/ꜣ",
        "910161": "SC.pass.spec.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10162": "SC.pass.spec.2sgm",
        "110162": "SC.pass.spec.2sgm_Neg.n",
        "210162": "SC.pass.spec.2sgm_Neg.nn",
        "310162": "SC.pass.spec.2sgm_Neg.n js",
        "410162": "SC.pass.spec.2sgm_Neg.jmi",
        "510162": "SC.pass.spec.2sgm_Neg.n-zp/jwt-zp",
        "610162": "SC.pass.spec.2sgm_Neg.jwtj",
        "710162": "SC.pass.spec.2sgm_Neg.jwt",
        "810162": "SC.pass.spec.2sgm_Neg.w/ꜣ",
        "910162": "SC.pass.spec.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10163": "SC.pass.spec.2sgf",
        "110163": "SC.pass.spec.2sgf_Neg.n",
        "210163": "SC.pass.spec.2sgf_Neg.nn",
        "310163": "SC.pass.spec.2sgf_Neg.n js",
        "410163": "SC.pass.spec.2sgf_Neg.jmi",
        "510163": "SC.pass.spec.2sgf_Neg.n-zp/jwt-zp",
        "610163": "SC.pass.spec.2sgf_Neg.jwtj",
        "710163": "SC.pass.spec.2sgf_Neg.jwt",
        "810163": "SC.pass.spec.2sgf_Neg.w/ꜣ",
        "910163": "SC.pass.spec.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10164": "SC.pass.spec.3sgm",
        "110164": "SC.pass.spec.3sgm_Neg.n",
        "210164": "SC.pass.spec.3sgm_Neg.nn",
        "310164": "SC.pass.spec.3sgm_Neg.n js",
        "410164": "SC.pass.spec.3sgm_Neg.jmi",
        "510164": "SC.pass.spec.3sgm_Neg.n-zp/jwt-zp",
        "610164": "SC.pass.spec.3sgm_Neg.jwtj",
        "710164": "SC.pass.spec.3sgm_Neg.jwt",
        "810164": "SC.pass.spec.3sgm_Neg.w/ꜣ",
        "910164": "SC.pass.spec.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10165": "SC.pass.spec.3sgf",
        "110165": "SC.pass.spec.3sgf_Neg.n",
        "210165": "SC.pass.spec.3sgf_Neg.nn",
        "310165": "SC.pass.spec.3sgf_Neg.n js",
        "410165": "SC.pass.spec.3sgf_Neg.jmi",
        "510165": "SC.pass.spec.3sgf_Neg.n-zp/jwt-zp",
        "610165": "SC.pass.spec.3sgf_Neg.jwtj",
        "710165": "SC.pass.spec.3sgf_Neg.jwt",
        "810165": "SC.pass.spec.3sgf_Neg.w/ꜣ",
        "910165": "SC.pass.spec.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10166": "SC.pass.spec.3sg",
        "110166": "SC.pass.spec.3sg_Neg.n",
        "210166": "SC.pass.spec.3sg_Neg.nn",
        "310166": "SC.pass.spec.3sg_Neg.n js",
        "410166": "SC.pass.spec.3sg_Neg.jmi",
        "510166": "SC.pass.spec.3sg_Neg.n-zp/jwt-zp",
        "610166": "SC.pass.spec.3sg_Neg.jwtj",
        "710166": "SC.pass.spec.3sg_Neg.jwt",
        "810166": "SC.pass.spec.3sg_Neg.w/ꜣ",
        "910166": "SC.pass.spec.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10167": "SC.pass.spec.1pl",
        "-10167": "SC.pass.spec.1du",
        "110167": "SC.pass.spec.1pl_Neg.n",
        "-110167": "SC.pass.spec.1du_Neg.n",
        "210167": "SC.pass.spec.1pl_Neg.nn",
        "-210167": "SC.pass.spec.1du_Neg.nn",
        "310167": "SC.pass.spec.1pl_Neg.n js",
        "-310167": "SC.pass.spec.1du_Neg.n js",
        "410167": "SC.pass.spec.1pl_Neg.jmi",
        "-410167": "SC.pass.spec.1du_Neg.jmi",
        "510167": "SC.pass.spec.1pl_Neg.n-zp/jwt-zp",
        "-510167": "SC.pass.spec.1du_Neg.n-zp/jwt-zp",
        "610167": "SC.pass.spec.1pl_Neg.jwtj",
        "-610167": "SC.pass.spec.1du_Neg.jwtj",
        "710167": "SC.pass.spec.1pl_Neg.jwt",
        "-710167": "SC.pass.spec.1du_Neg.jwt",
        "810167": "SC.pass.spec.1pl_Neg.w/ꜣ",
        "-810167": "SC.pass.spec.1du_Neg.w/ꜣ",
        "910167": "SC.pass.spec.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910167": "SC.pass.spec.1du_Neg.nfr/nfr-n/nfr-pw",
        "10168": "SC.pass.spec.2pl",
        "-10168": "SC.pass.spec.2du",
        "110168": "SC.pass.spec.2pl_Neg.n",
        "-110168": "SC.pass.spec.2du_Neg.n",
        "210168": "SC.pass.spec.2pl_Neg.nn",
        "-210168": "SC.pass.spec.2du_Neg.nn",
        "310168": "SC.pass.spec.2pl_Neg.n js",
        "-310168": "SC.pass.spec.2du_Neg.n js",
        "410168": "SC.pass.spec.2pl_Neg.jmi",
        "-410168": "SC.pass.spec.2du_Neg.jmi",
        "510168": "SC.pass.spec.2pl_Neg.n-zp/jwt-zp",
        "-510168": "SC.pass.spec.2du_Neg.n-zp/jwt-zp",
        "610168": "SC.pass.spec.2pl_Neg.jwtj",
        "-610168": "SC.pass.spec.2du_Neg.jwtj",
        "710168": "SC.pass.spec.2pl_Neg.jwt",
        "-710168": "SC.pass.spec.2du_Neg.jwt",
        "810168": "SC.pass.spec.2pl_Neg.w/ꜣ",
        "-810168": "SC.pass.spec.2du_Neg.w/ꜣ",
        "910168": "SC.pass.spec.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910168": "SC.pass.spec.2du_Neg.nfr/nfr-n/nfr-pw",
        "10169": "SC.pass.spec.3pl",
        "-10169": "SC.pass.spec.3du",
        "110169": "SC.pass.spec.3pl_Neg.n",
        "-110169": "SC.pass.spec.3du_Neg.n",
        "210169": "SC.pass.spec.3pl_Neg.nn",
        "-210169": "SC.pass.spec.3du_Neg.nn",
        "310169": "SC.pass.spec.3pl_Neg.n js",
        "-310169": "SC.pass.spec.3du_Neg.n js",
        "410169": "SC.pass.spec.3pl_Neg.jmi",
        "-410169": "SC.pass.spec.3du_Neg.jmi",
        "510169": "SC.pass.spec.3pl_Neg.n-zp/jwt-zp",
        "-510169": "SC.pass.spec.3du_Neg.n-zp/jwt-zp",
        "610169": "SC.pass.spec.3pl_Neg.jwtj",
        "-610169": "SC.pass.spec.3du_Neg.jwtj",
        "710169": "SC.pass.spec.3pl_Neg.jwt",
        "-710169": "SC.pass.spec.3du_Neg.jwt",
        "810169": "SC.pass.spec.3pl_Neg.w/ꜣ",
        "-810169": "SC.pass.spec.3du_Neg.w/ꜣ",
        "910169": "SC.pass.spec.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910169": "SC.pass.spec.3du_Neg.nfr/nfr-n/nfr-pw",
        "10170": "SC.tw.pass.spec.nom.subj",
        "110170": "SC.tw.pass.spec.nom.subj_Neg.n",
        "210170": "SC.tw.pass.spec.nom.subj_Neg.nn",
        "310170": "SC.tw.pass.spec.nom.subj_Neg.n js",
        "410170": "SC.tw.pass.spec.nom.subj_Neg.jmi",
        "510170": "SC.tw.pass.spec.nom.subj_Neg.n-zp/jwt-zp",
        "610170": "SC.tw.pass.spec.nom.subj_Neg.jwtj",
        "710170": "SC.tw.pass.spec.nom.subj_Neg.jwt",
        "810170": "SC.tw.pass.spec.nom.subj_Neg.w/ꜣ",
        "910170": "SC.tw.pass.spec.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10171": "SC.tw.pass.spec.1sg",
        "110171": "SC.tw.pass.spec.1sg_Neg.n",
        "210171": "SC.tw.pass.spec.1sg_Neg.nn",
        "310171": "SC.tw.pass.spec.1sg_Neg.n js",
        "410171": "SC.tw.pass.spec.1sg_Neg.jmi",
        "510171": "SC.tw.pass.spec.1sg_Neg.n-zp/jwt-zp",
        "610171": "SC.tw.pass.spec.1sg_Neg.jwtj",
        "710171": "SC.tw.pass.spec.1sg_Neg.jwt",
        "810171": "SC.tw.pass.spec.1sg_Neg.w/ꜣ",
        "910171": "SC.tw.pass.spec.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10172": "SC.tw.pass.spec.2sgm",
        "110172": "SC.tw.pass.spec.2sgm_Neg.n",
        "210172": "SC.tw.pass.spec.2sgm_Neg.nn",
        "310172": "SC.tw.pass.spec.2sgm_Neg.n js",
        "410172": "SC.tw.pass.spec.2sgm_Neg.jmi",
        "510172": "SC.tw.pass.spec.2sgm_Neg.n-zp/jwt-zp",
        "610172": "SC.tw.pass.spec.2sgm_Neg.jwtj",
        "710172": "SC.tw.pass.spec.2sgm_Neg.jwt",
        "810172": "SC.tw.pass.spec.2sgm_Neg.w/ꜣ",
        "910172": "SC.tw.pass.spec.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10173": "SC.tw.pass.spec.2sgf",
        "110173": "SC.tw.pass.spec.2sgf_Neg.n",
        "210173": "SC.tw.pass.spec.2sgf_Neg.nn",
        "310173": "SC.tw.pass.spec.2sgf_Neg.n js",
        "410173": "SC.tw.pass.spec.2sgf_Neg.jmi",
        "510173": "SC.tw.pass.spec.2sgf_Neg.n-zp/jwt-zp",
        "610173": "SC.tw.pass.spec.2sgf_Neg.jwtj",
        "710173": "SC.tw.pass.spec.2sgf_Neg.jwt",
        "810173": "SC.tw.pass.spec.2sgf_Neg.w/ꜣ",
        "910173": "SC.tw.pass.spec.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10174": "SC.tw.pass.spec.3sgm",
        "110174": "SC.tw.pass.spec.3sgm_Neg.n",
        "210174": "SC.tw.pass.spec.3sgm_Neg.nn",
        "310174": "SC.tw.pass.spec.3sgm_Neg.n js",
        "410174": "SC.tw.pass.spec.3sgm_Neg.jmi",
        "510174": "SC.tw.pass.spec.3sgm_Neg.n-zp/jwt-zp",
        "610174": "SC.tw.pass.spec.3sgm_Neg.jwtj",
        "710174": "SC.tw.pass.spec.3sgm_Neg.jwt",
        "810174": "SC.tw.pass.spec.3sgm_Neg.w/ꜣ",
        "910174": "SC.tw.pass.spec.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10175": "SC.tw.pass.spec.3sgf",
        "110175": "SC.tw.pass.spec.3sgf_Neg.n",
        "210175": "SC.tw.pass.spec.3sgf_Neg.nn",
        "310175": "SC.tw.pass.spec.3sgf_Neg.n js",
        "410175": "SC.tw.pass.spec.3sgf_Neg.jmi",
        "510175": "SC.tw.pass.spec.3sgf_Neg.n-zp/jwt-zp",
        "610175": "SC.tw.pass.spec.3sgf_Neg.jwtj",
        "710175": "SC.tw.pass.spec.3sgf_Neg.jwt",
        "810175": "SC.tw.pass.spec.3sgf_Neg.w/ꜣ",
        "910175": "SC.tw.pass.spec.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10176": "SC.tw.pass.spec.3sg",
        "110176": "SC.tw.pass.spec.3sg_Neg.n",
        "210176": "SC.tw.pass.spec.3sg_Neg.nn",
        "310176": "SC.tw.pass.spec.3sg_Neg.n js",
        "410176": "SC.tw.pass.spec.3sg_Neg.jmi",
        "510176": "SC.tw.pass.spec.3sg_Neg.n-zp/jwt-zp",
        "610176": "SC.tw.pass.spec.3sg_Neg.jwtj",
        "710176": "SC.tw.pass.spec.3sg_Neg.jwt",
        "810176": "SC.tw.pass.spec.3sg_Neg.w/ꜣ",
        "910176": "SC.tw.pass.spec.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10177": "SC.tw.pass.spec.1pl",
        "-10177": "SC.tw.pass.spec.1du",
        "110177": "SC.tw.pass.spec.1pl_Neg.n",
        "-110177": "SC.tw.pass.spec.1du_Neg.n",
        "210177": "SC.tw.pass.spec.1pl_Neg.nn",
        "-210177": "SC.tw.pass.spec.1du_Neg.nn",
        "310177": "SC.tw.pass.spec.1pl_Neg.n js",
        "-310177": "SC.tw.pass.spec.1du_Neg.n js",
        "410177": "SC.tw.pass.spec.1pl_Neg.jmi",
        "-410177": "SC.tw.pass.spec.3pl_Neg.jmi",
        "510177": "SC.tw.pass.spec.1pl_Neg.n-zp/jwt-zp",
        "-510177": "SC.tw.pass.spec.1du_Neg.n-zp/jwt-zp",
        "610177": "SC.tw.pass.spec.1pl_Neg.jwtj",
        "-610177": "SC.w.act.ngem.nom.subj_Neg.jwtj",
        "710177": "SC.tw.pass.spec.1pl_Neg.jwt",
        "-710177": "SC.tw.pass.spec.1du_Neg.jwt",
        "810177": "SC.tw.pass.spec.1pl_Neg.w/ꜣ",
        "-810177": "SC.tw.pass.spec.1du_Neg.w/ꜣ",
        "910177": "SC.tw.pass.spec.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910177": "SC.tw.pass.spec.1du_Neg.nfr/nfr-n/nfr-pw",
        "10178": "SC.tw.pass.spec.2pl",
        "-10178": "SC.tw.pass.spec.2du",
        "110178": "SC.tw.pass.spec.2pl_Neg.n",
        "-110178": "SC.tw.pass.spec.2du_Neg.n",
        "210178": "SC.tw.pass.spec.2pl_Neg.nn",
        "-210178": "SC.tw.pass.spec.2du_Neg.nn",
        "310178": "SC.tw.pass.spec.2pl_Neg.n js",
        "-310178": "SC.tw.pass.spec.2du_Neg.n js",
        "410178": "SC.tw.pass.spec.2pl_Neg.jmi",
        "-410178": "SC.tw.pass.spec.1du_Neg.jmi",
        "510178": "SC.tw.pass.spec.2pl_Neg.n-zp/jwt-zp",
        "-510178": "SC.tw.pass.spec.2du_Neg.n-zp/jwt-zp",
        "610178": "SC.tw.pass.spec.2pl_Neg.jwtj",
        "-610178": "SC.w.act.ngem.1sg_Neg.jwtj",
        "710178": "SC.tw.pass.spec.2pl_Neg.jwt",
        "-710178": "SC.tw.pass.spec.2du_Neg.jwt",
        "810178": "SC.tw.pass.spec.2pl_Neg.w/ꜣ",
        "-810178": "SC.tw.pass.spec.2du_Neg.w/ꜣ",
        "910178": "SC.tw.pass.spec.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910178": "SC.tw.pass.spec.2du_Neg.nfr/nfr-n/nfr-pw",
        "10179": "SC.tw.pass.spec.3pl",
        "-10179": "SC.tw.pass.spec.3du",
        "110179": "SC.tw.pass.spec.3pl_Neg.n",
        "-110179": "SC.tw.pass.spec.3du_Neg.n",
        "210179": "SC.tw.pass.spec.3pl_Neg.nn",
        "-210179": "SC.tw.pass.spec.3du_Neg.nn",
        "310179": "SC.tw.pass.spec.3pl_Neg.n js",
        "-310179": "SC.tw.pass.spec.3du_Neg.n js",
        "410179": "SC.tw.pass.spec.3pl_Neg.jmi",
        "-410179": "SC.tw.pass.spec.2du_Neg.jmi",
        "510179": "SC.tw.pass.spec.3pl_Neg.n-zp/jwt-zp",
        "-510179": "SC.tw.pass.spec.3du_Neg.n-zp/jwt-zp",
        "610179": "SC.tw.pass.spec.3pl_Neg.jwtj",
        "-610179": "SC.w.act.ngem.2sgm_Neg.jwtj",
        "710179": "SC.tw.pass.spec.3pl_Neg.jwt",
        "-710179": "SC.tw.pass.spec.3du_Neg.jwt",
        "810179": "SC.tw.pass.spec.3pl_Neg.w/ꜣ",
        "-810179": "SC.tw.pass.spec.3du_Neg.w/ꜣ",
        "910179": "SC.tw.pass.spec.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910179": "SC.tw.pass.spec.3du_Neg.nfr/nfr-n/nfr-pw",
        "10180": "SC.w.act.ngem.nom.subj",
        "110180": "SC.w.act.ngem.nom.subj_Neg.n",
        "210180": "SC.w.act.ngem.nom.subj_Neg.nn",
        "310180": "SC.w.act.ngem.nom.subj_Neg.n js",
        "410180": "SC.w.act.ngem.nom.subj_Neg.jmi",
        "510180": "SC.w.act.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "710180": "SC.w.act.ngem.nom.subj_Neg.jwt",
        "810180": "SC.w.act.ngem.nom.subj_Neg.w/ꜣ",
        "910180": "SC.w.act.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10181": "SC.w.act.ngem.1sg",
        "110181": "SC.w.act.ngem.1sg_Neg.n",
        "210181": "SC.w.act.ngem.1sg_Neg.nn",
        "310181": "SC.w.act.ngem.1sg_Neg.n js",
        "410181": "SC.w.act.ngem.1sg_Neg.jmi",
        "510181": "SC.w.act.ngem.1sg_Neg.n-zp/jwt-zp",
        "710181": "SC.w.act.ngem.1sg_Neg.jwt",
        "810181": "SC.w.act.ngem.1sg_Neg.w/ꜣ",
        "910181": "SC.w.act.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10182": "SC.w.act.ngem.2sgm",
        "110182": "SC.w.act.ngem.2sgm_Neg.n",
        "210182": "SC.w.act.ngem.2sgm_Neg.nn",
        "310182": "SC.w.act.ngem.2sgm_Neg.n js",
        "410182": "SC.w.act.ngem.2sgm_Neg.jmi",
        "510182": "SC.w.act.ngem.2sgm_Neg.n-zp/jwt-zp",
        "710182": "SC.w.act.ngem.2sgm_Neg.jwt",
        "810182": "SC.w.act.ngem.2sgm_Neg.w/ꜣ",
        "910182": "SC.w.act.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10183": "SC.w.act.ngem.2sgf",
        "110183": "SC.w.act.ngem.2sgf_Neg.n",
        "210183": "SC.w.act.ngem.2sgf_Neg.nn",
        "310183": "SC.w.act.ngem.2sgf_Neg.n js",
        "410183": "SC.w.act.ngem.2sgf_Neg.jmi",
        "510183": "SC.w.act.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610183": "SC.w.act.ngem.2sgf_Neg.jwtj",
        "710183": "SC.w.act.ngem.2sgf_Neg.jwt",
        "810183": "SC.w.act.ngem.2sgf_Neg.w/ꜣ",
        "910183": "SC.w.act.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10184": "SC.w.act.ngem.3sgm",
        "110184": "SC.w.act.ngem.3sgm_Neg.n",
        "210184": "SC.w.act.ngem.3sgm_Neg.nn",
        "310184": "SC.w.act.ngem.3sgm_Neg.n js",
        "410184": "SC.w.act.ngem.3sgm_Neg.jmi",
        "510184": "SC.w.act.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610184": "SC.w.act.ngem.3sgm_Neg.jwtj",
        "710184": "SC.w.act.ngem.3sgm_Neg.jwt",
        "810184": "SC.w.act.ngem.3sgm_Neg.w/ꜣ",
        "910184": "SC.w.act.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10185": "SC.w.act.ngem.3sgf",
        "110185": "SC.w.act.ngem.3sgf_Neg.n",
        "210185": "SC.w.act.ngem.3sgf_Neg.nn",
        "310185": "SC.w.act.ngem.3sgf_Neg.n js",
        "410185": "SC.w.act.ngem.3sgf_Neg.jmi",
        "510185": "SC.w.act.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610185": "SC.w.act.ngem.3sgf_Neg.jwtj",
        "710185": "SC.w.act.ngem.3sgf_Neg.jwt",
        "810185": "SC.w.act.ngem.3sgf_Neg.w/ꜣ",
        "910185": "SC.w.act.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10186": "SC.w.act.ngem.3sg",
        "110186": "SC.w.act.ngem.3sg_Neg.n",
        "210186": "SC.w.act.ngem.3sg_Neg.nn",
        "310186": "SC.w.act.ngem.3sg_Neg.n js",
        "410186": "SC.w.act.ngem.3sg_Neg.jmi",
        "510186": "SC.w.act.ngem.3sg_Neg.n-zp/jwt-zp",
        "610186": "SC.w.act.ngem.3sg_Neg.jwtj",
        "710186": "SC.w.act.ngem.3sg_Neg.jwt",
        "810186": "SC.w.act.ngem.3sg_Neg.w/ꜣ",
        "910186": "SC.w.act.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10187": "SC.w.act.ngem.1pl",
        "-10187": "SC.w.act.ngem.1du",
        "110187": "SC.w.act.ngem.1pl_Neg.n",
        "-110187": "SC.w.act.ngem.1du_Neg.n",
        "210187": "SC.w.act.ngem.1pl_Neg.nn",
        "-210187": "SC.w.act.ngem.1du_Neg.nn",
        "310187": "SC.w.act.ngem.1pl_Neg.n js",
        "-310187": "SC.w.act.ngem.1du_Neg.n js",
        "410187": "SC.w.act.ngem.1pl_Neg.jmi",
        "-410187": "SC.w.act.ngem.1du_Neg.jmi",
        "510187": "SC.w.act.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510187": "SC.w.act.ngem.1du_Neg.n-zp/jwt-zp",
        "610187": "SC.w.act.ngem.1pl_Neg.jwtj",
        "-610187": "SC.w.act.ngem.1du_Neg.jwtj",
        "710187": "SC.w.act.ngem.1pl_Neg.jwt",
        "-710187": "SC.w.act.ngem.1du_Neg.jwt",
        "810187": "SC.w.act.ngem.1pl_Neg.w/ꜣ",
        "-810187": "SC.w.act.ngem.1du_Neg.w/ꜣ",
        "910187": "SC.w.act.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910187": "SC.w.act.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10188": "SC.w.act.ngem.2pl",
        "-10188": "SC.w.act.ngem.2du",
        "110188": "SC.w.act.ngem.2pl_Neg.n",
        "-110188": "SC.w.act.ngem.2du_Neg.n",
        "210188": "SC.w.act.ngem.2pl_Neg.nn",
        "-210188": "SC.w.act.ngem.2du_Neg.nn",
        "310188": "SC.w.act.ngem.2pl_Neg.n js",
        "-310188": "SC.w.act.ngem.2du_Neg.n js",
        "410188": "SC.w.act.ngem.2pl_Neg.jmi",
        "-410188": "SC.w.act.ngem.2du_Neg.jmi",
        "510188": "SC.w.act.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510188": "SC.w.act.ngem.2du_Neg.n-zp/jwt-zp",
        "610188": "SC.w.act.ngem.2pl_Neg.jwtj",
        "-610188": "SC.w.act.ngem.2du_Neg.jwtj",
        "710188": "SC.w.act.ngem.2pl_Neg.jwt",
        "-710188": "SC.w.act.ngem.2du_Neg.jwt",
        "810188": "SC.w.act.ngem.2pl_Neg.w/ꜣ",
        "-810188": "SC.w.act.ngem.2du_Neg.w/ꜣ",
        "910188": "SC.w.act.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910188": "SC.w.act.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10189": "SC.w.act.ngem.3pl",
        "-10189": "SC.w.act.ngem.3du",
        "110189": "SC.w.act.ngem.3pl_Neg.n",
        "-110189": "SC.w.act.ngem.3du_Neg.n",
        "210189": "SC.w.act.ngem.3pl_Neg.nn",
        "-210189": "SC.w.act.ngem.3du_Neg.nn",
        "310189": "SC.w.act.ngem.3pl_Neg.n js",
        "-310189": "SC.w.act.ngem.3du_Neg.n js",
        "410189": "SC.w.act.ngem.3pl_Neg.jmi",
        "-410189": "SC.w.act.ngem.3du_Neg.jmi",
        "510189": "SC.w.act.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510189": "SC.w.act.ngem.3du_Neg.n-zp/jwt-zp",
        "610189": "SC.w.act.ngem.3pl_Neg.jwtj",
        "-610189": "SC.w.act.ngem.3du_Neg.jwtj",
        "710189": "SC.w.act.ngem.3pl_Neg.jwt",
        "-710189": "SC.w.act.ngem.3du_Neg.jwt",
        "810189": "SC.w.act.ngem.3pl_Neg.w/ꜣ",
        "-810189": "SC.w.act.ngem.3du_Neg.w/ꜣ",
        "910189": "SC.w.act.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910189": "SC.w.act.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10190": "SC.tw.pass.spec.impers",
        "110190": "SC.tw.pass.spec.impers_Neg.n",
        "10200": "SC.w.act.short.nom.subj",
        "710200": "SC.w.act.short.nom.subj_Neg.jwt",
        "10201": "SC.w.act.short.1sg",
        "10202": "SC.w.act.short.2sgm",
        "10203": "SC.w.act.short.2sgf",
        "10204": "SC.w.act.short.3sgm",
        "10205": "SC.w.act.short.3sgf",
        "10206": "SC.w.act.short.3sg",
        "10207": "SC.w.act.short.1pl",
        "10208": "SC.w.act.short.2pl",
        "10209": "SC.w.act.short.3pl",
        "10220": "SC.w.act.gem.nom.subj",
        "110220": "SC.w.act.gem.nom.subj_Neg.n",
        "210220": "SC.w.act.gem.nom.subj_Neg.nn",
        "310220": "SC.w.act.gem.nom.subj_Neg.n js",
        "410220": "SC.w.act.gem.nom.subj_Neg.jmi",
        "510220": "SC.w.act.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610220": "SC.w.act.gem.nom.subj_Neg.jwtj",
        "710220": "SC.w.act.gem.nom.subj_Neg.jwt",
        "810220": "SC.w.act.gem.nom.subj_Neg.w/ꜣ",
        "910220": "SC.w.act.gem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10221": "SC.w.act.gem.1sg",
        "110221": "SC.w.act.gem.1sg_Neg.n",
        "210221": "SC.w.act.gem.1sg_Neg.nn",
        "310221": "SC.w.act.gem.1sg_Neg.n js",
        "410221": "SC.w.act.gem.1sg_Neg.jmi",
        "510221": "SC.w.act.gem.1sg_Neg.n-zp/jwt-zp",
        "610221": "SC.w.act.gem.1sg_Neg.jwtj",
        "710221": "SC.w.act.gem.1sg_Neg.jwt",
        "810221": "SC.w.act.gem.1sg_Neg.w/ꜣ",
        "910221": "SC.w.act.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10222": "SC.w.act.gem.2sgm",
        "110222": "SC.w.act.gem.2sgm_Neg.n",
        "210222": "SC.w.act.gem.2sgm_Neg.nn",
        "310222": "SC.w.act.gem.2sgm_Neg.n js",
        "410222": "SC.w.act.gem.2sgm_Neg.jmi",
        "510222": "SC.w.act.gem.2sgm_Neg.n-zp/jwt-zp",
        "610222": "SC.w.act.gem.2sgm_Neg.jwtj",
        "710222": "SC.w.act.gem.2sgm_Neg.jwt",
        "810222": "SC.w.act.gem.2sgm_Neg.w/ꜣ",
        "910222": "SC.w.act.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10223": "SC.w.act.gem.2sgf",
        "110223": "SC.w.act.gem.2sgf_Neg.n",
        "210223": "SC.w.act.gem.2sgf_Neg.nn",
        "310223": "SC.w.act.gem.2sgf_Neg.n js",
        "410223": "SC.w.act.gem.2sgf_Neg.jmi",
        "510223": "SC.w.act.gem.2sgf_Neg.n-zp/jwt-zp",
        "610223": "SC.w.act.gem.2sgf_Neg.jwtj",
        "710223": "SC.w.act.gem.2sgf_Neg.jwt",
        "810223": "SC.w.act.gem.2sgf_Neg.w/ꜣ",
        "910223": "SC.w.act.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10224": "SC.w.act.gem.3sgm",
        "110224": "SC.w.act.gem.3sgm_Neg.n",
        "210224": "SC.w.act.gem.3sgm_Neg.nn",
        "310224": "SC.w.act.gem.3sgm_Neg.n js",
        "410224": "SC.w.act.gem.3sgm_Neg.jmi",
        "510224": "SC.w.act.gem.3sgm_Neg.n-zp/jwt-zp",
        "610224": "SC.w.act.gem.3sgm_Neg.jwtj",
        "710224": "SC.w.act.gem.3sgm_Neg.jwt",
        "810224": "SC.w.act.gem.3sgm_Neg.w/ꜣ",
        "910224": "SC.w.act.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10225": "SC.w.act.gem.3sgf",
        "110225": "SC.w.act.gem.3sgf_Neg.n",
        "210225": "SC.w.act.gem.3sgf_Neg.nn",
        "310225": "SC.w.act.gem.3sgf_Neg.n js",
        "410225": "SC.w.act.gem.3sgf_Neg.jmi",
        "510225": "SC.w.act.gem.3sgf_Neg.n-zp/jwt-zp",
        "610225": "SC.w.act.gem.3sgf_Neg.jwtj",
        "710225": "SC.w.act.gem.3sgf_Neg.jwt",
        "810225": "SC.w.act.gem.3sgf_Neg.w/ꜣ",
        "910225": "SC.w.act.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10226": "SC.w.act.gem.3sg",
        "110226": "SC.w.act.gem.3sg_Neg.n",
        "210226": "SC.w.act.gem.3sg_Neg.nn",
        "310226": "SC.w.act.gem.3sg_Neg.n js",
        "410226": "SC.w.act.gem.3sg_Neg.jmi",
        "510226": "SC.w.act.gem.3sg_Neg.n-zp/jwt-zp",
        "610226": "SC.w.act.gem.3sg_Neg.jwtj",
        "710226": "SC.w.act.gem.3sg_Neg.jwt",
        "810226": "SC.w.act.gem.3sg_Neg.w/ꜣ",
        "910226": "SC.w.act.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10227": "SC.w.act.gem.1pl",
        "-10227": "SC.w.act.gem.1du",
        "110227": "SC.w.act.gem.1pl_Neg.n",
        "-110227": "SC.w.act.gem.1du_Neg.n",
        "210227": "SC.w.act.gem.1pl_Neg.nn",
        "-210227": "SC.w.act.gem.1du_Neg.nn",
        "310227": "SC.w.act.gem.1pl_Neg.n js",
        "-310227": "SC.w.act.gem.1du_Neg.n js",
        "410227": "SC.w.act.gem.1pl_Neg.jmi",
        "-410227": "SC.w.act.gem.1du_Neg.jmi",
        "510227": "SC.w.act.gem.1pl_Neg.n-zp/jwt-zp",
        "-510227": "SC.w.act.gem.1du_Neg.n-zp/jwt-zp",
        "610227": "SC.w.act.gem.1pl_Neg.jwtj",
        "-610227": "SC.w.act.gem.1du_Neg.jwtj",
        "710227": "SC.w.act.gem.1pl_Neg.jwt",
        "-710227": "SC.w.act.gem.1du_Neg.jwt",
        "810227": "SC.w.act.gem.1pl_Neg.w/ꜣ",
        "-810227": "SC.w.act.gem.1du_Neg.w/ꜣ",
        "910227": "SC.w.act.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910227": "SC.w.act.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10228": "SC.w.act.gem.2pl",
        "-10228": "SC.w.act.gem.2du",
        "110228": "SC.w.act.gem.2pl_Neg.n",
        "-110228": "SC.w.act.gem.2du_Neg.n",
        "210228": "SC.w.act.gem.2pl_Neg.nn",
        "-210228": "SC.w.act.gem.2du_Neg.nn",
        "310228": "SC.w.act.gem.2pl_Neg.n js",
        "-310228": "SC.w.act.gem.2du_Neg.n js",
        "410228": "SC.w.act.gem.2pl_Neg.jmi",
        "-410228": "SC.w.act.gem.2du_Neg.jmi",
        "510228": "SC.w.act.gem.2pl_Neg.n-zp/jwt-zp",
        "-510228": "SC.w.act.gem.2du_Neg.n-zp/jwt-zp",
        "610228": "SC.w.act.gem.2pl_Neg.jwtj",
        "-610228": "SC.w.act.gem.2du_Neg.jwtj",
        "710228": "SC.w.act.gem.2pl_Neg.jwt",
        "-710228": "SC.w.act.gem.2du_Neg.jwt",
        "810228": "SC.w.act.gem.2pl_Neg.w/ꜣ",
        "-810228": "SC.w.act.gem.2du_Neg.w/ꜣ",
        "910228": "SC.w.act.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910228": "SC.w.act.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10229": "SC.w.act.gem.3pl",
        "-10229": "SC.w.act.gem.3du",
        "110229": "SC.w.act.gem.3pl_Neg.n",
        "-110229": "SC.w.act.gem.3du_Neg.n",
        "210229": "SC.w.act.gem.3pl_Neg.nn",
        "-210229": "SC.w.act.gem.3du_Neg.nn",
        "310229": "SC.w.act.gem.3pl_Neg.n js",
        "-310229": "SC.w.act.gem.3du_Neg.n js",
        "410229": "SC.w.act.gem.3pl_Neg.jmi",
        "-410229": "SC.w.act.gem.3du_Neg.jmi",
        "510229": "SC.w.act.gem.3pl_Neg.n-zp/jwt-zp",
        "-510229": "SC.w.act.gem.3du_Neg.n-zp/jwt-zp",
        "610229": "SC.w.act.gem.3pl_Neg.jwtj",
        "-610229": "SC.w.act.gem.3du_Neg.jwtj",
        "710229": "SC.w.act.gem.3pl_Neg.jwt",
        "-710229": "SC.w.act.gem.3du_Neg.jwt",
        "810229": "SC.w.act.gem.3pl_Neg.w/ꜣ",
        "-810229": "SC.w.act.gem.3du_Neg.w/ꜣ",
        "910229": "SC.w.act.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910229": "SC.w.act.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10240": "SC.w.pass.ngem.nom.subj",
        "110240": "SC.w.pass.ngem.nom.subj_Neg.n",
        "210240": "SC.w.pass.ngem.nom.subj_Neg.nn",
        "310240": "SC.w.pass.ngem.nom.subj_Neg.n js",
        "410240": "SC.w.pass.ngem.nom.subj_Neg.jmi",
        "510240": "SC.w.pass.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610240": "SC.w.pass.ngem.nom.subj_Neg.jwtj",
        "710240": "SC.w.pass.ngem.nom.subj_Neg.jwt",
        "810240": "SC.w.pass.ngem.nom.subj_Neg.w/ꜣ",
        "910240": "SC.w.pass.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10241": "SC.w.pass.ngem.1sg",
        "110241": "SC.w.pass.ngem.1sg_Neg.n",
        "210241": "SC.w.pass.ngem.1sg_Neg.nn",
        "310241": "SC.w.pass.ngem.1sg_Neg.n js",
        "410241": "SC.w.pass.ngem.1sg_Neg.jmi",
        "510241": "SC.w.pass.ngem.1sg_Neg.n-zp/jwt-zp",
        "610241": "SC.w.pass.ngem.1sg_Neg.jwtj",
        "710241": "SC.w.pass.ngem.1sg_Neg.jwt",
        "810241": "SC.w.pass.ngem.1sg_Neg.w/ꜣ",
        "910241": "SC.w.pass.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10242": "SC.w.pass.ngem.2sgm",
        "110242": "SC.w.pass.ngem.2sgm_Neg.n",
        "210242": "SC.w.pass.ngem.2sgm_Neg.nn",
        "310242": "SC.w.pass.ngem.2sgm_Neg.n js",
        "410242": "SC.w.pass.ngem.2sgm_Neg.jmi",
        "510242": "SC.w.pass.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610242": "SC.w.pass.ngem.2sgm_Neg.jwtj",
        "710242": "SC.w.pass.ngem.2sgm_Neg.jwt",
        "810242": "SC.w.pass.ngem.2sgm_Neg.w/ꜣ",
        "910242": "SC.w.pass.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10243": "SC.w.pass.ngem.2sgf",
        "110243": "SC.w.pass.ngem.2sgf_Neg.n",
        "210243": "SC.w.pass.ngem.2sgf_Neg.nn",
        "310243": "SC.w.pass.ngem.2sgf_Neg.n js",
        "410243": "SC.w.pass.ngem.2sgf_Neg.jmi",
        "510243": "SC.w.pass.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610243": "SC.w.pass.ngem.2sgf_Neg.jwtj",
        "710243": "SC.w.pass.ngem.2sgf_Neg.jwt",
        "810243": "SC.w.pass.ngem.2sgf_Neg.w/ꜣ",
        "910243": "SC.w.pass.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10244": "SC.w.pass.ngem.3sgm",
        "110244": "SC.w.pass.ngem.3sgm_Neg.n",
        "210244": "SC.w.pass.ngem.3sgm_Neg.nn",
        "310244": "SC.w.pass.ngem.3sgm_Neg.n js",
        "410244": "SC.w.pass.ngem.3sgm_Neg.jmi",
        "510244": "SC.w.pass.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610244": "SC.w.pass.ngem.3sgm_Neg.jwtj",
        "710244": "SC.w.pass.ngem.3sgm_Neg.jwt",
        "810244": "SC.w.pass.ngem.3sgm_Neg.w/ꜣ",
        "910244": "SC.w.pass.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10245": "SC.w.pass.ngem.3sgf",
        "110245": "SC.w.pass.ngem.3sgf_Neg.n",
        "210245": "SC.w.pass.ngem.3sgf_Neg.nn",
        "310245": "SC.w.pass.ngem.3sgf_Neg.n js",
        "410245": "SC.w.pass.ngem.3sgf_Neg.jmi",
        "510245": "SC.w.pass.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610245": "SC.w.pass.ngem.3sgf_Neg.jwtj",
        "710245": "SC.w.pass.ngem.3sgf_Neg.jwt",
        "810245": "SC.w.pass.ngem.3sgf_Neg.w/ꜣ",
        "910245": "SC.w.pass.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10246": "SC.w.pass.ngem.3sg",
        "110246": "SC.w.pass.ngem.3sg_Neg.n",
        "210246": "SC.w.pass.ngem.3sg_Neg.nn",
        "310246": "SC.w.pass.ngem.3sg_Neg.n js",
        "410246": "SC.w.pass.ngem.3sg_Neg.jmi",
        "510246": "SC.w.pass.ngem.3sg_Neg.n-zp/jwt-zp",
        "610246": "SC.w.pass.ngem.3sg_Neg.jwtj",
        "710246": "SC.w.pass.ngem.3sg_Neg.jwt",
        "810246": "SC.w.pass.ngem.3sg_Neg.w/ꜣ",
        "910246": "SC.w.pass.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10247": "SC.w.pass.ngem.1pl",
        "-10247": "SC.w.pass.ngem.1du",
        "110247": "SC.w.pass.ngem.1pl_Neg.n",
        "-110247": "SC.w.pass.ngem.1du_Neg.n",
        "210247": "SC.w.pass.ngem.1pl_Neg.nn",
        "-210247": "SC.w.pass.ngem.1du_Neg.nn",
        "310247": "SC.w.pass.ngem.1pl_Neg.n js",
        "-310247": "SC.w.pass.ngem.1du_Neg.n js",
        "410247": "SC.w.pass.ngem.1pl_Neg.jmi",
        "-410247": "SC.w.pass.ngem.1du_Neg.jmi",
        "510247": "SC.w.pass.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510247": "SC.w.pass.ngem.1du_Neg.n-zp/jwt-zp",
        "610247": "SC.w.pass.ngem.1pl_Neg.jwtj",
        "-610247": "SC.w.pass.ngem.1du_Neg.jwtj",
        "710247": "SC.w.pass.ngem.1pl_Neg.jwt",
        "-710247": "SC.w.pass.ngem.1du_Neg.jwt",
        "810247": "SC.w.pass.ngem.1pl_Neg.w/ꜣ",
        "-810247": "SC.w.pass.ngem.1du_Neg.w/ꜣ",
        "910247": "SC.w.pass.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910247": "SC.w.pass.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10248": "SC.w.pass.ngem.2pl",
        "-10248": "SC.w.pass.ngem.2du",
        "110248": "SC.w.pass.ngem.2pl_Neg.n",
        "-110248": "SC.w.pass.ngem.2du_Neg.n",
        "210248": "SC.w.pass.ngem.2pl_Neg.nn",
        "-210248": "SC.w.pass.ngem.2du_Neg.nn",
        "310248": "SC.w.pass.ngem.2pl_Neg.n js",
        "-310248": "SC.w.pass.ngem.2du_Neg.n js",
        "410248": "SC.w.pass.ngem.2pl_Neg.jmi",
        "-410248": "SC.w.pass.ngem.2du_Neg.jmi",
        "510248": "SC.w.pass.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510248": "SC.w.pass.ngem.2du_Neg.n-zp/jwt-zp",
        "610248": "SC.w.pass.ngem.2pl_Neg.jwtj",
        "-610248": "SC.w.pass.ngem.2du_Neg.jwtj",
        "710248": "SC.w.pass.ngem.2pl_Neg.jwt",
        "-710248": "SC.w.pass.ngem.2du_Neg.jwt",
        "810248": "SC.w.pass.ngem.2pl_Neg.w/ꜣ",
        "-810248": "SC.w.pass.ngem.2du_Neg.w/ꜣ",
        "910248": "SC.w.pass.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910248": "SC.w.pass.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10249": "SC.w.pass.ngem.3pl",
        "-10249": "SC.w.pass.ngem.3du",
        "110249": "SC.w.pass.ngem.3pl_Neg.n",
        "-110249": "SC.w.pass.ngem.3du_Neg.n",
        "210249": "SC.w.pass.ngem.3pl_Neg.nn",
        "-210249": "SC.w.pass.ngem.3du_Neg.nn",
        "310249": "SC.w.pass.ngem.3pl_Neg.n js",
        "-310249": "SC.w.pass.ngem.3du_Neg.n js",
        "410249": "SC.w.pass.ngem.3pl_Neg.jmi",
        "-410249": "SC.w.pass.ngem.3du_Neg.jmi",
        "510249": "SC.w.pass.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510249": "SC.w.pass.ngem.3du_Neg.n-zp/jwt-zp",
        "610249": "SC.w.pass.ngem.3pl_Neg.jwtj",
        "-610249": "SC.w.pass.ngem.3du_Neg.jwtj",
        "710249": "SC.w.pass.ngem.3pl_Neg.jwt",
        "-710249": "SC.w.pass.ngem.3du_Neg.jwt",
        "810249": "SC.w.pass.ngem.3pl_Neg.w/ꜣ",
        "-810249": "SC.w.pass.ngem.3du_Neg.w/ꜣ",
        "910249": "SC.w.pass.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910249": "SC.w.pass.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10260": "",
        "10261": "",
        "10262": "",
        "10263": "",
        "10264": "",
        "10265": "",
        "10266": "",
        "10267": "",
        "10268": "",
        "10269": "",
        "10280": "SC.w.tw.pass.ngem.nom.subj",
        "110280": "SC.w.tw.pass.ngem.nom.subj_Neg.n",
        "210280": "SC.w.tw.pass.ngem.nom.subj_Neg.nn",
        "310280": "SC.w.tw.pass.ngem.nom.subj_Neg.n js",
        "410280": "SC.w.tw.pass.ngem.nom.subj_Neg.jmi",
        "510280": "SC.w.tw.pass.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610280": "SC.w.tw.pass.ngem.nom.subj_Neg.jwtj",
        "710280": "SC.w.tw.pass.ngem.nom.subj_Neg.jwt",
        "810280": "SC.w.tw.pass.ngem.nom.subj_Neg.w/ꜣ",
        "910280": "SC.w.tw.pass.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10281": "SC.w.tw.pass.ngem.1sg",
        "110281": "SC.w.tw.pass.ngem.1sg_Neg.n",
        "210281": "SC.w.tw.pass.ngem.1sg_Neg.nn",
        "310281": "SC.w.tw.pass.ngem.1sg_Neg.n js",
        "410281": "SC.w.tw.pass.ngem.1sg_Neg.jmi",
        "510281": "SC.w.tw.pass.ngem.1sg_Neg.n-zp/jwt-zp",
        "610281": "SC.w.tw.pass.ngem.1sg_Neg.jwtj",
        "710281": "SC.w.tw.pass.ngem.1sg_Neg.jwt",
        "810281": "SC.w.tw.pass.ngem.1sg_Neg.w/ꜣ",
        "910281": "SC.w.tw.pass.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10282": "SC.w.tw.pass.ngem.2sgm",
        "110282": "SC.w.tw.pass.ngem.2sgm_Neg.n",
        "210282": "SC.w.tw.pass.ngem.2sgm_Neg.nn",
        "310282": "SC.w.tw.pass.ngem.2sgm_Neg.n js",
        "410282": "SC.w.tw.pass.ngem.2sgm_Neg.jmi",
        "510282": "SC.w.tw.pass.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610282": "SC.w.tw.pass.ngem.2sgm_Neg.jwtj",
        "710282": "SC.w.tw.pass.ngem.2sgm_Neg.jwt",
        "810282": "SC.w.tw.pass.ngem.2sgm_Neg.w/ꜣ",
        "910282": "SC.w.tw.pass.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10283": "SC.w.tw.pass.ngem.2sgf",
        "110283": "SC.w.tw.pass.ngem.2sgf_Neg.n",
        "210283": "SC.w.tw.pass.ngem.2sgf_Neg.nn",
        "310283": "SC.w.tw.pass.ngem.2sgf_Neg.n js",
        "410283": "SC.w.tw.pass.ngem.2sgf_Neg.jmi",
        "510283": "SC.w.tw.pass.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610283": "SC.w.tw.pass.ngem.2sgf_Neg.jwtj",
        "710283": "SC.w.tw.pass.ngem.2sgf_Neg.jwt",
        "810283": "SC.w.tw.pass.ngem.2sgf_Neg.w/ꜣ",
        "910283": "SC.w.tw.pass.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10284": "SC.w.tw.pass.ngem.3sgm",
        "110284": "SC.w.tw.pass.ngem.3sgm_Neg.n",
        "210284": "SC.w.tw.pass.ngem.3sgm_Neg.nn",
        "310284": "SC.w.tw.pass.ngem.3sgm_Neg.n js",
        "410284": "SC.w.tw.pass.ngem.3sgm_Neg.jmi",
        "510284": "SC.w.tw.pass.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610284": "SC.w.tw.pass.ngem.3sgm_Neg.jwtj",
        "710284": "SC.w.tw.pass.ngem.3sgm_Neg.jwt",
        "810284": "SC.w.tw.pass.ngem.3sgm_Neg.w/ꜣ",
        "910284": "SC.w.tw.pass.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10285": "SC.w.tw.pass.ngem.3sgf",
        "110285": "SC.w.tw.pass.ngem.3sgf_Neg.n",
        "210285": "SC.w.tw.pass.ngem.3sgf_Neg.nn",
        "310285": "SC.w.tw.pass.ngem.3sgf_Neg.n js",
        "410285": "SC.w.tw.pass.ngem.3sgf_Neg.jmi",
        "510285": "SC.w.tw.pass.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610285": "SC.w.tw.pass.ngem.3sgf_Neg.jwtj",
        "710285": "SC.w.tw.pass.ngem.3sgf_Neg.jwt",
        "810285": "SC.w.tw.pass.ngem.3sgf_Neg.w/ꜣ",
        "910285": "SC.w.tw.pass.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10286": "SC.w.tw.pass.ngem.3sg",
        "110286": "SC.w.tw.pass.ngem.3sg_Neg.n",
        "210286": "SC.w.tw.pass.ngem.3sg_Neg.nn",
        "310286": "SC.w.tw.pass.ngem.3sg_Neg.n js",
        "410286": "SC.w.tw.pass.ngem.3sg_Neg.jmi",
        "510286": "SC.w.tw.pass.ngem.3sg_Neg.n-zp/jwt-zp",
        "610286": "SC.w.tw.pass.ngem.3sg_Neg.jwtj",
        "710286": "SC.w.tw.pass.ngem.3sg_Neg.jwt",
        "810286": "SC.w.tw.pass.ngem.3sg_Neg.w/ꜣ",
        "910286": "SC.w.tw.pass.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10287": "SC.w.tw.pass.ngem.1pl",
        "-10287": "SC.w.tw.pass.ngem.1du",
        "110287": "SC.w.tw.pass.ngem.1pl_Neg.n",
        "-110287": "SC.w.tw.pass.ngem.1du_Neg.n",
        "210287": "SC.w.tw.pass.ngem.1pl_Neg.nn",
        "-210287": "SC.w.tw.pass.ngem.1du_Neg.nn",
        "310287": "SC.w.tw.pass.ngem.1pl_Neg.n js",
        "-310287": "SC.w.tw.pass.ngem.1du_Neg.n js",
        "410287": "SC.w.tw.pass.ngem.1pl_Neg.jmi",
        "-410287": "SC.w.tw.pass.ngem.1du_Neg.jmi",
        "510287": "SC.w.tw.pass.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510287": "SC.w.tw.pass.ngem.1du_Neg.n-zp/jwt-zp",
        "610287": "SC.w.tw.pass.ngem.1pl_Neg.jwtj",
        "-610287": "SC.w.tw.pass.ngem.1du_Neg.jwtj",
        "710287": "SC.w.tw.pass.ngem.1pl_Neg.jwt",
        "-710287": "SC.w.tw.pass.ngem.1du_Neg.jwt",
        "810287": "SC.w.tw.pass.ngem.1pl_Neg.w/ꜣ",
        "-810287": "SC.w.tw.pass.ngem.1du_Neg.w/ꜣ",
        "910287": "SC.w.tw.pass.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910287": "SC.w.tw.pass.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10288": "SC.w.tw.pass.ngem.2pl",
        "-10288": "SC.w.tw.pass.ngem.2du",
        "110288": "SC.w.tw.pass.ngem.2pl_Neg.n",
        "-110288": "SC.w.tw.pass.ngem.2du_Neg.n",
        "210288": "SC.w.tw.pass.ngem.2pl_Neg.nn",
        "-210288": "SC.w.tw.pass.ngem.2du_Neg.nn",
        "310288": "SC.w.tw.pass.ngem.2pl_Neg.n js",
        "-310288": "SC.w.tw.pass.ngem.2du_Neg.n js",
        "410288": "SC.w.tw.pass.ngem.2pl_Neg.jmi",
        "-410288": "SC.w.tw.pass.ngem.2du_Neg.jmi",
        "510288": "SC.w.tw.pass.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510288": "SC.w.tw.pass.ngem.2du_Neg.n-zp/jwt-zp",
        "610288": "SC.w.tw.pass.ngem.2pl_Neg.jwtj",
        "-610288": "SC.w.tw.pass.ngem.2du_Neg.jwtj",
        "710288": "SC.w.tw.pass.ngem.2pl_Neg.jwt",
        "-710288": "SC.w.tw.pass.ngem.2du_Neg.jwt",
        "810288": "SC.w.tw.pass.ngem.2pl_Neg.w/ꜣ",
        "-810288": "SC.w.tw.pass.ngem.2du_Neg.w/ꜣ",
        "910288": "SC.w.tw.pass.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910288": "SC.w.tw.pass.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10289": "SC.w.tw.pass.ngem.3pl",
        "-10289": "SC.w.tw.pass.ngem.3du",
        "110289": "SC.w.tw.pass.ngem.3pl_Neg.n",
        "-110289": "SC.w.tw.pass.ngem.3du_Neg.n",
        "210289": "SC.w.tw.pass.ngem.3pl_Neg.nn",
        "-210289": "SC.w.tw.pass.ngem.3du_Neg.nn",
        "310289": "SC.w.tw.pass.ngem.3pl_Neg.n js",
        "-310289": "SC.w.tw.pass.ngem.3du_Neg.n js",
        "410289": "SC.w.tw.pass.ngem.3pl_Neg.jmi",
        "-410289": "SC.w.tw.pass.ngem.3du_Neg.jmi",
        "510289": "SC.w.tw.pass.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510289": "SC.w.tw.pass.ngem.3du_Neg.n-zp/jwt-zp",
        "610289": "SC.w.tw.pass.ngem.3pl_Neg.jwtj",
        "-610289": "SC.w.tw.pass.ngem.3du_Neg.jwtj",
        "710289": "SC.w.tw.pass.ngem.3pl_Neg.jwt",
        "-710289": "SC.w.tw.pass.ngem.3du_Neg.jwt",
        "810289": "SC.w.tw.pass.ngem.3pl_Neg.w/ꜣ",
        "-810289": "SC.w.tw.pass.ngem.3du_Neg.w/ꜣ",
        "910289": "SC.w.tw.pass.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910289": "SC.w.tw.pass.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10300": "",
        "10301": "",
        "10302": "",
        "10303": "",
        "10304": "",
        "10305": "",
        "10306": "",
        "10307": "",
        "10308": "",
        "10309": "",
        "10320": "SC.tw.pass.ngem.nom.subj",
        "110320": "SC.tw.pass.ngem.nom.subj_Neg.n",
        "210320": "SC.tw.pass.ngem.nom.subj_Neg.nn",
        "310320": "SC.tw.pass.ngem.nom.subj_Neg.n js",
        "410320": "SC.tw.pass.ngem.nom.subj_Neg.jmi",
        "510320": "SC.tw.pass.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610320": "SC.tw.pass.ngem.nom.subj_Neg.jwtj",
        "710320": "SC.tw.pass.ngem.nom.subj_Neg.jwt",
        "810320": "SC.tw.pass.ngem.nom.subj_Neg.w/ꜣ",
        "910320": "SC.tw.pass.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10321": "SC.tw.pass.ngem.1sg",
        "110321": "SC.tw.pass.ngem.1sg_Neg.n",
        "210321": "SC.tw.pass.ngem.1sg_Neg.nn",
        "310321": "SC.tw.pass.ngem.1sg_Neg.n js",
        "410321": "SC.tw.pass.ngem.1sg_Neg.jmi",
        "510321": "SC.tw.pass.ngem.1sg_Neg.n-zp/jwt-zp",
        "610321": "SC.tw.pass.ngem.1sg_Neg.jwtj",
        "710321": "SC.tw.pass.ngem.1sg_Neg.jwt",
        "810321": "SC.tw.pass.ngem.1sg_Neg.w/ꜣ",
        "910321": "SC.tw.pass.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10322": "SC.tw.pass.ngem.2sgm",
        "110322": "SC.tw.pass.ngem.2sgm_Neg.n",
        "210322": "SC.tw.pass.ngem.2sgm_Neg.nn",
        "310322": "SC.tw.pass.ngem.2sgm_Neg.n js",
        "410322": "SC.tw.pass.ngem.2sgm_Neg.jmi",
        "510322": "SC.tw.pass.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610322": "SC.tw.pass.ngem.2sgm_Neg.jwtj",
        "710322": "SC.tw.pass.ngem.2sgm_Neg.jwt",
        "810322": "SC.tw.pass.ngem.2sgm_Neg.w/ꜣ",
        "910322": "SC.tw.pass.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10323": "SC.tw.pass.ngem.2sgf",
        "110323": "SC.tw.pass.ngem.2sgf_Neg.n",
        "210323": "SC.tw.pass.ngem.2sgf_Neg.nn",
        "310323": "SC.tw.pass.ngem.2sgf_Neg.n js",
        "410323": "SC.tw.pass.ngem.2sgf_Neg.jmi",
        "510323": "SC.tw.pass.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610323": "SC.tw.pass.ngem.2sgf_Neg.jwtj",
        "710323": "SC.tw.pass.ngem.2sgf_Neg.jwt",
        "810323": "SC.tw.pass.ngem.2sgf_Neg.w/ꜣ",
        "910323": "SC.tw.pass.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10324": "SC.tw.pass.ngem.3sgm",
        "110324": "SC.tw.pass.ngem.3sgm_Neg.n",
        "210324": "SC.tw.pass.ngem.3sgm_Neg.nn",
        "310324": "SC.tw.pass.ngem.3sgm_Neg.n js",
        "410324": "SC.tw.pass.ngem.3sgm_Neg.jmi",
        "510324": "SC.tw.pass.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610324": "SC.tw.pass.ngem.3sgm_Neg.jwtj",
        "710324": "SC.tw.pass.ngem.3sgm_Neg.jwt",
        "810324": "SC.tw.pass.ngem.3sgm_Neg.w/ꜣ",
        "910324": "SC.tw.pass.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10325": "SC.tw.pass.ngem.3sgf",
        "110325": "SC.tw.pass.ngem.3sgf_Neg.n",
        "210325": "SC.tw.pass.ngem.3sgf_Neg.nn",
        "310325": "SC.tw.pass.ngem.3sgf_Neg.n js",
        "410325": "SC.tw.pass.ngem.3sgf_Neg.jmi",
        "510325": "SC.tw.pass.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610325": "SC.tw.pass.ngem.3sgf_Neg.jwtj",
        "710325": "SC.tw.pass.ngem.3sgf_Neg.jwt",
        "810325": "SC.tw.pass.ngem.3sgf_Neg.w/ꜣ",
        "910325": "SC.tw.pass.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10326": "SC.tw.pass.ngem.3sg",
        "110326": "SC.tw.pass.ngem.3sg_Neg.n",
        "210326": "SC.tw.pass.ngem.3sg_Neg.nn",
        "310326": "SC.tw.pass.ngem.3sg_Neg.n js",
        "410326": "SC.tw.pass.ngem.3sg_Neg.jmi",
        "510326": "SC.tw.pass.ngem.3sg_Neg.n-zp/jwt-zp",
        "610326": "SC.tw.pass.ngem.3sg_Neg.jwtj",
        "710326": "SC.tw.pass.ngem.3sg_Neg.jwt",
        "810326": "SC.tw.pass.ngem.3sg_Neg.w/ꜣ",
        "910326": "SC.tw.pass.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10327": "SC.tw.pass.ngem.1pl",
        "-10327": "SC.tw.pass.ngem.1du",
        "110327": "SC.tw.pass.ngem.1pl_Neg.n",
        "-110327": "SC.tw.pass.ngem.1du_Neg.n",
        "210327": "SC.tw.pass.ngem.1pl_Neg.nn",
        "-210327": "SC.tw.pass.ngem.1du_Neg.nn",
        "310327": "SC.tw.pass.ngem.1pl_Neg.n js",
        "-310327": "SC.tw.pass.ngem.1du_Neg.n js",
        "410327": "SC.tw.pass.ngem.1pl_Neg.jmi",
        "-410327": "SC.tw.pass.ngem.1du_Neg.jmi",
        "510327": "SC.tw.pass.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510327": "SC.tw.pass.ngem.1du_Neg.n-zp/jwt-zp",
        "610327": "SC.tw.pass.ngem.1pl_Neg.jwtj",
        "-610327": "SC.tw.pass.ngem.1du_Neg.jwtj",
        "710327": "SC.tw.pass.ngem.1pl_Neg.jwt",
        "-710327": "SC.tw.pass.ngem.1du_Neg.jwt",
        "810327": "SC.tw.pass.ngem.1pl_Neg.w/ꜣ",
        "-810327": "SC.tw.pass.ngem.1du_Neg.w/ꜣ",
        "910327": "SC.tw.pass.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910327": "SC.tw.pass.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10328": "SC.tw.pass.ngem.2pl",
        "-10328": "SC.tw.pass.ngem.2du",
        "110328": "SC.tw.pass.ngem.2pl_Neg.n",
        "-110328": "SC.tw.pass.ngem.2du_Neg.n",
        "210328": "SC.tw.pass.ngem.2pl_Neg.nn",
        "-210328": "SC.tw.pass.ngem.2du_Neg.nn",
        "310328": "SC.tw.pass.ngem.2pl_Neg.n js",
        "-310328": "SC.tw.pass.ngem.2du_Neg.n js",
        "410328": "SC.tw.pass.ngem.2pl_Neg.jmi",
        "-410328": "SC.tw.pass.ngem.2du_Neg.jmi",
        "510328": "SC.tw.pass.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510328": "SC.tw.pass.ngem.2du_Neg.n-zp/jwt-zp",
        "610328": "SC.tw.pass.ngem.2pl_Neg.jwtj",
        "-610328": "SC.tw.pass.ngem.2du_Neg.jwtj",
        "710328": "SC.tw.pass.ngem.2pl_Neg.jwt",
        "-710328": "SC.tw.pass.ngem.2du_Neg.jwt",
        "810328": "SC.tw.pass.ngem.2pl_Neg.w/ꜣ",
        "-810328": "SC.tw.pass.ngem.2du_Neg.w/ꜣ",
        "910328": "SC.tw.pass.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910328": "SC.tw.pass.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10329": "SC.tw.pass.ngem.3pl",
        "-10329": "SC.tw.pass.ngem.3du",
        "110329": "SC.tw.pass.ngem.3pl_Neg.n",
        "-110329": "SC.tw.pass.ngem.3du_Neg.n",
        "210329": "SC.tw.pass.ngem.3pl_Neg.nn",
        "-210329": "SC.tw.pass.ngem.3du_Neg.nn",
        "310329": "SC.tw.pass.ngem.3pl_Neg.n js",
        "-310329": "SC.tw.pass.ngem.3du_Neg.n js",
        "410329": "SC.tw.pass.ngem.3pl_Neg.jmi",
        "-410329": "SC.tw.pass.ngem.3du_Neg.jmi",
        "510329": "SC.tw.pass.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510329": "SC.tw.pass.ngem.3du_Neg.n-zp/jwt-zp",
        "610329": "SC.tw.pass.ngem.3pl_Neg.jwtj",
        "-610329": "SC.tw.pass.ngem.3du_Neg.jwtj",
        "710329": "SC.tw.pass.ngem.3pl_Neg.jwt",
        "-710329": "SC.tw.pass.ngem.3du_Neg.jwt",
        "810329": "SC.tw.pass.ngem.3pl_Neg.w/ꜣ",
        "-810329": "SC.tw.pass.ngem.3du_Neg.w/ꜣ",
        "910329": "SC.tw.pass.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910329": "SC.tw.pass.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "510333": "SC.n.pass.ngem.2sgf_Neg.n-zp/jwt-zp",
        "10340": "",
        "10341": "",
        "10342": "",
        "10343": "",
        "10344": "",
        "10345": "",
        "10346": "",
        "10347": "",
        "10348": "",
        "10349": "",
        "10360": "SC.tw.pass.gem.nom.subj",
        "110360": "SC.tw.pass.gem.nom.subj_Neg.n",
        "210360": "SC.tw.pass.gem.nom.subj_Neg.nn",
        "310360": "SC.tw.pass.gem.nom.subj_Neg.n js",
        "410360": "SC.tw.pass.gem.nom.subj_Neg.jmi",
        "510360": "SC.tw.pass.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610360": "SC.tw.pass.gem.nom.subj_Neg.jwtj",
        "710360": "SC.tw.pass.gem.nom.subj_Neg.jwt",
        "810360": "SC.tw.pass.gem.nom.subj_Neg.w/ꜣ",
        "910360": "SC.tw.pass.gem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10361": "SC.tw.pass.gem.1sg",
        "110361": "SC.tw.pass.gem.1sg_Neg.n",
        "210361": "SC.tw.pass.gem.1sg_Neg.nn",
        "310361": "SC.tw.pass.gem.1sg_Neg.n js",
        "410361": "SC.tw.pass.gem.1sg_Neg.jmi",
        "510361": "SC.tw.pass.gem.1sg_Neg.n-zp/jwt-zp",
        "610361": "SC.tw.pass.gem.1sg_Neg.jwtj",
        "710361": "SC.tw.pass.gem.1sg_Neg.jwt",
        "810361": "SC.tw.pass.gem.1sg_Neg.w/ꜣ",
        "910361": "SC.tw.pass.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10362": "SC.tw.pass.gem.2sgm",
        "110362": "SC.tw.pass.gem.2sgm_Neg.n",
        "210362": "SC.tw.pass.gem.2sgm_Neg.nn",
        "310362": "SC.tw.pass.gem.2sgm_Neg.n js",
        "410362": "SC.tw.pass.gem.2sgm_Neg.jmi",
        "510362": "SC.tw.pass.gem.2sgm_Neg.n-zp/jwt-zp",
        "610362": "SC.tw.pass.gem.2sgm_Neg.jwtj",
        "710362": "SC.tw.pass.gem.2sgm_Neg.jwt",
        "810362": "SC.tw.pass.gem.2sgm_Neg.w/ꜣ",
        "910362": "SC.tw.pass.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10363": "SC.tw.pass.gem.2sgf",
        "110363": "SC.tw.pass.gem.2sgf_Neg.n",
        "210363": "SC.tw.pass.gem.2sgf_Neg.nn",
        "310363": "SC.tw.pass.gem.2sgf_Neg.n js",
        "410363": "SC.tw.pass.gem.2sgf_Neg.jmi",
        "510363": "SC.tw.pass.gem.2sgf_Neg.n-zp/jwt-zp",
        "610363": "SC.tw.pass.gem.2sgf_Neg.jwtj",
        "710363": "SC.tw.pass.gem.2sgf_Neg.jwt",
        "810363": "SC.tw.pass.gem.2sgf_Neg.w/ꜣ",
        "910363": "SC.tw.pass.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10364": "SC.tw.pass.gem.3sgm",
        "110364": "SC.tw.pass.gem.3sgm_Neg.n",
        "210364": "SC.tw.pass.gem.3sgm_Neg.nn",
        "310364": "SC.tw.pass.gem.3sgm_Neg.n js",
        "410364": "SC.tw.pass.gem.3sgm_Neg.jmi",
        "510364": "SC.tw.pass.gem.3sgm_Neg.n-zp/jwt-zp",
        "610364": "SC.tw.pass.gem.3sgm_Neg.jwtj",
        "710364": "SC.tw.pass.gem.3sgm_Neg.jwt",
        "810364": "SC.tw.pass.gem.3sgm_Neg.w/ꜣ",
        "910364": "SC.tw.pass.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10365": "SC.tw.pass.gem.3sgf",
        "110365": "SC.tw.pass.gem.3sgf_Neg.n",
        "210365": "SC.tw.pass.gem.3sgf_Neg.nn",
        "310365": "SC.tw.pass.gem.3sgf_Neg.n js",
        "410365": "SC.tw.pass.gem.3sgf_Neg.jmi",
        "510365": "SC.tw.pass.gem.3sgf_Neg.n-zp/jwt-zp",
        "610365": "SC.tw.pass.gem.3sgf_Neg.jwtj",
        "710365": "SC.tw.pass.gem.3sgf_Neg.jwt",
        "810365": "SC.tw.pass.gem.3sgf_Neg.w/ꜣ",
        "910365": "SC.tw.pass.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10366": "SC.tw.pass.gem.3sg",
        "110366": "SC.tw.pass.gem.3sg_Neg.n",
        "210366": "SC.tw.pass.gem.3sg_Neg.nn",
        "310366": "SC.tw.pass.gem.3sg_Neg.n js",
        "410366": "SC.tw.pass.gem.3sg_Neg.jmi",
        "510366": "SC.tw.pass.gem.3sg_Neg.n-zp/jwt-zp",
        "610366": "SC.tw.pass.gem.3sg_Neg.jwtj",
        "710366": "SC.tw.pass.gem.3sg_Neg.jwt",
        "810366": "SC.tw.pass.gem.3sg_Neg.w/ꜣ",
        "910366": "SC.tw.pass.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10367": "SC.tw.pass.gem.1pl",
        "-10367": "SC.tw.pass.gem.1du",
        "110367": "SC.tw.pass.gem.1pl_Neg.n",
        "-110367": "SC.tw.pass.gem.1du_Neg.n",
        "210367": "SC.tw.pass.gem.1pl_Neg.nn",
        "-210367": "SC.tw.pass.gem.1du_Neg.nn",
        "310367": "SC.tw.pass.gem.1pl_Neg.n js",
        "-310367": "SC.tw.pass.gem.1du_Neg.n js",
        "410367": "SC.tw.pass.gem.1pl_Neg.jmi",
        "-410367": "SC.tw.pass.gem.1du_Neg.jmi",
        "510367": "SC.tw.pass.gem.1pl_Neg.n-zp/jwt-zp",
        "-510367": "SC.tw.pass.gem.1du_Neg.n-zp/jwt-zp",
        "610367": "SC.tw.pass.gem.1pl_Neg.jwtj",
        "-610367": "SC.tw.pass.gem.1du_Neg.jwtj",
        "710367": "SC.tw.pass.gem.1pl_Neg.jwt",
        "-710367": "SC.tw.pass.gem.1du_Neg.jwt",
        "810367": "SC.tw.pass.gem.1pl_Neg.w/ꜣ",
        "-810367": "SC.tw.pass.gem.1du_Neg.w/ꜣ",
        "910367": "SC.tw.pass.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910367": "SC.tw.pass.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10368": "SC.tw.pass.gem.2pl",
        "-10368": "SC.tw.pass.gem.2du",
        "110368": "SC.tw.pass.gem.2pl_Neg.n",
        "-110368": "SC.tw.pass.gem.2du_Neg.n",
        "210368": "SC.tw.pass.gem.2pl_Neg.nn",
        "-210368": "SC.tw.pass.gem.2du_Neg.nn",
        "310368": "SC.tw.pass.gem.2pl_Neg.n js",
        "-310368": "SC.tw.pass.gem.2du_Neg.n js",
        "410368": "SC.tw.pass.gem.2pl_Neg.jmi",
        "-410368": "SC.tw.pass.gem.2du_Neg.jmi",
        "510368": "SC.tw.pass.gem.2pl_Neg.n-zp/jwt-zp",
        "-510368": "SC.tw.pass.gem.2du_Neg.n-zp/jwt-zp",
        "610368": "SC.tw.pass.gem.2pl_Neg.jwtj",
        "-610368": "SC.tw.pass.gem.2du_Neg.jwtj",
        "710368": "SC.tw.pass.gem.2pl_Neg.jwt",
        "-710368": "SC.tw.pass.gem.2du_Neg.jwt",
        "810368": "SC.tw.pass.gem.2pl_Neg.w/ꜣ",
        "-810368": "SC.tw.pass.gem.2du_Neg.w/ꜣ",
        "910368": "SC.tw.pass.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910368": "SC.tw.pass.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10369": "SC.tw.pass.gem.3pl",
        "-10369": "SC.tw.pass.gem.3du",
        "110369": "SC.tw.pass.gem.3pl_Neg.n",
        "-110369": "SC.tw.pass.gem.3du_Neg.n",
        "210369": "SC.tw.pass.gem.3pl_Neg.nn",
        "-210369": "SC.tw.pass.gem.3du_Neg.nn",
        "310369": "SC.tw.pass.gem.3pl_Neg.n js",
        "-310369": "SC.tw.pass.gem.3du_Neg.n js",
        "410369": "SC.tw.pass.gem.3pl_Neg.jmi",
        "-410369": "SC.tw.pass.gem.3du_Neg.jmi",
        "510369": "SC.tw.pass.gem.3pl_Neg.n-zp/jwt-zp",
        "-510369": "SC.tw.pass.gem.3du_Neg.n-zp/jwt-zp",
        "610369": "SC.tw.pass.gem.3pl_Neg.jwtj",
        "-610369": "SC.tw.pass.gem.3du_Neg.jwtj",
        "710369": "SC.tw.pass.gem.3pl_Neg.jwt",
        "-710369": "SC.tw.pass.gem.3du_Neg.jwt",
        "810369": "SC.tw.pass.gem.3pl_Neg.w/ꜣ",
        "-810369": "SC.tw.pass.gem.3du_Neg.w/ꜣ",
        "910369": "SC.tw.pass.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910369": "SC.tw.pass.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10380": "SC.n.act.ngem.nom.subj",
        "110380": "SC.n.act.ngem.nom.subj_Neg.n",
        "210380": "SC.n.act.ngem.nom.subj_Neg.nn",
        "310380": "SC.n.act.ngem.nom.subj_Neg.n js",
        "410380": "SC.n.act.ngem.nom.subj_Neg.jmi",
        "510380": "SC.n.act.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610380": "SC.n.act.ngem.nom.subj_Neg.jwtj",
        "710380": "SC.n.act.ngem.nom.subj_Neg.jwt",
        "810380": "SC.n.act.ngem.nom.subj_Neg.w/ꜣ",
        "910380": "SC.n.act.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10381": "SC.n.act.ngem.1sg",
        "110381": "SC.n.act.ngem.1sg_Neg.n",
        "210381": "SC.n.act.ngem.1sg_Neg.nn",
        "310381": "SC.n.act.ngem.1sg_Neg.n js",
        "410381": "SC.n.act.ngem.1sg_Neg.jmi",
        "510381": "SC.n.act.ngem.1sg_Neg.n-zp/jwt-zp",
        "610381": "SC.n.act.ngem.1sg_Neg.jwtj",
        "710381": "SC.n.act.ngem.1sg_Neg.jwt",
        "810381": "SC.n.act.ngem.1sg_Neg.w/ꜣ",
        "910381": "SC.n.act.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10382": "SC.n.act.ngem.2sgm",
        "110382": "SC.n.act.ngem.2sgm_Neg.n",
        "210382": "SC.n.act.ngem.2sgm_Neg.nn",
        "310382": "SC.n.act.ngem.2sgm_Neg.n js",
        "410382": "SC.n.act.ngem.2sgm_Neg.jmi",
        "510382": "SC.n.act.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610382": "SC.n.act.ngem.2sgm_Neg.jwtj",
        "710382": "SC.n.act.ngem.2sgm_Neg.jwt",
        "810382": "SC.n.act.ngem.2sgm_Neg.w/ꜣ",
        "910382": "SC.n.act.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10383": "SC.n.act.ngem.2sgf",
        "110383": "SC.n.act.ngem.2sgf_Neg.n",
        "210383": "SC.n.act.ngem.2sgf_Neg.nn",
        "310383": "SC.n.act.ngem.2sgf_Neg.n js",
        "410383": "SC.n.act.ngem.2sgf_Neg.jmi",
        "510383": "SC.n.act.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610383": "SC.n.act.ngem.2sgf_Neg.jwtj",
        "710383": "SC.n.act.ngem.2sgf_Neg.jwt",
        "810383": "SC.n.act.ngem.2sgf_Neg.w/ꜣ",
        "910383": "SC.n.act.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10384": "SC.n.act.ngem.3sgm",
        "110384": "SC.n.act.ngem.3sgm_Neg.n",
        "210384": "SC.n.act.ngem.3sgm_Neg.nn",
        "310384": "SC.n.act.ngem.3sgm_Neg.n js",
        "410384": "SC.n.act.ngem.3sgm_Neg.jmi",
        "510384": "SC.n.act.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610384": "SC.n.act.ngem.3sgm_Neg.jwtj",
        "710384": "SC.n.act.ngem.3sgm_Neg.jwt",
        "810384": "SC.n.act.ngem.3sgm_Neg.w/ꜣ",
        "910384": "SC.n.act.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10385": "SC.n.act.ngem.3sgf",
        "110385": "SC.n.act.ngem.3sgf_Neg.n",
        "210385": "SC.n.act.ngem.3sgf_Neg.nn",
        "310385": "SC.n.act.ngem.3sgf_Neg.n js",
        "410385": "SC.n.act.ngem.3sgf_Neg.jmi",
        "510385": "SC.n.act.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610385": "SC.n.act.ngem.3sgf_Neg.jwtj",
        "710385": "SC.n.act.ngem.3sgf_Neg.jwt",
        "810385": "SC.n.act.ngem.3sgf_Neg.w/ꜣ",
        "910385": "SC.n.act.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10386": "SC.n.act.ngem.3sg",
        "110386": "SC.n.act.ngem.3sg_Neg.n",
        "210386": "SC.n.act.ngem.3sg_Neg.nn",
        "310386": "SC.n.act.ngem.3sg_Neg.n js",
        "410386": "SC.n.act.ngem.3sg_Neg.jmi",
        "510386": "SC.n.act.ngem.3sg_Neg.n-zp/jwt-zp",
        "610386": "SC.n.act.ngem.3sg_Neg.jwtj",
        "710386": "SC.n.act.ngem.3sg_Neg.jwt",
        "810386": "SC.n.act.ngem.3sg_Neg.w/ꜣ",
        "910386": "SC.n.act.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10387": "SC.n.act.ngem.1pl",
        "-10387": "SC.n.act.ngem.1du",
        "110387": "SC.n.act.ngem.1pl_Neg.n",
        "-110387": "SC.n.act.ngem.1du_Neg.n",
        "210387": "SC.n.act.ngem.1pl_Neg.nn",
        "-210387": "SC.n.act.ngem.1du_Neg.nn",
        "310387": "SC.n.act.ngem.1pl_Neg.n js",
        "-310387": "SC.n.act.ngem.1du_Neg.n js",
        "410387": "SC.n.act.ngem.1pl_Neg.jmi",
        "-410387": "SC.n.act.ngem.1du_Neg.jmi",
        "510387": "SC.n.act.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510387": "SC.n.act.ngem.1du_Neg.n-zp/jwt-zp",
        "610387": "SC.n.act.ngem.1pl_Neg.jwtj",
        "-610387": "SC.n.act.ngem.1du_Neg.jwtj",
        "710387": "SC.n.act.ngem.1pl_Neg.jwt",
        "-710387": "SC.n.act.ngem.1du_Neg.jwt",
        "810387": "SC.n.act.ngem.1pl_Neg.w/ꜣ",
        "-810387": "SC.n.act.ngem.1du_Neg.w/ꜣ",
        "910387": "SC.n.act.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910387": "SC.n.act.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10388": "SC.n.act.ngem.2pl",
        "-10388": "SC.n.act.ngem.2du",
        "110388": "SC.n.act.ngem.2pl_Neg.n",
        "-110388": "SC.n.act.ngem.2du_Neg.n",
        "210388": "SC.n.act.ngem.2pl_Neg.nn",
        "-210388": "SC.n.act.ngem.2du_Neg.nn",
        "310388": "SC.n.act.ngem.2pl_Neg.n js",
        "-310388": "SC.n.act.ngem.2du_Neg.n js",
        "410388": "SC.n.act.ngem.2pl_Neg.jmi",
        "-410388": "SC.n.act.ngem.2du_Neg.jmi",
        "510388": "SC.n.act.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510388": "SC.n.act.ngem.2du_Neg.n-zp/jwt-zp",
        "610388": "SC.n.act.ngem.2pl_Neg.jwtj",
        "-610388": "SC.n.act.ngem.2du_Neg.jwtj",
        "710388": "SC.n.act.ngem.2pl_Neg.jwt",
        "-710388": "SC.n.act.ngem.2du_Neg.jwt",
        "810388": "SC.n.act.ngem.2pl_Neg.w/ꜣ",
        "-810388": "SC.n.act.ngem.2du_Neg.w/ꜣ",
        "910388": "SC.n.act.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910388": "SC.n.act.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10389": "SC.n.act.ngem.3pl",
        "-10389": "SC.n.act.ngem.3du",
        "110389": "SC.n.act.ngem.3pl_Neg.n",
        "-110389": "SC.n.act.ngem.3du_Neg.n",
        "210389": "SC.n.act.ngem.3pl_Neg.nn",
        "-210389": "SC.n.act.ngem.3du_Neg.nn",
        "310389": "SC.n.act.ngem.3pl_Neg.n js",
        "-310389": "SC.n.act.ngem.3du_Neg.n-js",
        "410389": "SC.n.act.ngem.3pl_Neg.jmi",
        "-410389": "SC.n.act.ngem.3du_Neg.jmi",
        "510389": "SC.n.act.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510389": "SC.n.act.ngem.3du_Neg.n-zp/jwt-zp",
        "610389": "SC.n.act.ngem.3pl_Neg.jwtj",
        "-610389": "SC.n.act.ngem.3du_Neg.jwtj",
        "710389": "SC.n.act.ngem.3pl_Neg.jwt",
        "-710389": "SC.n.act.ngem.3du_Neg.jwt",
        "810389": "SC.n.act.ngem.3pl_Neg.w/ꜣ",
        "-810389": "SC.n.act.ngem.3du_Neg.w/ꜣ",
        "910389": "SC.n.act.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910389": "SC.n.act.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10400": "",
        "10401": "",
        "10402": "",
        "10403": "",
        "10404": "",
        "10405": "",
        "10406": "",
        "10407": "",
        "10408": "",
        "10409": "",
        "10420": "SC.n.act.gem.nom.subj",
        "110420": "SC.n.act.gem.nom.subj_Neg.n",
        "210420": "SC.n.act.gem.nom.subj_Neg.nn",
        "310420": "SC.n.act.gem.nom.subj_Neg.n js",
        "410420": "SC.n.act.gem.nom.subj_Neg.jmi",
        "510420": "SC.n.act.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610420": "SC.n.act.gem.nom.subj_Neg.jwtj",
        "710420": "SC.n.act.gem.nom.subj_Neg.jwt",
        "810420": "SC.n.act.gem.nom.subj_Neg.w/ꜣ",
        "910420": "SC.n.act.gem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10421": "SC.n.act.gem.1sg",
        "110421": "SC.n.act.gem.1sg_Neg.n",
        "210421": "SC.n.act.gem.1sg_Neg.nn",
        "310421": "SC.n.act.gem.1sg_Neg.n js",
        "410421": "SC.n.act.gem.1sg_Neg.jmi",
        "510421": "SC.n.act.gem.1sg_Neg.n-zp/jwt-zp",
        "610421": "SC.n.act.gem.1sg_Neg.jwtj",
        "710421": "SC.n.act.gem.1sg_Neg.jwt",
        "810421": "SC.n.act.gem.1sg_Neg.w/ꜣ",
        "910421": "SC.n.act.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10422": "SC.n.act.gem.2sgm",
        "110422": "SC.n.act.gem.2sgm_Neg.n",
        "210422": "SC.n.act.gem.2sgm_Neg.nn",
        "310422": "SC.n.act.gem.2sgm_Neg.n js",
        "410422": "SC.n.act.gem.2sgm_Neg.jmi",
        "510422": "SC.n.act.gem.2sgm_Neg.n-zp/jwt-zp",
        "610422": "SC.n.act.gem.2sgm_Neg.jwtj",
        "710422": "SC.n.act.gem.2sgm_Neg.jwt",
        "810422": "SC.n.act.gem.2sgm_Neg.w/ꜣ",
        "910422": "SC.n.act.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10423": "SC.n.act.gem.2sgf",
        "110423": "SC.n.act.gem.2sgf_Neg.n",
        "210423": "SC.n.act.gem.2sgf_Neg.nn",
        "310423": "SC.n.act.gem.2sgf_Neg.n js",
        "410423": "SC.n.act.gem.2sgf_Neg.jmi",
        "510423": "SC.n.act.gem.2sgf_Neg.n-zp/jwt-zp",
        "610423": "SC.n.act.gem.2sgf_Neg.jwtj",
        "710423": "SC.n.act.gem.2sgf_Neg.jwt",
        "810423": "SC.n.act.gem.2sgf_Neg.w/ꜣ",
        "910423": "SC.n.act.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10424": "SC.n.act.gem.3sgm",
        "110424": "SC.n.act.gem.3sgm_Neg.n",
        "210424": "SC.n.act.gem.3sgm_Neg.nn",
        "310424": "SC.n.act.gem.3sgm_Neg.n js",
        "410424": "SC.n.act.gem.3sgm_Neg.jmi",
        "510424": "SC.n.act.gem.3sgm_Neg.n-zp/jwt-zp",
        "610424": "SC.n.act.gem.3sgm_Neg.jwtj",
        "710424": "SC.n.act.gem.3sgm_Neg.jwt",
        "810424": "SC.n.act.gem.3sgm_Neg.w/ꜣ",
        "910424": "SC.n.act.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10425": "SC.n.act.gem.3sgf",
        "110425": "SC.n.act.gem.3sgf_Neg.n",
        "210425": "SC.n.act.gem.3sgf_Neg.nn",
        "310425": "SC.n.act.gem.3sgf_Neg.n js",
        "410425": "SC.n.act.gem.3sgf_Neg.jmi",
        "510425": "SC.n.act.gem.3sgf_Neg.n-zp/jwt-zp",
        "610425": "SC.n.act.gem.3sgf_Neg.jwtj",
        "710425": "SC.n.act.gem.3sgf_Neg.jwt",
        "810425": "SC.n.act.gem.3sgf_Neg.w/ꜣ",
        "910425": "SC.n.act.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10426": "SC.n.act.gem.3sg",
        "110426": "SC.n.act.gem.3sg_Neg.n",
        "210426": "SC.n.act.gem.3sg_Neg.nn",
        "310426": "SC.n.act.gem.3sg_Neg.n js",
        "410426": "SC.n.act.gem.3sg_Neg.jmi",
        "510426": "SC.n.act.gem.3sg_Neg.n-zp/jwt-zp",
        "610426": "SC.n.act.gem.3sg_Neg.jwtj",
        "710426": "SC.n.act.gem.3sg_Neg.jwt",
        "810426": "SC.n.act.gem.3sg_Neg.w/ꜣ",
        "910426": "SC.n.act.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10427": "SC.n.act.gem.1pl",
        "-10427": "SC.n.act.gem.1du",
        "110427": "SC.n.act.gem.1pl_Neg.n",
        "-110427": "SC.n.act.gem.1du_Neg.n",
        "210427": "SC.n.act.gem.1pl_Neg.nn",
        "-210427": "SC.n.act.gem.1du_Neg.nn",
        "310427": "SC.n.act.gem.1pl_Neg.n js",
        "-310427": "SC.n.act.gem.1du_Neg.n js",
        "410427": "SC.n.act.gem.1pl_Neg.jmi",
        "-410427": "SC.n.act.gem.1du_Neg.jmi",
        "510427": "SC.n.act.gem.1pl_Neg.n-zp/jwt-zp",
        "-510427": "SC.n.act.gem.1du_Neg.n-zp/jwt-zp",
        "610427": "SC.n.act.gem.1pl_Neg.jwtj",
        "-610427": "SC.n.act.gem.1du_Neg.jwtj",
        "710427": "SC.n.act.gem.1pl_Neg.jwt",
        "-710427": "SC.n.act.gem.1du_Neg.jwt",
        "810427": "SC.n.act.gem.1pl_Neg.w/ꜣ",
        "-810427": "SC.n.act.gem.1du_Neg.w/ꜣ",
        "910427": "SC.n.act.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910427": "SC.n.act.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10428": "SC.n.act.gem.2pl",
        "-10428": "SC.n.act.gem.2du",
        "110428": "SC.n.act.gem.2pl_Neg.n",
        "-110428": "SC.n.act.gem.2du_Neg.n",
        "210428": "SC.n.act.gem.2pl_Neg.nn",
        "-210428": "SC.n.act.gem.2du_Neg.nn",
        "310428": "SC.n.act.gem.2pl_Neg.n js",
        "-310428": "SC.n.act.gem.2du_Neg.n js",
        "410428": "SC.n.act.gem.2pl_Neg.jmi",
        "-410428": "SC.n.act.gem.2du_Neg.jmi",
        "510428": "SC.n.act.gem.2pl_Neg.n-zp/jwt-zp",
        "-510428": "SC.n.act.gem.2du_Neg.n-zp/jwt-zp",
        "610428": "SC.n.act.gem.2pl_Neg.jwtj",
        "-610428": "SC.n.act.gem.2du_Neg.jwtj",
        "710428": "SC.n.act.gem.2pl_Neg.jwt",
        "-710428": "SC.n.act.gem.2du_Neg.jwt",
        "810428": "SC.n.act.gem.2pl_Neg.w/ꜣ",
        "-810428": "SC.n.act.gem.2du_Neg.w/ꜣ",
        "910428": "SC.n.act.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910428": "SC.n.act.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10429": "SC.n.act.gem.3pl",
        "-10429": "SC.n.act.gem.3du",
        "110429": "SC.n.act.gem.3pl_Neg.n",
        "-110429": "SC.n.act.gem.3du_Neg.n",
        "210429": "SC.n.act.gem.3pl_Neg.nn",
        "-210429": "",
        "310429": "SC.n.act.gem.3pl_Neg.n js",
        "-310429": "SC.n.act.gem.3du_Neg.n js",
        "410429": "SC.n.act.gem.3pl_Neg.jmi",
        "-410429": "SC.n.act.gem.3du_Neg.jmi",
        "510429": "SC.n.act.gem.3pl_Neg.n-zp/jwt-zp",
        "-510429": "SC.n.act.gem.3du_Neg.n-zp/jwt-zp",
        "610429": "SC.n.act.gem.3pl_Neg.jwtj",
        "-610429": "SC.n.act.gem.3du_Neg.jwtj",
        "710429": "SC.n.act.gem.3pl_Neg.jwt",
        "-710429": "SC.n.act.gem.3du_Neg.jwt",
        "810429": "SC.n.act.gem.3pl_Neg.w/ꜣ",
        "-810429": "SC.n.act.gem.3du_Neg.w/ꜣ",
        "910429": "SC.n.act.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910429": "SC.n.act.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10430": "SC.n.pass.ngem.nom.subj",
        "110430": "SC.n.pass.ngem.nom.subj_Neg.n",
        "210430": "SC.n.pass.ngem.nom.subj_Neg.nn",
        "310430": "SC.n.pass.ngem.nom.subj_Neg.n js",
        "410430": "SC.n.pass.ngem.nom.subj_Neg.jmi",
        "510430": "SC.n.pass.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610430": "SC.n.pass.ngem.nom.subj_Neg.jwtj",
        "710430": "SC.n.pass.ngem.nom.subj_Neg.jwt",
        "810430": "SC.n.pass.ngem.nom.subj_Neg.w/ꜣ",
        "910430": "SC.n.pass.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10431": "SC.n.pass.ngem.sg1",
        "110431": "SC.n.pass.ngem.1sg_Neg.n",
        "210431": "SC.n.pass.ngem.1sg_Neg.nn",
        "310431": "SC.n.pass.ngem.1sg_Neg.n js",
        "410431": "SC.n.pass.ngem.1sg_Neg.jmi",
        "510431": "SC.n.pass.ngem.1sg_Neg.n-zp/jwt-zp",
        "610431": "SC.n.pass.ngem.1sg_Neg.jwtj",
        "710431": "SC.n.pass.ngem.1sg_Neg.jwt",
        "810431": "SC.n.pass.ngem.1sg_Neg.w/ꜣ",
        "910431": "SC.n.pass.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10432": "SC.n.pass.ngem.sg2m",
        "110432": "SC.n.pass.ngem.2sgm_Neg.n",
        "210432": "SC.n.pass.ngem.2sgm_Neg.nn",
        "310432": "SC.n.pass.ngem.2sgm_Neg.n js",
        "410432": "SC.n.pass.ngem.2sgm_Neg.jmi",
        "510432": "SC.n.pass.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610432": "SC.n.pass.ngem.2sgm_Neg.jwtj",
        "710432": "SC.n.pass.ngem.2sgm_Neg.jwt",
        "810432": "SC.n.pass.ngem.2sgm_Neg.w/ꜣ",
        "910432": "SC.n.pass.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10433": "SC.n.pass.ngem.sg2f",
        "110433": "SC.n.pass.ngem.2sgf_Neg.n",
        "210433": "SC.n.pass.ngem.2sgf_Neg.nn",
        "310433": "SC.n.pass.ngem.2sgf_Neg.n js",
        "410433": "SC.n.pass.ngem.2sgf_Neg.jmi",
        "610433": "SC.n.pass.ngem.2sgf_Neg.jwtj",
        "710433": "SC.n.pass.ngem.2sgf_Neg.jwt",
        "810433": "SC.n.pass.ngem.2sgf_Neg.w/ꜣ",
        "910433": "SC.n.pass.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10434": "SC.n.pass.ngem.sg3m",
        "110434": "SC.n.pass.ngem.3sgm_Neg.n",
        "210434": "SC.n.pass.ngem.3sgm_Neg.nn",
        "310434": "SC.n.pass.ngem.3sgm_Neg.n js",
        "410434": "SC.n.pass.ngem.3sgm_Neg.jmi",
        "510434": "SC.n.pass.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610434": "SC.n.pass.ngem.3sgm_Neg.jwtj",
        "710434": "SC.n.pass.ngem.3sgm_Neg.jwt",
        "810434": "SC.n.pass.ngem.3sgm_Neg.w/ꜣ",
        "910434": "SC.n.pass.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10435": "SC.n.pass.ngem.sg3f",
        "110435": "SC.n.pass.ngem.3sgf_Neg.n",
        "210435": "SC.n.pass.ngem.3sgf_Neg.nn",
        "310435": "SC.n.pass.ngem.3sgf_Neg.n js",
        "410435": "SC.n.pass.ngem.3sgf_Neg.jmi",
        "510435": "SC.n.pass.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610435": "SC.n.pass.ngem.3sgf_Neg.jwtj",
        "710435": "SC.n.pass.ngem.3sgf_Neg.jwt",
        "810435": "SC.n.pass.ngem.3sgf_Neg.w/ꜣ",
        "910435": "SC.n.pass.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10436": "SC.n.pass.ngem.sg3/tw",
        "110436": "SC.n.pass.ngem.3sg_Neg.n",
        "210436": "SC.n.pass.ngem.3sg_Neg.nn",
        "310436": "SC.n.pass.ngem.3sg_Neg.n js",
        "410436": "SC.n.pass.ngem.3sg_Neg.jmi",
        "510436": "SC.n.pass.ngem.3sg_Neg.n-zp/jwt-zp",
        "610436": "SC.n.pass.ngem.3sg_Neg.jwtj",
        "710436": "SC.n.pass.ngem.3sg_Neg.jwt",
        "810436": "SC.n.pass.ngem.3sg_Neg.w/ꜣ",
        "910436": "SC.n.pass.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10437": "SC.n.pass.ngem.1pl",
        "-10437": "SC.n.pass.ngem.1du",
        "110437": "SC.n.pass.ngem.1pl_Neg.n",
        "-110437": "SC.n.pass.ngem.1du_Neg.n",
        "210437": "SC.n.pass.ngem.1pl_Neg.nn",
        "-210437": "SC.n.pass.ngem.1du_Neg.nn",
        "310437": "SC.n.pass.ngem.1pl_Neg.n js",
        "-310437": "SC.n.pass.ngem.1du_Neg.n js",
        "410437": "SC.n.pass.ngem.1pl_Neg.jmi",
        "-410437": "SC.n.pass.ngem.1du_Neg.jmi",
        "510437": "SC.n.pass.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510437": "SC.n.pass.ngem.1du_Neg.n-zp/jwt-zp",
        "610437": "SC.n.pass.ngem.1pl_Neg.jwtj",
        "-610437": "SC.n.pass.ngem.1du_Neg.jwtj",
        "710437": "SC.n.pass.ngem.1pl_Neg.jwt",
        "-710437": "SC.n.pass.ngem.1du_Neg.jwt",
        "810437": "SC.n.pass.ngem.1pl_Neg.w/ꜣ",
        "-810437": "SC.n.pass.ngem.1du_Neg.w/ꜣ",
        "910437": "SC.n.pass.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910437": "SC.n.pass.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10438": "SC.n.pass.ngem.2pl",
        "-10438": "SC.n.pass.ngem.2du",
        "110438": "SC.n.pass.ngem.2pl_Neg.n",
        "-110438": "SC.n.pass.ngem.2du_Neg.n",
        "210438": "SC.n.pass.ngem.2pl_Neg.nn",
        "-210438": "SC.n.pass.ngem.2du_Neg.nn",
        "310438": "SC.n.pass.ngem.2pl_Neg.n js",
        "-310438": "SC.n.pass.ngem.2du_Neg.n js",
        "410438": "SC.n.pass.ngem.2pl_Neg.jmi",
        "-410438": "SC.n.pass.ngem.2du_Neg.jmi",
        "510438": "SC.n.pass.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510438": "SC.n.pass.ngem.2du_Neg.n-zp/jwt-zp",
        "610438": "SC.n.pass.ngem.2pl_Neg.jwtj",
        "-610438": "SC.n.pass.ngem.2du_Neg.jwtj",
        "710438": "SC.n.pass.ngem.2pl_Neg.jwt",
        "-710438": "SC.n.pass.ngem.2du_Neg.jwt",
        "810438": "SC.n.pass.ngem.2pl_Neg.w/ꜣ",
        "-810438": "SC.n.pass.ngem.2du_Neg.w/ꜣ",
        "910438": "SC.n.pass.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910438": "SC.n.pass.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10439": "SC.n.pass.ngem.3pl",
        "-10439": "SC.n.pass.ngem.3du",
        "110439": "SC.n.pass.ngem.3pl_Neg.n",
        "-110439": "SC.n.pass.ngem.3du_Neg.n",
        "210439": "SC.n.pass.ngem.3pl_Neg.nn",
        "-210439": "SC.n.pass.ngem.3du_Neg.nn",
        "310439": "SC.n.pass.ngem.3pl_Neg.n js",
        "-310439": "SC.n.pass.ngem.3du_Neg.n js",
        "410439": "SC.n.pass.ngem.3pl_Neg.jmi",
        "-410439": "SC.n.pass.ngem.3du_Neg.jmi",
        "510439": "SC.n.pass.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510439": "SC.n.pass.ngem.3du_Neg.n-zp/jwt-zp",
        "610439": "SC.n.pass.ngem.3pl_Neg.jwtj",
        "-610439": "SC.n.pass.ngem.3du_Neg.jwtj",
        "710439": "SC.n.pass.ngem.3pl_Neg.jwt",
        "-710439": "SC.n.pass.ngem.3du_Neg.jwt",
        "810439": "SC.n.pass.ngem.3pl_Neg.w/ꜣ",
        "-810439": "SC.n.pass.ngem.3du_Neg.w/ꜣ",
        "910439": "SC.n.pass.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910439": "SC.n.pass.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10440": "SC.n.tw.pass.ngem.nom.subj",
        "110440": "SC.n.tw.pass.ngem.nom.subj_Neg.n",
        "210440": "SC.n.tw.pass.ngem.nom.subj_Neg.nn",
        "310440": "SC.n.tw.pass.ngem.nom.subj_Neg.n js",
        "410440": "SC.n.tw.pass.ngem.nom.subj_Neg.jmi",
        "510440": "SC.n.tw.pass.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610440": "SC.n.tw.pass.ngem.nom.subj_Neg.jwtj",
        "710440": "SC.n.tw.pass.ngem.nom.subj_Neg.jwt",
        "810440": "SC.n.tw.pass.ngem.nom.subj_Neg.w/ꜣ",
        "910440": "SC.n.tw.pass.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10441": "SC.n.tw.pass.ngem.1sg",
        "110441": "SC.n.tw.pass.ngem.1sg_Neg.n",
        "210441": "SC.n.tw.pass.ngem.1sg_Neg.nn",
        "310441": "SC.n.tw.pass.ngem.1sg_Neg.n js",
        "410441": "SC.n.tw.pass.ngem.1sg_Neg.jmi",
        "510441": "SC.n.tw.pass.ngem.1sg_Neg.n-zp/jwt-zp",
        "610441": "SC.n.tw.pass.ngem.1sg_Neg.jwtj",
        "710441": "SC.n.tw.pass.ngem.1sg_Neg.jwt",
        "810441": "SC.n.tw.pass.ngem.1sg_Neg.w/ꜣ",
        "910441": "SC.n.tw.pass.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10442": "SC.n.tw.pass.ngem.2sgm",
        "110442": "SC.n.tw.pass.ngem.2sgm_Neg.n",
        "210442": "SC.n.tw.pass.ngem.2sgm_Neg.nn",
        "310442": "SC.n.tw.pass.ngem.2sgm_Neg.n js",
        "410442": "SC.n.tw.pass.ngem.2sgm_Neg.jmi",
        "510442": "SC.n.tw.pass.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610442": "SC.n.tw.pass.ngem.2sgm_Neg.jwtj",
        "710442": "SC.n.tw.pass.ngem.2sgm_Neg.jwt",
        "810442": "SC.n.tw.pass.ngem.2sgm_Neg.w/ꜣ",
        "910442": "SC.n.tw.pass.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10443": "SC.n.tw.pass.ngem.2sgf",
        "110443": "SC.n.tw.pass.ngem.2sgf_Neg.n",
        "210443": "SC.n.tw.pass.ngem.2sgf_Neg.nn",
        "310443": "SC.n.tw.pass.ngem.2sgf_Neg.n js",
        "410443": "SC.n.tw.pass.ngem.2sgf_Neg.jmi",
        "510443": "SC.n.tw.pass.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610443": "SC.n.tw.pass.ngem.2sgf_Neg.jwtj",
        "710443": "SC.n.tw.pass.ngem.2sgf_Neg.jwt",
        "810443": "SC.n.tw.pass.ngem.2sgf_Neg.w/ꜣ",
        "910443": "SC.n.tw.pass.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10444": "SC.n.tw.pass.ngem.3sgm",
        "110444": "SC.n.tw.pass.ngem.3sgm_Neg.n",
        "210444": "SC.n.tw.pass.ngem.3sgm_Neg.nn",
        "310444": "SC.n.tw.pass.ngem.3sgm_Neg.n js",
        "410444": "SC.n.tw.pass.ngem.3sgm_Neg.jmi",
        "510444": "SC.n.tw.pass.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610444": "SC.n.tw.pass.ngem.3sgm_Neg.jwtj",
        "710444": "SC.n.tw.pass.ngem.3sgm_Neg.jwt",
        "810444": "SC.n.tw.pass.ngem.3sgm_Neg.w/ꜣ",
        "910444": "SC.n.tw.pass.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10445": "SC.n.tw.pass.ngem.3sgf",
        "110445": "SC.n.tw.pass.ngem.3sgf_Neg.n",
        "210445": "SC.n.tw.pass.ngem.3sgf_Neg.nn",
        "310445": "SC.n.tw.pass.ngem.3sgf_Neg.n js",
        "410445": "SC.n.tw.pass.ngem.3sgf_Neg.jmi",
        "510445": "SC.n.tw.pass.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610445": "SC.n.tw.pass.ngem.3sgf_Neg.jwtj",
        "710445": "SC.n.tw.pass.ngem.3sgf_Neg.jwt",
        "810445": "SC.n.tw.pass.ngem.3sgf_Neg.w/ꜣ",
        "910445": "SC.n.tw.pass.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10446": "SC.n.tw.pass.ngem.3sg",
        "110446": "SC.n.tw.pass.ngem.3sg_Neg.n",
        "210446": "SC.n.tw.pass.ngem.3sg_Neg.nn",
        "310446": "SC.n.tw.pass.ngem.3sg_Neg.n js",
        "410446": "SC.n.tw.pass.ngem.3sg_Neg.jmi",
        "510446": "SC.n.tw.pass.ngem.3sg_Neg.n-zp/jwt-zp",
        "610446": "SC.n.tw.pass.ngem.3sg_Neg.jwtj",
        "710446": "SC.n.tw.pass.ngem.3sg_Neg.jwt",
        "810446": "SC.n.tw.pass.ngem.3sg_Neg.w/ꜣ",
        "910446": "SC.n.tw.pass.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10447": "SC.n.tw.pass.ngem.1pl",
        "-10447": "SC.n.tw.pass.ngem.1du",
        "110447": "SC.n.tw.pass.ngem.1pl_Neg.n",
        "-110447": "SC.n.tw.pass.ngem.1du_Neg.n",
        "210447": "SC.n.tw.pass.ngem.1pl_Neg.nn",
        "-210447": "SC.n.tw.pass.ngem.1du_Neg.nn",
        "310447": "SC.n.tw.pass.ngem.1pl_Neg.n js",
        "-310447": "SC.n.tw.pass.ngem.1du_Neg.n js",
        "410447": "SC.n.tw.pass.ngem.1pl_Neg.jmi",
        "-410447": "SC.n.tw.pass.ngem.1du_Neg.jmi",
        "510447": "SC.n.tw.pass.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510447": "SC.n.tw.pass.ngem.1du_Neg.n-zp/jwt-zp",
        "610447": "SC.n.tw.pass.ngem.1pl_Neg.jwtj",
        "-610447": "SC.n.tw.pass.ngem.1du_Neg.jwtj",
        "710447": "SC.n.tw.pass.ngem.1pl_Neg.jwt",
        "-710447": "SC.n.tw.pass.ngem.1du_Neg.jwt",
        "810447": "SC.n.tw.pass.ngem.1pl_Neg.w/ꜣ",
        "-810447": "SC.n.tw.pass.ngem.1du_Neg.w/ꜣ",
        "910447": "SC.n.tw.pass.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910447": "SC.n.tw.pass.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10448": "SC.n.tw.pass.ngem.2pl",
        "-10448": "SC.n.tw.pass.ngem.2du",
        "110448": "SC.n.tw.pass.ngem.2pl_Neg.n",
        "-110448": "SC.n.tw.pass.ngem.2du_Neg.n",
        "210448": "SC.n.tw.pass.ngem.2pl_Neg.nn",
        "-210448": "SC.n.tw.pass.ngem.2du_Neg.nn",
        "310448": "SC.n.tw.pass.ngem.2pl_Neg.n js",
        "-310448": "SC.n.tw.pass.ngem.2du_Neg.n js",
        "410448": "SC.n.tw.pass.ngem.2pl_Neg.jmi",
        "-410448": "SC.n.tw.pass.ngem.2du_Neg.jmi",
        "510448": "SC.n.tw.pass.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510448": "SC.n.tw.pass.ngem.2du_Neg.n-zp/jwt-zp",
        "610448": "SC.n.tw.pass.ngem.2pl_Neg.jwtj",
        "-610448": "SC.n.tw.pass.ngem.2du_Neg.jwtj",
        "710448": "SC.n.tw.pass.ngem.2pl_Neg.jwt",
        "-710448": "SC.n.tw.pass.ngem.2du_Neg.jwt",
        "810448": "SC.n.tw.pass.ngem.2pl_Neg.w/ꜣ",
        "-810448": "SC.n.tw.pass.ngem.2du_Neg.w/ꜣ",
        "910448": "SC.n.tw.pass.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910448": "SC.n.tw.pass.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10449": "SC.n.tw.pass.ngem.3pl",
        "-10449": "SC.n.tw.pass.ngem.3du",
        "110449": "SC.n.tw.pass.ngem.3pl_Neg.n",
        "-110449": "SC.n.tw.pass.ngem.3du_Neg.n",
        "210449": "SC.n.tw.pass.ngem.3pl_Neg.nn",
        "-210449": "SC.n.tw.pass.ngem.3du_Neg.nn",
        "310449": "SC.n.tw.pass.ngem.3pl_Neg.n js",
        "-310449": "SC.n.tw.pass.ngem.3du_Neg.n js",
        "410449": "SC.n.tw.pass.ngem.3pl_Neg.jmi",
        "-410449": "SC.n.tw.pass.ngem.3du_Neg.jmi",
        "510449": "SC.n.tw.pass.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510449": "SC.n.tw.pass.ngem.3du_Neg.n-zp/jwt-zp",
        "610449": "SC.n.tw.pass.ngem.3pl_Neg.jwtj",
        "-610449": "SC.n.tw.pass.ngem.3du_Neg.jwtj",
        "710449": "SC.n.tw.pass.ngem.3pl_Neg.jwt",
        "-710449": "SC.n.tw.pass.ngem.3du_Neg.jwt",
        "810449": "SC.n.tw.pass.ngem.3pl_Neg.w/ꜣ",
        "-810449": "SC.n.tw.pass.ngem.3du_Neg.w/ꜣ",
        "910449": "SC.n.tw.pass.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910449": "SC.n.tw.pass.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10460": "",
        "10461": "",
        "10462": "",
        "10463": "",
        "10464": "",
        "10465": "",
        "10466": "",
        "10467": "",
        "10468": "",
        "10469": "",
        "10480": "SC.n.tw.pass.gem.nom.subj",
        "110480": "SC.n.tw.pass.gem.nom.subj_Neg.n",
        "210480": "SC.n.tw.pass.gem.nom.subj_Neg.nn",
        "310480": "SC.n.tw.pass.gem.nom.subj_Neg.n js",
        "410480": "SC.n.tw.pass.gem.nom.subj_Neg.jmi",
        "510480": "SC.n.tw.pass.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610480": "SC.n.tw.pass.gem.nom.subj_Neg.jwtj",
        "710480": "SC.n.tw.pass.gem.nom.subj_Neg.jwt",
        "810480": "SC.n.tw.pass.gem.nom.subj_Neg.w/ꜣ",
        "910480": "SC.n.tw.pass.gem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10481": "SC.n.tw.pass.gem.1sg",
        "110481": "SC.n.tw.pass.gem.1sg_Neg.n",
        "210481": "SC.n.tw.pass.gem.1sg_Neg.nn",
        "310481": "SC.n.tw.pass.gem.1sg_Neg.n js",
        "410481": "SC.n.tw.pass.gem.1sg_Neg.jmi",
        "510481": "SC.n.tw.pass.gem.1sg_Neg.n-zp/jwt-zp",
        "610481": "SC.n.tw.pass.gem.1sg_Neg.jwtj",
        "710481": "SC.n.tw.pass.gem.1sg_Neg.jwt",
        "810481": "SC.n.tw.pass.gem.1sg_Neg.w/ꜣ",
        "910481": "SC.n.tw.pass.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10482": "SC.n.tw.pass.gem.2sgm",
        "110482": "SC.n.tw.pass.gem.2sgm_Neg.n",
        "210482": "SC.n.tw.pass.gem.2sgm_Neg.nn",
        "310482": "SC.n.tw.pass.gem.2sgm_Neg.n js",
        "410482": "SC.n.tw.pass.gem.2sgm_Neg.jmi",
        "510482": "SC.n.tw.pass.gem.2sgm_Neg.n-zp/jwt-zp",
        "610482": "SC.n.tw.pass.gem.2sgm_Neg.jwtj",
        "710482": "SC.n.tw.pass.gem.2sgm_Neg.jwt",
        "810482": "SC.n.tw.pass.gem.2sgm_Neg.w/ꜣ",
        "910482": "SC.n.tw.pass.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10483": "SC.n.tw.pass.gem.2sgf",
        "110483": "SC.n.tw.pass.gem.2sgf_Neg.n",
        "210483": "SC.n.tw.pass.gem.2sgf_Neg.nn",
        "310483": "SC.n.tw.pass.gem.2sgf_Neg.n js",
        "410483": "SC.n.tw.pass.gem.2sgf_Neg.jmi",
        "510483": "SC.n.tw.pass.gem.2sgf_Neg.n-zp/jwt-zp",
        "610483": "SC.n.tw.pass.gem.2sgf_Neg.jwtj",
        "710483": "SC.n.tw.pass.gem.2sgf_Neg.jwt",
        "810483": "SC.n.tw.pass.gem.2sgf_Neg.w/ꜣ",
        "910483": "SC.n.tw.pass.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10484": "SC.n.tw.pass.gem.3sgm",
        "110484": "SC.n.tw.pass.gem.3sgm_Neg.n",
        "210484": "SC.n.tw.pass.gem.3sgm_Neg.nn",
        "310484": "SC.n.tw.pass.gem.3sgm_Neg.n js",
        "410484": "SC.n.tw.pass.gem.3sgm_Neg.jmi",
        "510484": "SC.n.tw.pass.gem.3sgm_Neg.n-zp/jwt-zp",
        "610484": "SC.n.tw.pass.gem.3sgm_Neg.jwtj",
        "710484": "SC.n.tw.pass.gem.3sgm_Neg.jwt",
        "810484": "SC.n.tw.pass.gem.3sgm_Neg.w/ꜣ",
        "910484": "SC.n.tw.pass.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10485": "SC.n.tw.pass.gem.3sgf",
        "110485": "SC.n.tw.pass.gem.3sgf_Neg.n",
        "210485": "SC.n.tw.pass.gem.3sgf_Neg.nn",
        "310485": "SC.n.tw.pass.gem.3sgf_Neg.n js",
        "410485": "SC.n.tw.pass.gem.3sgf_Neg.jmi",
        "510485": "SC.n.tw.pass.gem.3sgf_Neg.n-zp/jwt-zp",
        "610485": "SC.n.tw.pass.gem.3sgf_Neg.jwtj",
        "710485": "SC.n.tw.pass.gem.3sgf_Neg.jwt",
        "810485": "SC.n.tw.pass.gem.3sgf_Neg.w/ꜣ",
        "910485": "SC.n.tw.pass.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10486": "SC.n.tw.pass.gem.3sg",
        "110486": "SC.n.tw.pass.gem.3sg_Neg.n",
        "210486": "SC.n.tw.pass.gem.3sg_Neg.nn",
        "310486": "SC.n.tw.pass.gem.3sg_Neg.n js",
        "410486": "SC.n.tw.pass.gem.3sg_Neg.jmi",
        "510486": "SC.n.tw.pass.gem.3sg_Neg.n-zp/jwt-zp",
        "610486": "SC.n.tw.pass.gem.3sg_Neg.jwtj",
        "710486": "SC.n.tw.pass.gem.3sg_Neg.jwt",
        "810486": "SC.n.tw.pass.gem.3sg_Neg.w/ꜣ",
        "910486": "SC.n.tw.pass.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10487": "SC.n.tw.pass.gem.1pl",
        "-10487": "SC.n.tw.pass.gem.1du",
        "110487": "SC.n.tw.pass.gem.1pl_Neg.n",
        "-110487": "SC.n.tw.pass.gem.1du_Neg.n",
        "210487": "SC.n.tw.pass.gem.1pl_Neg.nn",
        "-210487": "SC.n.tw.pass.gem.1du_Neg.nn",
        "310487": "SC.n.tw.pass.gem.1pl_Neg.n js",
        "-310487": "SC.n.tw.pass.gem.1du_Neg.n js",
        "410487": "SC.n.tw.pass.gem.1pl_Neg.jmi",
        "-410487": "SC.n.tw.pass.gem.1du_Neg.jmi",
        "510487": "SC.n.tw.pass.gem.1pl_Neg.n-zp/jwt-zp",
        "-510487": "SC.n.tw.pass.gem.1du_Neg.n-zp/jwt-zp",
        "610487": "SC.n.tw.pass.gem.1pl_Neg.jwtj",
        "-610487": "SC.n.tw.pass.gem.1du_Neg.jwtj",
        "710487": "SC.n.tw.pass.gem.1pl_Neg.jwt",
        "-710487": "SC.n.tw.pass.gem.1du_Neg.jwt",
        "810487": "SC.n.tw.pass.gem.1pl_Neg.w/ꜣ",
        "-810487": "SC.n.tw.pass.gem.1du_Neg.w/ꜣ",
        "910487": "SC.n.tw.pass.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910487": "SC.n.tw.pass.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10488": "SC.n.tw.pass.gem.2pl",
        "-10488": "SC.n.tw.pass.gem.2du",
        "110488": "SC.n.tw.pass.gem.2pl_Neg.n",
        "-110488": "SC.n.tw.pass.gem.2du_Neg.n",
        "210488": "SC.n.tw.pass.gem.2pl_Neg.nn",
        "-210488": "SC.n.tw.pass.gem.2du_Neg.nn",
        "310488": "SC.n.tw.pass.gem.2pl_Neg.n js",
        "-310488": "SC.n.tw.pass.gem.2du_Neg.n js",
        "410488": "SC.n.tw.pass.gem.2pl_Neg.jmi",
        "-410488": "SC.n.tw.pass.gem.2du_Neg.jmi",
        "510488": "SC.n.tw.pass.gem.2pl_Neg.n-zp/jwt-zp",
        "-510488": "SC.n.tw.pass.gem.2du_Neg.n-zp/jwt-zp",
        "610488": "SC.n.tw.pass.gem.2pl_Neg.jwtj",
        "-610488": "SC.n.tw.pass.gem.2du_Neg.jwtj",
        "710488": "SC.n.tw.pass.gem.2pl_Neg.jwt",
        "-710488": "SC.n.tw.pass.gem.2du_Neg.jwt",
        "810488": "SC.n.tw.pass.gem.2pl_Neg.w/ꜣ",
        "-810488": "SC.n.tw.pass.gem.2du_Neg.w/ꜣ",
        "910488": "SC.n.tw.pass.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910488": "SC.n.tw.pass.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10489": "SC.n.tw.pass.gem.3pl",
        "-10489": "SC.n.tw.pass.gem.3du",
        "110489": "SC.n.tw.pass.gem.3pl_Neg.n",
        "-110489": "SC.n.tw.pass.gem.3du_Neg.n",
        "210489": "SC.n.tw.pass.gem.3pl_Neg.nn",
        "-210489": "SC.n.tw.pass.gem.3du_Neg.nn",
        "310489": "SC.n.tw.pass.gem.3pl_Neg.n js",
        "-310489": "SC.n.tw.pass.gem.3du_Neg.n js",
        "410489": "SC.n.tw.pass.gem.3pl_Neg.jmi",
        "-410489": "SC.n.tw.pass.gem.3du_Neg.jmi",
        "510489": "SC.n.tw.pass.gem.3pl_Neg.n-zp/jwt-zp",
        "-510489": "SC.n.tw.pass.gem.3du_Neg.n-zp/jwt-zp",
        "610489": "SC.n.tw.pass.gem.3pl_Neg.jwtj",
        "-610489": "SC.n.tw.pass.gem.3du_Neg.jwtj",
        "710489": "SC.n.tw.pass.gem.3pl_Neg.jwt",
        "-710489": "SC.n.tw.pass.gem.3du_Neg.jwt",
        "810489": "SC.n.tw.pass.gem.3pl_Neg.w/ꜣ",
        "-810489": "SC.n.tw.pass.gem.3du_Neg.w/ꜣ",
        "910489": "SC.n.tw.pass.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910489": "SC.n.tw.pass.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10500": "SC.jn.act.ngem.nom.subj",
        "10501": "SC.jn.act.ngem.1sg",
        "10502": "SC.jn.act.ngem.2sgm",
        "10503": "SC.jn.act.ngem.2sgf",
        "10504": "SC.jn.act.ngem.3sgm",
        "10505": "SC.jn.act.ngem.3sgf",
        "10506": "SC.jn.act.ngem.3sg",
        "10507": "SC.jn.act.ngem.1pl",
        "-10507": "SC.jn.act.ngem.1du",
        "10508": "SC.jn.act.ngem.2pl",
        "-10508": "SC.jn.act.ngem.2du",
        "10509": "SC.jn.act.ngem.3pl",
        "-10509": "SC.jn.act.ngem.3du",
        "10520": "",
        "10521": "",
        "10522": "",
        "10523": "",
        "10524": "",
        "10525": "",
        "10526": "",
        "10527": "",
        "10528": "",
        "10529": "",
        "10540": "SC.jn.act.gem.nom.subj",
        "10541": "SC.jn.act.gem.1sg",
        "10542": "SC.jn.act.gem.2sgm",
        "10543": "SC.jn.act.gem.2sgf",
        "10544": "SC.jn.act.gem.3sgm",
        "10545": "SC.jn.act.gem.3sgf",
        "10546": "SC.jn.act.gem.3sg",
        "10547": "SC.jn.act.gem.1pl",
        "-10547": "SC.jn.act.gem.1du",
        "10548": "SC.jn.act.gem.2pl",
        "-10548": "SC.jn.act.gem.2du",
        "10549": "SC.jn.act.gem.3pl",
        "-10549": "SC.jn.act.gem.3du",
        "10560": "SC.jn.tw.pass.ngem.nom.subj",
        "10561": "SC.jn.tw.pass.ngem.1sg",
        "10562": "SC.jn.tw.pass.ngem.2sgm",
        "10563": "SC.jn.tw.pass.ngem.2sgf",
        "10564": "SC.jn.tw.pass.ngem.3sgm",
        "10565": "SC.jn.tw.pass.ngem.3sgf",
        "10566": "SC.jn.tw.pass.ngem.3sg",
        "10567": "SC.jn.tw.pass.ngem.1pl",
        "-10567": "SC.jn.tw.pass.ngem.1du",
        "10568": "SC.jn.tw.pass.ngem.2pl",
        "-10568": "SC.jn.tw.pass.ngem.2du",
        "10569": "SC.jn.tw.pass.ngem.3pl",
        "-10569": "SC.jn.tw.pass.ngem.3du",
        "10570": "SC.jn.tw.pass.ngem.impers",
        "10580": "",
        "10581": "",
        "10582": "",
        "10583": "",
        "10584": "",
        "10585": "",
        "10586": "",
        "10587": "",
        "10588": "",
        "10589": "",
        "10600": "SC.ḫr.act.ngem.nom.subj",
        "10601": "SC.ḫr.act.ngem.1sg",
        "10602": "SC.ḫr.act.ngem.2sgm",
        "10603": "SC.ḫr.act.ngem.2sgf",
        "10604": "SC.ḫr.act.ngem.3sgm",
        "10605": "SC.ḫr.act.ngem.3sgf",
        "10606": "SC.ḫr.act.ngem.3sg",
        "10607": "SC.ḫr.act.ngem.1pl",
        "-10607": "SC.ḫr.act.ngem.1du",
        "10608": "SC.ḫr.act.ngem.2pl",
        "-10608": "SC.ḫr.act.ngem.2du",
        "10609": "SC.ḫr.act.ngem.3pl",
        "-10609": "SC.ḫr.act.ngem.3du",
        "10610": "ḫr+SC.act.ngem.nom.subj",
        "10611": "ḫr+SC.act.ngem.1sg",
        "10612": "ḫr+SC.act.ngem.2sgm",
        "10613": "ḫr+SC.act.ngem.2sgf",
        "10614": "ḫr+SC.act.ngem.3sgm",
        "10615": "ḫr+SC.act.ngem.3sgf",
        "10616": "ḫr+SC.act.ngem.3sg",
        "10617": "ḫr+SC.act.ngem.1pl",
        "-10617": "ḫr+SC.act.ngem.1du",
        "10618": "ḫr+SC.act.ngem.2pl",
        "-10618": "ḫr+SC.act.ngem.2du",
        "10619": "ḫr+SC.act.ngem.3pl",
        "-10619": "ḫr+SC.act.ngem.3du",
        "10620": "",
        "10621": "",
        "10622": "",
        "10623": "",
        "10624": "",
        "10625": "",
        "10626": "",
        "10627": "",
        "10628": "",
        "10629": "",
        "10640": "SC.ḫr.act.gem.nom.subj",
        "10641": "SC.ḫr.act.gem.1sg",
        "10642": "SC.ḫr.act.gem.2sgm",
        "10643": "SC.ḫr.act.gem.2sgf",
        "10644": "SC.ḫr.act.gem.3sgm",
        "10645": "SC.ḫr.act.gem.3sgf",
        "10646": "SC.ḫr.act.gem.3sg",
        "10647": "SC.ḫr.act.gem.1pl",
        "-10647": "SC.ḫr.act.gem.1du",
        "10648": "SC.ḫr.act.gem.2pl",
        "-10648": "SC.ḫr.act.gem.2du",
        "10649": "SC.ḫr.act.gem.3pl",
        "-10649": "SC.ḫr.act.gem.3du",
        "10650": "ḫr+SC.act.gem.nom.subj",
        "10651": "ḫr+SC.act.gem.1sg",
        "10652": "ḫr+SC.act.gem.2sgm",
        "10653": "ḫr+SC.act.gem.2sgf",
        "10654": "ḫr+SC.act.gem.3sgm",
        "10655": "ḫr+SC.act.gem.3sgf",
        "10656": "ḫr+SC.act.gem.3sg",
        "10657": "ḫr+SC.act.gem.1pl",
        "-10657": "ḫr+SC.act.gem.1du",
        "10658": "ḫr+SC.act.gem.2pl",
        "-10658": "ḫr+SC.act.gem.2du",
        "10659": "ḫr+SC.act.gem.3pl",
        "-10659": "ḫr+SC.act.gem.3du",
        "10660": "SC.ḫr.tw.pass.ngem.nom.subj",
        "10661": "SC.ḫr.tw.pass.ngem.1sg",
        "10662": "SC.ḫr.tw.pass.ngem.2sgm",
        "10663": "SC.ḫr.tw.pass.ngem.2sgf",
        "10664": "SC.ḫr.tw.pass.ngem.3sgm",
        "10665": "SC.ḫr.tw.pass.ngem.3sgf",
        "10666": "SC.ḫr.tw.pass.ngem.3sg",
        "10667": "SC.ḫr.tw.pass.ngem.1pl",
        "-10667": "SC.ḫr.tw.pass.ngem.1du",
        "10668": "SC.ḫr.tw.pass.ngem.2pl",
        "-10668": "SC.ḫr.tw.pass.ngem.2du",
        "10669": "SC.ḫr.tw.pass.ngem.3pl",
        "-10669": "SC.ḫr.tw.pass.ngem.3du",
        "10670": "ḫr+SC.tw.pass.ngem.nom.subj",
        "10671": "ḫr+SC.tw.pass.ngem.1sg",
        "10672": "ḫr+SC.tw.pass.ngem.2sgm",
        "10673": "ḫr+SC.tw.pass.ngem.2sgf",
        "10674": "ḫr+SC.tw.pass.ngem.3sgm",
        "10675": "ḫr+SC.tw.pass.ngem.3sgf",
        "10676": "ḫr+SC.tw.pass.ngem.3sg",
        "10677": "ḫr+SC.tw.pass.ngem.1pl",
        "-10677": "ḫr+SC.tw.pass.ngem.1du",
        "10678": "ḫr+SC.tw.pass.ngem.2pl",
        "-10678": "ḫr+SC.tw.pass.ngem.2du",
        "10679": "ḫr+SC.tw.pass.ngem.3pl",
        "-10679": "ḫr+SC.tw.pass.ngem.3du",
        "10680": "",
        "10681": "",
        "10682": "",
        "10683": "",
        "10684": "",
        "10685": "",
        "10686": "",
        "10687": "",
        "10688": "",
        "10689": "",
        "10700": "SC.ḫr.tw.pass.gem.nom.subj",
        "10701": "SC.ḫr.tw.pass.gem.1sg",
        "10702": "SC.ḫr.tw.pass.gem.2sgm",
        "10703": "SC.ḫr.tw.pass.gem.2sgf",
        "10704": "SC.ḫr.tw.pass.gem.3sgm",
        "10705": "SC.ḫr.tw.pass.gem.3sgf",
        "10706": "SC.ḫr.tw.pass.gem.3sg",
        "10707": "SC.ḫr.tw.pass.gem.1pl",
        "-10707": "SC.ḫr.tw.pass.gem.1du",
        "10708": "SC.ḫr.tw.pass.gem.2pl",
        "-10708": "SC.ḫr.tw.pass.gem.2du",
        "10709": "SC.ḫr.tw.pass.gem.3pl",
        "-10709": "SC.ḫr.tw.pass.gem.3du",
        "10710": "ḫr+SC.tw.pass.gem.nom.subj",
        "10711": "ḫr+SC.tw.pass.gem.1sg",
        "10712": "ḫr+SC.tw.pass.gem.2sgm",
        "10713": "ḫr+SC.tw.pass.gem.2sgf",
        "10714": "ḫr+SC.tw.pass.gem.3sgm",
        "10715": "ḫr+SC.tw.pass.gem.3sgf",
        "10716": "ḫr+SC.tw.pass.gem.3sg",
        "10717": "ḫr+SC.tw.pass.gem.1pl",
        "-10717": "ḫr+SC.tw.pass.gem.1du",
        "10718": "ḫr+SC.tw.pass.gem.2pl",
        "-10718": "ḫr+SC.tw.pass.gem.2du",
        "10719": "ḫr+SC.tw.pass.gem.3pl",
        "-10719": "ḫr+SC.tw.pass.gem.3du",
        "10720": "SC.kꜣ.act.ngem.nom.subj",
        "10721": "SC.kꜣ.act.ngem.1sg",
        "10722": "SC.kꜣ.act.ngem.2sgm",
        "10723": "SC.kꜣ.act.ngem.2sgf",
        "10724": "SC.kꜣ.act.ngem.3sgm",
        "10725": "SC.kꜣ.act.ngem.3sgf",
        "10726": "SC.kꜣ.act.ngem.3sg",
        "10727": "SC.kꜣ.act.ngem.1pl",
        "-10727": "SC.kꜣ.act.ngem.1du",
        "10728": "SC.kꜣ.act.ngem.2pl",
        "-10728": "SC.kꜣ.act.ngem.2du",
        "10729": "SC.kꜣ.act.ngem.3pl",
        "-10729": "SC.kꜣ.act.ngem.3du",
        "10730": "kꜣ+SC.act.ngem.nom.subj",
        "10731": "kꜣ+SC.act.ngem.1sg",
        "10732": "kꜣ+SC.act.ngem.2sgm",
        "10733": "kꜣ+SC.act.ngem.2sgf",
        "10734": "kꜣ+SC.act.ngem.3sgm",
        "10735": "kꜣ+SC.act.ngem.3sgf",
        "10736": "kꜣ+SC.act.ngem.3sg",
        "10737": "kꜣ+SC.act.ngem.1pl",
        "-10737": "kꜣ+SC.act.ngem.1du",
        "10738": "kꜣ+SC.act.ngem.2pl",
        "-10738": "kꜣ+SC.act.ngem.2du",
        "10739": "kꜣ+SC.act.ngem.3pl",
        "-10739": "kꜣ+SC.act.ngem.3du",
        "10740": "",
        "10741": "",
        "10742": "",
        "10743": "",
        "10744": "",
        "10745": "",
        "10746": "",
        "10747": "",
        "10748": "",
        "10749": "",
        "10760": "SC.kꜣ.act.gem.nom.subj",
        "10761": "SC.kꜣ.act.gem.1sg",
        "10762": "SC.kꜣ.act.gem.2sgm",
        "10763": "SC.kꜣ.act.gem.2sgf",
        "10764": "SC.kꜣ.act.gem.3sgm",
        "10765": "SC.kꜣ.act.gem.3sgf",
        "10766": "SC.kꜣ.act.gem.3sg",
        "10767": "SC.kꜣ.act.gem.1pl",
        "-10767": "SC.kꜣ.act.gem.1du",
        "10768": "SC.kꜣ.act.gem.2pl",
        "-10768": "SC.kꜣ.act.gem.2du",
        "10769": "SC.kꜣ.act.gem.3pl",
        "-10769": "SC.kꜣ.act.gem.3du",
        "10770": "kꜣ+SC.act.gem.nom.subj",
        "10771": "kꜣ+SC.act.gem.1sg",
        "10772": "kꜣ+SC.act.gem.2sgm",
        "10773": "kꜣ+SC.act.gem.2sgf",
        "10774": "kꜣ+SC.act.gem.3sgm",
        "10775": "kꜣ+SC.act.gem.3sgf",
        "10776": "kꜣ+SC.act.gem.3sg",
        "10777": "kꜣ+SC.act.gem.1pl",
        "-10777": "kꜣ+SC.act.gem.1du",
        "10778": "kꜣ+SC.act.gem.2pl",
        "-10778": "kꜣ+SC.act.gem.2du",
        "10779": "kꜣ+SC.act.gem.3pl",
        "-10779": "kꜣ+SC.act.gem.3du",
        "10780": "SC.kꜣ.tw.pass.ngem.nom.subj",
        "10781": "SC.kꜣ.tw.pass.ngem.1sg",
        "10782": "SC.kꜣ.tw.pass.ngem.2sgm",
        "10783": "SC.kꜣ.tw.pass.ngem.2sgf",
        "10784": "SC.kꜣ.tw.pass.ngem.3sgm",
        "10785": "SC.kꜣ.tw.pass.ngem.3sgf",
        "10786": "SC.kꜣ.tw.pass.ngem.3sg",
        "10787": "SC.kꜣ.tw.pass.ngem.1pl",
        "-10787": "SC.kꜣ.tw.pass.ngem.1du",
        "10788": "SC.kꜣ.tw.pass.ngem.2pl",
        "-10788": "SC.kꜣ.tw.pass.ngem.2du",
        "10789": "SC.kꜣ.tw.pass.ngem.3pl",
        "-10789": "SC.kꜣ.tw.pass.ngem.3du",
        "10790": "kꜣ+SC.tw.pass.ngem.nom.subj",
        "10791": "kꜣ+SC.tw.pass.ngem.1sg",
        "10792": "kꜣ+SC.tw.pass.ngem.2sgm",
        "10793": "kꜣ+SC.tw.pass.ngem.2sgf",
        "10794": "kꜣ+SC.tw.pass.ngem.3sgm",
        "10795": "kꜣ+SC.tw.pass.ngem.3sgf",
        "10796": "kꜣ+SC.tw.pass.ngem.3sg",
        "10797": "kꜣ+SC.tw.pass.ngem.1pl",
        "-10797": "kꜣ+SC.tw.pass.ngem.1du",
        "10798": "kꜣ+SC.tw.pass.ngem.2pl",
        "-10798": "kꜣ+SC.tw.pass.ngem.2du",
        "10799": "kꜣ+SC.tw.pass.ngem.3pl",
        "-10799": "kꜣ+SC.tw.pass.ngem.3du",
        "10800": "SC.n.act.ngem.impers",
        "110800": "SC.n.act.ngem.impers_Neg.n",
        "210800": "SC.n.act.ngem.impers_Neg.nn",
        "10810": "SC.n.tw.pass.ngem.impers",
        "110810": "SC.n.tw.pass.ngem.impers_Neg.n",
        "210810": "SC.n.tw.pass.ngem.impers_Neg.nn",
        "10820": "SC.kꜣ.tw.pass.gem.nom.subj",
        "10821": "SC.kꜣ.tw.pass.gem.1sg",
        "10822": "SC.kꜣ.tw.pass.gem.2sgm",
        "10823": "SC.kꜣ.tw.pass.gem.2sgf",
        "10824": "SC.kꜣ.tw.pass.gem.3sgm",
        "10825": "SC.kꜣ.tw.pass.gem.3sgf",
        "10826": "SC.kꜣ.tw.pass.gem.3sg",
        "10827": "SC.kꜣ.tw.pass.gem.1pl",
        "-10827": "SC.kꜣ.tw.pass.gem.1du",
        "10828": "SC.kꜣ.tw.pass.gem.2pl",
        "-10828": "SC.kꜣ.tw.pass.gem.2du",
        "10829": "SC.kꜣ.tw.pass.gem.3pl",
        "-10829": "SC.kꜣ.tw.pass.gem.3du",
        "10830": "kꜣ+SC.tw.pass.gem.nom.subj",
        "10831": "kꜣ+SC.tw.pass.gem.1sg",
        "10832": "kꜣ+SC.tw.pass.gem.2sgm",
        "10833": "kꜣ+SC.tw.pass.gem.2sgf",
        "10834": "kꜣ+SC.tw.pass.gem.3sgm",
        "10835": "kꜣ+SC.tw.pass.gem.3sgf",
        "10836": "kꜣ+SC.tw.pass.gem.3sg",
        "10837": "kꜣ+SC.tw.pass.gem.1pl",
        "-10837": "kꜣ+SC.tw.pass.gem.1du",
        "10838": "kꜣ+SC.tw.pass.gem.2pl",
        "-10838": "kꜣ+SC.tw.pass.gem.2du",
        "10839": "kꜣ+SC.tw.pass.gem.3pl",
        "-10839": "kꜣ+SC.tw.pass.gem.3du",
        "10840": "SC.t.act.ngem.nom.subj",
        "110840": "SC.t.act.ngem.nom.subj_Neg.n",
        "210840": "SC.t.act.ngem.nom.subj_Neg.nn",
        "310840": "SC.t.act.ngem.nom.subj_Neg.n js",
        "410840": "SC.t.act.ngem.nom.subj_Neg.jmi",
        "510840": "SC.t.act.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610840": "SC.t.act.ngem.nom.subj_Neg.jwtj",
        "710840": "SC.t.act.ngem.nom.subj_Neg.jwt",
        "810840": "SC.t.act.ngem.nom.subj_Neg.w/ꜣ",
        "910840": "SC.t.act.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10841": "SC.t.act.ngem.1sg",
        "110841": "SC.t.act.ngem.1sg_Neg.n",
        "210841": "SC.t.act.ngem.1sg_Neg.nn",
        "310841": "SC.t.act.ngem.1sg_Neg.n js",
        "410841": "SC.t.act.ngem.1sg_Neg.jmi",
        "510841": "SC.t.act.ngem.1sg_Neg.n-zp/jwt-zp",
        "610841": "SC.t.act.ngem.1sg_Neg.jwtj",
        "710841": "SC.t.act.ngem.1sg_Neg.jwt",
        "810841": "SC.t.act.ngem.1sg_Neg.w/ꜣ",
        "910841": "SC.t.act.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10842": "SC.t.act.ngem.2sgm",
        "110842": "SC.t.act.ngem.2sgm_Neg.n",
        "210842": "SC.t.act.ngem.2sgm_Neg.nn",
        "310842": "SC.t.act.ngem.2sgm_Neg.n js",
        "410842": "SC.t.act.ngem.2sgm_Neg.jmi",
        "510842": "SC.t.act.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610842": "SC.t.act.ngem.2sgm_Neg.jwtj",
        "710842": "SC.t.act.ngem.2sgm_Neg.jwt",
        "810842": "SC.t.act.ngem.2sgm_Neg.w/ꜣ",
        "910842": "SC.t.act.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10843": "SC.t.act.ngem.2sgf",
        "110843": "SC.t.act.ngem.2sgf_Neg.n",
        "210843": "SC.t.act.ngem.2sgf_Neg.nn",
        "310843": "SC.t.act.ngem.2sgf_Neg.n js",
        "410843": "SC.t.act.ngem.2sgf_Neg.jmi",
        "510843": "SC.t.act.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610843": "SC.t.act.ngem.2sgf_Neg.jwtj",
        "710843": "SC.t.act.ngem.2sgf_Neg.jwt",
        "810843": "SC.t.act.ngem.2sgf_Neg.w/ꜣ",
        "910843": "SC.t.act.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10844": "SC.t.act.ngem.3sgm",
        "110844": "SC.t.act.ngem.3sgm_Neg.n",
        "210844": "SC.t.act.ngem.3sgm_Neg.nn",
        "310844": "SC.t.act.ngem.3sgm_Neg.n js",
        "410844": "SC.t.act.ngem.3sgm_Neg.jmi",
        "510844": "SC.t.act.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610844": "SC.t.act.ngem.3sgm_Neg.jwtj",
        "710844": "SC.t.act.ngem.3sgm_Neg.jwt",
        "810844": "SC.t.act.ngem.3sgm_Neg.w/ꜣ",
        "910844": "SC.t.act.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10845": "SC.t.act.ngem.3sgf",
        "110845": "SC.t.act.ngem.3sgf_Neg.n",
        "210845": "SC.t.act.ngem.3sgf_Neg.nn",
        "310845": "SC.t.act.ngem.3sgf_Neg.n js",
        "410845": "SC.t.act.ngem.3sgf_Neg.jmi",
        "510845": "SC.t.act.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610845": "SC.t.act.ngem.3sgf_Neg.jwtj",
        "710845": "SC.t.act.ngem.3sgf_Neg.jwt",
        "810845": "SC.t.act.ngem.3sgf_Neg.w/ꜣ",
        "910845": "SC.t.act.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10846": "SC.t.act.ngem.3sg",
        "110846": "SC.t.act.ngem.3sg_Neg.n",
        "210846": "SC.t.act.ngem.3sg_Neg.nn",
        "310846": "SC.t.act.ngem.3sg_Neg.n js",
        "410846": "SC.t.act.ngem.3sg_Neg.jmi",
        "510846": "SC.t.act.ngem.3sg_Neg.n-zp/jwt-zp",
        "610846": "SC.t.act.ngem.3sg_Neg.jwtj",
        "710846": "SC.t.act.ngem.3sg_Neg.jwt",
        "810846": "SC.t.act.ngem.3sg_Neg.w/ꜣ",
        "910846": "SC.t.act.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10847": "SC.t.act.ngem.1pl",
        "-10847": "SC.t.act.ngem.1du",
        "110847": "SC.t.act.ngem.1pl_Neg.n",
        "-110847": "SC.t.act.ngem.1du_Neg.n",
        "210847": "SC.t.act.ngem.1pl_Neg.nn",
        "-210847": "SC.t.act.ngem.1du_Neg.nn",
        "310847": "SC.t.act.ngem.1pl_Neg.n js",
        "-310847": "SC.t.act.ngem.1du_Neg.n js",
        "410847": "SC.t.act.ngem.1pl_Neg.jmi",
        "-410847": "SC.t.act.ngem.1du_Neg.jmi",
        "510847": "SC.t.act.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510847": "SC.t.act.ngem.1du_Neg.n-zp/jwt-zp",
        "610847": "SC.t.act.ngem.1pl_Neg.jwtj",
        "-610847": "SC.t.act.ngem.1du_Neg.jwtj",
        "710847": "SC.t.act.ngem.1pl_Neg.jwt",
        "-710847": "SC.t.act.ngem.1du_Neg.jwt",
        "810847": "SC.t.act.ngem.1pl_Neg.w/ꜣ",
        "-810847": "SC.t.act.ngem.1du_Neg.w/ꜣ",
        "910847": "SC.t.act.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910847": "SC.t.act.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10848": "SC.t.act.ngem.2pl",
        "-10848": "SC.t.act.ngem.2du",
        "110848": "SC.t.act.ngem.2pl_Neg.n",
        "-110848": "SC.t.act.ngem.2du_Neg.n",
        "210848": "SC.t.act.ngem.2pl_Neg.nn",
        "-210848": "SC.t.act.ngem.2du_Neg.nn",
        "310848": "SC.t.act.ngem.2pl_Neg.n js",
        "-310848": "SC.t.act.ngem.2du_Neg.n js",
        "410848": "SC.t.act.ngem.2pl_Neg.jmi",
        "-410848": "SC.t.act.ngem.2du_Neg.jmi",
        "510848": "SC.t.act.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510848": "SC.t.act.ngem.2du_Neg.n-zp/jwt-zp",
        "610848": "SC.t.act.ngem.2pl_Neg.jwtj",
        "-610848": "SC.t.act.ngem.2du_Neg.jwtj",
        "710848": "SC.t.act.ngem.2pl_Neg.jwt",
        "-710848": "SC.t.act.ngem.2du_Neg.jwt",
        "810848": "SC.t.act.ngem.2pl_Neg.w/ꜣ",
        "-810848": "SC.t.act.ngem.2du_Neg.w/ꜣ",
        "910848": "SC.t.act.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910848": "SC.t.act.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10849": "SC.t.act.ngem.3pl",
        "-10849": "SC.t.act.ngem.3du",
        "110849": "SC.t.act.ngem.3pl_Neg.n",
        "-110849": "SC.t.act.ngem.3du_Neg.n",
        "210849": "SC.t.act.ngem.3pl_Neg.nn",
        "-210849": "SC.t.act.ngem.3du_Neg.nn",
        "310849": "SC.t.act.ngem.3pl_Neg.n js",
        "-310849": "SC.t.act.ngem.3du_Neg.n js",
        "410849": "SC.t.act.ngem.3pl_Neg.jmi",
        "-410849": "SC.t.act.ngem.3du_Neg.jmi",
        "510849": "SC.t.act.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510849": "SC.t.act.ngem.3du_Neg.n-zp/jwt-zp",
        "610849": "SC.t.act.ngem.3pl_Neg.jwtj",
        "-610849": "SC.t.act.ngem.3du_Neg.jwtj",
        "710849": "SC.t.act.ngem.3pl_Neg.jwt",
        "-710849": "SC.t.act.ngem.3du_Neg.jwt",
        "810849": "SC.t.act.ngem.3pl_Neg.w/ꜣ",
        "-810849": "SC.t.act.ngem.3du_Neg.w/ꜣ",
        "910849": "SC.t.act.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910849": "SC.t.act.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10850": "SC.t.act.gem.nom.subj",
        "110850": "SC.t.act.gem.nom.subj_Neg.n",
        "210850": "SC.t.act.gem.nom.subj_Neg.nn",
        "310850": "SC.t.act.gem.nom.subj_Neg.n js",
        "410850": "SC.t.act.gem.nom.subj_Neg.jmi",
        "510850": "SC.t.act.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610850": "SC.t.act.gem.nom.subj_Neg.jwtj",
        "710850": "SC.t.act.gem.nom.subj_Neg.jwt",
        "810850": "SC.t.act.gem.nom.subj_Neg.w/ꜣ",
        "910850": "SC.t.act.gem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10851": "SC.t.act.gem.1sg",
        "110851": "SC.t.act.gem.1sg_Neg.n",
        "210851": "SC.t.act.gem.1sg_Neg.nn",
        "310851": "SC.t.act.gem.1sg_Neg.n js",
        "410851": "SC.t.act.gem.1sg_Neg.jmi",
        "510851": "SC.t.act.gem.1sg_Neg.n-zp/jwt-zp",
        "610851": "SC.t.act.gem.1sg_Neg.jwtj",
        "710851": "SC.t.act.gem.1sg_Neg.jwt",
        "810851": "SC.t.act.gem.1sg_Neg.w/ꜣ",
        "910851": "SC.t.act.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10852": "SC.t.act.gem.2sgm",
        "110852": "SC.t.act.gem.2sgm_Neg.n",
        "210852": "SC.t.act.gem.2sgm_Neg.nn",
        "310852": "SC.t.act.gem.2sgm_Neg.n js",
        "410852": "SC.t.act.gem.2sgm_Neg.jmi",
        "510852": "SC.t.act.gem.2sgm_Neg.n-zp/jwt-zp",
        "610852": "SC.t.act.gem.2sgm_Neg.jwtj",
        "710852": "SC.t.act.gem.2sgm_Neg.jwt",
        "810852": "SC.t.act.gem.2sgm_Neg.w/ꜣ",
        "910852": "SC.t.act.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10853": "SC.t.act.gem.2sgf",
        "110853": "SC.t.act.gem.2sgf_Neg.n",
        "210853": "SC.t.act.gem.2sgf_Neg.nn",
        "310853": "SC.t.act.gem.2sgf_Neg.n js",
        "410853": "SC.t.act.gem.2sgf_Neg.jmi",
        "510853": "SC.t.act.gem.2sgf_Neg.n-zp/jwt-zp",
        "610853": "SC.t.act.gem.2sgf_Neg.jwtj",
        "710853": "SC.t.act.gem.2sgf_Neg.jwt",
        "810853": "SC.t.act.gem.2sgf_Neg.w/ꜣ",
        "910853": "SC.t.act.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10854": "SC.t.act.gem.3sgm",
        "110854": "SC.t.act.gem.3sgm_Neg.n",
        "210854": "SC.t.act.gem.3sgm_Neg.nn",
        "310854": "SC.t.act.gem.3sgm_Neg.n js",
        "410854": "SC.t.act.gem.3sgm_Neg.jmi",
        "510854": "SC.t.act.gem.3sgm_Neg.n-zp/jwt-zp",
        "610854": "SC.t.act.gem.3sgm_Neg.jwtj",
        "710854": "SC.t.act.gem.3sgm_Neg.jwt",
        "810854": "SC.t.act.gem.3sgm_Neg.w/ꜣ",
        "910854": "SC.t.act.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10855": "SC.t.act.gem.3sgf",
        "110855": "SC.t.act.gem.3sgf_Neg.n",
        "210855": "SC.t.act.gem.3sgf_Neg.nn",
        "310855": "SC.t.act.gem.3sgf_Neg.n js",
        "410855": "SC.t.act.gem.3sgf_Neg.jmi",
        "510855": "SC.t.act.gem.3sgf_Neg.n-zp/jwt-zp",
        "610855": "SC.t.act.gem.3sgf_Neg.jwtj",
        "710855": "SC.t.act.gem.3sgf_Neg.jwt",
        "810855": "SC.t.act.gem.3sgf_Neg.w/ꜣ",
        "910855": "SC.t.act.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10856": "SC.t.act.gem.3sg",
        "110856": "SC.t.act.gem.3sg_Neg.n",
        "210856": "SC.t.act.gem.3sg_Neg.nn",
        "310856": "SC.t.act.gem.3sg_Neg.n js",
        "410856": "SC.t.act.gem.3sg_Neg.jmi",
        "510856": "SC.t.act.gem.3sg_Neg.n-zp/jwt-zp",
        "610856": "SC.t.act.gem.3sg_Neg.jwtj",
        "710856": "SC.t.act.gem.3sg_Neg.jwt",
        "810856": "SC.t.act.gem.3sg_Neg.w/ꜣ",
        "910856": "SC.t.act.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10857": "SC.t.act.gem.1pl",
        "-10857": "SC.t.act.gem.1du",
        "110857": "SC.t.act.gem.1pl_Neg.n",
        "-110857": "SC.t.act.gem.1du_Neg.n",
        "210857": "SC.t.act.gem.1pl_Neg.nn",
        "-210857": "SC.t.act.gem.1du_Neg.nn",
        "310857": "SC.t.act.gem.1pl_Neg.n js",
        "-310857": "SC.t.act.gem.1du_Neg.n js",
        "410857": "SC.t.act.gem.1pl_Neg.jmi",
        "-410857": "SC.t.act.gem.1du_Neg.jmi",
        "510857": "SC.t.act.gem.1pl_Neg.n-zp/jwt-zp",
        "-510857": "SC.t.act.gem.1du_Neg.n-zp/jwt-zp",
        "610857": "SC.t.act.gem.1pl_Neg.jwtj",
        "-610857": "SC.t.act.gem.1du_Neg.jwtj",
        "710857": "SC.t.act.gem.1pl_Neg.jwt",
        "-710857": "SC.t.act.gem.1du_Neg.jwt",
        "810857": "SC.t.act.gem.1pl_Neg.w/ꜣ",
        "-810857": "SC.t.act.gem.1du_Neg.w/ꜣ",
        "910857": "SC.t.act.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910857": "SC.t.act.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10858": "SC.t.act.gem.2pl",
        "-10858": "SC.t.act.gem.2du",
        "110858": "SC.t.act.gem.2pl_Neg.n",
        "-110858": "SC.t.act.gem.2du_Neg.n",
        "210858": "SC.t.act.gem.2pl_Neg.nn",
        "-210858": "SC.t.act.gem.2du_Neg.nn",
        "310858": "SC.t.act.gem.2pl_Neg.n js",
        "-310858": "SC.t.act.gem.2du_Neg.n js",
        "410858": "SC.t.act.gem.2pl_Neg.jmi",
        "-410858": "SC.t.act.gem.2du_Neg.jmi",
        "510858": "SC.t.act.gem.2pl_Neg.n-zp/jwt-zp",
        "-510858": "SC.t.act.gem.2du_Neg.n-zp/jwt-zp",
        "610858": "SC.t.act.gem.2pl_Neg.jwtj",
        "-610858": "SC.t.act.gem.2du_Neg.jwtj",
        "710858": "SC.t.act.gem.2pl_Neg.jwt",
        "-710858": "SC.t.act.gem.2du_Neg.jwt",
        "810858": "SC.t.act.gem.2pl_Neg.w/ꜣ",
        "-810858": "SC.t.act.gem.2du_Neg.w/ꜣ",
        "910858": "SC.t.act.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910858": "SC.t.act.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10859": "SC.t.act.gem.3pl",
        "-10859": "SC.t.act.gem.3du",
        "110859": "SC.t.act.gem.3pl_Neg.n",
        "-110859": "SC.t.act.gem.3du_Neg.n",
        "210859": "SC.t.act.gem.3pl_Neg.nn",
        "-210859": "SC.t.act.gem.3du_Neg.nn",
        "310859": "SC.t.act.gem.3pl_Neg.n js",
        "-310859": "SC.t.act.gem.3du_Neg.n js",
        "410859": "SC.t.act.gem.3pl_Neg.jmi",
        "-410859": "SC.t.act.gem.3du_Neg.jmi",
        "510859": "SC.t.act.gem.3pl_Neg.n-zp/jwt-zp",
        "-510859": "SC.t.act.gem.3du_Neg.n-zp/jwt-zp",
        "610859": "SC.t.act.gem.3pl_Neg.jwtj",
        "-610859": "SC.t.act.gem.3du_Neg.jwtj",
        "710859": "SC.t.act.gem.3pl_Neg.jwt",
        "-710859": "SC.t.act.gem.3du_Neg.jwt",
        "810859": "SC.t.act.gem.3pl_Neg.w/ꜣ",
        "-810859": "SC.t.act.gem.3du_Neg.w/ꜣ",
        "910859": "SC.t.act.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910859": "SC.t.act.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10860": "SC.t.pass.ngem.nom.subj",
        "110860": "SC.t.pass.ngem.nom.subj_Neg.n",
        "210860": "SC.t.pass.ngem.nom.subj_Neg.nn",
        "310860": "SC.t.pass.ngem.nom.subj_Neg.n js",
        "410860": "SC.t.pass.ngem.nom.subj_Neg.jmi",
        "510860": "SC.t.pass.ngem.nom.subj_Neg.n-zp/jwt-zp",
        "610860": "SC.t.pass.ngem.nom.subj_Neg.jwtj",
        "710860": "SC.t.pass.ngem.nom.subj_Neg.jwt",
        "810860": "SC.t.pass.ngem.nom.subj_Neg.w/ꜣ",
        "910860": "SC.t.pass.ngem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10861": "SC.t.pass.ngem.1sg",
        "110861": "SC.t.pass.ngem.1sg_Neg.n",
        "210861": "SC.t.pass.ngem.1sg_Neg.nn",
        "310861": "SC.t.pass.ngem.1sg_Neg.n js",
        "410861": "SC.t.pass.ngem.1sg_Neg.jmi",
        "510861": "SC.t.pass.ngem.1sg_Neg.n-zp/jwt-zp",
        "610861": "SC.t.pass.ngem.1sg_Neg.jwtj",
        "710861": "SC.t.pass.ngem.1sg_Neg.jwt",
        "810861": "SC.t.pass.ngem.1sg_Neg.w/ꜣ",
        "910861": "SC.t.pass.ngem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10862": "SC.t.pass.ngem.2sgm",
        "110862": "SC.t.pass.ngem.2sgm_Neg.n",
        "210862": "SC.t.pass.ngem.2sgm_Neg.nn",
        "310862": "SC.t.pass.ngem.2sgm_Neg.n js",
        "410862": "SC.t.pass.ngem.2sgm_Neg.jmi",
        "510862": "SC.t.pass.ngem.2sgm_Neg.n-zp/jwt-zp",
        "610862": "SC.t.pass.ngem.2sgm_Neg.jwtj",
        "710862": "SC.t.pass.ngem.2sgm_Neg.jwt",
        "810862": "SC.t.pass.ngem.2sgm_Neg.w/ꜣ",
        "910862": "SC.t.pass.ngem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10863": "SC.t.pass.ngem.2sgf",
        "110863": "SC.t.pass.ngem.2sgf_Neg.n",
        "210863": "SC.t.pass.ngem.2sgf_Neg.nn",
        "310863": "SC.t.pass.ngem.2sgf_Neg.n js",
        "410863": "SC.t.pass.ngem.2sgf_Neg.jmi",
        "510863": "SC.t.pass.ngem.2sgf_Neg.n-zp/jwt-zp",
        "610863": "SC.t.pass.ngem.2sgf_Neg.jwtj",
        "710863": "SC.t.pass.ngem.2sgf_Neg.jwt",
        "810863": "SC.t.pass.ngem.2sgf_Neg.w/ꜣ",
        "910863": "SC.t.pass.ngem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10864": "SC.t.pass.ngem.3sgm",
        "110864": "SC.t.pass.ngem.3sgm_Neg.n",
        "210864": "SC.t.pass.ngem.3sgm_Neg.nn",
        "310864": "SC.t.pass.ngem.3sgm_Neg.n js",
        "410864": "SC.t.pass.ngem.3sgm_Neg.jmi",
        "510864": "SC.t.pass.ngem.3sgm_Neg.n-zp/jwt-zp",
        "610864": "SC.t.pass.ngem.3sgm_Neg.jwtj",
        "710864": "SC.t.pass.ngem.3sgm_Neg.jwt",
        "810864": "SC.t.pass.ngem.3sgm_Neg.w/ꜣ",
        "910864": "SC.t.pass.ngem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10865": "SC.t.pass.ngem.3sgf",
        "110865": "SC.t.pass.ngem.3sgf_Neg.n",
        "210865": "SC.t.pass.ngem.3sgf_Neg.nn",
        "310865": "SC.t.pass.ngem.3sgf_Neg.n js",
        "410865": "SC.t.pass.ngem.3sgf_Neg.jmi",
        "510865": "SC.t.pass.ngem.3sgf_Neg.n-zp/jwt-zp",
        "610865": "SC.t.pass.ngem.3sgf_Neg.jwtj",
        "710865": "SC.t.pass.ngem.3sgf_Neg.jwt",
        "810865": "SC.t.pass.ngem.3sgf_Neg.w/ꜣ",
        "910865": "SC.t.pass.ngem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10866": "SC.t.pass.ngem.3sg",
        "110866": "SC.t.pass.ngem.3sg_Neg.n",
        "210866": "SC.t.pass.ngem.3sg_Neg.nn",
        "310866": "SC.t.pass.ngem.3sg_Neg.n js",
        "410866": "SC.t.pass.ngem.3sg_Neg.jmi",
        "510866": "SC.t.pass.ngem.3sg_Neg.n-zp/jwt-zp",
        "610866": "SC.t.pass.ngem.3sg_Neg.jwtj",
        "710866": "SC.t.pass.ngem.3sg_Neg.jwt",
        "810866": "SC.t.pass.ngem.3sg_Neg.w/ꜣ",
        "910866": "SC.t.pass.ngem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10867": "SC.t.pass.ngem.1pl",
        "-10867": "SC.t.pass.ngem.1du",
        "110867": "SC.t.pass.ngem.1pl_Neg.n",
        "-110867": "SC.t.pass.ngem.1du_Neg.n",
        "210867": "SC.t.pass.ngem.1pl_Neg.nn",
        "-210867": "SC.t.pass.ngem.1du_Neg.nn",
        "310867": "SC.t.pass.ngem.1pl_Neg.n js",
        "-310867": "SC.t.pass.ngem.1du_Neg.n js",
        "410867": "SC.t.pass.ngem.1pl_Neg.jmi",
        "-410867": "SC.t.pass.ngem.1du_Neg.jmi",
        "510867": "SC.t.pass.ngem.1pl_Neg.n-zp/jwt-zp",
        "-510867": "SC.t.pass.ngem.1du_Neg.n-zp/jwt-zp",
        "610867": "SC.t.pass.ngem.1pl_Neg.jwtj",
        "-610867": "SC.t.pass.ngem.1du_Neg.jwtj",
        "710867": "SC.t.pass.ngem.1pl_Neg.jwt",
        "-710867": "SC.t.pass.ngem.1du_Neg.jwt",
        "810867": "SC.t.pass.ngem.1pl_Neg.w/ꜣ",
        "-810867": "SC.t.pass.ngem.1du_Neg.w/ꜣ",
        "910867": "SC.t.pass.ngem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910867": "SC.t.pass.ngem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10868": "SC.t.pass.ngem.2pl",
        "-10868": "SC.t.pass.ngem.2du",
        "110868": "SC.t.pass.ngem.2pl_Neg.n",
        "-110868": "SC.t.pass.ngem.2du_Neg.n",
        "210868": "SC.t.pass.ngem.2pl_Neg.nn",
        "-210868": "SC.t.pass.ngem.2du_Neg.nn",
        "310868": "SC.t.pass.ngem.2pl_Neg.n js",
        "-310868": "SC.t.pass.ngem.2du_Neg.n js",
        "410868": "SC.t.pass.ngem.2pl_Neg.jmi",
        "-410868": "SC.t.pass.ngem.2du_Neg.jmi",
        "510868": "SC.t.pass.ngem.2pl_Neg.n-zp/jwt-zp",
        "-510868": "SC.t.pass.ngem.2du_Neg.n-zp/jwt-zp",
        "610868": "SC.t.pass.ngem.2pl_Neg.jwtj",
        "-610868": "SC.t.pass.ngem.2du_Neg.jwtj",
        "710868": "SC.t.pass.ngem.2pl_Neg.jwt",
        "-710868": "SC.t.pass.ngem.2du_Neg.jwt",
        "810868": "SC.t.pass.ngem.2pl_Neg.w/ꜣ",
        "-810868": "SC.t.pass.ngem.2du_Neg.w/ꜣ",
        "910868": "SC.t.pass.ngem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910868": "SC.t.pass.ngem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10869": "SC.t.pass.ngem.3pl",
        "-10869": "SC.t.pass.ngem.3du",
        "110869": "SC.t.pass.ngem.3pl_Neg.n",
        "-110869": "SC.t.pass.ngem.3du_Neg.n",
        "210869": "SC.t.pass.ngem.3pl_Neg.nn",
        "-210869": "SC.t.pass.ngem.3du_Neg.nn",
        "310869": "SC.t.pass.ngem.3pl_Neg.n js",
        "-310869": "SC.t.pass.ngem.3du_Neg.n js",
        "410869": "SC.t.pass.ngem.3pl_Neg.jmi",
        "-410869": "SC.t.pass.ngem.3du_Neg.jmi",
        "510869": "SC.t.pass.ngem.3pl_Neg.n-zp/jwt-zp",
        "-510869": "SC.t.pass.ngem.3du_Neg.n-zp/jwt-zp",
        "610869": "SC.t.pass.ngem.3pl_Neg.jwtj",
        "-610869": "SC.t.pass.ngem.3du_Neg.jwtj",
        "710869": "SC.t.pass.ngem.3pl_Neg.jwt",
        "-710869": "SC.t.pass.ngem.3du_Neg.jwt",
        "810869": "SC.t.pass.ngem.3pl_Neg.w/ꜣ",
        "-810869": "SC.t.pass.ngem.3du_Neg.w/ꜣ",
        "910869": "SC.t.pass.ngem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910869": "SC.t.pass.ngem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10870": "SC.t.pass.gem.nom.subj",
        "110870": "SC.t.pass.gem.nom.subj_Neg.n",
        "210870": "SC.t.pass.gem.nom.subj_Neg.nn",
        "310870": "SC.t.pass.gem.nom.subj_Neg.n js",
        "410870": "SC.t.pass.gem.nom.subj_Neg.jmi",
        "510870": "SC.t.pass.gem.nom.subj_Neg.n-zp/jwt-zp",
        "610870": "SC.t.pass.gem.nom.subj_Neg.jwtj",
        "710870": "SC.t.pass.gem.nom.subj_Neg.jwt",
        "810870": "SC.t.pass.gem.nom.subj_Neg.w/ꜣ",
        "910870": "SC.t.pass.gem.nom.subj_Neg.nfr/nfr-n/nfr-pw",
        "10871": "SC.t.pass.gem.1sg",
        "110871": "SC.t.pass.gem.1sg_Neg.n",
        "210871": "SC.t.pass.gem.1sg_Neg.nn",
        "310871": "SC.t.pass.gem.1sg_Neg.n js",
        "410871": "SC.t.pass.gem.1sg_Neg.jmi",
        "510871": "SC.t.pass.gem.1sg_Neg.n-zp/jwt-zp",
        "610871": "SC.t.pass.gem.1sg_Neg.jwtj",
        "710871": "SC.t.pass.gem.1sg_Neg.jwt",
        "810871": "SC.t.pass.gem.1sg_Neg.w/ꜣ",
        "910871": "SC.t.pass.gem.1sg_Neg.nfr/nfr-n/nfr-pw",
        "10872": "SC.t.pass.gem.2sgm",
        "110872": "SC.t.pass.gem.2sgm_Neg.n",
        "210872": "SC.t.pass.gem.2sgm_Neg.nn",
        "310872": "SC.t.pass.gem.2sgm_Neg.n js",
        "410872": "SC.t.pass.gem.2sgm_Neg.jmi",
        "510872": "SC.t.pass.gem.2sgm_Neg.n-zp/jwt-zp",
        "610872": "SC.t.pass.gem.2sgm_Neg.jwtj",
        "710872": "SC.t.pass.gem.2sgm_Neg.jwt",
        "810872": "SC.t.pass.gem.2sgm_Neg.w/ꜣ",
        "910872": "SC.t.pass.gem.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "10873": "SC.t.pass.gem.2sgf",
        "110873": "SC.t.pass.gem.2sgf_Neg.n",
        "210873": "SC.t.pass.gem.2sgf_Neg.nn",
        "310873": "SC.t.pass.gem.2sgf_Neg.n js",
        "410873": "SC.t.pass.gem.2sgf_Neg.jmi",
        "510873": "SC.t.pass.gem.2sgf_Neg.n-zp/jwt-zp",
        "610873": "SC.t.pass.gem.2sgf_Neg.jwtj",
        "710873": "SC.t.pass.gem.2sgf_Neg.jwt",
        "810873": "SC.t.pass.gem.2sgf_Neg.w/ꜣ",
        "910873": "SC.t.pass.gem.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "10874": "SC.t.pass.gem.3sgm",
        "110874": "SC.t.pass.gem.3sgm_Neg.n",
        "210874": "SC.t.pass.gem.3sgm_Neg.nn",
        "310874": "SC.t.pass.gem.3sgm_Neg.n js",
        "410874": "SC.t.pass.gem.3sgm_Neg.jmi",
        "510874": "SC.t.pass.gem.3sgm_Neg.n-zp/jwt-zp",
        "610874": "SC.t.pass.gem.3sgm_Neg.jwtj",
        "710874": "SC.t.pass.gem.3sgm_Neg.jwt",
        "810874": "SC.t.pass.gem.3sgm_Neg.w/ꜣ",
        "910874": "SC.t.pass.gem.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "10875": "SC.t.pass.gem.3sgf",
        "110875": "SC.t.pass.gem.3sgf_Neg.n",
        "210875": "SC.t.pass.gem.3sgf_Neg.nn",
        "310875": "SC.t.pass.gem.3sgf_Neg.n js",
        "410875": "SC.t.pass.gem.3sgf_Neg.jmi",
        "510875": "SC.t.pass.gem.3sgf_Neg.n-zp/jwt-zp",
        "610875": "SC.t.pass.gem.3sgf_Neg.jwtj",
        "710875": "SC.t.pass.gem.3sgf_Neg.jwt",
        "810875": "SC.t.pass.gem.3sgf_Neg.w/ꜣ",
        "910875": "SC.t.pass.gem.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "10876": "SC.t.pass.gem.3sg",
        "110876": "SC.t.pass.gem.3sg_Neg.n",
        "210876": "SC.t.pass.gem.3sg_Neg.nn",
        "310876": "SC.t.pass.gem.3sg_Neg.n js",
        "410876": "SC.t.pass.gem.3sg_Neg.jmi",
        "510876": "SC.t.pass.gem.3sg_Neg.n-zp/jwt-zp",
        "610876": "SC.t.pass.gem.3sg_Neg.jwtj",
        "710876": "SC.t.pass.gem.3sg_Neg.jwt",
        "810876": "SC.t.pass.gem.3sg_Neg.w/ꜣ",
        "910876": "SC.t.pass.gem.3sg_Neg.nfr/nfr-n/nfr-pw",
        "10877": "SC.t.pass.gem.1pl",
        "-10877": "SC.t.pass.gem.1du",
        "110877": "SC.t.pass.gem.1pl_Neg.n",
        "-110877": "SC.t.pass.gem.1du_Neg.n",
        "210877": "SC.t.pass.gem.1pl_Neg.nn",
        "-210877": "SC.t.pass.gem.1du_Neg.nn",
        "310877": "SC.t.pass.gem.1pl_Neg.n js",
        "-310877": "SC.t.pass.gem.1du_Neg.n js",
        "410877": "SC.t.pass.gem.1pl_Neg.jmi",
        "-410877": "SC.t.pass.gem.1du_Neg.jmi",
        "510877": "SC.t.pass.gem.1pl_Neg.n-zp/jwt-zp",
        "-510877": "SC.t.pass.gem.1du_Neg.n-zp/jwt-zp",
        "610877": "SC.t.pass.gem.1pl_Neg.jwtj",
        "-610877": "SC.t.pass.gem.1du_Neg.jwtj",
        "710877": "SC.t.pass.gem.1pl_Neg.jwt",
        "-710877": "SC.t.pass.gem.1du_Neg.jwt",
        "810877": "SC.t.pass.gem.1pl_Neg.w/ꜣ",
        "-810877": "SC.t.pass.gem.1du_Neg.w/ꜣ",
        "910877": "SC.t.pass.gem.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-910877": "SC.t.pass.gem.1du_Neg.nfr/nfr-n/nfr-pw",
        "10878": "SC.t.pass.gem.2pl",
        "-10878": "SC.t.pass.gem.2du",
        "110878": "SC.t.pass.gem.2pl_Neg.n",
        "-110878": "SC.t.pass.gem.2du_Neg.n",
        "210878": "SC.t.pass.gem.2pl_Neg.nn",
        "-210878": "SC.t.pass.gem.2du_Neg.nn",
        "310878": "SC.t.pass.gem.2pl_Neg.n js",
        "-310878": "SC.t.pass.gem.2du_Neg.n js",
        "410878": "SC.t.pass.gem.2pl_Neg.jmi",
        "-410878": "SC.t.pass.gem.2du_Neg.jmi",
        "510878": "SC.t.pass.gem.2pl_Neg.n-zp/jwt-zp",
        "-510878": "SC.t.pass.gem.2du_Neg.n-zp/jwt-zp",
        "610878": "SC.t.pass.gem.2pl_Neg.jwtj",
        "-610878": "SC.t.pass.gem.2du_Neg.jwtj",
        "710878": "SC.t.pass.gem.2pl_Neg.jwt",
        "-710878": "SC.t.pass.gem.2du_Neg.jwt",
        "810878": "SC.t.pass.gem.2pl_Neg.w/ꜣ",
        "-810878": "SC.t.pass.gem.2du_Neg.w/ꜣ",
        "910878": "SC.t.pass.gem.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-910878": "SC.t.pass.gem.2du_Neg.nfr/nfr-n/nfr-pw",
        "10879": "SC.t.pass.gem.3pl",
        "-10879": "SC.t.pass.gem.3du",
        "110879": "SC.t.pass.gem.3pl_Neg.n",
        "-110879": "SC.t.pass.gem.3du_Neg.n",
        "210879": "SC.t.pass.gem.3pl_Neg.nn",
        "-210879": "SC.t.pass.gem.3du_Neg.nn",
        "310879": "SC.t.pass.gem.3pl_Neg.n js",
        "-310879": "SC.t.pass.gem.3du_Neg.n js",
        "410879": "SC.t.pass.gem.3pl_Neg.jmi",
        "-410879": "SC.t.pass.gem.3du_Neg.jmi",
        "510879": "SC.t.pass.gem.3pl_Neg.n-zp/jwt-zp",
        "-510879": "SC.t.pass.gem.3du_Neg.n-zp/jwt-zp",
        "610879": "SC.t.pass.gem.3pl_Neg.jwtj",
        "-610879": "SC.t.pass.gem.3du_Neg.jwtj",
        "710879": "SC.t.pass.gem.3pl_Neg.jwt",
        "-710879": "SC.t.pass.gem.3du_Neg.jwt",
        "810879": "SC.t.pass.gem.3pl_Neg.w/ꜣ",
        "-810879": "SC.t.pass.gem.3du_Neg.w/ꜣ",
        "910879": "SC.t.pass.gem.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-910879": "SC.t.pass.gem.3du_Neg.nfr/nfr-n/nfr-pw",
        "10900": "SC.act.ngem.impers",
        "410900": "SC.act.ngem.impers_Neg.jmi",
        "110900": "SC.act.ngem.impers_Neg.n",
        "910900": "SC.act.ngem.impers_Neg.nfr/nfr-n/nfr-pw",
        "210900": "SC.act.ngem.impers_Neg.nn",
        "10910": "SC.pass.ngem.impers",
        "110910": "SC.pass.ngem.impers_Neg.n",
        "10920": "SC.act.gem.impers",
        "10921": "",
        "10922": "",
        "10923": "",
        "10924": "",
        "10925": "",
        "10926": "",
        "10927": "",
        "10928": "",
        "10929": "",
        "10930": "SC.pass.gem.impers",
        "110930": "SC.pass.gem.impers_Neg.n",
        "10940": "SC.w.pass.impers",
        "110940": "SC.w.pass.impers_Neg.n",
        "10950": "SC.tw.pass.ngem.impers",
        "110950": "SC.tw.pass.ngem.impers_Neg.n",
        "210950": "SC.tw.pass.ngem.impers_Neg.nn",
        "10960": "SC.tw.pass.gem.impers",
        "110960": "SC.tw.pass.gem.impers_Neg.n",
        "10970": "SC.act.spec.impers",
        "10980": "SC.pass.spec.impers",
        "10990": "SC.t.act.ngem.impers",
        "110990": "SC.t.act.ngem.impers_Neg.n",
        "210990": "SC.t.act.ngem.impers_Neg.nn",
        "11000": "SC.prefx.",
        "11020": "SC.act.prefx.nom.subj",
        "11021": "SC.act.prefx.1sg",
        "11022": "SC.act.prefx.2sgm",
        "11023": "SC.act.prefx.2sgf",
        "11024": "SC.act.prefx.3sgm",
        "111024": "SC.act.prefx.3sgm_Neg.n",
        "11025": "SC.act.prefx.3sgf",
        "11026": "SC.act.prefx.3sg",
        "11027": "SC.act.prefx.1pl",
        "-11027": "SC.act.prefx.1du",
        "11028": "SC.act.prefx.2pl",
        "-11028": "SC.act.prefx.2du",
        "11029": "SC.act.prefx.3pl",
        "-11029": "SC.act.prefx.3du",
        "11040": "SC.pass.prefx.nom.subj",
        "11041": "SC.pass.prefx.1sg",
        "11042": "SC.pass.prefx.2sgm",
        "11043": "SC.pass.prefx.2sgf",
        "11044": "SC.pass.prefx.3sgm",
        "11045": "SC.pass.prefx.3sgf",
        "11046": "SC.pass.prefx.3sg",
        "11047": "SC.pass.prefx.1pl",
        "-11047": "SC.pass.prefx.1du",
        "11048": "SC.pass.prefx.2pl",
        "-11048": "SC.pass.prefx.2du",
        "11049": "SC.pass.prefx.3pl",
        "-11049": "SC.pass.prefx.3du",
        "11060": "",
        "11061": "",
        "11062": "",
        "11063": "",
        "11064": "",
        "11065": "",
        "11066": "",
        "11067": "",
        "11068": "",
        "11069": "",
        "11100": "SC.act.gem.prefx",
        "11104": "SC.act.gem.prefx.3sgm",
        "11141": "SC.act.spec.prefx.1sg",
        "11142": "SC.act.spec.prefx.2sgm",
        "11148": "SC.act.spec.prefx.2pl",
        "11320": "SC.tw.pass.prefx.nom.subj",
        "11321": "SC.tw.pass.prefx.1sg",
        "11322": "SC.tw.pass.prefx.2sgm",
        "11323": "SC.tw.pass.prefx.2sgf",
        "11324": "SC.tw.pass.prefx.3sgm",
        "11325": "SC.tw.pass.prefx.3sgf",
        "11326": "SC.tw.pass.prefx.3sg",
        "11327": "SC.tw.pass.prefx.1pl",
        "-11327": "SC.tw.pass.prefx.1du",
        "11328": "SC.tw.pass.prefx.2pl",
        "-11328": "SC.tw.pass.prefx.2du",
        "11329": "SC.tw.pass.prefx.3pl",
        "-11329": "SC.tw.pass.prefx.3du",
        "11340": "",
        "11341": "",
        "11342": "",
        "11343": "",
        "11344": "",
        "11345": "",
        "11346": "",
        "11347": "",
        "-11347": "",
        "11348": "",
        "-11348": "",
        "11349": "",
        "-11349": "",
        "11380": "SC.n.act.prefx.nom.subj",
        "11381": "SC.n.act.prefx.1sg",
        "11382": "SC.n.act.prefx.2sgm",
        "11383": "SC.n.act.prefx.2sgf",
        "11384": "SC.n.act.prefx.3sgm",
        "11385": "SC.n.act.prefx.3sgf",
        "11386": "SC.n.act.prefx.3sg",
        "11387": "SC.n.act.prefx.1pl",
        "-11387": "SC.n.act.prefx.1du",
        "11388": "SC.n.act.prefx.2pl",
        "-11388": "SC.n.act.prefx.2du",
        "11389": "SC.n.act.prefx.3pl",
        "-11389": "SC.n.act.prefx.3du",
        "11400": "",
        "11401": "",
        "11402": "",
        "11403": "",
        "11404": "",
        "11405": "",
        "11406": "",
        "11407": "",
        "11408": "",
        "11409": "",
        "11840": "SC.t.act.prefx.nom.subj",
        "11841": "SC.t.act.prefx.1sg",
        "11842": "SC.t.act.prefx.2sgm",
        "11843": "SC.t.act.prefx.2sgf",
        "11844": "SC.t.act.prefx.3sgm",
        "11845": "SC.t.act.prefx.3sgf",
        "11846": "SC.t.act.prefx.3sg",
        "11847": "SC.t.act.prefx.1pl",
        "-11847": "SC.t.act.prefx.1du",
        "11848": "SC.t.act.prefx.2pl",
        "-11848": "SC.t.act.prefx.2du",
        "11849": "SC.t.act.prefx.3pl",
        "-11849": "SC.t.act.prefx.3du",
        "11900": "SC.act.ngem.prefx.impers",
        "11950": "SC.tw.pass.ngem.prefx.impers",
        "11970": "SC.act.spec.prefx.impers",
        "12020": "SC.act.ngem.nom.subj_Aux.others",
        "12021": "SC.act.ngem.1sg_Aux.others",
        "12022": "SC.act.ngem.2sgm_Aux.others",
        "12023": "SC.act.ngem.2sgf_Aux.others",
        "12024": "SC.act.ngem.3sgm_Aux.others",
        "12025": "SC.act.ngem.3sgf_Aux.others",
        "12026": "SC.act.ngem.3sg_Aux.others",
        "12027": "SC.act.ngem.1pl_Aux.others",
        "-12027": "SC.act.ngem.1du_Aux.others",
        "12028": "SC.act.ngem.2pl_Aux.others",
        "-12028": "SC.act.ngem.2du_Aux.others",
        "12029": "SC.act.ngem.3pl_Aux.others",
        "-12029": "SC.act.ngem.3du_Aux.others",
        "12040": "SC.pass.ngem.nom.subj_Aux.others",
        "12041": "SC.pass.ngem.1sg_Aux.others",
        "12042": "SC.pass.ngem.2sgm_Aux.others",
        "12043": "SC.pass.ngem.2sgf_Aux.others",
        "12044": "SC.pass.ngem.3sgm_Aux.others",
        "12045": "SC.pass.ngem.3sgf_Aux.others",
        "12046": "SC.pass.ngem.3sg_Aux.others",
        "12047": "SC.pass.ngem.1pl_Aux.others",
        "-12047": "SC.pass.ngem.1du_Aux.others",
        "12048": "SC.pass.ngem.2pl_Aux.others",
        "-12048": "SC.pass.ngem.2du_Aux.others",
        "12049": "SC.pass.ngem.3pl_Aux.others",
        "-12049": "SC.pass.ngem.3du_Aux.others",
        "12100": "SC.act.gem.nom.subj_Aux.others",
        "12101": "SC.act.gem.1sg_Aux.others",
        "12102": "SC.act.gem.2sgm_Aux.others",
        "12103": "SC.act.gem.2sgf_Aux.others",
        "12104": "SC.act.gem.3sgm_Aux.others",
        "12105": "SC.act.gem.3sgf_Aux.others",
        "12106": "SC.act.gem.3sg_Aux.others",
        "12107": "SC.act.gem.1pl_Aux.others",
        "-12107": "SC.act.gem.1du_Aux.others",
        "12108": "SC.act.gem.2pl_Aux.others",
        "-12108": "SC.act.gem.2du_Aux.others",
        "12109": "SC.act.gem.3pl_Aux.others",
        "-12109": "SC.act.gem.3du_Aux.others",
        "12120": "SC.pass.gem(redupl).nom.subj_Aux.others ",
        "12121": "SC.pass.gem(redupl).1sg_Aux.others",
        "12122": "SC.pass.gem(redupl).2sgm_Aux.others",
        "12123": "SC.pass.gem(redupl).2sgf_Aux.others",
        "12124": "SC.pass.gem(redupl).3sgm_Aux.others",
        "12125": "SC.pass.gem(redupl).3sgf_Aux.others",
        "12126": "SC.pass.gem(redupl).3sg_Aux.others",
        "12127": "SC.pass.gem(redupl).1pl_Aux.others",
        "-12127": "SC.pass.gem(redupl).1du_Aux.others",
        "12128": "SC.pass.gem(redupl).2pl_Aux.others",
        "-12128": "SC.pass.gem(redupl).2du_Aux.others",
        "12129": "SC.pass.gem(redupl).3pl_Aux.others",
        "-12129": "SC.pass.gem(redupl).3du_Aux.others",
        "12140": "SC.act.spec.nom.subj_Aux.others",
        "12141": "SC.act.spec.1sg_Aux.others",
        "12142": "SC.act.spec.2sgm_Aux.others",
        "12143": "SC.act.spec.2sgf_Aux.others",
        "12144": "SC.act.spec.3sgm_Aux.others",
        "12145": "SC.act.spec.3sgf_Aux.others",
        "12146": "SC.act.spec.3sg_Aux.others",
        "12147": "SC.act.spec.1pl_Aux.others",
        "-12147": "SC.act.spec.1du_Aux.others",
        "12148": "SC.act.spec.2pl_Aux.others",
        "-12148": "SC.act.spec.2du_Aux.others",
        "12149": "SC.act.spec.3pl_Aux.others",
        "-12149": "SC.act.spec.3du_Aux.others",
        "12160": "SC.pass.spec.nom.subj_Aux.others",
        "12161": "SC.pass.spec.1sg_Aux.others",
        "12162": "SC.pass.spec.2sgm_Aux.others",
        "12163": "SC.pass.spec.2sgf_Aux.others",
        "12164": "SC.pass.spec.3sgm_Aux.others",
        "12165": "SC.pass.spec.3sgf_Aux.others",
        "12166": "SC.pass.spec.3sg_Aux.others",
        "12167": "SC.pass.spec.1pl_Aux.others",
        "-12167": "SC.pass.spec.1du_Aux.others",
        "12168": "SC.pass.spec.2pl_Aux.others",
        "-12168": "SC.pass.spec.2du_Aux.others",
        "12169": "SC.pass.spec.3pl_Aux.others",
        "-12169": "SC.pass.spec.3du_Aux.others",
        "12170": "SC.tw.pass.spec.nom.subj_Aux.others",
        "12171": "SC.tw.pass.spec.1sg_Aux.others",
        "12172": "SC.tw.pass.spec.2sgm_Aux.others",
        "12173": "SC.tw.pass.spec.2sgf_Aux.others",
        "12174": "SC.tw.pass.spec.3sgm_Aux.others",
        "12175": "SC.tw.pass.spec.3sgf_Aux.others",
        "12176": "SC.tw.pass.spec.3sg_Aux.others",
        "12177": "SC.tw.pass.spec.1pl_Aux.others",
        "-12177": "SC.tw.pass.spec.1du_Aux.others",
        "12178": "SC.tw.pass.spec.2pl_Aux.others",
        "-12178": "SC.tw.pass.spec.2du_Aux.others",
        "12179": "SC.tw.pass.spec.3pl_Aux.others",
        "-12179": "SC.tw.pass.spec.3du_Aux.others",
        "12180": "SC.w.act.ngem.nom.subj_Aux.others",
        "12181": "SC.w.act.ngem.1sg_Aux.others",
        "12182": "SC.w.act.ngem.2sgm_Aux.others",
        "12183": "SC.w.act.ngem.2sgf_Aux.others",
        "12184": "SC.w.act.ngem.3sgm_Aux.others",
        "12185": "SC.w.act.ngem.3sgf_Aux.others",
        "12186": "SC.w.act.ngem.3sg_Aux.others",
        "12187": "SC.w.act.ngem.1pl_Aux.others",
        "-12187": "SC.w.act.ngem.1du_Aux.others",
        "12188": "SC.w.act.ngem.2pl_Aux.others",
        "-12188": "SC.w.act.ngem.2du_Aux.others",
        "12189": "SC.w.act.ngem.3pl_Aux.others",
        "-12189": "SC.w.act.ngem.3du_Aux.others",
        "12220": "SC.w.act.gem.nom.subj_Aux.others",
        "12221": "SC.w.act.gem.1sg_Aux.others",
        "12222": "SC.w.act.gem.2sgm_Aux.others",
        "12223": "SC.w.act.gem.2sgf_Aux.others",
        "12224": "SC.w.act.gem.3sgm_Aux.others",
        "12225": "SC.w.act.gem.3sgf_Aux.others",
        "12226": "SC.w.act.gem.3sg_Aux.others",
        "12227": "SC.w.act.gem.1pl_Aux.others",
        "-12227": "SC.w.act.gem.1du_Aux.others",
        "12228": "SC.w.act.gem.2pl_Aux.others",
        "-12228": "SC.w.act.gem.2du_Aux.others",
        "12229": "SC.w.act.gem.3pl_Aux.others",
        "-12229": "SC.w.act.gem.3du_Aux.others",
        "12240": "SC.w.pass.ngem.nom.subj_Aux.others",
        "12241": "SC.w.pass.ngem.1sg_Aux.others",
        "12242": "SC.w.pass.ngem.2sgm_Aux.others",
        "12243": "SC.w.pass.ngem.2sgf_Aux.others",
        "12244": "SC.w.pass.ngem.3sgm_Aux.others",
        "12245": "SC.w.pass.ngem.3sgf_Aux.others",
        "12246": "SC.w.pass.ngem.3sg_Aux.others",
        "12247": "SC.w.pass.ngem.1pl_Aux.others",
        "-12247": "SC.w.pass.ngem.1du_Aux.others",
        "12248": "SC.w.pass.ngem.2pl_Aux.others",
        "-12248": "SC.w.pass.ngem.2du_Aux.others",
        "12249": "SC.w.pass.ngem.3pl_Aux.others",
        "-12249": "SC.w.pass.ngem.3du_Aux.others",
        "12280": "SC.w.tw.pass.ngem.nom.subj_Aux.others",
        "12281": "SC.w.tw.pass.ngem.1sg_Aux.others",
        "12282": "SC.w.tw.pass.ngem.2sgm_Aux.others",
        "12283": "SC.w.tw.pass.ngem.2sgf_Aux.others",
        "12284": "SC.w.tw.pass.ngem.3sgm_Aux.others",
        "12285": "SC.w.tw.pass.ngem.3sgf_Aux.others",
        "12286": "SC.w.tw.pass.ngem.3sg_Aux.others",
        "12287": "SC.w.tw.pass.ngem.1pl_Aux.others",
        "-12287": "SC.w.tw.pass.ngem.1du_Aux.others",
        "12288": "SC.w.tw.pass.ngem.2pl_Aux.others",
        "-12288": "SC.w.tw.pass.ngem.2du_Aux.others",
        "12289": "SC.w.tw.pass.ngem.3pl_Aux.others",
        "-12289": "SC.w.tw.pass.ngem.3du_Aux.others",
        "12320": "SC.tw.pass.ngem.nom.subj_Aux.others",
        "12321": "SC.tw.pass.ngem.1sg_Aux.others",
        "12322": "SC.tw.pass.ngem.2sgm_Aux.others",
        "12323": "SC.tw.pass.ngem.2sgf_Aux.others",
        "12324": "SC.tw.pass.ngem.3sgm_Aux.others",
        "12325": "SC.tw.pass.ngem.3sgf_Aux.others",
        "12326": "SC.tw.pass.ngem.3sg_Aux.others",
        "12327": "SC.tw.pass.ngem.1pl_Aux.others",
        "-12327": "SC.tw.pass.ngem.1du_Aux.others",
        "12328": "SC.tw.pass.ngem.2pl_Aux.others",
        "-12328": "SC.tw.pass.ngem.2du_Aux.others",
        "12329": "SC.tw.pass.ngem.3pl_Aux.others",
        "-12329": "SC.tw.pass.ngem.3du_Aux.others",
        "12360": "SC.tw.pass.gem.nom.subj_Aux.others",
        "12361": "SC.tw.pass.gem.1sg_Aux.others",
        "12362": "SC.tw.pass.gem.2sgm_Aux.others",
        "12363": "SC.tw.pass.gem.2sgf_Aux.others",
        "12364": "SC.tw.pass.gem.3sgm_Aux.others",
        "12365": "SC.tw.pass.gem.3sgf_Aux.others",
        "12366": "SC.tw.pass.gem.3sg_Aux.others",
        "12367": "SC.tw.pass.gem.1pl_Aux.others",
        "-12367": "SC.tw.pass.gem.1du_Aux.others",
        "12368": "SC.tw.pass.gem.2pl_Aux.others",
        "-12368": "SC.tw.pass.gem.2du_Aux.others",
        "12369": "SC.tw.pass.gem.3pl_Aux.others",
        "-12369": "SC.tw.pass.gem.3du_Aux.others",
        "12380": "SC.n.act.ngem.nom.subj_Aux.others",
        "12381": "SC.n.act.ngem.1sg_Aux.others",
        "12382": "SC.n.act.ngem.2sgm_Aux.others",
        "12383": "SC.n.act.ngem.2sgf_Aux.others",
        "12384": "SC.n.act.ngem.3sgm_Aux.others",
        "12385": "SC.n.act.ngem.3sgf_Aux.others",
        "12386": "SC.n.act.ngem.3sg_Aux.others",
        "12387": "SC.n.act.ngem.1pl_Aux.others",
        "-12387": "SC.n.act.ngem.1du_Aux.others",
        "12388": "SC.n.act.ngem.2pl_Aux.others",
        "-12388": "SC.n.act.ngem.2du_Aux.others",
        "12389": "SC.n.act.ngem.3pl_Aux.others",
        "-12389": "SC.n.act.ngem.3du_Aux.others",
        "12420": "SC.n.act.gem.nom.subj_Aux.others",
        "12421": "SC.n.act.gem.1sg_Aux.others",
        "12422": "SC.n.act.gem.2sgm_Aux.others",
        "12423": "SC.n.act.gem.2sgf_Aux.others",
        "12424": "SC.n.act.gem.3sgm_Aux.others",
        "12425": "SC.n.act.gem.3sgf_Aux.others",
        "12426": "SC.n.act.gem.3sg_Aux.others",
        "12427": "SC.n.act.gem.1pl_Aux.others",
        "-12427": "SC.n.act.gem.1du_Aux.others",
        "12428": "SC.n.act.gem.2pl_Aux.others",
        "-12428": "SC.n.act.gem.2du_Aux.others",
        "12429": "SC.n.act.gem.3pl_Aux.others",
        "-12429": "SC.n.act.gem.3du_Aux.others",
        "12430": "SC.n.pass.ngem.nom.subj_Aux.others",
        "12431": "SC.n.pass.ngem.1sg_Aux.others",
        "12432": "SC.n.pass.ngem.2sgm_Aux.others",
        "12433": "SC.n.pass.ngem.sg2f_Aux.others",
        "12434": "SC.n.pass.ngem.3sgm_Aux.others",
        "12435": "SC.n.pass.ngem.3sgf_Aux.others",
        "12436": "SC.n.pass.ngem.3sg_Aux.others",
        "12437": "SC.n.pass.ngem.1pl_Aux.others",
        "-12437": "SC.n.pass.ngem.1du_Aux.others",
        "12438": "SC.n.pass.ngem.2pl_Aux.others",
        "-12438": "SC.n.pass.ngem.2du_Aux.others",
        "12439": "SC.n.pass.ngem.3pl_Aux.others",
        "-12439": "SC.n.pass.ngem.3du_Aux.others",
        "12440": "SC.n.tw.pass.ngem.nom.subj_Aux.others",
        "12441": "SC.n.tw.pass.ngem.1sg_Aux.others",
        "12442": "SC.n.tw.pass.ngem.2sgm_Aux.others",
        "12443": "SC.n.tw.pass.ngem.2sgf_Aux.others",
        "12444": "SC.n.tw.pass.ngem.3sgm_Aux.others",
        "12445": "SC.n.tw.pass.ngem.3sgf_Aux.others",
        "12446": "SC.n.tw.pass.ngem.3sg_Aux.others",
        "12447": "SC.n.tw.pass.ngem.1pl_Aux.others",
        "-12447": "SC.n.tw.pass.ngem.1du_Aux.others",
        "12448": "SC.n.tw.pass.ngem.2pl_Aux.others",
        "-12448": "SC.n.tw.pass.ngem.2du_Aux.others",
        "12449": "SC.n.tw.pass.ngem.3pl_Aux.others",
        "-12449": "SC.n.tw.pass.ngem.3du_Aux.others",
        "12480": "SC.n.tw.pass.gem.nom.subj_Aux.others",
        "12481": "SC.n.tw.pass.gem.1sg_Aux.others",
        "12482": "SC.n.tw.pass.gem.2sgm_Aux.others",
        "12483": "SC.n.tw.pass.gem.2sgf_Aux.others",
        "12484": "SC.n.tw.pass.gem.3sgm_Aux.others",
        "12485": "SC.n.tw.pass.gem.3sgf_Aux.others",
        "12486": "SC.n.tw.pass.gem.3sg_Aux.others",
        "12487": "SC.n.tw.pass.gem.1pl_Aux.others",
        "-12487": "SC.n.tw.pass.gem.1du_Aux.others",
        "12488": "SC.n.tw.pass.gem.2pl_Aux.others",
        "-12488": "SC.n.tw.pass.gem.2du_Aux.others",
        "12489": "SC.n.tw.pass.gem.3pl_Aux.others",
        "-12489": "SC.n.tw.pass.gem.3du_Aux.others",
        "12840": "SC.t.act.ngem.nom.subj_Aux.others",
        "12841": "SC.t.act.ngem.1sg_Aux.others",
        "12842": "SC.t.act.ngem.2sgm_Aux.others",
        "12843": "SC.t.act.ngem.2sgf_Aux.others",
        "12844": "SC.t.act.ngem.3sgm_Aux.others",
        "12845": "SC.t.act.ngem.3sgf_Aux.others",
        "12846": "SC.t.act.ngem.3sg_Aux.others",
        "12847": "SC.t.act.ngem.1pl_Aux.others",
        "-12847": "SC.t.act.ngem.1du_Aux.others",
        "12848": "SC.t.act.ngem.2pl_Aux.others",
        "-12848": "SC.t.act.ngem.2du_Aux.others",
        "12849": "SC.t.act.ngem.3pl_Aux.others",
        "-12849": "SC.t.act.ngem.3du_Aux.others",
        "12850": "SC.t.act.gem.nom.subj_Aux.others",
        "12851": "SC.t.act.gem.1sg_Aux.others",
        "12852": "SC.t.act.gem.2sgm_Aux.others",
        "12853": "SC.t.act.gem.2sgf_Aux.others",
        "12854": "SC.t.act.gem.3sgm_Aux.others",
        "12855": "SC.t.act.gem.3sgf_Aux.others",
        "12856": "SC.t.act.gem.3sg_Aux.others",
        "12857": "SC.t.act.gem.1pl_Aux.others",
        "-12857": "SC.t.act.gem.1du_Aux.others",
        "12858": "SC.t.act.gem.2pl_Aux.others",
        "-12858": "SC.t.act.gem.2du_Aux.others",
        "12859": "SC.t.act.gem.3pl_Aux.others",
        "-12859": "SC.t.act.gem.3du_Aux.others",
        "12860": "SC.t.pass.ngem.nom.subj_Aux.others",
        "12861": "SC.t.pass.ngem.1sg_Aux.others",
        "12862": "SC.t.pass.ngem.2sgm_Aux.others",
        "12863": "SC.t.pass.ngem.2sgf_Aux.others",
        "12864": "SC.t.pass.ngem.3sgm_Aux.others",
        "12865": "SC.t.pass.ngem.3sgf_Aux.others",
        "12866": "SC.t.pass.ngem.3sg_Aux.others",
        "12867": "SC.t.pass.ngem.1pl_Aux.others",
        "-12867": "SC.t.pass.ngem.1du_Aux.others",
        "12868": "SC.t.pass.ngem.2pl_Aux.others",
        "-12868": "SC.t.pass.ngem.2du_Aux.others",
        "12869": "SC.t.pass.ngem.3pl_Aux.others",
        "-12869": "SC.t.pass.ngem.3du_Aux.others",
        "12870": "SC.t.pass.gem.nom.subj_Aux.others",
        "12871": "SC.t.pass.gem.1sg_Aux.others",
        "12872": "SC.t.pass.gem.2sgm_Aux.others",
        "12873": "SC.t.pass.gem.2sgf_Aux.others",
        "12874": "SC.t.pass.gem.3sgm_Aux.others",
        "12875": "SC.t.pass.gem.3sgf_Aux.others",
        "12876": "SC.t.pass.gem.3sg_Aux.others",
        "12877": "SC.t.pass.gem.1pl_Aux.others",
        "-12877": "SC.t.pass.gem.1du_Aux.others",
        "12878": "SC.t.pass.gem.2pl_Aux.others",
        "-12878": "SC.t.pass.gem.2du_Aux.others",
        "12879": "SC.t.pass.gem.3pl_Aux.others",
        "-12879": "SC.t.pass.gem.3du_Aux.others",
        "13000": "SC.unspec.nom.subj_Aux.jw",
        "613000": "SC.unspec.nom.subj_Neg.jwtj_Aux.jw",
        "13001": "SC.unspec.1sg_Aux.jw",
        "13002": "SC.unspec.2sgm_Aux.jw",
        "13005": "SC.unspec.3sgf_Aux.jw",
        "13020": "SC.act.ngem_Aux.jw",
        "113020": "SC.act.ngem.nom.subj_Neg.n_Aux.jw",
        "213020": "SC.act.ngem.nom.subj_Neg.nn_Aux.jw",
        "13021": "SC.act.ngem.1sg_Aux.jw",
        "13022": "SC.act.ngem.2sgm_Aux.jw",
        "213022": "SC.act.ngem.2sgm_Neg.nn_Aux.jw",
        "13023": "SC.act.ngem.2sgf_Aux.jw",
        "13024": "SC.act.ngem.3sgm_Aux.jw",
        "13025": "SC.act.ngem.3sgf_Aux.jw",
        "13026": "SC.act.ngem.3sg_Aux.jw",
        "213026": "SC.act.ngem.3sg_Neg.nn_Aux.jw",
        "13027": "SC.act.ngem.1pl_Aux.jw",
        "-13027": "SC.act.ngem.1du_Aux.jw",
        "13028": "SC.act.ngem.2pl_Aux.jw",
        "-13028": "SC.act.ngem.2du_Aux.jw",
        "13029": "SC.act.ngem.3pl_Aux.jw",
        "-13029": "SC.act.ngem.3du_Aux.jw",
        "213029": "SC.act.ngem.3pl_Neg.nn_Aux.jw",
        "13040": "SC.pass.ngem_Aux.jw",
        "13041": "SC.pass.ngem.1sg_Aux.jw",
        "13042": "SC.pass.ngem.2sgm_Aux.jw",
        "13043": "SC.pass.ngem.2sgf_Aux.jw",
        "13044": "SC.pass.ngem.3sgm_Aux.jw",
        "13045": "SC.pass.ngem.3sgf_Aux.jw",
        "13046": "SC.pass.ngem.3sg_Aux.jw",
        "13047": "SC.pass.ngem.1pl_Aux.jw",
        "-13047": "SC.pass.ngem.1du_Aux.jw",
        "13048": "SC.pass.ngem.2pl_Aux.jw",
        "-13048": "SC.pass.ngem.2du_Aux.jw",
        "13049": "SC.pass.ngem.3pl_Aux.jw",
        "-13049": "SC.pass.ngem.3du_Aux.jw",
        "13100": "SC.act.gem_Aux.jw",
        "13101": "SC.act.gem.1sg_Aux.jw",
        "13102": "SC.act.gem.2sgm_Aux.jw",
        "13103": "SC.act.gem.2sgf_Aux.jw",
        "13104": "SC.act.gem.3sgm_Aux.jw",
        "13105": "SC.act.gem.3sgf_Aux.jw",
        "13106": "SC.act.gem.3sg_Aux.jw",
        "13107": "SC.act.gem.1pl_Aux.jw",
        "-13107": "SC.act.gem.1du_Aux.jw",
        "13108": "SC.act.gem.2pl_Aux.jw",
        "-13108": "SC.act.gem.2du_Aux.jw",
        "13109": "SC.act.gem.3pl_Aux.jw",
        "-13109": "SC.act.gem.3du_Aux.jw",
        "13120": "SC.pass.gem(redupl).nom.subj_Aux.jw ",
        "13121": "SC.pass.gem(redupl).1sg_Aux.jw",
        "13122": "SC.pass.gem(redupl).2sgm_Aux.jw",
        "13123": "SC.pass.gem(redupl).2sgf_Aux.jw",
        "13124": "SC.pass.gem(redupl).3sgm_Aux.jw",
        "13125": "SC.pass.gem(redupl).3sgf_Aux.jw",
        "13126": "SC.pass.gem(redupl).3sg_Aux.jw",
        "13127": "SC.pass.gem(redupl).1pl_Aux.jw",
        "-13127": "SC.pass.gem(redupl).1du_Aux.jw",
        "13128": "SC.pass.gem(redupl).2pl_Aux.jw",
        "-13128": "SC.pass.gem(redupl).2du_Aux.jw",
        "13129": "SC.pass.gem(redupl).3pl_Aux.jw",
        "-13129": "SC.pass.gem(redupl).3du_Aux.jw",
        "13140": "SC.act.spec_Aux.jw",
        "13141": "SC.act.spec.1sg_Aux.jw",
        "13142": "SC.act.spec.2sgm_Aux.jw",
        "13143": "SC.act.spec.2sgf_Aux.jw",
        "13144": "SC.act.spec.3sgm_Aux.jw",
        "13145": "SC.act.spec.3sgf_Aux.jw",
        "13146": "SC.act.spec.3sg_Aux.jw",
        "13147": "SC.act.spec.1pl_Aux.jw",
        "-13147": "SC.act.spec.1du_Aux.jw",
        "13148": "SC.act.spec.2pl_Aux.jw",
        "-13148": "SC.act.spec.2du_Aux.jw",
        "13149": "SC.act.spec.3pl_Aux.jw",
        "-13149": "SC.act.spec.3du_Aux.jw",
        "13160": "SC.pass.spec.nom.subj_Aux.jw",
        "13161": "SC.pass.spec.1sg_Aux.jw",
        "13162": "SC.pass.spec.2sgm_Aux.jw",
        "13163": "SC.pass.spec.2sgf_Aux.jw",
        "13164": "SC.pass.spec.3sgm_Aux.jw",
        "13165": "SC.pass.spec.3sgf_Aux.jw",
        "13166": "SC.pass.spec.3sg_Aux.jw",
        "13167": "SC.pass.spec.1pl_Aux.jw",
        "-13167": "SC.pass.spec.1du_Aux.jw",
        "13168": "SC.pass.spec.2pl_Aux.jw",
        "-13168": "SC.pass.spec.2du_Aux.jw",
        "13169": "SC.pass.spec.3pl_Aux.jw",
        "-13169": "SC.pass.spec.3du_Aux.jw",
        "13170": "SC.tw.pass.spec.nom.subj_Aux.jw",
        "13171": "SC.tw.pass.spec.1sg_Aux.jw",
        "13172": "SC.tw.pass.spec.2sgm_Aux.jw",
        "13173": "SC.tw.pass.spec.2sgf_Aux.jw",
        "13174": "SC.tw.pass.spec.3sgm_Aux.jw",
        "13175": "SC.tw.pass.spec.3sgf_Aux.jw",
        "13176": "SC.tw.pass.spec.3sg_Aux.jw",
        "13177": "SC.tw.pass.spec.1pl_Aux.jw",
        "-13177": "SC.tw.pass.spec.1du_Aux.jw",
        "13178": "SC.tw.pass.spec.2pl_Aux.jw",
        "-13178": "SC.tw.pass.spec.2du_Aux.jw",
        "13179": "SC.tw.pass.spec.3pl_Aux.jw",
        "-13179": "SC.tw.pass.spec.3du_Aux.jw",
        "13180": "SC.w.act.ngem.nom.subj_Aux.jw",
        "13181": "SC.w.act.ngem.1sg_Aux.jw",
        "13182": "SC.w.act.ngem.2sgm_Aux.jw",
        "13183": "SC.w.act.ngem.2sgf_Aux.jw",
        "13184": "SC.w.act.ngem.3sgm_Aux.jw",
        "13185": "SC.w.act.ngem.3sgf_Aux.jw",
        "13186": "SC.w.act.ngem.3sg_Aux.jw",
        "13187": "SC.w.act.ngem.1pl_Aux.jw",
        "-13187": "SC.w.act.ngem.1du_Aux.jw",
        "13188": "SC.w.act.ngem.2pl_Aux.jw",
        "-13188": "SC.w.act.ngem.2du_Aux.jw",
        "13189": "SC.w.act.ngem.3pl_Aux.jw",
        "-13189": "SC.w.act.ngem.3du_Aux.jw",
        "13220": "SC.w.act.gem.nom.subj_Aux.jw",
        "13221": "SC.w.act.gem.1sg_Aux.jw",
        "13222": "SC.w.act.gem.2sgm_Aux.jw",
        "13223": "SC.w.act.gem.2sgf_Aux.jw",
        "13224": "SC.w.act.gem.3sgm_Aux.jw",
        "13225": "SC.w.act.gem.3sgf_Aux.jw",
        "13226": "SC.w.act.gem.3sg_Aux.jw",
        "13227": "SC.w.act.gem.1pl_Aux.jw",
        "-13227": "SC.w.act.gem.1du_Aux.jw",
        "13228": "SC.w.act.gem.2pl_Aux.jw",
        "-13228": "SC.w.act.gem.2du_Aux.jw",
        "13229": "SC.w.act.gem.3pl_Aux.jw",
        "-13229": "SC.w.act.gem.3du_Aux.jw",
        "13240": "SC.w.pass.ngem.nom.subj_Aux.jw",
        "13241": "SC.w.pass.ngem.1sg_Aux.jw",
        "13242": "SC.w.pass.ngem.2sgm_Aux.jw",
        "13243": "SC.w.pass.ngem.2sgf_Aux.jw",
        "13244": "SC.w.pass.ngem.3sgm_Aux.jw",
        "13245": "SC.w.pass.ngem.3sgf_Aux.jw",
        "13246": "SC.w.pass.ngem.3sg_Aux.jw",
        "13247": "SC.w.pass.ngem.1pl_Aux.jw",
        "-13247": "SC.w.pass.ngem.1du_Aux.jw",
        "13248": "SC.w.pass.ngem.2pl_Aux.jw",
        "-13248": "SC.w.pass.ngem.2du_Aux.jw",
        "13249": "SC.w.pass.ngem.3pl_Aux.jw",
        "-13249": "SC.w.pass.ngem.3du_Aux.jw",
        "13280": "SC.w.tw.pass.ngem.nom.subj_Aux.jw",
        "13281": "SC.w.tw.pass.ngem.1sg_Aux.jw",
        "13282": "SC.w.tw.pass.ngem.2sgm_Aux.jw",
        "13283": "SC.w.tw.pass.ngem.2sgf_Aux.jw",
        "13284": "SC.w.tw.pass.ngem.3sgm_Aux.jw",
        "13285": "SC.w.tw.pass.ngem.3sgf_Aux.jw",
        "13286": "SC.w.tw.pass.ngem.3sg_Aux.jw",
        "13287": "SC.w.tw.pass.ngem.1pl_Aux.jw",
        "-13287": "SC.w.tw.pass.ngem.1du_Aux.jw",
        "13288": "SC.w.tw.pass.ngem.2pl_Aux.jw",
        "-13288": "SC.w.tw.pass.ngem.2du_Aux.jw",
        "13289": "SC.w.tw.pass.ngem.3pl_Aux.jw",
        "-13289": "SC.w.tw.pass.ngem.3du_Aux.jw",
        "13320": "SC.tw.pass.ngem.nom.subj_Aux.jw",
        "13321": "SC.tw.pass.ngem.1sg_Aux.jw",
        "13322": "SC.tw.pass.ngem.2sgm_Aux.jw",
        "13323": "SC.tw.pass.ngem.2sgf_Aux.jw",
        "13324": "SC.tw.pass.ngem.3sgm_Aux.jw",
        "13325": "SC.tw.pass.ngem.3sgf_Aux.jw",
        "13326": "SC.tw.pass.ngem.3sg_Aux.jw",
        "13327": "SC.tw.pass.ngem.1pl_Aux.jw",
        "-13327": "SC.tw.pass.ngem.1du_Aux.jw",
        "13328": "SC.tw.pass.ngem.2pl_Aux.jw",
        "-13328": "SC.tw.pass.ngem.2du_Aux.jw",
        "13329": "SC.tw.pass.ngem.3pl_Aux.jw",
        "-13329": "SC.tw.pass.ngem.3du_Aux.jw",
        "13360": "SC.tw.pass.gem.nom.subj_Aux.jw",
        "13361": "SC.tw.pass.gem.1sg_Aux.jw",
        "13362": "SC.tw.pass.gem.2sgm_Aux.jw",
        "13363": "SC.tw.pass.gem.2sgf_Aux.jw",
        "13364": "SC.tw.pass.gem.3sgm_Aux.jw",
        "13365": "SC.tw.pass.gem.3sgf_Aux.jw",
        "13366": "SC.tw.pass.gem.3sg_Aux.jw",
        "13367": "SC.tw.pass.gem.1pl_Aux.jw",
        "-13367": "SC.tw.pass.gem.1du_Aux.jw",
        "13368": "SC.tw.pass.gem.2pl_Aux.jw",
        "-13368": "SC.tw.pass.gem.2du_Aux.jw",
        "13369": "SC.tw.pass.gem.3pl_Aux.jw",
        "-13369": "SC.tw.pass.gem.3du_Aux.jw",
        "13380": "SC.n.act.ngem.nom.subj_Aux.jw",
        "13381": "SC.n.act.ngem.1sg_Aux.jw",
        "13382": "SC.n.act.ngem.2sgm_Aux.jw",
        "13383": "SC.n.act.ngem.2sgf_Aux.jw",
        "13384": "SC.n.act.ngem.3sgm_Aux.jw",
        "13385": "SC.n.act.ngem.3sgf_Aux.jw",
        "13386": "SC.n.act.ngem.3sg_Aux.jw",
        "13387": "SC.n.act.ngem.1pl_Aux.jw",
        "-13387": "SC.n.act.ngem.1du_Aux.jw",
        "13388": "SC.n.act.ngem.2pl_Aux.jw",
        "-13388": "SC.n.act.ngem.2du_Aux.jw",
        "13389": "SC.n.act.ngem.3pl_Aux.jw",
        "-13389": "SC.n.act.ngem.3du_Aux.jw",
        "13420": "SC.n.act.gem.nom.subj_Aux.jw",
        "13421": "SC.n.act.gem.1sg_Aux.jw",
        "13422": "SC.n.act.gem.2sgm_Aux.jw",
        "13423": "SC.n.act.gem.2sgf_Aux.jw",
        "13424": "SC.n.act.gem.3sgm_Aux.jw",
        "13425": "SC.n.act.gem.3sgf_Aux.jw",
        "13426": "SC.n.act.gem.3sg_Aux.jw",
        "13427": "SC.n.act.gem.1pl_Aux.jw",
        "-13427": "SC.n.act.gem.1du_Aux.jw",
        "13428": "SC.n.act.gem.2pl_Aux.jw",
        "-13428": "SC.n.act.gem.2du_Aux.jw",
        "13429": "SC.n.act.gem.3pl_Aux.jw",
        "-13429": "SC.n.act.gem.3du_Aux.jw",
        "13430": "SC.n.pass.ngem.nom.subj_Aux.jw",
        "13431": "SC.n.pass.ngem.1sg_Aux.jw",
        "13432": "SC.n.pass.ngem.2sgm_Aux.jw",
        "13433": "SC.n.pass.ngem.sg2f_Aux.jw",
        "13434": "SC.n.pass.ngem.3sgm_Aux.jw",
        "13435": "SC.n.pass.ngem.3sgf_Aux.jw",
        "13436": "SC.n.pass.ngem.3sg_Aux.jw",
        "13437": "SC.n.pass.ngem.1pl_Aux.jw",
        "-13437": "SC.n.pass.ngem.1du_Aux.jw",
        "13438": "SC.n.pass.ngem.2pl_Aux.jw",
        "-13438": "SC.n.pass.ngem.2du_Aux.jw",
        "13439": "SC.n.pass.ngem.3pl_Aux.jw",
        "-13439": "SC.n.pass.ngem.3du_Aux.jw",
        "13440": "SC.n.tw.pass.ngem.nom.subj_Aux.jw",
        "13441": "SC.n.tw.pass.ngem.1sg_Aux.jw",
        "13442": "SC.n.tw.pass.ngem.2sgm_Aux.jw",
        "13443": "SC.n.tw.pass.ngem.2sgf_Aux.jw",
        "13444": "SC.n.tw.pass.ngem.3sgm_Aux.jw",
        "13445": "SC.n.tw.pass.ngem.3sgf_Aux.jw",
        "13446": "SC.n.tw.pass.ngem.3sg_Aux.jw",
        "13447": "SC.n.tw.pass.ngem.1pl_Aux.jw",
        "-13447": "SC.n.tw.pass.ngem.1du_Aux.jw",
        "13448": "SC.n.tw.pass.ngem.2pl_Aux.jw",
        "-13448": "SC.n.tw.pass.ngem.2du_Aux.jw",
        "13449": "SC.n.tw.pass.ngem.3pl_Aux.jw",
        "-13449": "SC.n.tw.pass.ngem.3du_Aux.jw",
        "13480": "SC.n.tw.pass.gem.nom.subj_Aux.jw",
        "13481": "SC.n.tw.pass.gem.1sg_Aux.jw",
        "13482": "SC.n.tw.pass.gem.2sgm_Aux.jw",
        "13483": "SC.n.tw.pass.gem.2sgf_Aux.jw",
        "13484": "SC.n.tw.pass.gem.3sgm_Aux.jw",
        "13485": "SC.n.tw.pass.gem.3sgf_Aux.jw",
        "13486": "SC.n.tw.pass.gem.3sg_Aux.jw",
        "13487": "SC.n.tw.pass.gem.1pl_Aux.jw",
        "-13487": "SC.n.tw.pass.gem.1du_Aux.jw",
        "13488": "SC.n.tw.pass.gem.2pl_Aux.jw",
        "-13488": "SC.n.tw.pass.gem.2du_Aux.jw",
        "13489": "SC.n.tw.pass.gem.3pl_Aux.jw",
        "-13489": "SC.n.tw.pass.gem.3du_Aux.jw",
        "13613": "ḫr+SC.act.ngem.2sgf_Aux.jw",
        "13800": "SC.n.act.ngem.impers_Aux.jw",
        "13840": "SC.t.act.ngem.nom.subj_Aux.jw",
        "13841": "SC.t.act.ngem.1sg_Aux.jw",
        "13842": "SC.t.act.ngem.2sgm_Aux.jw",
        "13843": "SC.t.act.ngem.2sgf_Aux.jw",
        "13844": "SC.t.act.ngem.3sgm_Aux.jw",
        "13845": "SC.t.act.ngem.3sgf_Aux.jw",
        "13846": "SC.t.act.ngem.3sg_Aux.jw",
        "13847": "SC.t.act.ngem.1pl_Aux.jw",
        "-13847": "SC.t.act.ngem.1du_Aux.jw",
        "13848": "SC.t.act.ngem.2pl_Aux.jw",
        "-13848": "SC.t.act.ngem.2du_Aux.jw",
        "13849": "SC.t.act.ngem.3pl_Aux.jw",
        "-13849": "SC.t.act.ngem.3du_Aux.jw",
        "13850": "SC.t.act.gem.nom.subj_Aux.jw",
        "13851": "SC.t.act.gem.1sg_Aux.jw",
        "13852": "SC.t.act.gem.2sgm_Aux.jw",
        "13853": "SC.t.act.gem.2sgf_Aux.jw",
        "13854": "SC.t.act.gem.3sgm_Aux.jw",
        "13855": "SC.t.act.gem.3sgf_Aux.jw",
        "13856": "SC.t.act.gem.3sg_Aux.jw",
        "13857": "SC.t.act.gem.1pl_Aux.jw",
        "-13857": "SC.t.act.gem.1du_Aux.jw",
        "13858": "SC.t.act.gem.2pl_Aux.jw",
        "-13858": "SC.t.act.gem.2du_Aux.jw",
        "13859": "SC.t.act.gem.3pl_Aux.jw",
        "-13859": "SC.t.act.gem.3du_Aux.jw",
        "13860": "SC.t.pass.ngem.nom.subj_Aux.jw",
        "13861": "SC.t.pass.ngem.1sg_Aux.jw",
        "13862": "SC.t.pass.ngem.2sgm_Aux.jw",
        "13863": "SC.t.pass.ngem.2sgf_Aux.jw",
        "13864": "SC.t.pass.ngem.3sgm_Aux.jw",
        "13865": "SC.t.pass.ngem.3sgf_Aux.jw",
        "13866": "SC.t.pass.ngem.3sg_Aux.jw",
        "13867": "SC.t.pass.ngem.1pl_Aux.jw",
        "-13867": "SC.t.pass.ngem.1du_Aux.jw",
        "13868": "SC.t.pass.ngem.2pl_Aux.jw",
        "-13868": "SC.t.pass.ngem.2du_Aux.jw",
        "13869": "SC.t.pass.ngem.3pl_Aux.jw",
        "-13869": "SC.t.pass.ngem.3du_Aux.jw",
        "13870": "SC.t.pass.gem.nom.subj_Aux.jw",
        "13871": "SC.t.pass.gem.1sg_Aux.jw",
        "13872": "SC.t.pass.gem.2sgm_Aux.jw",
        "13873": "SC.t.pass.gem.2sgf_Aux.jw",
        "13874": "SC.t.pass.gem.3sgm_Aux.jw",
        "13875": "SC.t.pass.gem.3sgf_Aux.jw",
        "13876": "SC.t.pass.gem.3sg_Aux.jw",
        "13877": "SC.t.pass.gem.1pl_Aux.jw",
        "-13877": "SC.t.pass.gem.1du_Aux.jw",
        "13878": "SC.t.pass.gem.2pl_Aux.jw",
        "-13878": "SC.t.pass.gem.2du_Aux.jw",
        "13879": "SC.t.pass.gem.3pl_Aux.jw",
        "-13879": "SC.t.pass.gem.3du_Aux.jw",
        "13900": "SC.act.ngem.impers_Aux.jw",
        "13910": "SC.pass.ngem.impers_Aux.jw",
        "13950": "SC.tw.pass.ngem.impers_Aux.jw",
        "14000": "SC.unspec.nom.subj_Aux.ꜥḥꜥ.n",
        "14020": "SC.act.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14021": "SC.act.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14022": "SC.act.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14023": "SC.act.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14024": "SC.act.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14025": "SC.act.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14026": "SC.act.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14027": "SC.act.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14027": "SC.act.ngem.1du_Aux.ꜥḥꜥ.n",
        "14028": "SC.act.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14028": "SC.act.ngem.2du_Aux.ꜥḥꜥ.n",
        "14029": "SC.act.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14029": "SC.act.ngem.3du_Aux.ꜥḥꜥ.n",
        "14040": "SC.pass.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14041": "SC.pass.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14042": "SC.pass.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14043": "SC.pass.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14044": "SC.pass.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14045": "SC.pass.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14046": "SC.pass.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14047": "SC.pass.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14047": "SC.pass.ngem.1du_Aux.ꜥḥꜥ.n",
        "14048": "SC.pass.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14048": "SC.pass.ngem.2du_Aux.ꜥḥꜥ.n",
        "14049": "SC.pass.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14049": "SC.pass.ngem.3du_Aux.ꜥḥꜥ.n",
        "14100": "SC.act.gem.nom.subj_Aux.ꜥḥꜥ.n",
        "14101": "SC.act.gem.1sg_Aux.ꜥḥꜥ.n",
        "14102": "SC.act.gem.2sgm_Aux.ꜥḥꜥ.n",
        "14103": "SC.act.gem.2sgf_Aux.ꜥḥꜥ.n",
        "14104": "SC.act.gem.3sgm_Aux.ꜥḥꜥ.n",
        "14105": "SC.act.gem.3sgf_Aux.ꜥḥꜥ.n",
        "14106": "SC.act.gem.3sg_Aux.ꜥḥꜥ.n",
        "14107": "SC.act.gem.1pl_Aux.ꜥḥꜥ.n",
        "-14107": "SC.act.gem.1du_Aux.ꜥḥꜥ.n",
        "14108": "SC.act.gem.2pl_Aux.ꜥḥꜥ.n",
        "-14108": "SC.act.gem.2du_Aux.ꜥḥꜥ.n",
        "14109": "SC.act.gem.3pl_Aux.ꜥḥꜥ.n",
        "-14109": "SC.act.gem.3du_Aux.ꜥḥꜥ.n",
        "14120": "SC.pass.gem(redupl).nom.subj_Aux.ꜥḥꜥ.n",
        "14121": "SC.pass.gem(redupl).1sg_Aux.ꜥḥꜥ.n",
        "14122": "SC.pass.gem(redupl).2sgm_Aux.ꜥḥꜥ.n",
        "14123": "SC.pass.gem(redupl).2sgf_Aux.ꜥḥꜥ.n",
        "14124": "SC.pass.gem(redupl).3sgm_Aux.ꜥḥꜥ.n",
        "14125": "SC.pass.gem(redupl).3sgf_Aux.ꜥḥꜥ.n",
        "14126": "SC.pass.gem(redupl).3sg_Aux.ꜥḥꜥ.n",
        "14127": "SC.pass.gem(redupl).1pl_Aux.ꜥḥꜥ.n",
        "-14127": "SC.pass.gem(redupl).1du_Aux.ꜥḥꜥ.n",
        "14128": "SC.pass.gem(redupl).2pl_Aux.ꜥḥꜥ.n",
        "-14128": "SC.pass.gem(redupl).2du_Aux.ꜥḥꜥ.n",
        "14129": "SC.pass.gem(redupl).3pl_Aux.ꜥḥꜥ.n",
        "-14129": "SC.pass.gem(redupl).3du_Aux.ꜥḥꜥ.n",
        "14140": "SC.act.spec.nom.subj_Aux.ꜥḥꜥ.n",
        "14141": "SC.act.spec.1sg_Aux.ꜥḥꜥ.n",
        "14142": "SC.act.spec.2sgm_Aux.ꜥḥꜥ.n",
        "14143": "SC.act.spec.2sgf_Aux.ꜥḥꜥ.n",
        "14144": "SC.act.spec.3sgm_Aux.ꜥḥꜥ.n",
        "14145": "SC.act.spec.3sgf_Aux.ꜥḥꜥ.n",
        "14146": "SC.act.spec.3sg_Aux.ꜥḥꜥ.n",
        "14147": "SC.act.spec.1pl_Aux.ꜥḥꜥ.n",
        "-14147": "SC.act.spec.1du_Aux.ꜥḥꜥ.n",
        "14148": "SC.act.spec.2pl_Aux.ꜥḥꜥ.n",
        "-14148": "SC.act.spec.2du_Aux.ꜥḥꜥ.n",
        "14149": "SC.act.spec.3pl_Aux.ꜥḥꜥ.n",
        "-14149": "SC.act.spec.3du_Aux.ꜥḥꜥ.n",
        "14160": "SC.pass.spec.nom.subj_Aux.ꜥḥꜥ.n",
        "14161": "SC.pass.spec.1sg_Aux.ꜥḥꜥ.n",
        "14162": "SC.pass.spec.2sgm_Aux.ꜥḥꜥ.n",
        "14163": "SC.pass.spec.2sgf_Aux.ꜥḥꜥ.n",
        "14164": "SC.pass.spec.3sgm_Aux.ꜥḥꜥ.n",
        "14165": "SC.pass.spec.3sgf_Aux.ꜥḥꜥ.n",
        "14166": "SC.pass.spec.3sg_Aux.ꜥḥꜥ.n",
        "14167": "SC.pass.spec.1pl_Aux.ꜥḥꜥ.n",
        "-14167": "SC.pass.spec.1du_Aux.ꜥḥꜥ.n",
        "14168": "SC.pass.spec.2pl_Aux.ꜥḥꜥ.n",
        "-14168": "SC.pass.spec.2du_Aux.ꜥḥꜥ.n",
        "14169": "SC.pass.spec.3pl_Aux.ꜥḥꜥ.n",
        "-14169": "SC.pass.spec.3du_Aux.ꜥḥꜥ.n",
        "14170": "SC.tw.pass.spec.nom.subj_Aux.ꜥḥꜥ.n",
        "14171": "SC.tw.pass.spec.1sg_Aux.ꜥḥꜥ.n",
        "14172": "SC.tw.pass.spec.2sgm_Aux.ꜥḥꜥ.n",
        "14173": "SC.tw.pass.spec.2sgf_Aux.ꜥḥꜥ.n",
        "14174": "SC.tw.pass.spec.3sgm_Aux.ꜥḥꜥ.n",
        "14175": "SC.tw.pass.spec.3sgf_Aux.ꜥḥꜥ.n",
        "14176": "SC.tw.pass.spec.3sg_Aux.ꜥḥꜥ.n",
        "14177": "SC.tw.pass.spec.1pl_Aux.ꜥḥꜥ.n",
        "-14177": "SC.tw.pass.spec.1du_Aux.ꜥḥꜥ.n",
        "14178": "SC.tw.pass.spec.2pl_Aux.ꜥḥꜥ.n",
        "-14178": "SC.tw.pass.spec.2du_Aux.ꜥḥꜥ.n",
        "14179": "SC.tw.pass.spec.3pl_Aux.ꜥḥꜥ.n",
        "-14179": "SC.tw.pass.spec.3du_Aux.ꜥḥꜥ.n",
        "14180": "SC.w.act.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14181": "SC.w.act.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14182": "SC.w.act.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14183": "SC.w.act.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14184": "SC.w.act.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14185": "SC.w.act.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14186": "SC.w.act.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14187": "SC.w.act.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14187": "SC.w.act.ngem.1du_Aux.ꜥḥꜥ.n",
        "14188": "SC.w.act.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14188": "SC.w.act.ngem.2du_Aux.ꜥḥꜥ.n",
        "14189": "SC.w.act.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14189": "SC.w.act.ngem.3du_Aux.ꜥḥꜥ.n",
        "14220": "SC.w.act.gem.nom.subj_Aux.ꜥḥꜥ.n",
        "14221": "SC.w.act.gem.1sg_Aux.ꜥḥꜥ.n",
        "14222": "SC.w.act.gem.2sgm_Aux.ꜥḥꜥ.n",
        "14223": "SC.w.act.gem.2sgf_Aux.ꜥḥꜥ.n",
        "14224": "SC.w.act.gem.3sgm_Aux.ꜥḥꜥ.n",
        "14225": "SC.w.act.gem.3sgf_Aux.ꜥḥꜥ.n",
        "14226": "SC.w.act.gem.3sg_Aux.ꜥḥꜥ.n",
        "14227": "SC.w.act.gem.1pl_Aux.ꜥḥꜥ.n",
        "-14227": "SC.w.act.gem.1du_Aux.ꜥḥꜥ.n",
        "14228": "SC.w.act.gem.2pl_Aux.ꜥḥꜥ.n",
        "-14228": "SC.w.act.gem.2du_Aux.ꜥḥꜥ.n",
        "14229": "SC.w.act.gem.3pl_Aux.ꜥḥꜥ.n",
        "-14229": "SC.w.act.gem.3du_Aux.ꜥḥꜥ.n",
        "14240": "SC.w.pass.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14241": "SC.w.pass.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14242": "SC.w.pass.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14243": "SC.w.pass.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14244": "SC.w.pass.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14245": "SC.w.pass.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14246": "SC.w.pass.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14247": "SC.w.pass.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14247": "SC.w.pass.ngem.1du_Aux.ꜥḥꜥ.n",
        "14248": "SC.w.pass.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14248": "SC.w.pass.ngem.2du_Aux.ꜥḥꜥ.n",
        "14249": "SC.w.pass.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14249": "SC.w.pass.ngem.3du_Aux.ꜥḥꜥ.n",
        "14280": "SC.w.tw.pass.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14281": "SC.w.tw.pass.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14282": "SC.w.tw.pass.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14283": "SC.w.tw.pass.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14284": "SC.w.tw.pass.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14285": "SC.w.tw.pass.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14286": "SC.w.tw.pass.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14287": "SC.w.tw.pass.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14287": "SC.w.tw.pass.ngem.1du_Aux.ꜥḥꜥ.n",
        "14288": "SC.w.tw.pass.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14288": "SC.w.tw.pass.ngem.2du_Aux.ꜥḥꜥ.n",
        "14289": "SC.w.tw.pass.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14289": "SC.w.tw.pass.ngem.3du_Aux.ꜥḥꜥ.n",
        "14320": "SC.tw.pass.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14321": "SC.tw.pass.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14322": "SC.tw.pass.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14323": "SC.tw.pass.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14324": "SC.tw.pass.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14325": "SC.tw.pass.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14326": "SC.tw.pass.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14327": "SC.tw.pass.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14327": "SC.tw.pass.ngem.1du_Aux.ꜥḥꜥ.n",
        "14328": "SC.tw.pass.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14328": "SC.tw.pass.ngem.2du_Aux.ꜥḥꜥ.n",
        "14329": "SC.tw.pass.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14329": "SC.tw.pass.ngem.3du_Aux.ꜥḥꜥ.n",
        "14360": "SC.tw.pass.gem.nom.subj_Aux.ꜥḥꜥ.n",
        "14361": "SC.tw.pass.gem.1sg_Aux.ꜥḥꜥ.n",
        "14362": "SC.tw.pass.gem.2sgm_Aux.ꜥḥꜥ.n",
        "14363": "SC.tw.pass.gem.2sgf_Aux.ꜥḥꜥ.n",
        "14364": "SC.tw.pass.gem.3sgm_Aux.ꜥḥꜥ.n",
        "14365": "SC.tw.pass.gem.3sgf_Aux.ꜥḥꜥ.n",
        "14366": "SC.tw.pass.gem.3sg_Aux.ꜥḥꜥ.n",
        "14367": "SC.tw.pass.gem.1pl_Aux.ꜥḥꜥ.n",
        "-14367": "SC.tw.pass.gem.1du_Aux.ꜥḥꜥ.n",
        "14368": "SC.tw.pass.gem.2pl_Aux.ꜥḥꜥ.n",
        "-14368": "SC.tw.pass.gem.2du_Aux.ꜥḥꜥ.n",
        "14369": "SC.tw.pass.gem.3pl_Aux.ꜥḥꜥ.n",
        "-14369": "SC.tw.pass.gem.3du_Aux.ꜥḥꜥ.n",
        "14380": "SC.n.act.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14381": "SC.n.act.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14382": "SC.n.act.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14383": "SC.n.act.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14384": "SC.n.act.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14385": "SC.n.act.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14386": "SC.n.act.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14387": "SC.n.act.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14387": "SC.n.act.ngem.1du_Aux.ꜥḥꜥ.n",
        "14388": "SC.n.act.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14388": "SC.n.act.ngem.2du_Aux.ꜥḥꜥ.n",
        "14389": "SC.n.act.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14389": "SC.n.act.ngem.3du_Aux.ꜥḥꜥ.n",
        "14420": "SC.n.act.gem.nom.subj_Aux.ꜥḥꜥ.n",
        "14421": "SC.n.act.gem.1sg_Aux.ꜥḥꜥ.n",
        "14422": "SC.n.act.gem.2sgm_Aux.ꜥḥꜥ.n",
        "14423": "SC.n.act.gem.2sgf_Aux.ꜥḥꜥ.n",
        "14424": "SC.n.act.gem.3sgm_Aux.ꜥḥꜥ.n",
        "14425": "SC.n.act.gem.3sgf_Aux.ꜥḥꜥ.n",
        "14426": "SC.n.act.gem.3sg_Aux.ꜥḥꜥ.n",
        "14427": "SC.n.act.gem.1pl_Aux.ꜥḥꜥ.n",
        "-14427": "SC.n.act.gem.1du_Aux.ꜥḥꜥ.n",
        "14428": "SC.n.act.gem.2pl_Aux.ꜥḥꜥ.n",
        "-14428": "SC.n.act.gem.2du_Aux.ꜥḥꜥ.n",
        "14429": "SC.n.act.gem.3pl_Aux.ꜥḥꜥ.n",
        "-14429": "SC.n.act.gem.3du_Aux.ꜥḥꜥ.n",
        "14430": "SC.n.pass.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14431": "SC.n.pass.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14432": "SC.n.pass.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14433": "SC.n.pass.ngem.sg2f_Aux.ꜥḥꜥ.n",
        "14434": "SC.n.pass.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14435": "SC.n.pass.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14436": "SC.n.pass.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14437": "SC.n.pass.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14437": "SC.n.pass.ngem.1du_Aux.ꜥḥꜥ.n",
        "14438": "SC.n.pass.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14438": "SC.n.pass.ngem.2du_Aux.ꜥḥꜥ.n",
        "14439": "SC.n.pass.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14439": "SC.n.pass.ngem.3du_Aux.ꜥḥꜥ.n",
        "14440": "SC.n.tw.pass.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14441": "SC.n.tw.pass.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14442": "SC.n.tw.pass.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14443": "SC.n.tw.pass.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14444": "SC.n.tw.pass.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14445": "SC.n.tw.pass.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14446": "SC.n.tw.pass.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14447": "SC.n.tw.pass.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14447": "SC.n.tw.pass.ngem.1du_Aux.ꜥḥꜥ.n",
        "14448": "SC.n.tw.pass.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14448": "SC.n.tw.pass.ngem.2du_Aux.ꜥḥꜥ.n",
        "14449": "SC.n.tw.pass.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14449": "SC.n.tw.pass.ngem.3du_Aux.ꜥḥꜥ.n",
        "14480": "SC.n.tw.pass.gem.nom.subj_Aux.ꜥḥꜥ.n",
        "14481": "SC.n.tw.pass.gem.1sg_Aux.ꜥḥꜥ.n",
        "14482": "SC.n.tw.pass.gem.2sgm_Aux.ꜥḥꜥ.n",
        "14483": "SC.n.tw.pass.gem.2sgf_Aux.ꜥḥꜥ.n",
        "14484": "SC.n.tw.pass.gem.3sgm_Aux.ꜥḥꜥ.n",
        "14485": "SC.n.tw.pass.gem.3sgf_Aux.ꜥḥꜥ.n",
        "14486": "SC.n.tw.pass.gem.3sg_Aux.ꜥḥꜥ.n",
        "14487": "SC.n.tw.pass.gem.1pl_Aux.ꜥḥꜥ.n",
        "-14487": "SC.n.tw.pass.gem.1du_Aux.ꜥḥꜥ.n",
        "14488": "SC.n.tw.pass.gem.2pl_Aux.ꜥḥꜥ.n",
        "-14488": "SC.n.tw.pass.gem.2du_Aux.ꜥḥꜥ.n",
        "14489": "SC.n.tw.pass.gem.3pl_Aux.ꜥḥꜥ.n",
        "-14489": "SC.n.tw.pass.gem.3du_Aux.ꜥḥꜥ.n",
        "14840": "SC.t.act.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14841": "SC.t.act.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14842": "SC.t.act.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14843": "SC.t.act.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14844": "SC.t.act.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14845": "SC.t.act.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14846": "SC.t.act.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14847": "SC.t.act.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14847": "SC.t.act.ngem.1du_Aux.ꜥḥꜥ.n",
        "14848": "SC.t.act.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14848": "SC.t.act.ngem.2du_Aux.ꜥḥꜥ.n",
        "14849": "SC.t.act.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14849": "SC.t.act.ngem.3du_Aux.ꜥḥꜥ.n",
        "14850": "SC.t.act.gem.nom.subj_Aux.ꜥḥꜥ.n",
        "14851": "SC.t.act.gem.1sg_Aux.ꜥḥꜥ.n",
        "14852": "SC.t.act.gem.2sgm_Aux.ꜥḥꜥ.n",
        "14853": "SC.t.act.gem.2sgf_Aux.ꜥḥꜥ.n",
        "14854": "SC.t.act.gem.3sgm_Aux.ꜥḥꜥ.n",
        "14855": "SC.t.act.gem.3sgf_Aux.ꜥḥꜥ.n",
        "14856": "SC.t.act.gem.3sg_Aux.ꜥḥꜥ.n",
        "14857": "SC.t.act.gem.1pl_Aux.ꜥḥꜥ.n",
        "-14857": "SC.t.act.gem.1du_Aux.ꜥḥꜥ.n",
        "14858": "SC.t.act.gem.2pl_Aux.ꜥḥꜥ.n",
        "-14858": "SC.t.act.gem.2du_Aux.ꜥḥꜥ.n",
        "14859": "SC.t.act.gem.3pl_Aux.ꜥḥꜥ.n",
        "-14859": "SC.t.act.gem.3du_Aux.ꜥḥꜥ.n",
        "14860": "SC.t.pass.ngem.nom.subj_Aux.ꜥḥꜥ.n",
        "14861": "SC.t.pass.ngem.1sg_Aux.ꜥḥꜥ.n",
        "14862": "SC.t.pass.ngem.2sgm_Aux.ꜥḥꜥ.n",
        "14863": "SC.t.pass.ngem.2sgf_Aux.ꜥḥꜥ.n",
        "14864": "SC.t.pass.ngem.3sgm_Aux.ꜥḥꜥ.n",
        "14865": "SC.t.pass.ngem.3sgf_Aux.ꜥḥꜥ.n",
        "14866": "SC.t.pass.ngem.3sg_Aux.ꜥḥꜥ.n",
        "14867": "SC.t.pass.ngem.1pl_Aux.ꜥḥꜥ.n",
        "-14867": "SC.t.pass.ngem.1du_Aux.ꜥḥꜥ.n",
        "14868": "SC.t.pass.ngem.2pl_Aux.ꜥḥꜥ.n",
        "-14868": "SC.t.pass.ngem.2du_Aux.ꜥḥꜥ.n",
        "14869": "SC.t.pass.ngem.3pl_Aux.ꜥḥꜥ.n",
        "-14869": "SC.t.pass.ngem.3du_Aux.ꜥḥꜥ.n",
        "14870": "SC.t.pass.gem.nom.subj_Aux.ꜥḥꜥ.n",
        "14871": "SC.t.pass.gem.1sg_Aux.ꜥḥꜥ.n",
        "14872": "SC.t.pass.gem.2sgm_Aux.ꜥḥꜥ.n",
        "14873": "SC.t.pass.gem.2sgf_Aux.ꜥḥꜥ.n",
        "14874": "SC.t.pass.gem.3sgm_Aux.ꜥḥꜥ.n",
        "14875": "SC.t.pass.gem.3sgf_Aux.ꜥḥꜥ.n",
        "14876": "SC.t.pass.gem.3sg_Aux.ꜥḥꜥ.n",
        "14877": "SC.t.pass.gem.1pl_Aux.ꜥḥꜥ.n",
        "-14877": "SC.t.pass.gem.1du_Aux.ꜥḥꜥ.n",
        "14878": "SC.t.pass.gem.2pl_Aux.ꜥḥꜥ.n",
        "-14878": "SC.t.pass.gem.2du_Aux.ꜥḥꜥ.n",
        "14879": "SC.t.pass.gem.3pl_Aux.ꜥḥꜥ.n",
        "-14879": "SC.t.pass.gem.3du_Aux.ꜥḥꜥ.n",
        "14910": "SC.pass.ngem.impers_Aux.ꜥḥꜥ.n",
        "14940": "SC.w.pass.impers_Aux.ꜥḥꜥ.n",
        "15020": "SC.act.ngem.nom.subj_Aux.wn",
        "15021": "SC.act.ngem.1sg_Aux.wn",
        "15022": "SC.act.ngem.2sgm_Aux.wn",
        "15023": "SC.act.ngem.2sgf_Aux.wn",
        "15024": "SC.act.ngem.3sgm_Aux.wn",
        "15025": "SC.act.ngem.3sgf_Aux.wn",
        "15026": "SC.act.ngem.3sg_Aux.wn",
        "115026": "SC.act.ngem.3sg_Neg.n_Aux.wn",
        "15027": "SC.act.ngem.1pl_Aux.wn",
        "-15027": "SC.act.ngem.1du_Aux.wn",
        "15028": "SC.act.ngem.2pl_Aux.wn",
        "-15028": "SC.act.ngem.2du_Aux.wn",
        "15029": "SC.act.ngem.3pl_Aux.wn",
        "-15029": "SC.act.ngem.3du_Aux.wn",
        "15040": "SC.pass.ngem.nom.subj_Aux.wn",
        "15041": "SC.pass.ngem.1sg_Aux.wn",
        "15042": "SC.pass.ngem.2sgm_Aux.wn",
        "15043": "SC.pass.ngem.2sgf_Aux.wn",
        "15044": "SC.pass.ngem.3sgm_Aux.wn",
        "15045": "SC.pass.ngem.3sgf_Aux.wn",
        "15046": "SC.pass.ngem.3sg_Aux.wn",
        "15047": "SC.pass.ngem.1pl_Aux.wn",
        "-15047": "SC.pass.ngem.1du_Aux.wn",
        "15048": "SC.pass.ngem.2pl_Aux.wn",
        "-15048": "SC.pass.ngem.2du_Aux.wn",
        "15049": "SC.pass.ngem.3pl_Aux.wn",
        "-15049": "SC.pass.ngem.3du_Aux.wn",
        "15100": "SC.act.gem.nom.subj_Aux.wn",
        "15101": "SC.act.gem.1sg_Aux.wn",
        "15102": "SC.act.gem.2sgm_Aux.wn",
        "15103": "SC.act.gem.2sgf_Aux.wn",
        "15104": "SC.act.gem.3sgm_Aux.wn",
        "15105": "SC.act.gem.3sgf_Aux.wn",
        "15106": "SC.act.gem.3sg_Aux.wn",
        "15107": "SC.act.gem.1pl_Aux.wn",
        "-15107": "SC.act.gem.1du_Aux.wn",
        "15108": "SC.act.gem.2pl_Aux.wn",
        "-15108": "SC.act.gem.2du_Aux.wn",
        "15109": "SC.act.gem.3pl_Aux.wn",
        "-15109": "SC.act.gem.3du_Aux.wn",
        "15120": "SC.pass.gem(redupl).nom.subj_Aux.wn ",
        "15121": "SC.pass.gem(redupl).1sg_Aux.wn",
        "15122": "SC.pass.gem(redupl).2sgm_Aux.wn",
        "15123": "SC.pass.gem(redupl).2sgf_Aux.wn",
        "15124": "SC.pass.gem(redupl).3sgm_Aux.wn",
        "15125": "SC.pass.gem(redupl).3sgf_Aux.wn",
        "15126": "SC.pass.gem(redupl).3sg_Aux.wn",
        "15127": "SC.pass.gem(redupl).1pl_Aux.wn",
        "-15127": "SC.pass.gem(redupl).1du_Aux.wn",
        "15128": "SC.pass.gem(redupl).2pl_Aux.wn",
        "-15128": "SC.pass.gem(redupl).2du_Aux.wn",
        "15129": "SC.pass.gem(redupl).3pl_Aux.wn",
        "-15129": "SC.pass.gem(redupl).3du_Aux.wn",
        "15140": "SC.act.spec.nom.subj_Aux.wn",
        "15141": "SC.act.spec.1sg_Aux.wn",
        "15142": "SC.act.spec.2sgm_Aux.wn",
        "15143": "SC.act.spec.2sgf_Aux.wn",
        "15144": "SC.act.spec.3sgm_Aux.wn",
        "15145": "SC.act.spec.3sgf_Aux.wn",
        "15146": "SC.act.spec.3sg_Aux.wn",
        "15147": "SC.act.spec.1pl_Aux.wn",
        "-15147": "SC.act.spec.1du_Aux.wn",
        "15148": "SC.act.spec.2pl_Aux.wn",
        "-15148": "SC.act.spec.2du_Aux.wn",
        "15149": "SC.act.spec.3pl_Aux.wn",
        "-15149": "SC.act.spec.3du_Aux.wn",
        "15160": "SC.pass.spec.nom.subj_Aux.wn",
        "15161": "SC.pass.spec.1sg_Aux.wn",
        "15162": "SC.pass.spec.2sgm_Aux.wn",
        "15163": "SC.pass.spec.2sgf_Aux.wn",
        "15164": "SC.pass.spec.3sgm_Aux.wn",
        "15165": "SC.pass.spec.3sgf_Aux.wn",
        "15166": "SC.pass.spec.3sg_Aux.wn",
        "15167": "SC.pass.spec.1pl_Aux.wn",
        "-15167": "SC.pass.spec.1du_Aux.wn",
        "15168": "SC.pass.spec.2pl_Aux.wn",
        "-15168": "SC.pass.spec.2du_Aux.wn",
        "15169": "SC.pass.spec.3pl_Aux.wn",
        "-15169": "SC.pass.spec.3du_Aux.wn",
        "15170": "SC.tw.pass.spec.nom.subj_Aux.wn",
        "15171": "SC.tw.pass.spec.1sg_Aux.wn",
        "15172": "SC.tw.pass.spec.2sgm_Aux.wn",
        "15173": "SC.tw.pass.spec.2sgf_Aux.wn",
        "15174": "SC.tw.pass.spec.3sgm_Aux.wn",
        "15175": "SC.tw.pass.spec.3sgf_Aux.wn",
        "15176": "SC.tw.pass.spec.3sg_Aux.wn",
        "15177": "SC.tw.pass.spec.1pl_Aux.wn",
        "-15177": "SC.tw.pass.spec.1du_Aux.wn",
        "15178": "SC.tw.pass.spec.2pl_Aux.wn",
        "-15178": "SC.tw.pass.spec.2du_Aux.wn",
        "15179": "SC.tw.pass.spec.3pl_Aux.wn",
        "-15179": "SC.tw.pass.spec.3du_Aux.wn",
        "15180": "SC.w.act.ngem.nom.subj_Aux.wn",
        "15181": "SC.w.act.ngem.1sg_Aux.wn",
        "15182": "SC.w.act.ngem.2sgm_Aux.wn",
        "15183": "SC.w.act.ngem.2sgf_Aux.wn",
        "15184": "SC.w.act.ngem.3sgm_Aux.wn",
        "15185": "SC.w.act.ngem.3sgf_Aux.wn",
        "15186": "SC.w.act.ngem.3sg_Aux.wn",
        "15187": "SC.w.act.ngem.1pl_Aux.wn",
        "-15187": "SC.w.act.ngem.1du_Aux.wn",
        "15188": "SC.w.act.ngem.2pl_Aux.wn",
        "-15188": "SC.w.act.ngem.2du_Aux.wn",
        "15189": "SC.w.act.ngem.3pl_Aux.wn",
        "-15189": "SC.w.act.ngem.3du_Aux.wn",
        "15220": "SC.w.act.gem.nom.subj_Aux.wn",
        "15221": "SC.w.act.gem.1sg_Aux.wn",
        "15222": "SC.w.act.gem.2sgm_Aux.wn",
        "15223": "SC.w.act.gem.2sgf_Aux.wn",
        "15224": "SC.w.act.gem.3sgm_Aux.wn",
        "15225": "SC.w.act.gem.3sgf_Aux.wn",
        "15226": "SC.w.act.gem.3sg_Aux.wn",
        "15227": "SC.w.act.gem.1pl_Aux.wn",
        "-15227": "SC.w.act.gem.1du_Aux.wn",
        "15228": "SC.w.act.gem.2pl_Aux.wn",
        "-15228": "SC.w.act.gem.2du_Aux.wn",
        "15229": "SC.w.act.gem.3pl_Aux.wn",
        "-15229": "SC.w.act.gem.3du_Aux.wn",
        "15240": "SC.w.pass.ngem.nom.subj_Aux.wn",
        "15241": "SC.w.pass.ngem.1sg_Aux.wn",
        "15242": "SC.w.pass.ngem.2sgm_Aux.wn",
        "15243": "SC.w.pass.ngem.2sgf_Aux.wn",
        "15244": "SC.w.pass.ngem.3sgm_Aux.wn",
        "15245": "SC.w.pass.ngem.3sgf_Aux.wn",
        "15246": "SC.w.pass.ngem.3sg_Aux.wn",
        "15247": "SC.w.pass.ngem.1pl_Aux.wn",
        "-15247": "SC.w.pass.ngem.1du_Aux.wn",
        "15248": "SC.w.pass.ngem.2pl_Aux.wn",
        "-15248": "SC.w.pass.ngem.2du_Aux.wn",
        "15249": "SC.w.pass.ngem.3pl_Aux.wn",
        "-15249": "SC.w.pass.ngem.3du_Aux.wn",
        "15280": "SC.w.tw.pass.ngem.nom.subj_Aux.wn",
        "15281": "SC.w.tw.pass.ngem.1sg_Aux.wn",
        "15282": "SC.w.tw.pass.ngem.2sgm_Aux.wn",
        "15283": "SC.w.tw.pass.ngem.2sgf_Aux.wn",
        "15284": "SC.w.tw.pass.ngem.3sgm_Aux.wn",
        "15285": "SC.w.tw.pass.ngem.3sgf_Aux.wn",
        "15286": "SC.w.tw.pass.ngem.3sg_Aux.wn",
        "15287": "SC.w.tw.pass.ngem.1pl_Aux.wn",
        "-15287": "SC.w.tw.pass.ngem.1du_Aux.wn",
        "15288": "SC.w.tw.pass.ngem.2pl_Aux.wn",
        "-15288": "SC.w.tw.pass.ngem.2du_Aux.wn",
        "15289": "SC.w.tw.pass.ngem.3pl_Aux.wn",
        "-15289": "SC.w.tw.pass.ngem.3du_Aux.wn",
        "15320": "SC.tw.pass.ngem.nom.subj_Aux.wn",
        "15321": "SC.tw.pass.ngem.1sg_Aux.wn",
        "15322": "SC.tw.pass.ngem.2sgm_Aux.wn",
        "15323": "SC.tw.pass.ngem.2sgf_Aux.wn",
        "15324": "SC.tw.pass.ngem.3sgm_Aux.wn",
        "15325": "SC.tw.pass.ngem.3sgf_Aux.wn",
        "15326": "SC.tw.pass.ngem.3sg_Aux.wn",
        "15327": "SC.tw.pass.ngem.1pl_Aux.wn",
        "-15327": "SC.tw.pass.ngem.1du_Aux.wn",
        "15328": "SC.tw.pass.ngem.2pl_Aux.wn",
        "-15328": "SC.tw.pass.ngem.2du_Aux.wn",
        "15329": "SC.tw.pass.ngem.3pl_Aux.wn",
        "-15329": "SC.tw.pass.ngem.3du_Aux.wn",
        "15360": "SC.tw.pass.gem.nom.subj_Aux.wn",
        "15361": "SC.tw.pass.gem.1sg_Aux.wn",
        "15362": "SC.tw.pass.gem.2sgm_Aux.wn",
        "15363": "SC.tw.pass.gem.2sgf_Aux.wn",
        "15364": "SC.tw.pass.gem.3sgm_Aux.wn",
        "15365": "SC.tw.pass.gem.3sgf_Aux.wn",
        "15366": "SC.tw.pass.gem.3sg_Aux.wn",
        "15367": "SC.tw.pass.gem.1pl_Aux.wn",
        "-15367": "SC.tw.pass.gem.1du_Aux.wn",
        "15368": "SC.tw.pass.gem.2pl_Aux.wn",
        "-15368": "SC.tw.pass.gem.2du_Aux.wn",
        "15369": "SC.tw.pass.gem.3pl_Aux.wn",
        "-15369": "SC.tw.pass.gem.3du_Aux.wn",
        "15380": "SC.n.act.ngem.nom.subj_Aux.wn",
        "15381": "SC.n.act.ngem.1sg_Aux.wn",
        "15382": "SC.n.act.ngem.2sgm_Aux.wn",
        "15383": "SC.n.act.ngem.2sgf_Aux.wn",
        "15384": "SC.n.act.ngem.3sgm_Aux.wn",
        "15385": "SC.n.act.ngem.3sgf_Aux.wn",
        "15386": "SC.n.act.ngem.3sg_Aux.wn",
        "15387": "SC.n.act.ngem.1pl_Aux.wn",
        "-15387": "SC.n.act.ngem.1du_Aux.wn",
        "15388": "SC.n.act.ngem.2pl_Aux.wn",
        "-15388": "SC.n.act.ngem.2du_Aux.wn",
        "15389": "SC.n.act.ngem.3pl_Aux.wn",
        "-15389": "SC.n.act.ngem.3du_Aux.wn",
        "15420": "SC.n.act.gem.nom.subj_Aux.wn",
        "15421": "SC.n.act.gem.1sg_Aux.wn",
        "15422": "SC.n.act.gem.2sgm_Aux.wn",
        "15423": "SC.n.act.gem.2sgf_Aux.wn",
        "15424": "SC.n.act.gem.3sgm_Aux.wn",
        "15425": "SC.n.act.gem.3sgf_Aux.wn",
        "15426": "SC.n.act.gem.3sg_Aux.wn",
        "15427": "SC.n.act.gem.1pl_Aux.wn",
        "-15427": "SC.n.act.gem.1du_Aux.wn",
        "15428": "SC.n.act.gem.2pl_Aux.wn",
        "-15428": "SC.n.act.gem.2du_Aux.wn",
        "15429": "SC.n.act.gem.3pl_Aux.wn",
        "-15429": "SC.n.act.gem.3du_Aux.wn",
        "15430": "SC.n.pass.ngem.nom.subj_Aux.wn",
        "15431": "SC.n.pass.ngem.1sg_Aux.wn",
        "15432": "SC.n.pass.ngem.2sgm_Aux.wn",
        "15433": "SC.n.pass.ngem.sg2f_Aux.wn",
        "15434": "SC.n.pass.ngem.3sgm_Aux.wn",
        "15435": "SC.n.pass.ngem.3sgf_Aux.wn",
        "15436": "SC.n.pass.ngem.3sg_Aux.wn",
        "15437": "SC.n.pass.ngem.1pl_Aux.wn",
        "-15437": "SC.n.pass.ngem.1du_Aux.wn",
        "15438": "SC.n.pass.ngem.2pl_Aux.wn",
        "-15438": "SC.n.pass.ngem.2du_Aux.wn",
        "15439": "SC.n.pass.ngem.3pl_Aux.wn",
        "-15439": "SC.n.pass.ngem.3du_Aux.wn",
        "15440": "SC.n.tw.pass.ngem.nom.subj_Aux.wn",
        "15441": "SC.n.tw.pass.ngem.1sg_Aux.wn",
        "15442": "SC.n.tw.pass.ngem.2sgm_Aux.wn",
        "15443": "SC.n.tw.pass.ngem.2sgf_Aux.wn",
        "15444": "SC.n.tw.pass.ngem.3sgm_Aux.wn",
        "15445": "SC.n.tw.pass.ngem.3sgf_Aux.wn",
        "15446": "SC.n.tw.pass.ngem.3sg_Aux.wn",
        "15447": "SC.n.tw.pass.ngem.1pl_Aux.wn",
        "-15447": "SC.n.tw.pass.ngem.1du_Aux.wn",
        "15448": "SC.n.tw.pass.ngem.2pl_Aux.wn",
        "-15448": "SC.n.tw.pass.ngem.2du_Aux.wn",
        "15449": "SC.n.tw.pass.ngem.3pl_Aux.wn",
        "-15449": "SC.n.tw.pass.ngem.3du_Aux.wn",
        "15480": "SC.n.tw.pass.gem.nom.subj_Aux.wn",
        "15481": "SC.n.tw.pass.gem.1sg_Aux.wn",
        "15482": "SC.n.tw.pass.gem.2sgm_Aux.wn",
        "15483": "SC.n.tw.pass.gem.2sgf_Aux.wn",
        "15484": "SC.n.tw.pass.gem.3sgm_Aux.wn",
        "15485": "SC.n.tw.pass.gem.3sgf_Aux.wn",
        "15486": "SC.n.tw.pass.gem.3sg_Aux.wn",
        "15487": "SC.n.tw.pass.gem.1pl_Aux.wn",
        "-15487": "SC.n.tw.pass.gem.1du_Aux.wn",
        "15488": "SC.n.tw.pass.gem.2pl_Aux.wn",
        "-15488": "SC.n.tw.pass.gem.2du_Aux.wn",
        "15489": "SC.n.tw.pass.gem.3pl_Aux.wn",
        "-15489": "SC.n.tw.pass.gem.3du_Aux.wn",
        "15840": "SC.t.act.ngem.nom.subj_Aux.wn",
        "15841": "SC.t.act.ngem.1sg_Aux.wn",
        "15842": "SC.t.act.ngem.2sgm_Aux.wn",
        "15843": "SC.t.act.ngem.2sgf_Aux.wn",
        "15844": "SC.t.act.ngem.3sgm_Aux.wn",
        "15845": "SC.t.act.ngem.3sgf_Aux.wn",
        "15846": "SC.t.act.ngem.3sg_Aux.wn",
        "15847": "SC.t.act.ngem.1pl_Aux.wn",
        "-15847": "SC.t.act.ngem.1du_Aux.wn",
        "15848": "SC.t.act.ngem.2pl_Aux.wn",
        "-15848": "SC.t.act.ngem.2du_Aux.wn",
        "15849": "SC.t.act.ngem.3pl_Aux.wn",
        "-15849": "SC.t.act.ngem.3du_Aux.wn",
        "15850": "SC.t.act.gem.nom.subj_Aux.wn",
        "15851": "SC.t.act.gem.1sg_Aux.wn",
        "15852": "SC.t.act.gem.2sgm_Aux.wn",
        "15853": "SC.t.act.gem.2sgf_Aux.wn",
        "15854": "SC.t.act.gem.3sgm_Aux.wn",
        "15855": "SC.t.act.gem.3sgf_Aux.wn",
        "15856": "SC.t.act.gem.3sg_Aux.wn",
        "15857": "SC.t.act.gem.1pl_Aux.wn",
        "-15857": "SC.t.act.gem.1du_Aux.wn",
        "15858": "SC.t.act.gem.2pl_Aux.wn",
        "-15858": "SC.t.act.gem.2du_Aux.wn",
        "15859": "SC.t.act.gem.3pl_Aux.wn",
        "-15859": "SC.t.act.gem.3du_Aux.wn",
        "15860": "SC.t.pass.ngem.nom.subj_Aux.wn",
        "15861": "SC.t.pass.ngem.1sg_Aux.wn",
        "15862": "SC.t.pass.ngem.2sgm_Aux.wn",
        "15863": "SC.t.pass.ngem.2sgf_Aux.wn",
        "15864": "SC.t.pass.ngem.3sgm_Aux.wn",
        "15865": "SC.t.pass.ngem.3sgf_Aux.wn",
        "15866": "SC.t.pass.ngem.3sg_Aux.wn",
        "15867": "SC.t.pass.ngem.1pl_Aux.wn",
        "-15867": "SC.t.pass.ngem.1du_Aux.wn",
        "15868": "SC.t.pass.ngem.2pl_Aux.wn",
        "-15868": "SC.t.pass.ngem.2du_Aux.wn",
        "15869": "SC.t.pass.ngem.3pl_Aux.wn",
        "-15869": "SC.t.pass.ngem.3du_Aux.wn",
        "15870": "SC.t.pass.gem.nom.subj_Aux.wn",
        "15871": "SC.t.pass.gem.1sg_Aux.wn",
        "15872": "SC.t.pass.gem.2sgm_Aux.wn",
        "15873": "SC.t.pass.gem.2sgf_Aux.wn",
        "15874": "SC.t.pass.gem.3sgm_Aux.wn",
        "15875": "SC.t.pass.gem.3sgf_Aux.wn",
        "15876": "SC.t.pass.gem.3sg_Aux.wn",
        "15877": "SC.t.pass.gem.1pl_Aux.wn",
        "-15877": "SC.t.pass.gem.1du_Aux.wn",
        "15878": "SC.t.pass.gem.2pl_Aux.wn",
        "-15878": "SC.t.pass.gem.2du_Aux.wn",
        "15879": "SC.t.pass.gem.3pl_Aux.wn",
        "-15879": "SC.t.pass.gem.3du_Aux.wn",
        "15950": "SC.tw.pass.ngem.impers_Aux.wn",
        "16020": "SC.act.ngem.nom.subj_Aux.wn.jn",
        "16021": "SC.act.ngem.1sg_Aux.wn.jn",
        "16022": "SC.act.ngem.2sgm_Aux.wn.jn",
        "16023": "SC.act.ngem.2sgf_Aux.wn.jn",
        "16024": "SC.act.ngem.3sgm_Aux.wn.jn",
        "16025": "SC.act.ngem.3sgf_Aux.wn.jn",
        "16026": "SC.act.ngem.3sg_Aux.wn.jn",
        "16027": "SC.act.ngem.1pl_Aux.wn.jn",
        "-16027": "SC.act.ngem.1du_Aux.wn.jn",
        "16028": "SC.act.ngem.2pl_Aux.wn.jn",
        "-16028": "SC.act.ngem.2du_Aux.wn.jn",
        "16029": "SC.act.ngem.3pl_Aux.wn.jn",
        "-16029": "SC.act.ngem.3du_Aux.wn.jn",
        "16040": "SC.pass.ngem.nom.subj_Aux.wn.jn",
        "16041": "SC.pass.ngem.1sg_Aux.wn.jn",
        "16042": "SC.pass.ngem.2sgm_Aux.wn.jn",
        "16043": "SC.pass.ngem.2sgf_Aux.wn.jn",
        "16044": "SC.pass.ngem.3sgm_Aux.wn.jn",
        "16045": "SC.pass.ngem.3sgf_Aux.wn.jn",
        "16046": "SC.pass.ngem.3sg_Aux.wn.jn",
        "16047": "SC.pass.ngem.1pl_Aux.wn.jn",
        "-16047": "SC.pass.ngem.1du_Aux.wn.jn",
        "16048": "SC.pass.ngem.2pl_Aux.wn.jn",
        "-16048": "SC.pass.ngem.2du_Aux.wn.jn",
        "16049": "SC.pass.ngem.3pl_Aux.wn.jn",
        "-16049": "SC.pass.ngem.3du_Aux.wn.jn",
        "16100": "SC.act.gem.nom.subj_Aux.wn.jn",
        "16101": "SC.act.gem.1sg_Aux.wn.jn",
        "16102": "SC.act.gem.2sgm_Aux.wn.jn",
        "16103": "SC.act.gem.2sgf_Aux.wn.jn",
        "16104": "SC.act.gem.3sgm_Aux.wn.jn",
        "16105": "SC.act.gem.3sgf_Aux.wn.jn",
        "16106": "SC.act.gem.3sg_Aux.wn.jn",
        "16107": "SC.act.gem.1pl_Aux.wn.jn",
        "-16107": "SC.act.gem.1du_Aux.wn.jn",
        "16108": "SC.act.gem.2pl_Aux.wn.jn",
        "-16108": "SC.act.gem.2du_Aux.wn.jn",
        "16109": "SC.act.gem.3pl_Aux.wn.jn",
        "-16109": "SC.act.gem.3du_Aux.wn.jn",
        "16120": "SC.pass.gem(redupl).nom.subj_Aux.wn.jn",
        "16121": "SC.pass.gem(redupl).1sg_Aux.wn.jn",
        "16122": "SC.pass.gem(redupl).2sgm_Aux.wn.jn",
        "16123": "SC.pass.gem(redupl).2sgf_Aux.wn.jn",
        "16124": "SC.pass.gem(redupl).3sgm_Aux.wn.jn",
        "16125": "SC.pass.gem(redupl).3sgf_Aux.wn.jn",
        "16126": "SC.pass.gem(redupl).3sg_Aux.wn.jn",
        "16127": "SC.pass.gem(redupl).1pl_Aux.wn.jn",
        "-16127": "SC.pass.gem(redupl).1du_Aux.wn.jn",
        "16128": "SC.pass.gem(redupl).2pl_Aux.wn.jn",
        "-16128": "SC.pass.gem(redupl).2du_Aux.wn.jn",
        "16129": "SC.pass.gem(redupl).3pl_Aux.wn.jn",
        "-16129": "SC.pass.gem(redupl).3du_Aux.wn.jn",
        "16140": "SC.act.spec.nom.subj_Aux.wn.jn",
        "16141": "SC.act.spec.1sg_Aux.wn.jn",
        "16142": "SC.act.spec.2sgm_Aux.wn.jn",
        "16143": "SC.act.spec.2sgf_Aux.wn.jn",
        "16144": "SC.act.spec.3sgm_Aux.wn.jn",
        "16145": "SC.act.spec.3sgf_Aux.wn.jn",
        "16146": "SC.act.spec.3sg_Aux.wn.jn",
        "16147": "SC.act.spec.1pl_Aux.wn.jn",
        "-16147": "SC.act.spec.1du_Aux.wn.jn",
        "16148": "SC.act.spec.2pl_Aux.wn.jn",
        "-16148": "SC.act.spec.2du_Aux.wn.jn",
        "16149": "SC.act.spec.3pl_Aux.wn.jn",
        "-16149": "SC.act.spec.3du_Aux.wn.jn",
        "16160": "SC.pass.spec.nom.subj_Aux.wn.jn",
        "16161": "SC.pass.spec.1sg_Aux.wn.jn",
        "16162": "SC.pass.spec.2sgm_Aux.wn.jn",
        "16163": "SC.pass.spec.2sgf_Aux.wn.jn",
        "16164": "SC.pass.spec.3sgm_Aux.wn.jn",
        "16165": "SC.pass.spec.3sgf_Aux.wn.jn",
        "16166": "SC.pass.spec.3sg_Aux.wn.jn",
        "16167": "SC.pass.spec.1pl_Aux.wn.jn",
        "-16167": "SC.pass.spec.1du_Aux.wn.jn",
        "16168": "SC.pass.spec.2pl_Aux.wn.jn",
        "-16168": "SC.pass.spec.2du_Aux.wn.jn",
        "16169": "SC.pass.spec.3pl_Aux.wn.jn",
        "-16169": "SC.pass.spec.3du_Aux.wn.jn",
        "16170": "SC.tw.pass.spec.nom.subj_Aux.wn.jn",
        "16171": "SC.tw.pass.spec.1sg_Aux.wn.jn",
        "16172": "SC.tw.pass.spec.2sgm_Aux.wn.jn",
        "16173": "SC.tw.pass.spec.2sgf_Aux.wn.jn",
        "16174": "SC.tw.pass.spec.3sgm_Aux.wn.jn",
        "16175": "SC.tw.pass.spec.3sgf_Aux.wn.jn",
        "16176": "SC.tw.pass.spec.3sg_Aux.wn.jn",
        "16177": "SC.tw.pass.spec.1pl_Aux.wn.jn",
        "-16177": "SC.tw.pass.spec.1du_Aux.wn.jn",
        "16178": "SC.tw.pass.spec.2pl_Aux.wn.jn",
        "-16178": "SC.tw.pass.spec.2du_Aux.wn.jn",
        "16179": "SC.tw.pass.spec.3pl_Aux.wn.jn",
        "-16179": "SC.tw.pass.spec.3du_Aux.wn.jn",
        "16180": "SC.w.act.ngem.nom.subj_Aux.wn.jn",
        "16181": "SC.w.act.ngem.1sg_Aux.wn.jn",
        "16182": "SC.w.act.ngem.2sgm_Aux.wn.jn",
        "16183": "SC.w.act.ngem.2sgf_Aux.wn.jn",
        "16184": "SC.w.act.ngem.3sgm_Aux.wn.jn",
        "16185": "SC.w.act.ngem.3sgf_Aux.wn.jn",
        "16186": "SC.w.act.ngem.3sg_Aux.wn.jn",
        "16187": "SC.w.act.ngem.1pl_Aux.wn.jn",
        "-16187": "SC.w.act.ngem.1du_Aux.wn.jn",
        "16188": "SC.w.act.ngem.2pl_Aux.wn.jn",
        "-16188": "SC.w.act.ngem.2du_Aux.wn.jn",
        "16189": "SC.w.act.ngem.3pl_Aux.wn.jn",
        "-16189": "SC.w.act.ngem.3du_Aux.wn.jn",
        "16220": "SC.w.act.gem.nom.subj_Aux.wn.jn",
        "16221": "SC.w.act.gem.1sg_Aux.wn.jn",
        "16222": "SC.w.act.gem.2sgm_Aux.wn.jn",
        "16223": "SC.w.act.gem.2sgf_Aux.wn.jn",
        "16224": "SC.w.act.gem.3sgm_Aux.wn.jn",
        "16225": "SC.w.act.gem.3sgf_Aux.wn.jn",
        "16226": "SC.w.act.gem.3sg_Aux.wn.jn",
        "16227": "SC.w.act.gem.1pl_Aux.wn.jn",
        "-16227": "SC.w.act.gem.1du_Aux.wn.jn",
        "16228": "SC.w.act.gem.2pl_Aux.wn.jn",
        "-16228": "SC.w.act.gem.2du_Aux.wn.jn",
        "16229": "SC.w.act.gem.3pl_Aux.wn.jn",
        "-16229": "SC.w.act.gem.3du_Aux.wn.jn",
        "16240": "SC.w.pass.ngem.nom.subj_Aux.wn.jn",
        "16241": "SC.w.pass.ngem.1sg_Aux.wn.jn",
        "16242": "SC.w.pass.ngem.2sgm_Aux.wn.jn",
        "16243": "SC.w.pass.ngem.2sgf_Aux.wn.jn",
        "16244": "SC.w.pass.ngem.3sgm_Aux.wn.jn",
        "16245": "SC.w.pass.ngem.3sgf_Aux.wn.jn",
        "16246": "SC.w.pass.ngem.3sg_Aux.wn.jn",
        "16247": "SC.w.pass.ngem.1pl_Aux.wn.jn",
        "-16247": "SC.w.pass.ngem.1du_Aux.wn.jn",
        "16248": "SC.w.pass.ngem.2pl_Aux.wn.jn",
        "-16248": "SC.w.pass.ngem.2du_Aux.wn.jn",
        "16249": "SC.w.pass.ngem.3pl_Aux.wn.jn",
        "-16249": "SC.w.pass.ngem.3du_Aux.wn.jn",
        "16280": "SC.w.tw.pass.ngem.nom.subj_Aux.wn.jn",
        "16281": "SC.w.tw.pass.ngem.1sg_Aux.wn.jn",
        "16282": "SC.w.tw.pass.ngem.2sgm_Aux.wn.jn",
        "16283": "SC.w.tw.pass.ngem.2sgf_Aux.wn.jn",
        "16284": "SC.w.tw.pass.ngem.3sgm_Aux.wn.jn",
        "16285": "SC.w.tw.pass.ngem.3sgf_Aux.wn.jn",
        "16286": "SC.w.tw.pass.ngem.3sg_Aux.wn.jn",
        "16287": "SC.w.tw.pass.ngem.1pl_Aux.wn.jn",
        "-16287": "SC.w.tw.pass.ngem.1du_Aux.wn.jn",
        "16288": "SC.w.tw.pass.ngem.2pl_Aux.wn.jn",
        "-16288": "SC.w.tw.pass.ngem.2du_Aux.wn.jn",
        "16289": "SC.w.tw.pass.ngem.3pl_Aux.wn.jn",
        "-16289": "SC.w.tw.pass.ngem.3du_Aux.wn.jn",
        "16320": "SC.tw.pass.ngem.nom.subj_Aux.wn.jn",
        "16321": "SC.tw.pass.ngem.1sg_Aux.wn.jn",
        "16322": "SC.tw.pass.ngem.2sgm_Aux.wn.jn",
        "16323": "SC.tw.pass.ngem.2sgf_Aux.wn.jn",
        "16324": "SC.tw.pass.ngem.3sgm_Aux.wn.jn",
        "16325": "SC.tw.pass.ngem.3sgf_Aux.wn.jn",
        "16326": "SC.tw.pass.ngem.3sg_Aux.wn.jn",
        "16327": "SC.tw.pass.ngem.1pl_Aux.wn.jn",
        "-16327": "SC.tw.pass.ngem.1du_Aux.wn.jn",
        "16328": "SC.tw.pass.ngem.2pl_Aux.wn.jn",
        "-16328": "SC.tw.pass.ngem.2du_Aux.wn.jn",
        "16329": "SC.tw.pass.ngem.3pl_Aux.wn.jn",
        "-16329": "SC.tw.pass.ngem.3du_Aux.wn.jn",
        "16360": "SC.tw.pass.gem.nom.subj_Aux.wn.jn",
        "16361": "SC.tw.pass.gem.1sg_Aux.wn.jn",
        "16362": "SC.tw.pass.gem.2sgm_Aux.wn.jn",
        "16363": "SC.tw.pass.gem.2sgf_Aux.wn.jn",
        "16364": "SC.tw.pass.gem.3sgm_Aux.wn.jn",
        "16365": "SC.tw.pass.gem.3sgf_Aux.wn.jn",
        "16366": "SC.tw.pass.gem.3sg_Aux.wn.jn",
        "16367": "SC.tw.pass.gem.1pl_Aux.wn.jn",
        "-16367": "SC.tw.pass.gem.1du_Aux.wn.jn",
        "16368": "SC.tw.pass.gem.2pl_Aux.wn.jn",
        "-16368": "SC.tw.pass.gem.2du_Aux.wn.jn",
        "16369": "SC.tw.pass.gem.3pl_Aux.wn.jn",
        "-16369": "SC.tw.pass.gem.3du_Aux.wn.jn",
        "16380": "SC.n.act.ngem.nom.subj_Aux.wn.jn",
        "16381": "SC.n.act.ngem.1sg_Aux.wn.jn",
        "16382": "SC.n.act.ngem.2sgm_Aux.wn.jn",
        "16383": "SC.n.act.ngem.2sgf_Aux.wn.jn",
        "16384": "SC.n.act.ngem.3sgm_Aux.wn.jn",
        "16385": "SC.n.act.ngem.3sgf_Aux.wn.jn",
        "16386": "SC.n.act.ngem.3sg_Aux.wn.jn",
        "16387": "SC.n.act.ngem.1pl_Aux.wn.jn",
        "-16387": "SC.n.act.ngem.1du_Aux.wn.jn",
        "16388": "SC.n.act.ngem.2pl_Aux.wn.jn",
        "-16388": "SC.n.act.ngem.2du_Aux.wn.jn",
        "16389": "SC.n.act.ngem.3pl_Aux.wn.jn",
        "-16389": "SC.n.act.ngem.3du_Aux.wn.jn",
        "16420": "SC.n.act.gem.nom.subj_Aux.wn.jn",
        "16421": "SC.n.act.gem.1sg_Aux.wn.jn",
        "16422": "SC.n.act.gem.2sgm_Aux.wn.jn",
        "16423": "SC.n.act.gem.2sgf_Aux.wn.jn",
        "16424": "SC.n.act.gem.3sgm_Aux.wn.jn",
        "16425": "SC.n.act.gem.3sgf_Aux.wn.jn",
        "16426": "SC.n.act.gem.3sg_Aux.wn.jn",
        "16427": "SC.n.act.gem.1pl_Aux.wn.jn",
        "-16427": "SC.n.act.gem.1du_Aux.wn.jn",
        "16428": "SC.n.act.gem.2pl_Aux.wn.jn",
        "-16428": "SC.n.act.gem.2du_Aux.wn.jn",
        "16429": "SC.n.act.gem.3pl_Aux.wn.jn",
        "-16429": "SC.n.act.gem.3du_Aux.wn.jn",
        "16430": "SC.n.pass.ngem.nom.subj_Aux.wn.jn",
        "16431": "SC.n.pass.ngem.1sg_Aux.wn.jn",
        "16432": "SC.n.pass.ngem.2sgm_Aux.wn.jn",
        "16433": "SC.n.pass.ngem.sg2f_Aux.wn.jn",
        "16434": "SC.n.pass.ngem.3sgm_Aux.wn.jn",
        "16435": "SC.n.pass.ngem.3sgf_Aux.wn.jn",
        "16436": "SC.n.pass.ngem.3sg_Aux.wn.jn",
        "16437": "SC.n.pass.ngem.1pl_Aux.wn.jn",
        "-16437": "SC.n.pass.ngem.1du_Aux.wn.jn",
        "16438": "SC.n.pass.ngem.2pl_Aux.wn.jn",
        "-16438": "SC.n.pass.ngem.2du_Aux.wn.jn",
        "16439": "SC.n.pass.ngem.3pl_Aux.wn.jn",
        "-16439": "SC.n.pass.ngem.3du_Aux.wn.jn",
        "16440": "SC.n.tw.pass.ngem.nom.subj_Aux.wn.jn",
        "16441": "SC.n.tw.pass.ngem.1sg_Aux.wn.jn",
        "16442": "SC.n.tw.pass.ngem.2sgm_Aux.wn.jn",
        "16443": "SC.n.tw.pass.ngem.2sgf_Aux.wn.jn",
        "16444": "SC.n.tw.pass.ngem.3sgm_Aux.wn.jn",
        "16445": "SC.n.tw.pass.ngem.3sgf_Aux.wn.jn",
        "16446": "SC.n.tw.pass.ngem.3sg_Aux.wn.jn",
        "16447": "SC.n.tw.pass.ngem.1pl_Aux.wn.jn",
        "-16447": "SC.n.tw.pass.ngem.1du_Aux.wn.jn",
        "16448": "SC.n.tw.pass.ngem.2pl_Aux.wn.jn",
        "-16448": "SC.n.tw.pass.ngem.2du_Aux.wn.jn",
        "16449": "SC.n.tw.pass.ngem.3pl_Aux.wn.jn",
        "-16449": "SC.n.tw.pass.ngem.3du_Aux.wn.jn",
        "16480": "SC.n.tw.pass.gem.nom.subj_Aux.wn.jn",
        "16481": "SC.n.tw.pass.gem.1sg_Aux.wn.jn",
        "16482": "SC.n.tw.pass.gem.2sgm_Aux.wn.jn",
        "16483": "SC.n.tw.pass.gem.2sgf_Aux.wn.jn",
        "16484": "SC.n.tw.pass.gem.3sgm_Aux.wn.jn",
        "16485": "SC.n.tw.pass.gem.3sgf_Aux.wn.jn",
        "16486": "SC.n.tw.pass.gem.3sg_Aux.wn.jn",
        "16487": "SC.n.tw.pass.gem.1pl_Aux.wn.jn",
        "-16487": "SC.n.tw.pass.gem.1du_Aux.wn.jn",
        "16488": "SC.n.tw.pass.gem.2pl_Aux.wn.jn",
        "-16488": "SC.n.tw.pass.gem.2du_Aux.wn.jn",
        "16489": "SC.n.tw.pass.gem.3pl_Aux.wn.jn",
        "-16489": "SC.n.tw.pass.gem.3du_Aux.wn.jn",
        "16840": "SC.t.act.ngem.nom.subj_Aux.wn.jn",
        "16841": "SC.t.act.ngem.1sg_Aux.wn.jn",
        "16842": "SC.t.act.ngem.2sgm_Aux.wn.jn",
        "16843": "SC.t.act.ngem.2sgf_Aux.wn.jn",
        "16844": "SC.t.act.ngem.3sgm_Aux.wn.jn",
        "16845": "SC.t.act.ngem.3sgf_Aux.wn.jn",
        "16846": "SC.t.act.ngem.3sg_Aux.wn.jn",
        "16847": "SC.t.act.ngem.1pl_Aux.wn.jn",
        "-16847": "SC.t.act.ngem.1du_Aux.wn.jn",
        "16848": "SC.t.act.ngem.2pl_Aux.wn.jn",
        "-16848": "SC.t.act.ngem.2du_Aux.wn.jn",
        "16849": "SC.t.act.ngem.3pl_Aux.wn.jn",
        "-16849": "SC.t.act.ngem.3du_Aux.wn.jn",
        "16850": "SC.t.act.gem.nom.subj_Aux.wn.jn",
        "16851": "SC.t.act.gem.1sg_Aux.wn.jn",
        "16852": "SC.t.act.gem.2sgm_Aux.wn.jn",
        "16853": "SC.t.act.gem.2sgf_Aux.wn.jn",
        "16854": "SC.t.act.gem.3sgm_Aux.wn.jn",
        "16855": "SC.t.act.gem.3sgf_Aux.wn.jn",
        "16856": "SC.t.act.gem.3sg_Aux.wn.jn",
        "16857": "SC.t.act.gem.1pl_Aux.wn.jn",
        "-16857": "SC.t.act.gem.1du_Aux.wn.jn",
        "16858": "SC.t.act.gem.2pl_Aux.wn.jn",
        "-16858": "SC.t.act.gem.2du_Aux.wn.jn",
        "16859": "SC.t.act.gem.3pl_Aux.wn.jn",
        "-16859": "SC.t.act.gem.3du_Aux.wn.jn",
        "16860": "SC.t.pass.ngem.nom.subj_Aux.wn.jn",
        "16861": "SC.t.pass.ngem.1sg_Aux.wn.jn",
        "16862": "SC.t.pass.ngem.2sgm_Aux.wn.jn",
        "16863": "SC.t.pass.ngem.2sgf_Aux.wn.jn",
        "16864": "SC.t.pass.ngem.3sgm_Aux.wn.jn",
        "16865": "SC.t.pass.ngem.3sgf_Aux.wn.jn",
        "16866": "SC.t.pass.ngem.3sg_Aux.wn.jn",
        "16867": "SC.t.pass.ngem.1pl_Aux.wn.jn",
        "-16867": "SC.t.pass.ngem.1du_Aux.wn.jn",
        "16868": "SC.t.pass.ngem.2pl_Aux.wn.jn",
        "-16868": "SC.t.pass.ngem.2du_Aux.wn.jn",
        "16869": "SC.t.pass.ngem.3pl_Aux.wn.jn",
        "-16869": "SC.t.pass.ngem.3du_Aux.wn.jn",
        "16870": "SC.t.pass.gem.nom.subj_Aux.wn.jn",
        "16871": "SC.t.pass.gem.1sg_Aux.wn.jn",
        "16872": "SC.t.pass.gem.2sgm_Aux.wn.jn",
        "16873": "SC.t.pass.gem.2sgf_Aux.wn.jn",
        "16874": "SC.t.pass.gem.3sgm_Aux.wn.jn",
        "16875": "SC.t.pass.gem.3sgf_Aux.wn.jn",
        "16876": "SC.t.pass.gem.3sg_Aux.wn.jn",
        "16877": "SC.t.pass.gem.1pl_Aux.wn.jn",
        "-16877": "SC.t.pass.gem.1du_Aux.wn.jn",
        "16878": "SC.t.pass.gem.2pl_Aux.wn.jn",
        "-16878": "SC.t.pass.gem.2du_Aux.wn.jn",
        "16879": "SC.t.pass.gem.3pl_Aux.wn.jn",
        "-16879": "SC.t.pass.gem.3du_Aux.wn.jn",
        "17020": "SC.act.ngem.nom.subj_Aux.wn.ḫr",
        "17021": "SC.act.ngem.1sg_Aux.wn.ḫr",
        "17022": "SC.act.ngem.2sgm_Aux.wn.ḫr",
        "17023": "SC.act.ngem.2sgf_Aux.wn.ḫr",
        "17024": "SC.act.ngem.3sgm_Aux.wn.ḫr",
        "17025": "SC.act.ngem.3sgf_Aux.wn.ḫr",
        "17026": "SC.act.ngem.3sg_Aux.wn.ḫr",
        "17027": "SC.act.ngem.1pl_Aux.wn.ḫr",
        "-17027": "SC.act.ngem.1du_Aux.wn.ḫr",
        "17028": "SC.act.ngem.2pl_Aux.wn.ḫr",
        "-17028": "SC.act.ngem.2du_Aux.wn.ḫr",
        "17029": "SC.act.ngem.3pl_Aux.wn.ḫr",
        "-17029": "SC.act.ngem.3du_Aux.wn.ḫr",
        "17040": "SC.pass.ngem.nom.subj_Aux.wn.ḫr",
        "17041": "SC.pass.ngem.1sg_Aux.wn.ḫr",
        "17042": "SC.pass.ngem.2sgm_Aux.wn.ḫr",
        "17043": "SC.pass.ngem.2sgf_Aux.wn.ḫr",
        "17044": "SC.pass.ngem.3sgm_Aux.wn.ḫr",
        "17045": "SC.pass.ngem.3sgf_Aux.wn.ḫr",
        "17046": "SC.pass.ngem.3sg_Aux.wn.ḫr",
        "17047": "SC.pass.ngem.1pl_Aux.wn.ḫr",
        "-17047": "SC.pass.ngem.1du_Aux.wn.ḫr",
        "17048": "SC.pass.ngem.2pl_Aux.wn.ḫr",
        "-17048": "SC.pass.ngem.2du_Aux.wn.ḫr",
        "17049": "SC.pass.ngem.3pl_Aux.wn.ḫr",
        "-17049": "SC.pass.ngem.3du_Aux.wn.ḫr",
        "17100": "SC.act.gem.nom.subj_Aux.wn.ḫr",
        "17101": "SC.act.gem.1sg_Aux.wn.ḫr",
        "17102": "SC.act.gem.2sgm_Aux.wn.ḫr",
        "17103": "SC.act.gem.2sgf_Aux.wn.ḫr",
        "17104": "SC.act.gem.3sgm_Aux.wn.ḫr",
        "17105": "SC.act.gem.3sgf_Aux.wn.ḫr",
        "17106": "SC.act.gem.3sg_Aux.wn.ḫr",
        "17107": "SC.act.gem.1pl_Aux.wn.ḫr",
        "-17107": "SC.act.gem.1du_Aux.wn.ḫr",
        "17108": "SC.act.gem.2pl_Aux.wn.ḫr",
        "-17108": "SC.act.gem.2du_Aux.wn.ḫr",
        "17109": "SC.act.gem.3pl_Aux.wn.ḫr",
        "-17109": "SC.act.gem.3du_Aux.wn.ḫr",
        "17120": "SC.pass.gem(redupl).nom.subj_Aux.wn.ḫr",
        "17121": "SC.pass.gem(redupl).1sg_Aux.wn.ḫr",
        "17122": "SC.pass.gem(redupl).2sgm_Aux.wn.ḫr",
        "17123": "SC.pass.gem(redupl).2sgf_Aux.wn.ḫr",
        "17124": "SC.pass.gem(redupl).3sgm_Aux.wn.ḫr",
        "17125": "SC.pass.gem(redupl).3sgf_Aux.wn.ḫr",
        "17126": "SC.pass.gem(redupl).3sg_Aux.wn.ḫr",
        "17127": "SC.pass.gem(redupl).1pl_Aux.wn.ḫr",
        "-17127": "SC.pass.gem(redupl).1du_Aux.wn.ḫr",
        "17128": "SC.pass.gem(redupl).2pl_Aux.wn.ḫr",
        "-17128": "SC.pass.gem(redupl).2du_Aux.wn.ḫr",
        "17129": "SC.pass.gem(redupl).3pl_Aux.wn.ḫr",
        "-17129": "SC.pass.gem(redupl).3du_Aux.wn.ḫr",
        "17140": "SC.act.spec.nom.subj_Aux.wn.ḫr",
        "17141": "SC.act.spec.1sg_Aux.wn.ḫr",
        "17142": "SC.act.spec.2sgm_Aux.wn.ḫr",
        "17143": "SC.act.spec.2sgf_Aux.wn.ḫr",
        "17144": "SC.act.spec.3sgm_Aux.wn.ḫr",
        "17145": "SC.act.spec.3sgf_Aux.wn.ḫr",
        "17146": "SC.act.spec.3sg_Aux.wn.ḫr",
        "17147": "SC.act.spec.1pl_Aux.wn.ḫr",
        "-17147": "SC.act.spec.1du_Aux.wn.ḫr",
        "17148": "SC.act.spec.2pl_Aux.wn.ḫr",
        "-17148": "SC.act.spec.2du_Aux.wn.ḫr",
        "17149": "SC.act.spec.3pl_Aux.wn.ḫr",
        "-17149": "SC.act.spec.3du_Aux.wn.ḫr",
        "17160": "SC.pass.spec.nom.subj_Aux.wn.ḫr",
        "17161": "SC.pass.spec.1sg_Aux.wn.ḫr",
        "17162": "SC.pass.spec.2sgm_Aux.wn.ḫr",
        "17163": "SC.pass.spec.2sgf_Aux.wn.ḫr",
        "17164": "SC.pass.spec.3sgm_Aux.wn.ḫr",
        "17165": "SC.pass.spec.3sgf_Aux.wn.ḫr",
        "17166": "SC.pass.spec.3sg_Aux.wn.ḫr",
        "17167": "SC.pass.spec.1pl_Aux.wn.ḫr",
        "-17167": "SC.pass.spec.1du_Aux.wn.ḫr",
        "17168": "SC.pass.spec.2pl_Aux.wn.ḫr",
        "-17168": "SC.pass.spec.2du_Aux.wn.ḫr",
        "17169": "SC.pass.spec.3pl_Aux.wn.ḫr",
        "-17169": "SC.pass.spec.3du_Aux.wn.ḫr",
        "17170": "SC.tw.pass.spec.nom.subj_Aux.wn.ḫr",
        "17171": "SC.tw.pass.spec.1sg_Aux.wn.ḫr",
        "17172": "SC.tw.pass.spec.2sgm_Aux.wn.ḫr",
        "17173": "SC.tw.pass.spec.2sgf_Aux.wn.ḫr",
        "17174": "SC.tw.pass.spec.3sgm_Aux.wn.ḫr",
        "17175": "SC.tw.pass.spec.3sgf_Aux.wn.ḫr",
        "17176": "SC.tw.pass.spec.3sg_Aux.wn.ḫr",
        "17177": "SC.tw.pass.spec.1pl_Aux.wn.ḫr",
        "-17177": "SC.tw.pass.spec.1du_Aux.wn.ḫr",
        "17178": "SC.tw.pass.spec.2pl_Aux.wn.ḫr",
        "-17178": "SC.tw.pass.spec.2du_Aux.wn.ḫr",
        "17179": "SC.tw.pass.spec.3pl_Aux.wn.ḫr",
        "-17179": "SC.tw.pass.spec.3du_Aux.wn.ḫr",
        "17180": "SC.w.act.ngem.nom.subj_Aux.wn.ḫr",
        "17181": "SC.w.act.ngem.1sg_Aux.wn.ḫr",
        "17182": "SC.w.act.ngem.2sgm_Aux.wn.ḫr",
        "17183": "SC.w.act.ngem.2sgf_Aux.wn.ḫr",
        "17184": "SC.w.act.ngem.3sgm_Aux.wn.ḫr",
        "17185": "SC.w.act.ngem.3sgf_Aux.wn.ḫr",
        "17186": "SC.w.act.ngem.3sg_Aux.wn.ḫr",
        "17187": "SC.w.act.ngem.1pl_Aux.wn.ḫr",
        "-17187": "SC.w.act.ngem.1du_Aux.wn.ḫr",
        "17188": "SC.w.act.ngem.2pl_Aux.wn.ḫr",
        "-17188": "SC.w.act.ngem.2du_Aux.wn.ḫr",
        "17189": "SC.w.act.ngem.3pl_Aux.wn.ḫr",
        "-17189": "SC.w.act.ngem.3du_Aux.wn.ḫr",
        "17220": "SC.w.act.gem.nom.subj_Aux.wn.ḫr",
        "17221": "SC.w.act.gem.1sg_Aux.wn.ḫr",
        "17222": "SC.w.act.gem.2sgm_Aux.wn.ḫr",
        "17223": "SC.w.act.gem.2sgf_Aux.wn.ḫr",
        "17224": "SC.w.act.gem.3sgm_Aux.wn.ḫr",
        "17225": "SC.w.act.gem.3sgf_Aux.wn.ḫr",
        "17226": "SC.w.act.gem.3sg_Aux.wn.ḫr",
        "17227": "SC.w.act.gem.1pl_Aux.wn.ḫr",
        "-17227": "SC.w.act.gem.1du_Aux.wn.ḫr",
        "17228": "SC.w.act.gem.2pl_Aux.wn.ḫr",
        "-17228": "SC.w.act.gem.2du_Aux.wn.ḫr",
        "17229": "SC.w.act.gem.3pl_Aux.wn.ḫr",
        "-17229": "SC.w.act.gem.3du_Aux.wn.ḫr",
        "17240": "SC.w.pass.ngem.nom.subj_Aux.wn.ḫr",
        "17241": "SC.w.pass.ngem.1sg_Aux.wn.ḫr",
        "17242": "SC.w.pass.ngem.2sgm_Aux.wn.ḫr",
        "17243": "SC.w.pass.ngem.2sgf_Aux.wn.ḫr",
        "17244": "SC.w.pass.ngem.3sgm_Aux.wn.ḫr",
        "17245": "SC.w.pass.ngem.3sgf_Aux.wn.ḫr",
        "17246": "SC.w.pass.ngem.3sg_Aux.wn.ḫr",
        "17247": "SC.w.pass.ngem.1pl_Aux.wn.ḫr",
        "-17247": "SC.w.pass.ngem.1du_Aux.wn.ḫr",
        "17248": "SC.w.pass.ngem.2pl_Aux.wn.ḫr",
        "-17248": "SC.w.pass.ngem.2du_Aux.wn.ḫr",
        "17249": "SC.w.pass.ngem.3pl_Aux.wn.ḫr",
        "-17249": "SC.w.pass.ngem.3du_Aux.wn.ḫr",
        "17280": "SC.w.tw.pass.ngem.nom.subj_Aux.wn.ḫr",
        "17281": "SC.w.tw.pass.ngem.1sg_Aux.wn.ḫr",
        "17282": "SC.w.tw.pass.ngem.2sgm_Aux.wn.ḫr",
        "17283": "SC.w.tw.pass.ngem.2sgf_Aux.wn.ḫr",
        "17284": "SC.w.tw.pass.ngem.3sgm_Aux.wn.ḫr",
        "17285": "SC.w.tw.pass.ngem.3sgf_Aux.wn.ḫr",
        "17286": "SC.w.tw.pass.ngem.3sg_Aux.wn.ḫr",
        "17287": "SC.w.tw.pass.ngem.1pl_Aux.wn.ḫr",
        "-17287": "SC.w.tw.pass.ngem.1du_Aux.wn.ḫr",
        "17288": "SC.w.tw.pass.ngem.2pl_Aux.wn.ḫr",
        "-17288": "SC.w.tw.pass.ngem.2du_Aux.wn.ḫr",
        "17289": "SC.w.tw.pass.ngem.3pl_Aux.wn.ḫr",
        "-17289": "SC.w.tw.pass.ngem.3du_Aux.wn.ḫr",
        "17320": "SC.tw.pass.ngem.nom.subj_Aux.wn.ḫr",
        "17321": "SC.tw.pass.ngem.1sg_Aux.wn.ḫr",
        "17322": "SC.tw.pass.ngem.2sgm_Aux.wn.ḫr",
        "17323": "SC.tw.pass.ngem.2sgf_Aux.wn.ḫr",
        "17324": "SC.tw.pass.ngem.3sgm_Aux.wn.ḫr",
        "17325": "SC.tw.pass.ngem.3sgf_Aux.wn.ḫr",
        "17326": "SC.tw.pass.ngem.3sg.wn.ḫr",
        "17327": "SC.tw.pass.ngem.1pl_Aux.wn.ḫr",
        "-17327": "SC.tw.pass.ngem.1du_Aux.wn.ḫr",
        "17328": "SC.tw.pass.ngem.2pl_Aux.wn.ḫr",
        "-17328": "SC.tw.pass.ngem.2du_Aux.wn.ḫr",
        "17329": "SC.tw.pass.ngem.3pl_Aux.wn.ḫr",
        "-17329": "SC.tw.pass.ngem.3du_Aux.wn.ḫr",
        "17360": "SC.tw.pass.gem.nom.subj_Aux.wn.ḫr",
        "17361": "SC.tw.pass.gem.1sg_Aux.wn.ḫr",
        "17362": "SC.tw.pass.gem.2sgm_Aux.wn.ḫr",
        "17363": "SC.tw.pass.gem.2sgf_Aux.wn.ḫr",
        "17364": "SC.tw.pass.gem.3sgm_Aux.wn.ḫr",
        "17365": "SC.tw.pass.gem.3sgf_Aux.wn.ḫr",
        "17366": "SC.tw.pass.gem.3sg_Aux.wn.ḫr",
        "17367": "SC.tw.pass.gem.1pl_Aux.wn.ḫr",
        "-17367": "SC.tw.pass.gem.1du_Aux.wn.ḫr",
        "17368": "SC.tw.pass.gem.2pl_Aux.wn.ḫr",
        "-17368": "SC.tw.pass.gem.2du_Aux.wn.ḫr",
        "17369": "SC.tw.pass.gem.3pl_Aux.wn.ḫr",
        "-17369": "SC.tw.pass.gem.3du_Aux.wn.ḫr",
        "17380": "SC.n.act.ngem.nom.subj_Aux.wn.ḫr",
        "17381": "SC.n.act.ngem.1sg_Aux.wn.ḫr",
        "17382": "SC.n.act.ngem.2sgm_Aux.wn.ḫr",
        "17383": "SC.n.act.ngem.2sgf_Aux.wn.ḫr",
        "17384": "SC.n.act.ngem.3sgm_Aux.wn.ḫr",
        "17385": "SC.n.act.ngem.3sgf_Aux.wn.ḫr",
        "17386": "SC.n.act.ngem.3sg_Aux.wn.ḫr",
        "17387": "SC.n.act.ngem.1pl_Aux.wn.ḫr",
        "-17387": "SC.n.act.ngem.1du_Aux.wn.ḫr",
        "17388": "SC.n.act.ngem.2pl_Aux.wn.ḫr",
        "-17388": "SC.n.act.ngem.2du_Aux.wn.ḫr",
        "17389": "SC.n.act.ngem.3pl_Aux.wn.ḫr",
        "-17389": "SC.n.act.ngem.3du_Aux.wn.ḫr",
        "17420": "SC.n.act.gem.nom.subj_Aux.wn.ḫr",
        "17421": "SC.n.act.gem.1sg_Aux.wn.ḫr",
        "17422": "SC.n.act.gem.2sgm_Aux.wn.ḫr",
        "17423": "SC.n.act.gem.2sgf_Aux.wn.ḫr",
        "17424": "SC.n.act.gem.3sgm_Aux.wn.ḫr",
        "17425": "SC.n.act.gem.3sgf_Aux.wn.ḫr",
        "17426": "SC.n.act.gem.3sg_Aux.wn.ḫr",
        "17427": "SC.n.act.gem.1pl_Aux.wn.ḫr",
        "-17427": "SC.n.act.gem.1du_Aux.wn.ḫr",
        "17428": "SC.n.act.gem.2pl_Aux.wn.ḫr",
        "-17428": "SC.n.act.gem.2du_Aux.wn.ḫr",
        "17429": "SC.n.act.gem.3pl_Aux.wn.ḫr",
        "-17429": "SC.n.act.gem.3du_Aux.wn.ḫr",
        "17430": "SC.n.pass.ngem.nom.subj_Aux.wn.ḫr",
        "17431": "SC.n.pass.ngem.1sg_Aux.wn.ḫr",
        "17432": "SC.n.pass.ngem.2sgm_Aux.wn.ḫr",
        "17433": "SC.n.pass.ngem.sg2f_Aux.wn.ḫr",
        "17434": "SC.n.pass.ngem.3sgm_Aux.wn.ḫr",
        "17435": "SC.n.pass.ngem.3sgf_Aux.wn.ḫr",
        "17436": "SC.n.pass.ngem.3sg_Aux.wn.ḫr",
        "17437": "SC.n.pass.ngem.1pl_Aux.wn.ḫr",
        "-17437": "SC.n.pass.ngem.1du_Aux.wn.ḫr",
        "17438": "SC.n.pass.ngem.2pl_Aux.wn.ḫr",
        "-17438": "SC.n.pass.ngem.2du_Aux.wn.ḫr",
        "17439": "SC.n.pass.ngem.3pl_Aux.wn.ḫr",
        "-17439": "SC.n.pass.ngem.3du_Aux.wn.ḫr",
        "17440": "SC.n.tw.pass.ngem.nom.subj_Aux.wn.ḫr",
        "17441": "SC.n.tw.pass.ngem.1sg_Aux.wn.ḫr",
        "17442": "SC.n.tw.pass.ngem.2sgm_Aux.wn.ḫr",
        "17443": "SC.n.tw.pass.ngem.2sgf_Aux.wn.ḫr",
        "17444": "SC.n.tw.pass.ngem.3sgm_Aux.wn.ḫr",
        "17445": "SC.n.tw.pass.ngem.3sgf_Aux.wn.ḫr",
        "17446": "SC.n.tw.pass.ngem.3sg_Aux.wn.ḫr",
        "17447": "SC.n.tw.pass.ngem.1pl_Aux.wn.ḫr",
        "-17447": "SC.n.tw.pass.ngem.1du_Aux.wn.ḫr",
        "17448": "SC.n.tw.pass.ngem.2pl_Aux.wn.ḫr",
        "-17448": "SC.n.tw.pass.ngem.2du_Aux.wn.ḫr",
        "17449": "SC.n.tw.pass.ngem.3pl_Aux.wn.ḫr",
        "-17449": "SC.n.tw.pass.ngem.3du_Aux.wn.ḫr",
        "17480": "SC.n.tw.pass.gem.nom.subj_Aux.wn.ḫr",
        "17481": "SC.n.tw.pass.gem.1sg_Aux.wn.ḫr",
        "17482": "SC.n.tw.pass.gem.2sgm_Aux.wn.ḫr",
        "17483": "SC.n.tw.pass.gem.2sgf_Aux.wn.ḫr",
        "17484": "SC.n.tw.pass.gem.3sgm_Aux.wn.ḫr",
        "17485": "SC.n.tw.pass.gem.3sgf_Aux.wn.ḫr",
        "17486": "SC.n.tw.pass.gem.3sg_Aux.wn.ḫr",
        "17487": "SC.n.tw.pass.gem.1pl_Aux.wn.ḫr",
        "-17487": "SC.n.tw.pass.gem.1du_Aux.wn.ḫr",
        "17488": "SC.n.tw.pass.gem.2pl_Aux.wn.ḫr",
        "-17488": "SC.n.tw.pass.gem.2du_Aux.wn.ḫr",
        "17489": "SC.n.tw.pass.gem.3pl_Aux.wn.ḫr",
        "-17489": "SC.n.tw.pass.gem.3du_Aux.wn.ḫr",
        "17840": "SC.t.act.ngem.nom.subj_Aux.wn.ḫr",
        "17841": "SC.t.act.ngem.1sg_Aux.wn.ḫr",
        "17842": "SC.t.act.ngem.2sgm_Aux.wn.ḫr",
        "17843": "SC.t.act.ngem.2sgf_Aux.wn.ḫr",
        "17844": "SC.t.act.ngem.3sgm_Aux.wn.ḫr",
        "17845": "SC.t.act.ngem.3sgf_Aux.wn.ḫr",
        "17846": "SC.t.act.ngem.3sg_Aux.wn.ḫr",
        "17847": "SC.t.act.ngem.1pl_Aux.wn.ḫr",
        "-17847": "SC.t.act.ngem.1du_Aux.wn.ḫr",
        "17848": "SC.t.act.ngem.2pl_Aux.wn.ḫr",
        "-17848": "SC.t.act.ngem.2du_Aux.wn.ḫr",
        "17849": "SC.t.act.ngem.3pl_Aux.wn.ḫr",
        "-17849": "SC.t.act.ngem.3du_Aux.wn.ḫr",
        "17850": "SC.t.act.gem.nom.subj_Aux.wn.ḫr",
        "17851": "SC.t.act.gem.1sg_Aux.wn.ḫr",
        "17852": "SC.t.act.gem.2sgm_Aux.wn.ḫr",
        "17853": "SC.t.act.gem.2sgf_Aux.wn.ḫr",
        "17854": "SC.t.act.gem.3sgm_Aux.wn.ḫr",
        "17855": "SC.t.act.gem.3sgf_Aux.wn.ḫr",
        "17856": "SC.t.act.gem.3sg_Aux.wn.ḫr",
        "17857": "SC.t.act.gem.1pl_Aux.wn.ḫr",
        "-17857": "SC.t.act.gem.1du_Aux.wn.ḫr",
        "17858": "SC.t.act.gem.2pl_Aux.wn.ḫr",
        "-17858": "SC.t.act.gem.2du_Aux.wn.ḫr",
        "17859": "SC.t.act.gem.3pl_Aux.wn.ḫr",
        "-17859": "SC.t.act.gem.3du_Aux.wn.ḫr",
        "17860": "SC.t.pass.ngem.nom.subj_Aux.wn.ḫr",
        "17861": "SC.t.pass.ngem.1sg_Aux.wn.ḫr",
        "17862": "SC.t.pass.ngem.2sgm_Aux.wn.ḫr",
        "17863": "SC.t.pass.ngem.2sgf_Aux.wn.ḫr",
        "17864": "SC.t.pass.ngem.3sgm_Aux.wn.ḫr",
        "17865": "SC.t.pass.ngem.3sgf_Aux.wn.ḫr",
        "17866": "SC.t.pass.ngem.3sg_Aux.wn.ḫr",
        "17867": "SC.t.pass.ngem.1pl_Aux.wn.ḫr",
        "-17867": "SC.t.pass.ngem.1du_Aux.wn.ḫr",
        "17868": "SC.t.pass.ngem.2pl_Aux.wn.ḫr",
        "-17868": "SC.t.pass.ngem.2du_Aux.wn.ḫr",
        "17869": "SC.t.pass.ngem.3pl_Aux.wn.ḫr",
        "-17869": "SC.t.pass.ngem.3du_Aux.wn.ḫr",
        "17870": "SC.t.pass.gem.nom.subj_Aux.wn.ḫr",
        "17871": "SC.t.pass.gem.1sg_Aux.wn.ḫr",
        "17872": "SC.t.pass.gem.2sgm_Aux.wn.ḫr",
        "17873": "SC.t.pass.gem.2sgf_Aux.wn.ḫr",
        "17874": "SC.t.pass.gem.3sgm_Aux.wn.ḫr",
        "17875": "SC.t.pass.gem.3sgf_Aux.wn.ḫr",
        "17876": "SC.t.pass.gem.3sg_Aux.wn.ḫr",
        "17877": "SC.t.pass.gem.1pl_Aux.wn.ḫr",
        "-17877": "SC.t.pass.gem.1du_Aux.wn.ḫr",
        "17878": "SC.t.pass.gem.2pl_Aux.wn.ḫr",
        "-17878": "SC.t.pass.gem.2du_Aux.wn.ḫr",
        "17879": "SC.t.pass.gem.3pl_Aux.wn.ḫr",
        "-17879": "SC.t.pass.gem.3du_Aux.wn.ḫr",
        "18020": "SC.act.ngem.nom.subj_Aux.wnn",
        "18021": "SC.act.ngem.1sg_Aux.wnn",
        "18022": "SC.act.ngem.2sgm_Aux.wnn",
        "18023": "SC.act.ngem.2sgf_Aux.wnn",
        "18024": "SC.act.ngem.3sgm_Aux.wnn",
        "18025": "SC.act.ngem.3sgf_Aux.wnn",
        "18026": "SC.act.ngem.3sg_Aux.wnn",
        "18027": "SC.act.ngem.1pl_Aux.wnn",
        "-18027": "SC.act.ngem.1du_Aux.wnn",
        "18028": "SC.act.ngem.2pl_Aux.wnn",
        "-18028": "SC.act.ngem.2du_Aux.wnn",
        "18029": "SC.act.ngem.3pl_Aux.wnn",
        "-18029": "SC.act.ngem.3du_Aux.wnn",
        "18040": "SC.pass.ngem.nom.subj_Aux.wnn",
        "18041": "SC.pass.ngem.1sg_Aux.wnn",
        "18042": "SC.pass.ngem.2sgm_Aux.wnn",
        "18043": "SC.pass.ngem.2sgf_Aux.wnn",
        "18044": "SC.pass.ngem.3sgm_Aux.wnn",
        "18045": "SC.pass.ngem.3sgf_Aux.wnn",
        "18046": "SC.pass.ngem.3sg_Aux.wnn",
        "18047": "SC.pass.ngem.1pl_Aux.wnn",
        "-18047": "SC.pass.ngem.1du_Aux.wnn",
        "18048": "SC.pass.ngem.2pl_Aux.wnn",
        "-18048": "SC.pass.ngem.2du_Aux.wnn",
        "18049": "SC.pass.ngem.3pl_Aux.wnn",
        "-18049": "SC.pass.ngem.3du_Aux.wnn",
        "18100": "SC.act.gem.nom.subj_Aux.wnn",
        "18101": "SC.act.gem.1sg_Aux.wnn",
        "18102": "SC.act.gem.2sgm_Aux.wnn",
        "18103": "SC.act.gem.2sgf_Aux.wnn",
        "18104": "SC.act.gem.3sgm_Aux.wnn",
        "18105": "SC.act.gem.3sgf_Aux.wnn",
        "18106": "SC.act.gem.3sg_Aux.wnn",
        "18107": "SC.act.gem.1pl_Aux.wnn",
        "-18107": "SC.act.gem.1du_Aux.wnn",
        "18108": "SC.act.gem.2pl_Aux.wnn",
        "-18108": "SC.act.gem.2du_Aux.wnn",
        "18109": "SC.act.gem.3pl_Aux.wnn",
        "-18109": "SC.act.gem.3du_Aux.wnn",
        "18120": "SC.pass.gem(redupl).nom.subj_Aux.wnn ",
        "18121": "SC.pass.gem(redupl).1sg_Aux.wnn",
        "18122": "SC.pass.gem(redupl).2sgm_Aux.wnn",
        "18123": "SC.pass.gem(redupl).2sgf_Aux.wnn",
        "18124": "SC.pass.gem(redupl).3sgm_Aux.wnn",
        "18125": "SC.pass.gem(redupl).3sgf_Aux.wnn",
        "18126": "SC.pass.gem(redupl).3sg_Aux.wnn",
        "18127": "SC.pass.gem(redupl).1pl_Aux.wnn",
        "-18127": "SC.pass.gem(redupl).1du_Aux.wnn",
        "18128": "SC.pass.gem(redupl).2pl_Aux.wnn",
        "-18128": "SC.pass.gem(redupl).2du_Aux.wnn",
        "18129": "SC.pass.gem(redupl).3pl_Aux.wnn",
        "-18129": "SC.pass.gem(redupl).3du_Aux.wnn",
        "18140": "SC.act.spec.nom.subj_Aux.wnn",
        "18141": "SC.act.spec.1sg_Aux.wnn",
        "18142": "SC.act.spec.2sgm_Aux.wnn",
        "18143": "SC.act.spec.2sgf_Aux.wnn",
        "18144": "SC.act.spec.3sgm_Aux.wnn",
        "18145": "SC.act.spec.3sgf_Aux.wnn",
        "18146": "SC.act.spec.3sg_Aux.wnn",
        "18147": "SC.act.spec.1pl_Aux.wnn",
        "-18147": "SC.act.spec.1du_Aux.wnn",
        "18148": "SC.act.spec.2pl_Aux.wnn",
        "-18148": "SC.act.spec.2du_Aux.wnn",
        "18149": "SC.act.spec.3pl_Aux.wnn",
        "-18149": "SC.act.spec.3du_Aux.wnn",
        "18160": "SC.pass.spec.nom.subj_Aux.wnn",
        "18161": "SC.pass.spec.1sg_Aux.wnn",
        "18162": "SC.pass.spec.2sgm_Aux.wnn",
        "18163": "SC.pass.spec.2sgf_Aux.wnn",
        "18164": "SC.pass.spec.3sgm_Aux.wnn",
        "18165": "SC.pass.spec.3sgf_Aux.wnn",
        "18166": "SC.pass.spec.3sg_Aux.wnn",
        "18167": "SC.pass.spec.1pl_Aux.wnn",
        "-18167": "SC.pass.spec.1du_Aux.wnn",
        "18168": "SC.pass.spec.2pl_Aux.wnn",
        "-18168": "SC.pass.spec.2du_Aux.wnn",
        "18169": "SC.pass.spec.3pl_Aux.wnn",
        "-18169": "SC.pass.spec.3du_Aux.wnn",
        "18170": "SC.tw.pass.spec.nom.subj_Aux.wnn",
        "18171": "SC.tw.pass.spec.1sg_Aux.wnn",
        "18172": "SC.tw.pass.spec.2sgm_Aux.wnn",
        "18173": "SC.tw.pass.spec.2sgf_Aux.wnn",
        "18174": "SC.tw.pass.spec.3sgm_Aux.wnn",
        "18175": "SC.tw.pass.spec.3sgf_Aux.wnn",
        "18176": "SC.tw.pass.spec.3sg_Aux.wnn",
        "18177": "SC.tw.pass.spec.1pl_Aux.wnn",
        "-18177": "SC.tw.pass.spec.1du_Aux.wnn",
        "18178": "SC.tw.pass.spec.2pl_Aux.wnn",
        "-18178": "SC.tw.pass.spec.2du_Aux.wnn",
        "18179": "SC.tw.pass.spec.3pl_Aux.wnn",
        "-18179": "SC.tw.pass.spec.3du_Aux.wnn",
        "18180": "SC.w.act.ngem.nom.subj_Aux.wnn",
        "18181": "SC.w.act.ngem.1sg_Aux.wnn",
        "18182": "SC.w.act.ngem.2sgm_Aux.wnn",
        "18183": "SC.w.act.ngem.2sgf_Aux.wnn",
        "18184": "SC.w.act.ngem.3sgm_Aux.wnn",
        "18185": "SC.w.act.ngem.3sgf_Aux.wnn",
        "18186": "SC.w.act.ngem.3sg.aux.wnn",
        "18187": "SC.w.act.ngem.1pl_Aux.wnn",
        "-18187": "SC.w.act.ngem.1du_Aux.wnn",
        "18188": "SC.w.act.ngem.2pl_Aux.wnn",
        "-18188": "SC.w.act.ngem.2du_Aux.wnn",
        "18189": "SC.w.act.ngem.3pl_Aux.wnn",
        "-18189": "SC.w.act.ngem.3du_Aux.wnn",
        "18220": "SC.w.act.gem.nom.subj_Aux.wnn",
        "18221": "SC.w.act.gem.1sg_Aux.wnn",
        "18222": "SC.w.act.gem.2sgm_Aux.wnn",
        "18223": "SC.w.act.gem.2sgf_Aux.wnn",
        "18224": "SC.w.act.gem.3sgm_Aux.wnn",
        "18225": "SC.w.act.gem.3sgf_Aux.wnn",
        "18226": "SC.w.act.gem.3sg_Aux.wnn",
        "18227": "SC.w.act.gem.1pl_Aux.wnn",
        "-18227": "SC.w.act.gem.1du_Aux.wnn",
        "18228": "SC.w.act.gem.2pl_Aux.wnn",
        "-18228": "SC.w.act.gem.2du_Aux.wnn",
        "18229": "SC.w.act.gem.3pl_Aux.wnn",
        "-18229": "SC.w.act.gem.3du_Aux.wnn",
        "18240": "SC.w.pass.ngem.nom.subj_Aux.wnn",
        "18241": "SC.w.pass.ngem.1sg_Aux.wnn",
        "18242": "SC.w.pass.ngem.2sgm_Aux.wnn",
        "18243": "SC.w.pass.ngem.2sgf_Aux.wnn",
        "18244": "SC.w.pass.ngem.3sgm_Aux.wnn",
        "18245": "SC.w.pass.ngem.3sgf_Aux.wnn",
        "18246": "SC.w.pass.ngem.3sg_Aux.wnn",
        "18247": "SC.w.pass.ngem.1pl_Aux.wnn",
        "-18247": "SC.w.pass.ngem.1du_Aux.wnn",
        "18248": "SC.w.pass.ngem.2pl_Aux.wnn",
        "-18248": "SC.w.pass.ngem.2du_Aux.wnn",
        "18249": "SC.w.pass.ngem.3pl_Aux.wnn",
        "-18249": "SC.w.pass.ngem.3du_Aux.wnn",
        "18280": "SC.w.tw.pass.ngem.nom.subj_Aux.wnn",
        "18281": "SC.w.tw.pass.ngem.1sg_Aux.wnn",
        "18282": "SC.w.tw.pass.ngem.2sgm_Aux.wnn",
        "18283": "SC.w.tw.pass.ngem.2sgf_Aux.wnn",
        "18284": "SC.w.tw.pass.ngem.3sgm_Aux.wnn",
        "18285": "SC.w.tw.pass.ngem.3sgf_Aux.wnn",
        "18286": "SC.w.tw.pass.ngem.3sg_Aux.wnn",
        "18287": "SC.w.tw.pass.ngem.1pl_Aux.wnn",
        "-18287": "SC.w.tw.pass.ngem.1du_Aux.wnn",
        "18288": "SC.w.tw.pass.ngem.2pl_Aux.wnn",
        "-18288": "SC.w.tw.pass.ngem.2du_Aux.wnn",
        "18289": "SC.w.tw.pass.ngem.3pl_Aux.wnn",
        "-18289": "SC.w.tw.pass.ngem.3du_Aux.wnn",
        "18320": "SC.tw.pass.ngem.nom.subj_Aux.wnn",
        "18321": "SC.tw.pass.ngem.1sg_Aux.wnn",
        "18322": "SC.tw.pass.ngem.2sgm_Aux.wnn",
        "18323": "SC.tw.pass.ngem.2sgf_Aux.wnn",
        "18324": "SC.tw.pass.ngem.3sgm_Aux.wnn",
        "18325": "SC.tw.pass.ngem.3sgf_Aux.wnn",
        "18326": "SC.tw.pass.ngem.3sg_Aux.wnn",
        "18327": "SC.tw.pass.ngem.1pl_Aux.wnn",
        "-18327": "SC.tw.pass.ngem.1du_Aux.wnn",
        "18328": "SC.tw.pass.ngem.2pl_Aux.wnn",
        "-18328": "SC.tw.pass.ngem.2du_Aux.wnn",
        "18329": "SC.tw.pass.ngem.3pl_Aux.wnn",
        "-18329": "SC.tw.pass.ngem.3du_Aux.wnn",
        "18360": "SC.tw.pass.gem.nom.subj_Aux.wnn",
        "18361": "SC.tw.pass.gem.1sg_Aux.wnn",
        "18362": "SC.tw.pass.gem.2sgm_Aux.wnn",
        "18363": "SC.tw.pass.gem.2sgf_Aux.wnn",
        "18364": "SC.tw.pass.gem.3sgm_Aux.wnn",
        "18365": "SC.tw.pass.gem.3sgf_Aux.wnn",
        "18366": "SC.tw.pass.gem.3sg_Aux.wnn",
        "18367": "SC.tw.pass.gem.1pl_Aux.wnn",
        "-18367": "SC.tw.pass.gem.1du_Aux.wnn",
        "18368": "SC.tw.pass.gem.2pl_Aux.wnn",
        "-18368": "SC.tw.pass.gem.2du_Aux.wnn",
        "18369": "SC.tw.pass.gem.3pl_Aux.wnn",
        "-18369": "SC.tw.pass.gem.3du_Aux.wnn",
        "18380": "SC.n.act.ngem.nom.subj_Aux.wnn",
        "18381": "SC.n.act.ngem.1sg_Aux.wnn",
        "18382": "SC.n.act.ngem.2sgm_Aux.wnn",
        "18383": "SC.n.act.ngem.2sgf_Aux.wnn",
        "18384": "SC.n.act.ngem.3sgm_Aux.wnn",
        "18385": "SC.n.act.ngem.3sgf_Aux.wnn",
        "18386": "SC.n.act.ngem.3sg_Aux.wnn",
        "18387": "SC.n.act.ngem.1pl_Aux.wnn",
        "-18387": "SC.n.act.ngem.1du_Aux.wnn",
        "18388": "SC.n.act.ngem.2pl_Aux.wnn",
        "-18388": "SC.n.act.ngem.2du_Aux.wnn",
        "18389": "SC.n.act.ngem.3pl_Aux.wnn",
        "-18389": "SC.n.act.ngem.3du_Aux.wnn",
        "18420": "SC.n.act.gem.nom.subj_Aux.wnn",
        "18421": "SC.n.act.gem.1sg_Aux.wnn",
        "18422": "SC.n.act.gem.2sgm_Aux.wnn",
        "18423": "SC.n.act.gem.2sgf_Aux.wnn",
        "18424": "SC.n.act.gem.3sgm_Aux.wnn",
        "18425": "SC.n.act.gem.3sgf_Aux.wnn",
        "18426": "SC.n.act.gem.3sg_Aux.wnn",
        "18427": "SC.n.act.gem.1pl_Aux.wnn",
        "-18427": "SC.n.act.gem.1du_Aux.wnn",
        "18428": "SC.n.act.gem.2pl_Aux.wnn",
        "-18428": "SC.n.act.gem.2du_Aux.wnn",
        "18429": "SC.n.act.gem.3pl_Aux.wnn",
        "-18429": "SC.n.act.gem.3du_Aux.wnn",
        "18430": "SC.n.pass.ngem.nom.subj_Aux.wnn",
        "18431": "SC.n.pass.ngem.1sg_Aux.wnn",
        "18432": "SC.n.pass.ngem.2sgm_Aux.wnn",
        "18433": "SC.n.pass.ngem.sg2f_Aux.wnn",
        "18434": "SC.n.pass.ngem.3sgm_Aux.wnn",
        "18435": "SC.n.pass.ngem.3sgf_Aux.wnn",
        "18436": "SC.n.pass.ngem.3sg.aux.wnn",
        "18437": "SC.n.pass.ngem.1pl_Aux.wnn",
        "-18437": "SC.n.pass.ngem.1du_Aux.wnn",
        "18438": "SC.n.pass.ngem.2pl_Aux.wnn",
        "-18438": "SC.n.pass.ngem.2du_Aux.wnn",
        "18439": "SC.n.pass.ngem.3pl_Aux.wnn",
        "-18439": "SC.n.pass.ngem.3du_Aux.wnn",
        "18440": "SC.n.tw.pass.ngem.nom.subj_Aux.wnn",
        "18441": "SC.n.tw.pass.ngem.1sg_Aux.wnn",
        "18442": "SC.n.tw.pass.ngem.2sgm_Aux.wnn",
        "18443": "SC.n.tw.pass.ngem.2sgf_Aux.wnn",
        "18444": "SC.n.tw.pass.ngem.3sgm_Aux.wnn",
        "18445": "SC.n.tw.pass.ngem.3sgf_Aux.wnn",
        "18446": "SC.n.tw.pass.ngem.3sg_Aux.wnn",
        "18447": "SC.n.tw.pass.ngem.1pl_Aux.wnn",
        "-18447": "SC.n.tw.pass.ngem.1du_Aux.wnn",
        "18448": "SC.n.tw.pass.ngem.2pl_Aux.wnn",
        "-18448": "SC.n.tw.pass.ngem.2du_Aux.wnn",
        "18449": "SC.n.tw.pass.ngem.3pl_Aux.wnn",
        "-18449": "SC.n.tw.pass.ngem.3du_Aux.wnn",
        "18480": "SC.n.tw.pass.gem.nom.subj_Aux.wnn",
        "18481": "SC.n.tw.pass.gem.1sg_Aux.wnn",
        "18482": "SC.n.tw.pass.gem.2sgm_Aux.wnn",
        "18483": "SC.n.tw.pass.gem.2sgf_Aux.wnn",
        "18484": "SC.n.tw.pass.gem.3sgm_Aux.wnn",
        "18485": "SC.n.tw.pass.gem.3sgf_Aux.wnn",
        "18486": "SC.n.tw.pass.gem.3sg_Aux.wnn",
        "18487": "SC.n.tw.pass.gem.1pl_Aux.wnn",
        "-18487": "SC.n.tw.pass.gem.1du_Aux.wnn",
        "18488": "SC.n.tw.pass.gem.2pl_Aux.wnn",
        "-18488": "SC.n.tw.pass.gem.2du_Aux.wnn",
        "18489": "SC.n.tw.pass.gem.3pl_Aux.wnn",
        "-18489": "SC.n.tw.pass.gem.3du_Aux.wnn",
        "18840": "SC.t.act.ngem.nom.subj_Aux.wnn",
        "18841": "SC.t.act.ngem.1sg_Aux.wnn",
        "18842": "SC.t.act.ngem.2sgm_Aux.wnn",
        "18843": "SC.t.act.ngem.2sgf_Aux.wnn",
        "18844": "SC.t.act.ngem.3sgm_Aux.wnn",
        "18845": "SC.t.act.ngem.3sgf_Aux.wnn",
        "18846": "SC.t.act.ngem.3sg_Aux.wnn",
        "18847": "SC.t.act.ngem.1pl_Aux.wnn",
        "-18847": "SC.t.act.ngem.1du_Aux.wnn",
        "18848": "SC.t.act.ngem.2pl_Aux.wnn",
        "-18848": "SC.t.act.ngem.2du_Aux.wnn",
        "18849": "SC.t.act.ngem.3pl_Aux.wnn",
        "-18849": "SC.t.act.ngem.3du_Aux.wnn",
        "18850": "SC.t.act.gem.nom.subj_Aux.wnn",
        "18851": "SC.t.act.gem.1sg_Aux.wnn",
        "18852": "SC.t.act.gem.2sgm_Aux.wnn",
        "18853": "SC.t.act.gem.2sgf_Aux.wnn",
        "18854": "SC.t.act.gem.3sgm_Aux.wnn",
        "18855": "SC.t.act.gem.3sgf_Aux.wnn",
        "18856": "SC.t.act.gem.3sg_Aux.wnn",
        "18857": "SC.t.act.gem.1pl_Aux.wnn",
        "-18857": "SC.t.act.gem.1du_Aux.wnn",
        "18858": "SC.t.act.gem.2pl_Aux.wnn",
        "-18858": "SC.t.act.gem.2du_Aux.wnn",
        "18859": "SC.t.act.gem.3pl_Aux.wnn",
        "-18859": "SC.t.act.gem.3du_Aux.wnn",
        "18860": "SC.t.pass.ngem.nom.subj_Aux.wnn",
        "18861": "SC.t.pass.ngem.1sg_Aux.wnn",
        "18862": "SC.t.pass.ngem.2sgm_Aux.wnn",
        "18863": "SC.t.pass.ngem.2sgf_Aux.wnn",
        "18864": "SC.t.pass.ngem.3sgm_Aux.wnn",
        "18865": "SC.t.pass.ngem.3sgf_Aux.wnn",
        "18866": "SC.t.pass.ngem.3sg_Aux.wnn",
        "18867": "SC.t.pass.ngem.1pl_Aux.wnn",
        "-18867": "SC.t.pass.ngem.1du_Aux.wnn",
        "18868": "SC.t.pass.ngem.2pl_Aux.wnn",
        "-18868": "SC.t.pass.ngem.2du_Aux.wnn",
        "18869": "SC.t.pass.ngem.3pl_Aux.wnn",
        "-18869": "SC.t.pass.ngem.3du_Aux.wnn",
        "18870": "SC.t.pass.gem.nom.subj_Aux.wnn",
        "18871": "SC.t.pass.gem.1sg_Aux.wnn",
        "18872": "SC.t.pass.gem.2sgm_Aux.wnn",
        "18873": "SC.t.pass.gem.2sgf_Aux.wnn",
        "18874": "SC.t.pass.gem.3sgm_Aux.wnn",
        "18875": "SC.t.pass.gem.3sgf_Aux.wnn",
        "18876": "SC.t.pass.gem.3sg_Aux.wnn",
        "18877": "SC.t.pass.gem.1pl_Aux.wnn",
        "-18877": "SC.t.pass.gem.1du_Aux.wnn",
        "18878": "SC.t.pass.gem.2pl_Aux.wnn",
        "-18878": "SC.t.pass.gem.2du_Aux.wnn",
        "18879": "SC.t.pass.gem.3pl_Aux.wnn",
        "-18879": "SC.t.pass.gem.3du_Aux.wnn",
        "19000": "SC.unspec.nom.subj_Aux.jri̯",
        "19020": "SC.act.ngem.nom.subj_Aux.jri̯",
        "19021": "SC.act.ngem.1sg_Aux.jri̯",
        "19022": "SC.act.ngem.2sgm_Aux.jri̯",
        "19023": "SC.act.ngem.2sgf_Aux.jri̯",
        "19024": "SC.act.ngem.3sgm_Aux.jri̯",
        "19025": "SC.act.ngem.3sgf_Aux.jri̯",
        "19026": "SC.act.ngem.3sg_Aux.jri̯",
        "19027": "SC.act.ngem.1pl_Aux.jri̯",
        "-19027": "SC.act.ngem.1du_Aux.jri̯",
        "19028": "SC.act.ngem.2pl_Aux.jri̯",
        "-19028": "SC.act.ngem.2du_Aux.jri̯",
        "19029": "SC.act.ngem.3pl_Aux.jri̯",
        "-19029": "SC.act.ngem.3du_Aux.jri̯",
        "19040": "SC.pass.ngem.nom.subj_Aux.jri̯",
        "19041": "SC.pass.ngem.1sg_Aux.jri̯",
        "19042": "SC.pass.ngem.2sgm_Aux.jri̯",
        "19043": "SC.pass.ngem.2sgf_Aux.jri̯",
        "19044": "SC.pass.ngem.3sgm_Aux.jri̯",
        "19045": "SC.pass.ngem.3sgf_Aux.jri̯",
        "19046": "SC.pass.ngem.3sg_Aux.jri̯",
        "19047": "SC.pass.ngem.1pl_Aux.jri̯",
        "-19047": "SC.pass.ngem.1du_Aux.jri̯",
        "19048": "SC.pass.ngem.2pl_Aux.jri̯",
        "-19048": "SC.pass.ngem.2du_Aux.jri̯",
        "19049": "SC.pass.ngem.3pl_Aux.jri̯",
        "-19049": "SC.pass.ngem.3du_Aux.jri̯",
        "19100": "SC.act.gem.nom.subj_Aux.jri̯",
        "19101": "SC.act.gem.1sg_Aux.jri̯",
        "19102": "SC.act.gem.2sgm_Aux.jri̯",
        "19103": "SC.act.gem.2sgf_Aux.jri̯",
        "19104": "SC.act.gem.3sgm_Aux.jri̯",
        "19105": "SC.act.gem.3sgf_Aux.jri̯",
        "19106": "SC.act.gem.3sg_Aux.jri̯",
        "19107": "SC.act.gem.1pl_Aux.jri̯",
        "-19107": "SC.act.gem.1du_Aux.jri̯",
        "19108": "SC.act.gem.2pl_Aux.jri̯",
        "-19108": "SC.act.gem.2du_Aux.jri̯",
        "19109": "SC.act.gem.3pl_Aux.jri̯",
        "-19109": "SC.act.gem.3du_Aux.jri̯",
        "19120": "SC.pass.gem(redupl).nom.subj_Aux.jri̯. ",
        "19121": "SC.pass.gem(redupl).1sg_Aux.jri̯",
        "19122": "SC.pass.gem(redupl).2sgm_Aux.jri̯",
        "19123": "SC.pass.gem(redupl).2sgf_Aux.jri̯",
        "19124": "SC.pass.gem(redupl).3sgm_Aux.jri̯",
        "19125": "SC.pass.gem(redupl).3sgf_Aux.jri̯",
        "19126": "SC.pass.gem(redupl).3sg_Aux.jri̯",
        "19127": "SC.pass.gem(redupl).1pl_Aux.jri̯",
        "-19127": "SC.pass.gem(redupl).1du_Aux.jri̯",
        "19128": "SC.pass.gem(redupl).2pl_Aux.jri̯",
        "-19128": "SC.pass.gem(redupl).2du_Aux.jri̯",
        "19129": "SC.pass.gem(redupl).3pl_Aux.jri̯",
        "-19129": "SC.pass.gem(redupl).3du_Aux.jri̯",
        "19140": "SC.act.spec.nom.subj_Aux.jri̯",
        "19141": "SC.act.spec.1sg_Aux.jri̯",
        "19142": "SC.act.spec.2sgm_Aux.jri̯",
        "19143": "SC.act.spec.2sgf_Aux.jri̯",
        "19144": "SC.act.spec.3sgm_Aux.jri̯",
        "19145": "SC.act.spec.3sgf_Aux.jri̯",
        "19146": "SC.act.spec.3sg_Aux.jri̯",
        "19147": "SC.act.spec.1pl_Aux.jri̯",
        "-19147": "SC.act.spec.1du_Aux.jri̯",
        "19148": "SC.act.spec.2pl_Aux.jri̯",
        "-19148": "SC.act.spec.2du_Aux.jri̯",
        "19149": "SC.act.spec.3pl_Aux.jri̯",
        "-19149": "SC.act.spec.3du_Aux.jri̯",
        "19160": "SC.pass.spec.nom.subj_Aux.jri̯",
        "19161": "SC.pass.spec.1sg_Aux.jri̯",
        "19162": "SC.pass.spec.2sgm_Aux.jri̯",
        "19163": "SC.pass.spec.2sgf_Aux.jri̯",
        "19164": "SC.pass.spec.3sgm_Aux.jri̯",
        "19165": "SC.pass.spec.3sgf_Aux.jri̯",
        "19166": "SC.pass.spec.3sg_Aux.jri̯",
        "19167": "SC.pass.spec.1pl_Aux.jri̯",
        "-19167": "SC.pass.spec.1du_Aux.jri̯",
        "19168": "SC.pass.spec.2pl_Aux.jri̯",
        "-19168": "SC.pass.spec.2du_Aux.jri̯",
        "19169": "SC.pass.spec.3pl_Aux.jri̯",
        "-19169": "SC.pass.spec.3du_Aux.jri̯",
        "19170": "SC.tw.pass.spec.nom.subj_Aux.jri̯",
        "19171": "SC.tw.pass.spec.1sg_Aux.jri̯",
        "19172": "SC.tw.pass.spec.2sgm_Aux.jri̯",
        "19173": "SC.tw.pass.spec.2sgf_Aux.jri̯",
        "19174": "SC.tw.pass.spec.3sgm_Aux.jri̯",
        "19175": "SC.tw.pass.spec.3sgf_Aux.jri̯",
        "19176": "SC.tw.pass.spec.3sg_Aux.jri̯",
        "19177": "SC.tw.pass.spec.1pl_Aux.jri̯",
        "-19177": "SC.tw.pass.spec.1du_Aux.jri̯",
        "19178": "SC.tw.pass.spec.2pl_Aux.jri̯",
        "-19178": "SC.tw.pass.spec.2du_Aux.jri̯",
        "19179": "SC.tw.pass.spec.3pl_Aux.jri̯",
        "-19179": "SC.tw.pass.spec.3du_Aux.jri̯",
        "19180": "SC.w.act.ngem.nom.subj_Aux.jri̯",
        "19181": "SC.w.act.ngem.1sg_Aux.jri̯",
        "19182": "SC.w.act.ngem.2sgm_Aux.jri̯",
        "19183": "SC.w.act.ngem.2sgf_Aux.jri̯",
        "19184": "SC.w.act.ngem.3sgm_Aux.jri̯",
        "19185": "SC.w.act.ngem.3sgf_Aux.jri̯",
        "19186": "SC.w.act.ngem.3sg.aux.jri̯",
        "19187": "SC.w.act.ngem.1pl_Aux.jri̯",
        "-19187": "SC.w.act.ngem.1du_Aux.jri̯",
        "19188": "SC.w.act.ngem.2pl_Aux.jri̯",
        "-19188": "SC.w.act.ngem.2du_Aux.jri̯",
        "19189": "SC.w.act.ngem.3pl_Aux.jri̯",
        "-19189": "SC.w.act.ngem.3du_Aux.jri̯",
        "19220": "SC.w.act.gem.nom.subj_Aux.jri̯",
        "19221": "SC.w.act.gem.1sg_Aux.jri̯",
        "19222": "SC.w.act.gem.2sgm_Aux.jri̯",
        "19223": "SC.w.act.gem.2sgf_Aux.jri̯",
        "19224": "SC.w.act.gem.3sgm_Aux.jri̯",
        "19225": "SC.w.act.gem.3sgf_Aux.jri̯",
        "19226": "SC.w.act.gem.3sg_Aux.jri̯",
        "19227": "SC.w.act.gem.1pl_Aux.jri̯",
        "-19227": "SC.w.act.gem.1du_Aux.jri̯",
        "19228": "SC.w.act.gem.2pl_Aux.jri̯",
        "-19228": "SC.w.act.gem.2du_Aux.jri̯",
        "19229": "SC.w.act.gem.3pl_Aux.jri̯",
        "-19229": "SC.w.act.gem.3du_Aux.jri̯",
        "19240": "SC.w.pass.ngem.nom.subj_Aux.jri̯",
        "19241": "SC.w.pass.ngem.1sg_Aux.jri̯",
        "19242": "SC.w.pass.ngem.2sgm_Aux.jri̯",
        "19243": "SC.w.pass.ngem.2sgf_Aux.jri̯",
        "19244": "SC.w.pass.ngem.3sgm_Aux.jri̯",
        "19245": "SC.w.pass.ngem.3sgf_Aux.jri̯",
        "19246": "SC.w.pass.ngem.3sg_Aux.jri̯",
        "19247": "SC.w.pass.ngem.1pl_Aux.jri̯",
        "-19247": "SC.w.pass.ngem.1du_Aux.jri̯",
        "19248": "SC.w.pass.ngem.2pl_Aux.jri̯",
        "-19248": "SC.w.pass.ngem.2du_Aux.jri̯",
        "19249": "SC.w.pass.ngem.3pl_Aux.jri̯",
        "-19249": "SC.w.pass.ngem.3du_Aux.jri̯",
        "19280": "SC.w.tw.pass.ngem.nom.subj_Aux.jri̯",
        "19281": "SC.w.tw.pass.ngem.1sg_Aux.jri̯",
        "19282": "SC.w.tw.pass.ngem.2sgm_Aux.jri̯",
        "19283": "SC.w.tw.pass.ngem.2sgf_Aux.jri̯",
        "19284": "SC.w.tw.pass.ngem.3sgm_Aux.jri̯",
        "19285": "SC.w.tw.pass.ngem.3sgf_Aux.jri̯",
        "19286": "SC.w.tw.pass.ngem.3sg_Aux.jri̯",
        "19287": "SC.w.tw.pass.ngem.1pl_Aux.jri̯",
        "-19287": "SC.w.tw.pass.ngem.1du_Aux.jri̯",
        "19288": "SC.w.tw.pass.ngem.2pl_Aux.jri̯",
        "-19288": "SC.w.tw.pass.ngem.2du_Aux.jri̯",
        "19289": "SC.w.tw.pass.ngem.3pl_Aux.jri̯",
        "-19289": "SC.w.tw.pass.ngem.3du_Aux.jri̯",
        "19320": "SC.tw.pass.ngem.nom.subj_Aux.jri̯",
        "19321": "SC.tw.pass.ngem.1sg_Aux.jri̯",
        "19322": "SC.tw.pass.ngem.2sgm_Aux.jri̯",
        "19323": "SC.tw.pass.ngem.2sgf_Aux.jri̯",
        "19324": "SC.tw.pass.ngem.3sgm_Aux.jri̯",
        "19325": "SC.tw.pass.ngem.3sgf_Aux.jri̯",
        "19326": "SC.tw.pass.ngem.3sg_Aux.jri̯",
        "19327": "SC.tw.pass.ngem.1pl_Aux.jri̯",
        "-19327": "SC.tw.pass.ngem.1du_Aux.jri̯",
        "19328": "SC.tw.pass.ngem.2pl_Aux.jri̯",
        "-19328": "SC.tw.pass.ngem.2du_Aux.jri̯",
        "19329": "SC.tw.pass.ngem.3pl_Aux.jri̯",
        "-19329": "SC.tw.pass.ngem.3du_Aux.jri̯",
        "19360": "SC.tw.pass.gem.nom.subj_Aux.jri̯",
        "19361": "SC.tw.pass.gem.1sg_Aux.jri̯",
        "19362": "SC.tw.pass.gem.2sgm_Aux.jri̯",
        "19363": "SC.tw.pass.gem.2sgf_Aux.jri̯",
        "19364": "SC.tw.pass.gem.3sgm_Aux.jri̯",
        "19365": "SC.tw.pass.gem.3sgf_Aux.jri̯",
        "19366": "SC.tw.pass.gem.3sg_Aux.jri̯",
        "19367": "SC.tw.pass.gem.1pl_Aux.jri̯",
        "-19367": "SC.tw.pass.gem.1du_Aux.jri̯",
        "19368": "SC.tw.pass.gem.2pl_Aux.jri̯",
        "-19368": "SC.tw.pass.gem.2du_Aux.jri̯",
        "19369": "SC.tw.pass.gem.3pl_Aux.jri̯",
        "-19369": "SC.tw.pass.gem.3du_Aux.jri̯",
        "19380": "SC.n.act.ngem.nom.subj_Aux.jri̯",
        "19381": "SC.n.act.ngem.1sg_Aux.jri̯",
        "19382": "SC.n.act.ngem.2sgm_Aux.jri̯",
        "19383": "SC.n.act.ngem.2sgf_Aux.jri̯",
        "19384": "SC.n.act.ngem.3sgm_Aux.jri̯",
        "19385": "SC.n.act.ngem.3sgf_Aux.jri̯",
        "19386": "SC.n.act.ngem.3sg_Aux.jri̯",
        "19387": "SC.n.act.ngem.1pl_Aux.jri̯",
        "-19387": "SC.n.act.ngem.1du_Aux.jri̯",
        "19388": "SC.n.act.ngem.2pl_Aux.jri̯",
        "-19388": "SC.n.act.ngem.2du_Aux.jri̯",
        "19389": "SC.n.act.ngem.3pl_Aux.jri̯",
        "-19389": "SC.n.act.ngem.3du_Aux.jri̯",
        "19420": "SC.n.act.gem.nom.subj_Aux.jri̯",
        "19421": "SC.n.act.gem.1sg_Aux.jri̯",
        "19422": "SC.n.act.gem.2sgm_Aux.jri̯",
        "19423": "SC.n.act.gem.2sgf_Aux.jri̯",
        "19424": "SC.n.act.gem.3sgm_Aux.jri̯",
        "19425": "SC.n.act.gem.3sgf_Aux.jri̯",
        "19426": "SC.n.act.gem.3sg_Aux.jri̯",
        "19427": "SC.n.act.gem.1pl_Aux.jri̯",
        "-19427": "SC.n.act.gem.1du_Aux.jri̯",
        "19428": "SC.n.act.gem.2pl_Aux.jri̯",
        "-19428": "SC.n.act.gem.2du_Aux.jri̯",
        "19429": "SC.n.act.gem.3pl_Aux.jri̯",
        "-19429": "SC.n.act.gem.3du_Aux.jri̯",
        "19430": "SC.n.pass.ngem.nom.subj_Aux.jri̯",
        "19431": "SC.n.pass.ngem.1sg_Aux.jri̯",
        "19432": "SC.n.pass.ngem.2sgm_Aux.jri̯",
        "19433": "SC.n.pass.ngem.sg2f_Aux.jri̯",
        "19434": "SC.n.pass.ngem.3sgm_Aux.jri̯",
        "19435": "SC.n.pass.ngem.3sgf_Aux.jri̯",
        "19436": "SC.n.pass.ngem.3sg_Aux.jri̯",
        "19437": "SC.n.pass.ngem.1pl_Aux.jri̯",
        "-19437": "SC.n.pass.ngem.1du_Aux.jri̯",
        "19438": "SC.n.pass.ngem.2pl_Aux.jri̯",
        "-19438": "SC.n.pass.ngem.2du_Aux.jri̯",
        "19439": "SC.n.pass.ngem.3pl_Aux.jri̯",
        "-19439": "SC.n.pass.ngem.3du_Aux.jri̯",
        "19440": "SC.n.tw.pass.ngem.nom.subj_Aux.jri̯",
        "19441": "SC.n.tw.pass.ngem.1sg_Aux.jri̯",
        "19442": "SC.n.tw.pass.ngem.2sgm_Aux.jri̯",
        "19443": "SC.n.tw.pass.ngem.2sgf_Aux.jri̯",
        "19444": "SC.n.tw.pass.ngem.3sgm_Aux.jri̯",
        "19445": "SC.n.tw.pass.ngem.3sgf_Aux.jri̯",
        "19446": "SC.n.tw.pass.ngem.3sg_Aux.jri̯",
        "19447": "SC.n.tw.pass.ngem.1pl_Aux.jri̯",
        "-19447": "SC.n.tw.pass.ngem.1du_Aux.jri̯",
        "19448": "SC.n.tw.pass.ngem.2pl_Aux.jri̯",
        "-19448": "SC.n.tw.pass.ngem.2du_Aux.jri̯",
        "19449": "SC.n.tw.pass.ngem.3pl_Aux.jri̯",
        "-19449": "SC.n.tw.pass.ngem.3du_Aux.jri̯",
        "19480": "SC.n.tw.pass.gem.nom.subj_Aux.jri̯",
        "19481": "SC.n.tw.pass.gem.1sg_Aux.jri̯",
        "19482": "SC.n.tw.pass.gem.2sgm_Aux.jri̯",
        "19483": "SC.n.tw.pass.gem.2sgf_Aux.jri̯",
        "19484": "SC.n.tw.pass.gem.3sgm_Aux.jri̯",
        "19485": "SC.n.tw.pass.gem.3sgf_Aux.jri̯",
        "19486": "SC.n.tw.pass.gem.3sg_Aux.jri̯",
        "19487": "SC.n.tw.pass.gem.1pl_Aux.jri̯",
        "-19487": "SC.n.tw.pass.gem.1du_Aux.jri̯",
        "19488": "SC.n.tw.pass.gem.2pl_Aux.jri̯",
        "-19488": "SC.n.tw.pass.gem.2du_Aux.jri̯",
        "19489": "SC.n.tw.pass.gem.3pl_Aux.jri̯",
        "-19489": "SC.n.tw.pass.gem.3du_Aux.jri̯",
        "19840": "SC.t.act.ngem.nom.subj_Aux.jri̯",
        "19841": "SC.t.act.ngem.1sg_Aux.jri̯",
        "19842": "SC.t.act.ngem.2sgm_Aux.jri̯",
        "19843": "SC.t.act.ngem.2sgf_Aux.jri̯",
        "19844": "SC.t.act.ngem.3sgm_Aux.jri̯",
        "19845": "SC.t.act.ngem.3sgf_Aux.jri̯",
        "19846": "SC.t.act.ngem.3sg_Aux.jri̯",
        "19847": "SC.t.act.ngem.1pl_Aux.jri̯",
        "-19847": "SC.t.act.ngem.1du_Aux.jri̯",
        "19848": "SC.t.act.ngem.2pl_Aux.jri̯",
        "-19848": "SC.t.act.ngem.2du_Aux.jri̯",
        "19849": "SC.t.act.ngem.3pl_Aux.jri̯",
        "-19849": "SC.t.act.ngem.3du_Aux.jri̯",
        "19850": "SC.t.act.gem.nom.subj_Aux.jri̯",
        "19851": "SC.t.act.gem.1sg_Aux.jri̯",
        "19852": "SC.t.act.gem.2sgm_Aux.jri̯",
        "19853": "SC.t.act.gem.2sgf_Aux.jri̯",
        "19854": "SC.t.act.gem.3sgm_Aux.jri̯",
        "19855": "SC.t.act.gem.3sgf_Aux.jri̯",
        "19856": "SC.t.act.gem.3sg_Aux.jri̯",
        "19857": "SC.t.act.gem.1pl_Aux.jri̯",
        "-19857": "SC.t.act.gem.1du_Aux.jri̯",
        "19858": "SC.t.act.gem.2pl_Aux.jri̯",
        "-19858": "SC.t.act.gem.2du_Aux.jri̯",
        "19859": "SC.t.act.gem.3pl_Aux.jri̯",
        "-19859": "SC.t.act.gem.3du_Aux.jri̯",
        "19860": "SC.t.pass.ngem.nom.subj_Aux.jri̯",
        "19861": "SC.t.pass.ngem.1sg_Aux.jri̯",
        "19862": "SC.t.pass.ngem.2sgm_Aux.jri̯",
        "19863": "SC.t.pass.ngem.2sgf_Aux.jri̯",
        "19864": "SC.t.pass.ngem.3sgm_Aux.jri̯",
        "19865": "SC.t.pass.ngem.3sgf_Aux.jri̯",
        "19866": "SC.t.pass.ngem.3sg_Aux.jri̯",
        "19867": "SC.t.pass.ngem.1pl_Aux.jri̯",
        "-19867": "SC.t.pass.ngem.1du_Aux.jri̯",
        "19868": "SC.t.pass.ngem.2pl_Aux.jri̯",
        "-19868": "SC.t.pass.ngem.2du_Aux.jri̯",
        "19869": "SC.t.pass.ngem.3pl_Aux.jri̯",
        "-19869": "SC.t.pass.ngem.3du_Aux.jri̯",
        "19870": "SC.t.pass.gem.nom.subj_Aux.jri̯",
        "19871": "SC.t.pass.gem.1sg_Aux.jri̯",
        "19872": "SC.t.pass.gem.2sgm_Aux.jri̯",
        "19873": "SC.t.pass.gem.2sgf_Aux.jri̯",
        "19874": "SC.t.pass.gem.3sgm_Aux.jri̯",
        "19875": "SC.t.pass.gem.3sgf_Aux.jri̯",
        "19876": "SC.t.pass.gem.3sg_Aux.jri̯",
        "19877": "SC.t.pass.gem.1pl_Aux.jri̯",
        "-19877": "SC.t.pass.gem.1du_Aux.jri̯",
        "19878": "SC.t.pass.gem.2pl_Aux.jri̯",
        "-19878": "SC.t.pass.gem.2du_Aux.jri̯",
        "19879": "SC.t.pass.gem.3pl_Aux.jri̯",
        "-19879": "SC.t.pass.gem.3du_Aux.jri̯",
        "20000": "PsP",
        "20001": "PsP.unspec_Aux.jw ",
        "20007": "PsP.unspec_tw=",
        "20010": "PsP.1sg",
        "20011": "PsP.1sg_Aux.jw ",
        "20012": "PsP.1sg_Aux.jri̯",
        "20013": "PsP.1sg_Aux.j.jri̯",
        "20014": "PsP.1sg_Aux.j.jri̯.t",
        "20016": "PsP.1sg_Aux.others",
        "20017": "PsP.1sg_tw=",
        "20018": "PsP.1sg_Aux.wn.jn",
        "20019": "PsP.1sg_Aux.wn.ḫr",
        "20020": "PsP.2sgm",
        "20021": "PsP.2sgm_Aux.jw ",
        "20022": "PsP.2sgm_Aux.jri̯",
        "20023": "PsP.2sgm_Aux.j.jri̯",
        "20024": "PsP.2sgm_Aux.j.jri̯.t",
        "20026": "PsP.2sgm_Aux.others",
        "20027": "PsP.2sgm_tw=",
        "20028": "PsP.2sgm_Aux.wn.jn",
        "20029": "PsP.2sgm_Aux.wn.ḫr",
        "20030": "PsP.2sgf",
        "20031": "PsP.2sgf_Aux.jw ",
        "20032": "PsP.2sgf_Aux.jri̯",
        "20033": "PsP.2sgf_Aux.j.jri̯",
        "20034": "PsP.2sgf_Aux.j.jri̯.t",
        "20036": "PsP.2sgf_Aux.others",
        "20037": "PsP.2sgf_tw=",
        "20038": "PsP.2sgf_Aux.wn.jn",
        "20039": "PsP.2sgf_Aux.wn.ḫr",
        "20040": "PsP.3sgm",
        "20041": "PsP.3sgm_Aux.jw",
        "20042": "PsP.3sgm_Aux.jri̯",
        "20043": "PsP.3sgm_Aux.j.jri̯",
        "20044": "PsP.3sgm_Aux.j.jri̯.t",
        "20046": "PsP.3sgm_Aux.others",
        "20047": "PsP.3sgm_tw=",
        "20048": "PsP.3sgm_Aux.wn.jn",
        "20049": "PsP.3sgm_Aux.wn.ḫr",
        "20050": "PsP.3sgf",
        "20051": "PsP.3sgf_Aux.jw",
        "20052": "PsP.3sgf_Aux.jri̯",
        "20053": "PsP.3sgf_Aux.j.jri̯",
        "20054": "PsP.3sgf_Aux.j.jri̯.t",
        "20056": "PsP.3sgf_Aux.others",
        "20057": "PsP.3sgf_tw=",
        "20058": "PsP.3sgf_Aux.wn.jn",
        "20059": "PsP.3sgf_Aux.wn.ḫr",
        "20060": "PsP.1pl",
        "20061": "PsP.1pl_Aux.jw",
        "20062": "PsP.1pl_Aux.jri̯",
        "20063": "PsP.1pl_Aux.j.jri̯",
        "20064": "PsP.1pl_Aux.j.jri̯.t",
        "20066": "PsP.1pl_Aux.others",
        "20067": "PsP.1pl_tw",
        "20068": "PsP.1pl_Aux.wn.jn",
        "20069": "PsP.1pl_Aux.wn.ḫr",
        "20070": "PsP.2pl",
        "20071": "PsP.2pl_Aux.jw",
        "20072": "PsP.2pl_Aux.jri̯",
        "20073": "PsP.2pl_Aux.j.jri̯",
        "20074": "PsP.2pl_Aux.j.jri̯.t",
        "20076": "PsP.2pl_Aux.others",
        "20077": "PsP.2pl_tw=",
        "20078": "PsP.2pl_Aux.wn.jn",
        "20079": "PsP.2pl_Aux.wn.ḫr",
        "20080": "PsP.3plm",
        "20081": "PsP.3plm_Aux.jw",
        "20082": "PsP.3plm_Aux.jri̯",
        "20083": "PsP.3plm_Aux.j.jri̯",
        "20084": "PsP.3plm_Aux.j.jri̯.t",
        "20086": "PsP.3plm_Aux.others",
        "20087": "PsP.3plm_tw=",
        "20088": "PsP.3plm_Aux.wn.jn",
        "20089": "PsP.3plm_Aux.wn.ḫr",
        "20090": "PsP.3plf",
        "20091": "PsP.3plf_Aux.jw",
        "20092": "PsP.3plf_Aux.jri̯",
        "20093": "PsP.3plf_Aux.j.jri̯",
        "20094": "PsP.3plf_Aux.j.jri̯.t",
        "20096": "PsP.3plf_Aux.others",
        "20097": "PsP.3plf_tw=",
        "20098": "PsP.3plf_Aux.wn.jn",
        "20099": "PsP.3plf_Aux.wn.ḫr",
        "20100": "PsP.2du",
        "20101": "PsP.2du_Aux.jw",
        "20102": "PsP.2du_Aux.jri̯",
        "20103": "PsP.2du_Aux.j.jri̯",
        "20104": "PsP.2du_Aux.j.jri̯.t",
        "20106": "PsP.2du_Aux.others",
        "20107": "PsP.2du_tw=",
        "20108": "PsP.2du_Aux.wn.jn",
        "20109": "PsP.2du_Aux.wn.ḫr",
        "20110": "PsP.3dum",
        "20111": "PsP.3dum_Aux.jw",
        "20112": "PsP.3dum_Aux.jri̯",
        "20113": "PsP.3dum_Aux.jr",
        "20114": "PsP.3dum_Aux.j.jri̯.t",
        "20116": "PsP.3dum_Aux.others",
        "20117": "PsP.3dum_tw=",
        "20118": "PsP.3dum_Aux.wn.jn",
        "20119": "PsP.3dum_Aux.wn.ḫr",
        "20120": "PsP.3duf",
        "20121": "PsP.3duf_Aux.jw",
        "20122": "PsP.3duf_Aux.jri̯",
        "20123": "PsP.3duf_Aux.j.jri̯",
        "20124": "PsP.3duf_Aux.j.jri̯.t",
        "20126": "PsP.3duf_Aux.others",
        "20127": "PsP.3duf_tw=",
        "20128": "PsP.3duf_Aux.wn.jn",
        "20129": "PsP.3duf_Aux.wn.ḫr",
        "20130": "PsP.1du",
        "20131": "PsP.1du_Aux.jw",
        "20132": "PsP.1du_Aux.jri̯",
        "20133": "PsP.1du_Aux.j.jri̯",
        "20134": "PsP.1du_Aux.j.jri̯.t",
        "20136": "PsP.1du_Aux.others",
        "20137": "PsP.1du_tw=",
        "20138": "PsP.1du_Aux.wn.jn",
        "20139": "PsP.1du_Aux.wn.ḫr",
        "20310": "PsP.3du",
        "20311": "PsP.3du_Aux.jw",
        "20312": "PsP.3du_Aux.jri̯",
        "20313": "PsP.3du_Aux.j.jri̯",
        "20314": "PsP.3du_Aux.j.jri̯.t",
        "20316": "PsP.3du_Aux.others",
        "20317": "PsP.3du_tw=",
        "20318": "PsP.3du_Aux.wn.jn",
        "20319": "PsP.3du_Aux.wn.ḫr",
        "20340": "PsP.3sg",
        "20341": "PsP.3sg_Aux.jw",
        "20342": "PsP.3sg_Aux.jri̯",
        "20343": "PsP.3sg_Aux.j.jri̯",
        "20344": "PsP.3sg_Aux.j.jri̯.t",
        "20346": "PsP.3sg_Aux.others",
        "20347": "PsP.3sg_tw=",
        "20348": "PsP.3sg_Aux.wn.jn",
        "20349": "PsP.3sg_Aux.wn.ḫr",
        "20380": "PsP.3pl",
        "20381": "PsP.3pl_Aux.jw",
        "20382": "PsP.3pl_Aux.jri̯",
        "20383": "PsP.3pl_Aux.j.jri̯",
        "20384": "PsP.3pl_Aux.j.jri̯.t",
        "20386": "PsP.3pl_Aux.others",
        "20387": "PsP.3pl_tw=",
        "20388": "PsP.3pl_Aux.wn.jn",
        "20389": "PsP.3pl_Aux.wn.ḫr",
        "21000": "PsP.prefx",
        "21010": "PsP.prefx.1sg",
        "21020": "PsP.prefx.2sgm",
        "21030": "PsP.prefx.2sgf",
        "21040": "PsP.prefx.3sgm",
        "21050": "PsP.prefx.3sgf",
        "21060": "PsP.prefx.1pl",
        "21070": "PsP.prefx.2pl",
        "21080": "PsP.prefx.3plm",
        "21090": "PsP.prefx.3plf",
        "21100": "PsP.prefx.2du",
        "21110": "PsP.prefx.3dum",
        "21120": "PsP.prefx.3duf",
        "21130": "PsP.prefx.1du",
        "21310": "PsP.prefx.3du",
        "21340": "PsP.prefx.3sg",
        "21380": "PsP.prefx.3plc",
        "22000": "PsP.gem",
        "22010": "PsP.gem.1sg",
        "22017": "PsP.gem.1sg_tw=",
        "22020": "PsP.gem.2sgm",
        "22027": "PsP.gem.2sgm_tw=",
        "22030": "PsP.gem.2sgf",
        "22037": "PsP.gem.2sgf_tw=",
        "22040": "PsP.gem.3sgm",
        "22041": "PsP.gem.3sgm_Aux.jw",
        "22047": "PsP.gem.3sgm_tw=",
        "22050": "PsP.gem.3sgf",
        "22051": "PsP.gem.3sgf_Aux.jw",
        "22057": "PsP.gem.3sgf_tw=",
        "22060": "PsP.gem.1pl",
        "22067": "PsP.gem.1pl_tw=",
        "22070": "PsP.gem.2pl",
        "22077": "PsP.gem.2pl_tw=",
        "22080": "PsP.gem.3plm",
        "22087": "PsP.gem.3plm_tw=",
        "22090": "PsP.gem.3plf",
        "22097": "PsP.gem.3plf_tw=",
        "22100": "PsP.gem.2du",
        "22107": "PsP.gem.2du_tw=",
        "22110": "PsP.gem.3dum",
        "22117": "PsP.gem.3dum_tw=",
        "22120": "PsP.gem.3duf",
        "22127": "PsP.gem.3duf_tw=",
        "22130": "PsP.gem.1du",
        "22137": "PsP.gem.1du_tw=",
        "22310": "PsP.gem.3du",
        "22317": "PsP.gem.3du_tw=",
        "22340": "PsP.gem.3sg",
        "22347": "PsP.gem.3sg_tw=",
        "22380": "PsP.gem.3pl",
        "22387": "PsP.gem.3pl_tw=",
        "23000": "PsP.unspec_Aux.ꜥḥꜥ.n",
        "23010": "PsP.1sg_Aux.ꜥḥꜥ.n",
        "23020": "PsP.2sgm_Aux.ꜥḥꜥ.n",
        "23030": "PsP.2sgf_Aux.ꜥḥꜥ.n",
        "23040": "PsP.3sgm_Aux.ꜥḥꜥ.n",
        "23050": "PsP.3sgf_Aux.ꜥḥꜥ.n",
        "23060": "PsP.1pl_Aux.ꜥḥꜥ.n",
        "23070": "PsP.2pl_Aux.ꜥḥꜥ.n",
        "23080": "PsP.3plm_Aux.ꜥḥꜥ.n",
        "23090": "PsP.3plf_Aux.ꜥḥꜥ.n",
        "23100": "PsP.2du_Aux.ꜥḥꜥ.n",
        "23110": "PsP.3dum_Aux.ꜥḥꜥ.n",
        "23120": "PsP.3duf_Aux.ꜥḥꜥ.n",
        "23130": "PsP.1du_Aux.ꜥḥꜥ.n",
        "23310": "PsP.3du_Aux.ꜥḥꜥ.n",
        "23340": "PsP.3sg_Aux.aux.ꜥḥꜥ.n",
        "23380": "PsP.3plc_Aux.ꜥḥꜥ.n",
        "24010": "PsP.1sg_Aux.wn",
        "24020": "PsP.2sgm_Aux.wn",
        "24030": "PsP.2sgf_Aux.wn",
        "24040": "PsP.3sgm_Aux.wn",
        "24050": "PsP.3sgf_Aux.wn",
        "24060": "PsP.1pl_Aux.wn",
        "24070": "PsP.2pl_Aux.wn",
        "24080": "PsP.3plm_Aux.wn",
        "24090": "PsP.3plf_Aux.wn",
        "24100": "PsP.2du_Aux.wn",
        "24110": "PsP.3dum_Aux.wn",
        "24120": "PsP.3duf_Aux.wn",
        "24130": "PsP.1du_Aux.wn",
        "24310": "PsP.3du_Aux.wn",
        "24340": "PsP.3sg_Aux.wn",
        "24380": "PsP.3plc_Aux.wn",
        "25010": "PsP.1sg_Aux.mk",
        "25020": "PsP.2sgm_Aux.mk",
        "25030": "PsP.2sgf_Aux.mk",
        "25040": "PsP.3sgm_Aux.mk",
        "25050": "PsP.3sgf_Aux.mk",
        "25060": "PsP.1pl_Aux.mk",
        "25070": "PsP.2pl_Aux.mk",
        "25080": "PsP.3plm_Aux.mk",
        "25090": "PsP.3plf_Aux.mk",
        "25100": "PsP.2du_Aux.mk",
        "25110": "PsP.3dum_Aux.mk",
        "25120": "PsP.3duf_Aux.mk",
        "25130": "PsP.1du_Aux.mk",
        "25310": "PsP.3du_Aux.mk",
        "25340": "PsP.3sg_Aux.mk",
        "25380": "PsP.3plc_Aux.mk",
        "26010": "PsP.1sg_Neg.bn + tw= (jwnꜣ)",
        "26020": "PsP.2sgm_Neg.bn + tw= (jwnꜣ)",
        "26030": "PsP.2sgf_Neg.bn + tw= (jwnꜣ)",
        "26040": "PsP.3sgm_Neg.bn + tw= (jwnꜣ)",
        "26050": "PsP.3sgf_Neg.bn + tw= (jwnꜣ)",
        "26060": "PsP.1pl_Neg.bn + tw= (jwnꜣ)",
        "26070": "PsP.2pl_Neg.bn + tw= (jwnꜣ)",
        "26080": "PsP.3plm_Neg.bn + tw= (jwnꜣ)",
        "26090": "PsP.3plf_Neg.bn + tw= (jwnꜣ)",
        "26100": "PsP.2du_Neg.bn + tw= (jwnꜣ)",
        "26110": "PsP.3dum_Aux.bn + tw= (jwnꜣ)",
        "26120": "PsP.3duf_Neg.bn + tw= (jwnꜣ)",
        "26130": "PsP.1du_Neg.bn + tw= (jwnꜣ)",
        "26310": "PsP.3du_Neg.bn + tw= (jwnꜣ)",
        "26340": "PsP.3sg_Neg.bn + tw= (jwnꜣ)",
        "26380": "PsP.3plc_Neg.bn + tw= (jwnꜣ)",
        "27010": "PsP.1sg_Aux.wnn",
        "27020": "PsP.2sgm_Aux.wnn",
        "27030": "PsP.2sgf_Aux.wnn",
        "27040": "PsP.3sgm_Aux.wnn",
        "27050": "PsP.3sgf_Aux.wnn",
        "27060": "PsP.1pl_Aux.wnn",
        "27070": "PsP.2pl_Aux.wnn",
        "27080": "PsP.3plm_Aux.wnn",
        "27090": "PsP.3plf_Aux.wnn",
        "27100": "PsP.2du_Aux.wnn",
        "27110": "PsP.3dum_Aux.wnn",
        "27120": "PsP.3duf_Aux.wnn",
        "27130": "PsP.1du_Aux.wnn",
        "27310": "PsP.3du_Aux.wnn",
        "27340": "PsP.3sg_Aux.wnn",
        "27380": "PsP.3plc_Aux.wnn",
        "30000": "Partcp",
        "30010": "Partcp.act.ngem.sgm",
        "30011": "Partcp.act.ngem.sgm.stpr.1sg",
        "30014": "Partcp.act.ngem.sgm.stpr.3sgm",
        "30015": "Partcp.act.ngem.sgm.stpr.3sgf",
        "30020": "Partcp.act.ngem.sgf",
        "30022": "Partcp.act.ngem.sgf.stpr.2sgm",
        "30030": "Partcp.act.ngem.plm",
        "30034": "Partcp.act.ngem.plm.stpr.3sgm",
        "30040": "Partcp.act.ngem.plf",
        "30050": "Partcp.act.ngem.dum",
        "30060": "Partcp.act.ngem.duf",
        "30070": "Partcp.pass.ngem.sgm",
        "30071": "Partcp.pass.ngem.sgm.stpr.1sg",
        "30072": "Partcp.pass.ngem.sgm.stpr.2sgm",
        "30073": "Partcp.pass.ngem.sgm.stpr.2sgf",
        "30074": "Partcp.pass.ngem.sgm.stpr.3sgm",
        "30075": "Partcp.pass.ngem.sgm.stpr.3sgf",
        "30080": "Partcp.pass.ngem.sgf",
        "30082": "Partcp.pass.ngem.sgf.stpr.2sgm",
        "30084": "Partcp.pass.ngem.sgf.stpr.3sgm",
        "30089": "Partcp.pass.ngem.sgf.stpr.3pl",
        "30090": "Partcp.pass.ngem.plm",
        "30097": "Partcp.pass.ngem.plm.stpr.1pl",
        "30100": "Partcp.pass.ngem.plf",
        "30104": "Partcp.pass.ngem.plf.stpr.3sgm",
        "30110": "Partcp.pass.ngem.dum",
        "30120": "Partcp.pass.ngem.duf",
        "30320": "Partcp.act.ngem.f",
        "30380": "Partcp.pass.ngem.f",
        "30510": "Partcp.act.ngem._nfr-sw",
        "30570": "Partcp.pass.ngem._nfr-sw",
        "31000": "Partcp.act.gem",
        "31010": "Partcp.act.gem.sgm",
        "31014": "Partcp.act.gem.sgm.stpr.3sgm",
        "31020": "Partcp.act.gem.sgf",
        "31021": "Partcp.act.gem.sgf.stpr.1sg",
        "31030": "Partcp.act.gem.plm",
        "31040": "Partcp.act.gem.plf",
        "31050": "Partcp.act.gem.dum",
        "31060": "Partcp.act.gem.duf",
        "31070": "Partcp.pass.gem.sgm",
        "31080": "Partcp.pass.gem.sgf",
        "31090": "Partcp.pass.gem.plm",
        "31100": "Partcp.pass.gem.plf",
        "31110": "Partcp.pass.gem.dum",
        "31120": "Partcp.pass.gem.duf",
        "31320": "Partcp.act.gem.f",
        "31380": "Partcp.pass.gem.f",
        "32000": "Partcp.act.prefx",
        "32010": "Partcp.act.prefx.sgm",
        "32011": "Partcp.act.prefx.sgm.stpr.1sg",
        "32020": "Partcp.act.prefx.sgf",
        "32030": "Partcp.act.prefx.plm",
        "32040": "Partcp.act.prefx.plf",
        "32050": "Partcp.act.prefx.dum",
        "32060": "Partcp.act.prefx.duf",
        "32070": "Partcp.pass.prefx.sgm",
        "32072": "Partcp.pass.prefx.sgm.stpr.2sgm",
        "32080": "Partcp.pass.prefx.sgf",
        "32090": "Partcp.pass.prefx.plm",
        "32100": "Partcp.pass.prefx.plf",
        "32110": "Partcp.pass.prefx.dum",
        "32120": "Partcp.pass.prefx.duf",
        "32320": "Partcp.act.prefx.f",
        "32380": "Partcp.pass.prefx.f",
        "40000": "Rel.form.unspec",
        "40004": "Rel.unspec.3sgm",
        "40010": "Rel.form.n.sgm.nom.subj",
        "40011": "Rel.form.n.sgm.1sg",
        "40012": "Rel.form.n.sgm.2sgm",
        "40013": "Rel.form.n.sgm.2sgf",
        "40014": "Rel.form.n.sgm.3sgm",
        "40015": "Rel.form.n.sgm.3sgf",
        "40016": "Rel.form.n.sgm.3sg",
        "40017": "Rel.form.n.sgm.1pl",
        "40018": "Rel.form.n.sgm.2pl",
        "40019": "Rel.form.n.sgm.3pl",
        "40020": "Rel.form.n.sgf.nom.subj",
        "40021": "Rel.form.n.sgf.1sg",
        "40022": "Rel.form.n.sgf.2sgm",
        "40023": "Rel.form.n.sgf.2sgf",
        "40024": "Rel.form.n.sgf.3sgm",
        "40025": "Rel.form.n.sgf.3sgf",
        "40026": "Rel.form.n.sgf.3sg",
        "40027": "Rel.form.n.sgf.1pl",
        "40028": "Rel.form.n.sgf.2pl",
        "40029": "Rel.form.n.sgf.3pl",
        "40030": "Rel.form.n.plm.nom.subj",
        "40031": "Rel.form.n.plm.1sg",
        "40032": "Rel.form.n.plm.2sgm",
        "40033": "Rel.form.n.plm.2sgf",
        "40034": "Rel.form.n.plm.3sgm",
        "40035": "Rel.form.n.plm.3sgf",
        "40036": "Rel.form.n.plm.3sg",
        "40037": "Rel.form.n.plm.1pl",
        "40038": "Rel.form.n.plm.2pl",
        "40039": "Rel.form.n.plm.3pl",
        "40040": "Rel.form.n.plf.nom.subj",
        "40041": "Rel.form.n.plf.1sg",
        "40042": "Rel.form.n.plf.2sgm",
        "40043": "Rel.form.n.plf.2sgf",
        "40044": "Rel.form.n.plf.3sgm",
        "40045": "Rel.form.n.plf.3sgf",
        "40046": "Rel.form.n.plf.3sg",
        "40047": "Rel.form.n.plf.1pl",
        "40048": "Rel.form.n.plf.2pl",
        "40049": "Rel.form.n.plf.3pl",
        "40050": "Rel.form.n.dum.nom.subj",
        "40051": "Rel.form.n.dum.1sg",
        "40052": "Rel.form.n.dum.2sgm",
        "40053": "Rel.form.n.dum.2sgf",
        "40054": "Rel.form.n.dum.3sgm",
        "40055": "Rel.form.n.dum.3sgf",
        "40056": "Rel.form.n.dum.3sg",
        "40057": "Rel.form.n.dum.1pl",
        "40058": "Rel.form.n.dum.2pl",
        "40059": "Rel.form.n.dum.3pl",
        "40060": "Rel.form.n.duf.nom.subj",
        "40061": "Rel.form.n.duf.1sg",
        "40062": "Rel.form.n.duf.2sgm",
        "40063": "Rel.form.n.duf.2sgf",
        "40064": "Rel.form.n.duf.3sgm",
        "40065": "Rel.form.n.duf.3sgf",
        "40066": "Rel.form.n.duf.3sg",
        "40067": "Rel.form.n.duf.1pl",
        "40068": "Rel.form.n.duf.2pl",
        "40069": "Rel.form.n.duf.3pl",
        "40070": "Rel.form.ngem.sgm.nom.subj",
        "40071": "Rel.form.ngem.sgm.1sg",
        "40072": "Rel.form.ngem.sgm.2sgm",
        "40073": "Rel.form.ngem.sgm.2sgf",
        "40074": "Rel.form.ngem.sgm.3sgm",
        "40075": "Rel.form.ngem.sgm.3sgf",
        "40076": "Rel.form.ngem.sgm.3sg",
        "40077": "Rel.form.ngem.sgm.1pl",
        "40078": "Rel.form.ngem.sgm.2pl",
        "40079": "Rel.form.ngem.sgm.3pl",
        "40080": "Rel.form.ngem.sgf.nom.subj",
        "40081": "Rel.form.ngem.sgf.1sg",
        "40082": "Rel.form.ngem.sgf.2sgm",
        "40083": "Rel.form.ngem.sgf.2sgf",
        "40084": "Rel.form.ngem.sgf.3sgf",
        "40085": "Rel.form.ngem.sgf.3sgf",
        "40086": "Rel.form.ngem.sgf.3sg",
        "40087": "Rel.form.ngem.sgf.1pl",
        "40088": "Rel.form.ngem.sgf.2pl",
        "40089": "Rel.form.ngem.sgf.3pl",
        "40090": "Rel.form.ngem.plm.nom.subj",
        "40091": "Rel.form.ngem.plm.1sg",
        "40092": "Rel.form.ngem.plm.2sgm",
        "40093": "Rel.form.ngem.plm.2sgf",
        "40094": "Rel.form.ngem.plm.3sgm",
        "40095": "Rel.form.ngem.plm.3sgf",
        "40096": "Rel.form.ngem.plm.3sg",
        "40097": "Rel.form.ngem.plm.1pl",
        "40098": "Rel.form.ngem.plm.2pl",
        "40099": "Rel.form.ngem.plm.3pl",
        "40100": "Rel.form.ngem.plf.nom.subj",
        "40101": "Rel.form.ngem.plf.1sg",
        "40102": "Rel.form.ngem.plf.2sgm",
        "40103": "Rel.form.ngem.plf.2sgf",
        "40104": "Rel.form.ngem.plf.3sgm",
        "40105": "Rel.form.ngem.plf.3sgf",
        "40106": "Rel.form.ngem.plf.3sg",
        "40107": "Rel.form.ngem.plf.1pl",
        "40108": "Rel.form.ngem.plf.2pl",
        "40109": "Rel.form.ngem.plf.3pl",
        "40110": "Rel.form.ngem.dum.nom.subj",
        "40111": "Rel.form.ngem.dum.1sg",
        "40112": "Rel.form.ngem.dum.2sgm",
        "40113": "Rel.form.ngem.dum.2sgf",
        "40114": "Rel.form.ngem.dum.3sgm",
        "40115": "Rel.form.ngem.dum.3sgf",
        "40116": "Rel.form.ngem.dum.3sg",
        "40117": "Rel.form.ngem.dum.1pl",
        "40118": "Rel.form.ngem.dum.2pl",
        "40119": "Rel.form.ngem.dum.3pl",
        "40120": "Rel.form.ngem.duf.nom.subj",
        "40121": "Rel.form.ngem.duf.1sg",
        "40122": "Rel.form.ngem.duf.2sgf",
        "40123": "Rel.form.ngem.duf.2sgf",
        "40124": "Rel.form.ngem.duf.3sgm",
        "40125": "Rel.form.ngem.duf.3sgf",
        "40126": "Rel.form.ngem.duf.3sg",
        "40127": "Rel.form.ngem.duf.1pl",
        "40128": "Rel.form.ngem.duf.2pl",
        "40129": "Rel.form.ngem.duf.3pl",
        "40320": "Rel.form.n.f",
        "40380": "Rel.form.ngem.f",
        "41000": "Rel.form.gem.unspec",
        "41010": "Rel.form.n.gem.sgm.nom.subj",
        "41011": "Rel.form.n.gem.sgm.1sg",
        "41012": "Rel.form.n.gem.sgm.2sgm",
        "41013": "Rel.form.n.gem.sgm.2sgf",
        "41014": "Rel.form.n.gem.sgm.3sgm",
        "41015": "Rel.form.n.gem.sgm.3sgf",
        "41016": "Rel.form.n.gem.sgm.3sg",
        "41017": "Rel.form.n.gem.sgm.1pl",
        "41018": "Rel.form.n.gem.sgm.2pl",
        "41019": "Rel.form.n.gem.sgm.3pl",
        "41020": "Rel.form.n.gem.sgf.nom.subj",
        "41021": "Rel.form.n.gem.sgf.1sg",
        "41022": "Rel.form.n.gem.sgf.2sgm",
        "41023": "Rel.form.n.gem.sgf.2sgf",
        "41024": "Rel.form.n.gem.sgf.3sgm",
        "41025": "Rel.form.n.gem.sgf.3sgf",
        "41026": "Rel.form.n.gem.sgf.3sg",
        "41027": "Rel.form.n.gem.sgf.1pl",
        "41028": "Rel.form.n.gem.sgf.2pl",
        "41029": "Rel.form.n.gem.sgf.3pl",
        "41030": "Rel.form.n.gem.plm.nom.subj",
        "41031": "Rel.form.n.gem.plm.1sg",
        "41032": "Rel.form.n.gem.plm.2sgm",
        "41033": "Rel.form.n.gem.plm.2sgf",
        "41034": "Rel.form.n.gem.plm.3sgm",
        "41035": "Rel.form.n.gem.plm.3sgf",
        "41036": "Rel.form.n.gem.plm.3sg",
        "41037": "Rel.form.n.gem.plm.1pl",
        "41038": "Rel.form.n.gem.plm.2pl",
        "41039": "Rel.form.n.gem.plm.3pl",
        "41040": "Rel.form.n.gem.plf.nom.subj",
        "41041": "Rel.form.n.gem.plf.1sg",
        "41042": "Rel.form.n.gem.plf.2sgm",
        "41043": "Rel.form.n.gem.plf.2sgf",
        "41044": "Rel.form.n.gem.plf.3sgm",
        "41045": "Rel.form.n.gem.plf.3sgf",
        "41046": "Rel.form.n.gem.plf.3sg",
        "41047": "Rel.form.n.gem.plf.1pl",
        "41048": "Rel.form.n.gem.plf.2pl",
        "41049": "Rel.form.n.gem.plf.3pl",
        "41050": "Rel.form.n.gem.dum.nom.subj",
        "41051": "Rel.form.n.gem.dum.1sg",
        "41052": "Rel.form.n.gem.dum.2sgm",
        "41053": "Rel.form.n.gem.dum.2sgf",
        "41054": "Rel.form.n.gem.dum.3sgm",
        "41055": "Rel.form.n.gem.dum.3sgf",
        "41056": "Rel.form.n.gem.dum.3sg",
        "41057": "Rel.form.n.gem.dum.1pl",
        "41058": "Rel.form.n.gem.dum.2pl",
        "41059": "Rel.form.n.gem.dum.3pl",
        "41060": "Rel.form.n.gem.duf.nom.subj",
        "41061": "Rel.form.n.gem.duf.1sg",
        "41062": "Rel.form.n.gem.duf.2sgm",
        "41063": "Rel.form.n.gem.duf.2sgf",
        "41064": "Rel.form.n.gem.duf.3sgm",
        "41065": "Rel.form.n.gem.duf.3sgf",
        "41066": "Rel.form.n.gem.duf.3sg",
        "41067": "Rel.form.n.gem.duf.1pl",
        "41068": "Rel.form.n.gem.duf.2pl",
        "41069": "Rel.form.n.gem.duf.3pl",
        "41070": "Rel.form.gem.sgm.nom.subj",
        "41071": "Rel.form.gem.sgm.1sg",
        "41072": "Rel.form.gem.sgm.2sgm",
        "41073": "Rel.form.gem.sgm.2sgf",
        "41074": "Rel.form.gem.sgm.3sgm",
        "41075": "Rel.form.gem.sgm.3sgf",
        "41076": "Rel.form.gem.sgm.3sg",
        "41077": "Rel.form.gem.sgm.1pl",
        "41078": "Rel.form.gem.sgm.2pl",
        "41079": "Rel.form.gem.sgm.3pl",
        "41080": "Rel.form.gem.sgf.nom.subj",
        "41081": "Rel.form.gem.sgf.1sg",
        "41082": "Rel.form.gem.sgf.2sgm",
        "41083": "Rel.form.gem.sgf.2sgf",
        "41084": "Rel.form.gem.sgf.3sgm",
        "41085": "Rel.form.gem.sgf.3sgf",
        "41086": "Rel.form.gem.sgf.3sg",
        "41087": "Rel.form.gem.sgf.1pl",
        "41088": "Rel.form.gem.sgf.2pl",
        "41089": "Rel.form.gem.sgf.3pl",
        "41090": "Rel.form.gem.plm.nom.subj",
        "41091": "Rel.form.gem.plm.1sg",
        "41092": "Rel.form.gem.plm.2sgm",
        "41093": "Rel.form.gem.plm.2sgf",
        "41094": "Rel.form.gem.plm.3sgm",
        "41095": "Rel.form.gem.plm.3sgf",
        "41096": "Rel.form.gem.plm.3sg",
        "41097": "Rel.form.gem.plm.1pl",
        "41098": "Rel.form.gem.plm.2pl",
        "41099": "Rel.form.gem.plm.3pl",
        "41100": "Rel.form.gem.plf.nom.subj",
        "41101": "Rel.form.gem.plf.1sg",
        "41102": "Rel.form.gem.plf.2sgm",
        "41103": "Rel.form.gem.plf.2sgf",
        "41104": "Rel.form.gem.plf.3sgm",
        "41105": "Rel.form.gem.plf.3sgf",
        "41106": "Rel.form.gem.plf.3sg",
        "41107": "Rel.form.gem.plf.1pl",
        "41108": "Rel.form.gem.plf.2pl",
        "41109": "Rel.form.gem.plf.3pl",
        "41110": "Rel.form.gem.dum.nom.subj",
        "41111": "Rel.form.gem.dum.1sg",
        "41112": "Rel.form.gem.dum.2sgm",
        "41113": "Rel.form.gem.dum.2sgf",
        "41114": "Rel.form.gem.dum.3sgm",
        "41115": "Rel.form.gem.dum.3sgf",
        "41116": "Rel.form.gem.dum.3sg",
        "41117": "Rel.form.gem.dum.1pl",
        "41118": "Rel.form.gem.dum.2pl",
        "41119": "Rel.form.gem.dum.3pl",
        "41120": "Rel.form.gem.duf.nom.subj",
        "41121": "Rel.form.gem.duf.1sg",
        "41122": "Rel.form.gem.duf.2sgm",
        "41123": "Rel.form.gem.duf.2sgf",
        "41124": "Rel.form.gem.duf.3sgm",
        "41125": "Rel.form.gem.duf.3sgf",
        "41126": "Rel.form.gem.duf.3sg",
        "41127": "Rel.form.gem.duf.1pl",
        "41128": "Rel.form.gem.duf.2pl",
        "41129": "Rel.form.gem.duf.3pl",
        "41320": "Rel.form.n.gem.f",
        "41380": "Rel.form.gem.f",
        "42000": "Rel.form.prefx.unspec",
        "42002": "Rel.form.prefx.unspec.2sgm",
        "42004": "Rel.form.prefx.unspec.3sgm",
        "42006": "Rel.form.prefx.unspec.3sg",
        "42010": "Rel.form.n.prefx.sgm.nom.subj",
        "42011": "Rel.form.n.prefx.sgm.1sg",
        "42012": "Rel.form.n.prefx.sgm.2sgm",
        "42013": "Rel.form.n.prefx.sgm.2sgf",
        "42014": "Rel.form.n.prefx.sgm.3sgm",
        "42015": "Rel.form.n.prefx.sgm.3sgf",
        "42016": "Rel.form.n.prefx.sgm.3sg",
        "42017": "Rel.form.n.prefx.sgm.1pl",
        "42018": "Rel.form.n.prefx.sgm.2pl",
        "42019": "Rel.form.n.prefx.sgm.3pl",
        "42020": "Rel.form.n.prefx.sgf.nom.subj",
        "42021": "Rel.form.n.prefx.sgf.1sg",
        "42022": "Rel.form.n.prefx.sgf.2sgm",
        "42023": "Rel.form.n.prefx.sgf.2sgf",
        "42024": "Rel.form.n.prefx.sgf.3sgm",
        "42025": "Rel.form.n.prefx.sgf.3sgf",
        "42026": "Rel.form.n.prefx.sgf.3sg",
        "42027": "Rel.form.n.prefx.sgf.1pl",
        "42028": "Rel.form.n.prefx.sgf.2pl",
        "42029": "Rel.form.n.prefx.sgf.3pl",
        "42030": "Rel.form.n.prefx.plm.nom.subj",
        "42031": "Rel.form.n.prefx.plm.1sg",
        "42032": "Rel.form.n.prefx.plm.2sgm",
        "42033": "Rel.form.n.prefx.plm.2sgf",
        "42034": "Rel.form.n.prefx.plm.3sgm",
        "42035": "Rel.form.n.prefx.plm.3sgf",
        "42036": "Rel.form.n.prefx.plm.3sg",
        "42037": "Rel.form.n.prefx.plm.1pl",
        "42038": "Rel.form.n.prefx.plm.2pl",
        "42039": "Rel.form.n.prefx.plm.3pl",
        "42040": "Rel.form.n.prefx.plf.nom.subj",
        "42041": "Rel.form.n.prefx.plf.1sg",
        "42042": "Rel.form.n.prefx.plf.2sgm",
        "42043": "Rel.form.n.prefx.plf.2sgf",
        "42044": "Rel.form.n.prefx.plf.3sgm",
        "42045": "Rel.form.n.prefx.plf.3sgf",
        "42046": "Rel.form.n.prefx.plf.3sg",
        "42047": "Rel.form.n.prefx.plf.1pl",
        "42048": "Rel.form.n.prefx.plf.2pl",
        "42049": "Rel.form.n.prefx.plf.3pl",
        "42050": "Rel.form.n.prefx.dum.nom.subj",
        "42051": "Rel.form.n.prefx.dum.1sg",
        "42052": "Rel.form.n.prefx.dum.2sgm",
        "42053": "Rel.form.n.prefx.dum.2sgf",
        "42054": "Rel.form.n.prefx.dum.3sgm",
        "42055": "Rel.form.n.prefx.dum.3sgf",
        "42056": "Rel.form.n.prefx.dum.3sg",
        "42057": "Rel.form.n.prefx.dum.1pl",
        "42058": "Rel.form.n.prefx.dum.2pl",
        "42059": "Rel.form.n.prefx.dum.3pl",
        "42060": "Rel.form.n.prefx.duf.nom.subj",
        "42061": "Rel.form.n.prefx.duf.1sg",
        "42062": "Rel.form.n.prefx.duf.2sgm",
        "42063": "Rel.form.n.prefx.duf.2sgf",
        "42064": "Rel.form.n.prefx.duf.3sgm",
        "42065": "Rel.form.n.prefx.duf.3sgf",
        "42066": "Rel.form.n.prefx.duf.3sg",
        "42067": "Rel.form.n.prefx.duf.1pl",
        "42068": "Rel.form.n.prefx.duf.2pl",
        "42069": "Rel.form.n.prefx.duf.3pl",
        "42070": "Rel.form.prefx.sgm.nom.subj",
        "42071": "Rel.form.prefx.sgm.1sg",
        "42072": "Rel.form.prefx.sgm.2sgm",
        "42073": "Rel.form.prefx.sgm.2sgf",
        "42074": "Rel.form.prefx.sgm.3sgm",
        "42075": "Rel.form.prefx.sgm.3sgf",
        "42076": "Rel.form.prefx.sgm.3sg",
        "42077": "Rel.form.prefx.sgm.1pl",
        "42078": "Rel.form.prefx.sgm.2pl",
        "42079": "Rel.form.prefx.sgm.3pl",
        "42080": "Rel.form.prefx.sgf.nom.subj",
        "42081": "Rel.form.prefx.sgf.1sg",
        "42082": "Rel.form.prefx.sgf.2sgm",
        "42083": "Rel.form.prefx.sgf.2sgf",
        "42084": "Rel.form.prefx.sgf.3sgm",
        "42085": "Rel.form.prefx.sgf.3sgf",
        "42086": "Rel.form.prefx.sgf.3sg",
        "42087": "Rel.form.prefx.sgf.1pl",
        "42088": "Rel.form.prefx.sgf.2pl",
        "42089": "Rel.form.prefx.sgf.3pl",
        "42090": "Rel.form.prefx.plm.nom.subj",
        "42091": "Rel.form.prefx.plm.1sg",
        "42092": "Rel.form.prefx.plm.2sgm",
        "42093": "Rel.form.prefx.plm.2sgf",
        "42094": "Rel.form.prefx.plm.3sgm",
        "42095": "Rel.form.prefx.plm.3sgf",
        "42096": "Rel.form.prefx.plm.3sg",
        "42097": "Rel.form.prefx.plm.1pl",
        "42098": "Rel.form.prefx.plm.2pl",
        "42099": "Rel.form.prefx.plm.3pl",
        "42100": "Rel.form.prefx.plf.nom.subj",
        "42101": "Rel.form.prefx.plf.1sg",
        "42102": "Rel.form.prefx.plf.2sgm",
        "42103": "Rel.form.prefx.plf.2sgf",
        "42104": "Rel.form.prefx.plf.3sgm",
        "42105": "Rel.form.prefx.plf.3sgf",
        "42106": "Rel.form.prefx.plf.3sg",
        "42107": "Rel.form.prefx.plf.1pl",
        "42108": "Rel.form.prefx.plf.2pl",
        "42109": "Rel.form.prefx.plf.3pl",
        "42110": "Rel.form.prefx.dum.nom.subj",
        "42111": "Rel.form.prefx.dum.1sg",
        "42112": "Rel.form.prefx.dum.2sgm",
        "42113": "Rel.form.prefx.dum.2sgf",
        "42114": "Rel.form.prefx.dum.3sgm",
        "42115": "Rel.form.prefx.dum.3sgf",
        "42116": "Rel.form.prefx.dum.3sg",
        "42117": "Rel.form.prefx.dum.1pl",
        "42118": "Rel.form.prefx.dum.2pl",
        "42119": "Rel.form.prefx.dum.3pl",
        "42120": "Rel.form.prefx.duf.nom.subj",
        "42121": "Rel.form.prefx.duf.1sg",
        "42122": "Rel.form.prefx.duf.2sgm",
        "42123": "Rel.form.prefx.duf.2sgf",
        "42124": "Rel.form.prefx.duf.3sgm",
        "42125": "Rel.form.prefx.duf.3sgf",
        "42126": "Rel.form.prefx.duf.3sg",
        "42127": "Rel.form.prefx.duf.1pl",
        "42128": "Rel.form.prefx.duf.2pl",
        "42129": "Rel.form.prefx.duf.3pl",
        "42320": "Rel.form.n.prefx.f",
        "42380": "Rel.form.prefx.f",
        "50000": "Imp",
        "50010": "Imp.sg",
        "50020": "Imp.pl",
        "50030": "Imp.du",
        "50040": "Imp.jmi̯.tw=?",
        "50041": "Imp.jmi̯.tw=1sg",
        "50042": "Imp.jmi̯.tw=2sgm",
        "50043": "Imp.jmi̯.tw=2sgf",
        "50044": "Imp.jmi̯.tw=3sgm",
        "50045": "Imp.jmi̯.tw=3sgf",
        "50046": "Imp.jmi̯.tw=3sg",
        "50047": "Imp.jmi̯.tw=1pl",
        "50048": "Imp.jmi̯.tw=2pl",
        "50049": "Imp.jmi̯.tw=3pl",
        "51000": "Imp.prefx.",
        "51010": "Imp.prefx.sg",
        "51020": "Imp.prefx.pl",
        "51030": "Imp.prefx.du",
        "52000": "Imp.gem",
        "52010": "Imp.gem.sg",
        "52020": "Imp.gem.pl",
        "52030": "Imp.gem.du",
        "60000": "Nom.verbal.form/Adv.verbal.form",
        "60100": "Verbal.noun.unmarked",
        "60102": "Verbal.noun.unmarked.stpr.2sgm",
        "60104": "Verbal.noun.unmarked.stpr.3sgm",
        "60200": "Verbal.noun.w",
        "60209": "Verbal.noun.w.stpr.3pl",
        "60300": "Verbal.noun.t",
        "60400": "Verbal.noun.wt/jt",
        "60500": "Verbal.noun.gem",
        "60600": "Verbal.noun",
        "60700": "Inf",
        "61000": "Inf",
        "61001": "Inf.stpr.1sg",
        "61002": "Inf.stpr.2sgm",
        "61003": "Inf.stpr.2sgf",
        "61004": "Inf.stpr.3sgm",
        "61005": "Inf.stpr.3sgf",
        "61006": "Inf.stpr.3sg",
        "61007": "Inf.stpr.1pl",
        "-61007": "Inf.stpr.1du",
        "61008": "Inf.stpr.2pl",
        "-61008": "Inf.stpr.2du",
        "61009": "Inf.stpr.3pl",
        "-61009": "Inf.stpr.3du",
        "61010": "Inf_Aux.jw",
        "61011": "Inf.stpr.1sg_Aux.jw",
        "61012": "Inf.stpr.2sgm_Aux.jw",
        "61013": "Inf.stpr.2sgf_Aux.jw",
        "61014": "Inf.stpr.3sgm_Aux.jw",
        "61015": "Inf.stpr.3sgf_Aux.jw",
        "61016": "Inf.stpr.3sg_Aux.jw",
        "61017": "Inf.stpr.1pl_Aux.jw",
        "-61017": "Inf.stpr.1du_Aux.jw",
        "61018": "Inf.stpr.2pl_Aux.jw",
        "-61018": "Inf.stpr.2du_Aux.jw",
        "61019": "Inf.stpr.3pl_Aux.jw",
        "-61019": "Inf.stpr.3du_Aux.jw",
        "61020": "Inf_Aux.jri̯",
        "61021": "Inf.stpr.1sg_Aux.jri̯",
        "61022": "Inf.stpr.2sgm_Aux.jri̯",
        "61023": "Inf.stpr.2sgf_Aux.jri̯",
        "61024": "Inf.stpr.3sgm_Aux.jri̯",
        "61025": "Inf.stpr.3sgf_Aux.jri̯",
        "61026": "Inf.stpr.3sg_Aux.jri̯",
        "61027": "Inf.stpr.1pl_Aux.jri̯",
        "-61027": "Inf.stpr.1du_Aux.jri̯",
        "61028": "Inf.stpr.2pl_Aux.jri̯",
        "-61028": "Inf.stpr.2du_Aux.jri̯",
        "61029": "Inf.stpr.3pl_Aux.jri̯",
        "-61029": "Inf.stpr.3du_Aux.jri̯",
        "61030": "Inf_Aux.j.jri̯",
        "61031": "Inf.stpr.1sg_Aux.j.jri̯",
        "61032": "Inf.stpr.2sgm_Aux.j.jri̯",
        "61033": "Inf.stpr.2sgf_Aux.j.jri̯",
        "61034": "Inf.stpr.3sgm_Aux.j.jri̯",
        "61035": "Inf.stpr.3sgf_Aux.j.jri̯",
        "61036": "Inf.stpr.3sg_Aux.j.jri̯",
        "61037": "Inf.stpr.1pl_Aux.j.jri̯",
        "-61037": "Inf.stpr.1du_Aux.j.jri̯",
        "61038": "Inf.stpr.2pl_Aux.j.jri̯",
        "-61038": "Inf.stpr.2du_Aux.j.jri̯",
        "61039": "Inf.stpr.3pl_Aux.j.jri̯",
        "-61039": "Inf.stpr.3du_Aux.j.jri̯",
        "61040": "Inf_Aux.j.jri̯.t",
        "61041": "Inf.stpr.1sg_Aux.j.jri̯.t",
        "61042": "Inf.stpr.2sgm_Aux.j.jri̯.t",
        "61043": "Inf.stpr.2sgf_Aux.j.jri̯.t",
        "61044": "Inf.stpr.3sgm_Aux.j.jri̯.t",
        "61045": "Inf.stpr.3sgf_Aux.j.jri̯.t",
        "61046": "Inf.stpr.3sg_Aux.j.jri̯.t",
        "61047": "Inf.stpr.1pl_Aux.j.jri̯.t",
        "-61047": "Inf.stpr.1du_Aux.j.jri̯.t",
        "61048": "Inf.stpr.2pl_Aux.j.jri̯.t",
        "-61048": "Inf.stpr.2du_Aux.j.jri̯.t",
        "61049": "Inf.stpr.3pl_Aux.j.jri̯.t",
        "-61049": "Inf.stpr.3du_Aux.j.jri̯.t",
        "61050": "Inf_Neg.bwpw",
        "61051": "Inf.stpr.1sg_Neg.bwpw",
        "61052": "Inf.stpr.2sgm_Neg.bwpw",
        "61053": "Inf.stpr.2sgf_Neg.bwpw",
        "61054": "Inf.stpr.3sgm_Neg.bwpw",
        "61055": "Inf.stpr.3sgf_Neg.bwpw",
        "61056": "Inf.stpr.3sg_Neg.bwpw",
        "61057": "Inf.stpr.1pl_Neg.bwpw",
        "-61057": "Inf.stpr.1du_Neg.bwpw",
        "61058": "Inf.stpr.2pl_Neg.bwpw",
        "-61058": "Inf.stpr.2du_Neg.bwpw",
        "61059": "Inf.stpr.3pl_Neg.bwpw",
        "-61059": "Inf.stpr.3du_Neg.bwpw",
        "61060": "Inf_Aux.mtw=",
        "61061": "Inf.stpr.1sg_Aux.mtw=",
        "61062": "Inf.stpr.2sgm_Aux.mtw=",
        "61063": "Inf.stpr.2sgf_Aux.mtw=",
        "61064": "Inf.stpr.3sgm_Aux.mtw=",
        "61065": "Inf.stpr.3sgf_Aux.mtw=",
        "61066": "Inf.stpr.3sg_Aux.mtw=",
        "61067": "Inf.stpr.1pl_Aux.mtw=",
        "-61067": "Inf.stpr.1du_Aux.mtw=",
        "61068": "Inf.stpr.2pl_Aux.mtw=",
        "-61068": "Inf.stpr.2du_Aux.mtw=",
        "61069": "Inf.stpr.3pl_Aux.mtw=",
        "-61069": "Inf.stpr.3du_Aux.mtw=",
        "61070": "Inf_Aux.tw=",
        "61071": "Inf.stpr.1sg_Aux.tw=",
        "61072": "Inf.stpr.2sgm_Aux.tw=",
        "61073": "Inf.stpr.2sgf_Aux.tw=",
        "61074": "Inf.stpr.3sgm_Aux.tw=",
        "61075": "Inf.stpr.3sgf_Aux.tw=",
        "61076": "Inf.stpr.3sg_Aux.tw=",
        "61077": "Inf.stpr.1pl_Aux.tw=",
        "-61077": "Inf.stpr.1du_Aux.tw=",
        "61078": "Inf.stpr.2pl_Aux.tw=",
        "-61078": "Inf.stpr.2du_Aux.tw=",
        "61079": "Inf.stpr.3pl_Aux.tw=",
        "-61079": "Inf.stpr.3du_Aux.tw=",
        "61080": "Inf_Aux.wn.jn",
        "61081": "Inf.stpr.1sg_Aux.wn.jn",
        "61082": "Inf.stpr.2sgm_Aux.wn.jn",
        "61083": "Inf.stpr.2sgf_Aux.wn.jn",
        "61084": "Inf.stpr.3sgm_Aux.wn.jn",
        "61085": "Inf.stpr.3sgf_Aux.wn.jn",
        "61086": "Inf.stpr.3sg_Aux.wn.jn",
        "61087": "Inf.stpr.1pl_Aux.wn.jn",
        "-61087": "Inf.stpr.1du_Aux.wn.jn",
        "61088": "Inf.stpr.2pl_Aux.wn.jn",
        "-61088": "Inf.stpr.2du_Aux.wn.jn",
        "61089": "Inf.stpr.3pl_Aux.wn.jn",
        "-61089": "Inf.stpr.3du_Aux.wn.jn",
        "61090": "Inf_Aux.wn.ḫr",
        "61091": "Inf.stpr.1sg_Aux.wn.ḫr",
        "61092": "Inf.stpr.2sgm_Aux.wn.ḫr",
        "61093": "Inf.stpr.2sgf_Aux.wn.ḫr",
        "61094": "Inf.stpr.3sgm_Aux.wn.ḫr",
        "61095": "Inf.stpr.3sgf_Aux.wn.ḫr",
        "61096": "Inf.stpr.3sg_Aux.wn.ḫr",
        "61097": "Inf.stpr.1pl_Aux.wn.ḫr",
        "-61097": "Inf.stpr.1du_Aux.wn.ḫr",
        "61098": "Inf.stpr.2pl_Aux.wn.ḫr",
        "-61098": "Inf.stpr.2du_Aux.wn.ḫr",
        "61099": "Inf.stpr.3pl_Aux.wn.ḫr",
        "-61099": "Inf.stpr.3du_Aux.wn.ḫr",
        "61100": "Inf_Neg.bw jri̯",
        "61101": "Inf.stpr.1sg_Neg.bw jri̯",
        "61102": "Inf.stpr.2sgm_Neg.bw jri̯",
        "61103": "Inf.stpr.2sgf_Neg.bw jri̯",
        "61104": "Inf.stpr.3sgm_Neg.bw jri̯",
        "61105": "Inf.stpr.3sgf_Neg.bw jri̯",
        "61106": "Inf.stpr.3sg_Neg.bw jri̯",
        "61107": "Inf.stpr.1pl_Neg.bw jri̯",
        "-61107": "Inf.stpr.1du_Neg.bw jri̯",
        "61108": "Inf.stpr.2pl_Neg.bw jri̯",
        "-61108": "Inf.stpr.2du_Neg.bw jri̯",
        "61109": "Inf.stpr.3pl_Neg.bw jri̯",
        "-61109": "Inf.stpr.3du_Neg.bw jri̯",
        "61110": "Inf_Neg.bw j.jri̯.t",
        "61111": "Inf.stpr.1sg_Neg.bw j.jri̯.t",
        "61112": "Inf.stpr.2sgm_Neg.bw j.jri̯.t",
        "61113": "Inf.stpr.2sgf_Neg.bw j.jri̯.t",
        "61114": "Inf.stpr.3sgm_Neg.bw j.jri̯.t",
        "61115": "Inf.stpr.3sgf_Neg.bw j.jri̯.t",
        "61116": "Inf.stpr.3sg_Neg.bw j.jri̯.t",
        "61117": "Inf.stpr.1pl_Neg.bw j.jri̯.t",
        "-61117": "Inf.stpr.1du_Neg.bw j.jri̯.t",
        "61118": "Inf.stpr.2pl_Neg.bw j.jri̯.t",
        "-61118": "Inf.stpr.2du_Neg.bw j.jri̯.t",
        "61119": "Inf.stpr.3pl_Neg.bw j.jri̯.t",
        "-61119": "Inf.stpr.3du_Neg.bw j.jri̯.t",
        "61120": "Inf_Neg.bn jw",
        "61121": "Inf.stpr.1sg_Neg.bn jw",
        "61122": "Inf.stpr.2sgm_Neg.bn jw",
        "61123": "Inf.stpr.2sgf_Neg.bn jw",
        "61124": "Inf.stpr.3sgm_Neg.bn jw",
        "61125": "Inf.stpr.3sgf_Neg.bn jw",
        "61126": "Inf.stpr.3sg_Neg.bn jw",
        "61127": "Inf.stpr.1pl_Neg.bn jw",
        "-61127": "Inf.stpr.1du_Neg.bn jw",
        "61128": "Inf.stpr.2pl_Neg.bn jw",
        "-61128": "Inf.stpr.2du_Neg.bn jw",
        "61129": "Inf.stpr.3pl_Neg.bn jw",
        "-61129": "Inf.stpr.3du_Neg.bn jw",
        "61130": "Inf_Neg.bn jri̯ jwnꜣ",
        "61131": "Inf.stpr.1sg_Neg.bn jri̯ jwnꜣ",
        "61132": "Inf.stpr.2sgm_Neg.bn jri̯ jwnꜣ",
        "61133": "Inf.stpr.2sgf_Neg.bn jri̯ jwnꜣ",
        "61134": "Inf.stpr.3sgm_Neg.bn jri̯ jwnꜣ",
        "61135": "Inf.stpr.3sgf_Neg.bn jri̯ jwnꜣ",
        "61136": "Inf.stpr.3sg_Neg.bn jri̯ jwnꜣ",
        "61137": "Inf.stpr.1pl_Neg.bn jri̯ jwnꜣ",
        "-61137": "Inf.stpr.1du_Neg.bn jri̯ jwnꜣ",
        "61138": "Inf.stpr.2pl_Neg.bn jri̯ jwnꜣ",
        "-61138": "Inf.stpr.2du_Neg.bn jri̯ jwnꜣ",
        "61139": "Inf.stpr.3pl_Neg.bn jri̯ jwnꜣ",
        "-61139": "Inf.stpr.3du_Neg.bn jri̯ jwnꜣ",
        "61140": "Inf_Neg.bn tw= (jwnꜣ)",
        "61141": "Inf.stpr.1sg_Neg.bn tw= (jwnꜣ)",
        "61142": "Inf.stpr.2sgm_Neg.bn tw= (jwnꜣ)",
        "61143": "Inf.stpr.2sgf_Neg.bn tw= (jwnꜣ)",
        "61144": "Inf.stpr.3sgm_Neg.bn tw= (jwnꜣ)",
        "61145": "Inf.stpr.3sgf_Neg.bn tw= (jwnꜣ)",
        "61146": "Inf.stpr.3sg_Neg.bn tw= (jwnꜣ)",
        "61147": "Inf.stpr.1pl_Neg.bn tw= (jwnꜣ)",
        "-61147": "Inf.stpr.1du_Neg.bn tw= (jwnꜣ)",
        "61148": "Inf.stpr.2pl_Neg.bn tw= (jwnꜣ)",
        "-61148": "Inf.stpr.2du_Neg.bn tw= (jwnꜣ)",
        "61149": "Inf.stpr.3pl_Neg.bn tw= (jwnꜣ)",
        "-61149": "Inf.stpr.3du_Neg.bn tw= (jwnꜣ)",
        "61150": "Inf_Neg.tm",
        "61151": "Inf.stpr.1sg_Neg.tm",
        "61152": "Inf.stpr.2sgm_Neg.tm",
        "61153": "Inf.stpr.2sgf_Neg.tm",
        "61154": "Inf.stpr.3sgm_Neg.tm",
        "61155": "Inf.stpr.3sgf_Neg.tm",
        "61156": "Inf.stpr.3sg_Neg.tm",
        "61157": "Inf.stpr.1pl_Neg.tm",
        "-61157": "Inf.stpr.1du_Neg.tm",
        "61158": "Inf.stpr.2pl_Neg.tm",
        "-61158": "Inf.stpr.2du_Neg.tm",
        "61159": "Inf.stpr.3pl_Neg.tm",
        "-61159": "Inf.stpr.3du_Neg.tm",
        "61160": "Inf_Neg.m-jri̯",
        "61161": "Inf.stpr.1sg_Neg.m jri̯",
        "61162": "Inf.stpr.2sgm_Neg.m jri̯",
        "61163": "Inf.stpr.2sgf_Neg.m jri̯",
        "61164": "Inf.stpr.3sgm_Neg.m jri̯",
        "61165": "Inf.stpr.3sgf_Neg.m jri̯",
        "61166": "Inf.stpr.3sg_Neg.m jri̯",
        "61167": "Inf.stpr.1pl_Neg.m jri̯",
        "-61167": "Inf.stpr.1du_Neg.m jri̯",
        "61168": "Inf.stpr.2pl_Neg.m jri̯",
        "-61168": "Inf.stpr.2du_Neg.m jri̯",
        "61169": "Inf.stpr.3pl_Neg.m jri̯",
        "-61169": "Inf.stpr.3du_Neg.m jri̯",
        "61170": "Inf_Neg.nn jw",
        "61171": "Inf.stpr.1sg_Neg.nn jw",
        "61172": "Inf.stpr.2sgm_Neg.nn jw",
        "61173": "Inf.stpr.2sgf_Neg.nn jw",
        "61174": "Inf.stpr.3sgm_Neg.nn jw",
        "61175": "Inf.stpr.3sgf_Neg.nn jw",
        "61176": "Inf.stpr.3sg_Neg.nn jw",
        "61177": "Inf.stpr.1pl_Neg.nn jw",
        "-61177": "Inf.stpr.1du_Neg.nn jw",
        "61178": "Inf.stpr.2pl_Neg.nn jw",
        "-61178": "Inf.stpr.2du_Neg.nn jw",
        "61179": "Inf.stpr.3pl_Neg.nn jw",
        "-61179": "Inf.stpr.3du_Neg.nn jw",
        "61180": "Inf_Neg.m",
        "61181": "Inf.stpr.1sg_Neg.m",
        "61182": "Inf.stpr.2sgm_Neg.m",
        "61183": "Inf.stpr.2sgf_Neg.m",
        "61184": "Inf.stpr.3sgm_Neg.m",
        "61185": "Inf.stpr.3sgf_Neg.m",
        "61186": "Inf.stpr.3sg_Neg.m",
        "61187": "Inf.stpr.1pl_Neg.m",
        "-61187": "Inf.stpr.1du_Neg.m",
        "61188": "Inf.stpr.2pl_Neg.m",
        "-61188": "Inf.stpr.2du_Neg.m",
        "61189": "Inf.stpr.3pl_Neg.m",
        "-61189": "Inf.stpr.3du_Neg.m",
        "61190": "Inf._Neg.nfr/nfr-n/nfr-pw",
        "61191": "Inf.stpr.1sg_Neg.nfr/nfr-n/nfr-pw",
        "61192": "Inf.stpr.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "61193": "Inf.stpr.2.sgf_Neg.nfr/nfr-n/nfr-pw",
        "61194": "Inf.stpr.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "61195": "Inf.stpr.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "61196": "Inf.stpr.3sg_Neg.nfr/nfr-n/nfr-pw",
        "61197": "Inf.stpr.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-61197": "Inf.stpr.1du_Neg.nfr/nfr-n/nfr-pw",
        "61198": "Inf.stpr.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-61198": "Inf.stpr.2du_Neg.nfr/nfr-n/nfr-pw",
        "61199": "Inf.stpr.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-61199": "Inf.stpr.3du_Neg.nfr/nfr-n/nfr-pw",
        "61300": "Inf.t",
        "61301": "Inf.t.stpr.1sg",
        "61302": "Inf.t.stpr.2sgm",
        "61303": "Inf.t.stpr.2sgf",
        "61304": "Inf.t.stpr.3sgm",
        "61305": "Inf.t.stpr.3sgf",
        "61306": "Inf.t.stpr.3sg",
        "61307": "Inf.t.stpr.1pl",
        "-61307": "Inf.t.stpr.1du",
        "61308": "Inf.t.stpr.2pl",
        "-61308": "Inf.t.stpr.2du",
        "61309": "Inf.t.stpr.3pl",
        "-61309": "Inf.t.stpr.3du",
        "61310": "Inf.t_Aux.jw",
        "61311": "Inf.t.stpr.1sg_Aux.jw",
        "61312": "Inf.t.stpr.2sgm_Aux.jw",
        "61313": "Inf.t.stpr.2sgf_Aux.jw",
        "61314": "Inf.t.stpr.3sgm_Aux.jw",
        "61315": "Inf.t.stpr.3sgf_Aux.jw",
        "61316": "Inf.t.stpr.3sg_Aux.jw",
        "61317": "Inf.t.stpr.1pl_Aux.jw",
        "-61317": "Inf.t.stpr.1du_Aux.jw",
        "61318": "Inf.t.stpr.2pl_Aux.jw",
        "-61318": "Inf.t.stpr.2du_Aux.jw",
        "61319": "Inf.t.stpr.3pl_Aux.jw",
        "-61319": "Inf.t.stpr.3du_Aux.jw",
        "61320": "Inf.t_Aux.jri̯",
        "61321": "Inf.t.stpr.1sg_Aux.jri̯",
        "61322": "Inf.t.stpr.2sgm_Aux.jri̯",
        "61323": "Inf.t.stpr.2sgf_Aux.jri̯",
        "61324": "Inf.t.stpr.3sgm_Aux.jri̯",
        "61325": "Inf.t.stpr.3sgf_Aux.jri̯",
        "61326": "Inf.t.stpr.3sg_Aux.jri̯",
        "61327": "Inf.t.stpr.1pl_Aux.jri̯",
        "-61327": "Inf.t.stpr.1du_Aux.jri̯",
        "61328": "Inf.t.stpr.2pl_Aux.jri̯",
        "-61328": "Inf.t.stpr.2du_Aux.jri̯",
        "61329": "Inf.t.stpr.3pl_Aux.jri̯",
        "-61329": "Inf.t.stpr.3du_Aux.jri̯",
        "61330": "Inf.t_Aux.j.jri̯",
        "61331": "Inf.t.stpr.1sg_Aux.j.jri̯",
        "61332": "Inf.t.stpr.2sgm_Aux.j.jri̯",
        "61333": "Inf.t.stpr.2sgf_Aux.j.jri̯",
        "61334": "Inf.t.stpr.3sgm_Aux.j.jri̯",
        "61335": "Inf.t.stpr.3sgf_Aux.j.jri̯",
        "61336": "Inf.t.stpr.3sg_Aux.j.jri̯",
        "61337": "Inf.t.stpr.1pl_Aux.j.jri̯",
        "-61337": "Inf.t.stpr.1du_Aux.j.jri̯",
        "61338": "Inf.t.stpr.2pl_Aux.j.jri̯",
        "-61338": "Inf.t.stpr.2du_Aux.j.jri̯",
        "61339": "Inf.t.stpr.3pl_Aux.j.jri̯",
        "-61339": "Inf.t.stpr.3du_Aux.j.jri̯",
        "61340": "Inf.t_Aux.j.jri̯.t",
        "61341": "Inf.t.stpr.1sg_Aux.j.jri̯.t",
        "61342": "Inf.t.stpr.2sgm_Aux.j.jri̯.t",
        "61343": "Inf.t.stpr.2sgf_Aux.j.jri̯.t",
        "61344": "Inf.t.stpr.3sgm_Aux.j.jri̯.t",
        "61345": "Inf.t.stpr.3sgf_Aux.j.jri̯.t",
        "61346": "Inf.t.stpr.3sg_Aux.j.jri̯.t",
        "61347": "Inf.t.stpr.1pl_Aux.j.jri̯.t",
        "-61347": "Inf.t.stpr.1du_Aux.j.jri̯.t",
        "61348": "Inf.t.stpr.2pl_Aux.j.jri̯.t",
        "-61348": "Inf.t.stpr.2du_Aux.j.jri̯.t",
        "61349": "Inf.t.stpr.3pl_Aux.j.jri̯.t",
        "-61349": "Inf.t.stpr.3du_Aux.j.jri̯.t",
        "61350": "Inf.t_Neg.bwpw",
        "61351": "Inf.t.stpr.1sg_Neg.bwpw",
        "61352": "Inf.t.stpr.2sgm_Neg.bwpw",
        "61353": "Inf.t.stpr.2sgf_Neg.bwpw",
        "61354": "Inf.t.stpr.3sgm_Neg.bwpw",
        "61355": "Inf.t.stpr.3sgf_Neg.bwpw",
        "61356": "Inf.t.stpr.3sg_Neg.bwpw",
        "61357": "Inf.t.stpr.1pl_Neg.bwpw",
        "-61357": "Inf.t.stpr.1du_Neg.bwpw",
        "61358": "Inf.t.stpr.2pl_Neg.bwpw",
        "-61358": "Inf.t.stpr.2du_Neg.bwpw",
        "61359": "Inf.t.stpr.3pl_Neg.bwpw",
        "-61359": "Inf.t.stpr.3du_Neg.bwpw",
        "61360": "Inf.t_Aux.mtw=",
        "61361": "Inf.t.stpr.1sg_Aux.mtw=",
        "61362": "Inf.t.stpr.2sgm_Aux.mtw=",
        "61363": "Inf.t.stpr.2sgf_Aux.mtw=",
        "61364": "Inf.t.stpr.3sgm_Aux.mtw=",
        "61365": "Inf.t.stpr.3sgf_Aux.mtw=",
        "61366": "Inf.t.stpr.3sg_Aux.mtw=",
        "61367": "Inf.t.stpr.1pl_Aux.mtw=",
        "-61367": "Inf.t.stpr.1du_Aux.mtw=",
        "61368": "Inf.t.stpr.2pl_Aux.mtw=",
        "-61368": "Inf.t.stpr.2du_Aux.mtw=",
        "61369": "Inf.t.stpr.3pl_Aux.mtw=",
        "-61369": "Inf.t.stpr.3du_Aux.mtw=",
        "61370": "Inf.t_Aux.tw=",
        "61371": "Inf.t.stpr.1sg_Aux.tw=",
        "61372": "Inf.t.stpr.2sgm_Aux.tw=",
        "61373": "Inf.t.stpr.2sgf_Aux.tw=",
        "61374": "Inf.t.stpr.3sgm_Aux.tw=",
        "61375": "Inf.t.stpr.3sgf_Aux.tw=",
        "61376": "Inf.t.stpr.3sg_Aux.tw=",
        "61377": "Inf.t.stpr.1pl_Aux.tw=",
        "-61377": "Inf.t.stpr.1du_Aux.tw=",
        "61378": "Inf.t.stpr.2pl_Aux.tw=",
        "-61378": "Inf.t.stpr.2du_Aux.tw=",
        "61379": "Inf.t.stpr.3pl_Aux.tw=",
        "-61379": "Inf.t.stpr.3du_Aux.tw=",
        "61380": "Inf.t_Aux.wn.jn",
        "61381": "Inf.t.stpr.1sg_Aux.wn.jn",
        "61382": "Inf.t.stpr.2sgm_Aux.wn.jn",
        "61383": "Inf.t.stpr.2sgf_Aux.wn.jn",
        "61384": "Inf.t.stpr.3sgm_Aux.wn.jn",
        "61385": "Inf.t.stpr.3sgf_Aux.wn.jn",
        "61386": "Inf.t.stpr.3sg_Aux.wn.jn",
        "61387": "Inf.t.stpr.1pl_Aux.wn.jn",
        "-61387": "Inf.t.stpr.1du_Aux.wn.jn",
        "61388": "Inf.t.stpr.2pl_Aux.wn.jn",
        "-61388": "Inf.t.stpr.2du_Aux.wn.jn",
        "61389": "Inf.t.stpr.3pl_Aux.wn.jn",
        "-61389": "Inf.t.stpr.3du_Aux.wn.jn",
        "61390": "Inf.t_Aux.wn.ḫr",
        "61391": "Inf.t.stpr.1sg_Aux.wn.ḫr",
        "61392": "Inf.t.stpr.2sgm_Aux.wn.ḫr",
        "61393": "Inf.t.stpr.2sgf_Aux.wn.ḫr",
        "61394": "Inf.t.stpr.3sgm_Aux.wn.ḫr",
        "61395": "Inf.t.stpr.3sgf_Aux.wn.ḫr",
        "61396": "Inf.t.stpr.3sg_Aux.wn.ḫr",
        "61397": "Inf.t.stpr.1pl_Aux.wn.ḫr",
        "-61397": "Inf.t.stpr.1du_Aux.wn.ḫr",
        "61398": "Inf.t.stpr.2pl_Aux.wn.ḫr",
        "-61398": "Inf.t.stpr.2du_Aux.wn.ḫr",
        "61399": "Inf.t.stpr.3pl_Aux.wn.ḫr",
        "-61399": "Inf.t.stpr.3du_Aux.wn.ḫr",
        "61410": "Inf.t_Neg.bw jri̯",
        "61411": "Inf.t.stpr.1sg_Neg.bw jri̯",
        "61412": "Inf.t.stpr.2sgm_Neg.bw jri̯",
        "61413": "Inf.t.stpr.2sgf_Neg.bw jri̯",
        "61414": "Inf.t.stpr.3sgm_Neg.bw jri̯",
        "61415": "Inf.t.stpr.3sgf_Neg.bw jri̯",
        "61416": "Inf.t.stpr.3sg_Neg.bw jri̯",
        "61417": "Inf.t.stpr.1pl_Neg.bw jri̯",
        "-61417": "Inf.t.stpr.1du_Neg.bw jri̯",
        "61418": "Inf.t.stpr.2pl_Neg.bw jri̯",
        "-61418": "Inf.t.stpr.2du_Neg.bw jri̯",
        "61419": "Inf.t.stpr.3pl_Neg.bw jri̯",
        "-61419": "Inf.t.stpr.3du_Neg.bw jri̯",
        "61420": "Inf.t_Neg.bw j.jri̯.t",
        "61421": "Inf.t.stpr.1sg_Neg.bw j.jri̯.t",
        "61422": "Inf.t.stpr.2sgm_Neg.bw j.jri̯.t",
        "61423": "Inf.t.stpr.2sgf_Neg.bw j.jri̯.t",
        "61424": "Inf.t.stpr.3sgm_Neg.bw j.jri̯.t",
        "61425": "Inf.t.stpr.3sgf_Neg.bw j.jri̯.t",
        "61426": "Inf.t.stpr.3sg_Neg.bw j.jri̯.t",
        "61427": "Inf.t.stpr.1pl_Neg.bw j.jri̯.t",
        "-61427": "Inf.t.stpr.1du_Neg.bw j.jri̯.t",
        "61428": "Inf.t.stpr.2pl_Neg.bw j.jri̯.t",
        "-61428": "Inf.t.stpr.2du_Neg.bw j.jri̯.t",
        "61429": "Inf.t.stpr.3pl_Neg.bw j.jri̯.t",
        "-61429": "Inf.t.stpr.3du_Neg.bw j.jri̯.t",
        "61430": "Inf.t_Neg.bn jw",
        "61431": "Inf.t.stpr.1sg_Neg.bn jw",
        "61432": "Inf.t.stpr.2sgm_Neg.bn jw",
        "61433": "Inf.t.stpr.2sgf_Neg.bn jw",
        "61434": "Inf.t.stpr.3sgm_Neg.bn jw",
        "61435": "Inf.t.stpr.3sgf_Neg.bn jw",
        "61436": "Inf.t.stpr.3sg_Neg.bn jw",
        "61437": "Inf.t.stpr.1pl_Neg.bn jw",
        "-61437": "Inf.t.stpr.1du_Neg.bn jw",
        "61438": "Inf.t.stpr.2pl_Neg.bn jw",
        "-61438": "Inf.t.stpr.2du_Neg.bn jw",
        "61439": "Inf.t.stpr.3pl_Neg.bn jw",
        "-61439": "Inf.t.stpr.3du_Neg.bn jw",
        "61440": "Inf.t_Neg.bn jri̯ jwnꜣ",
        "61441": "Inf.t.stpr.1sg_Neg.bn jri̯ jwnꜣ",
        "61442": "Inf.t.stpr.2sgm_Neg.bn jri̯ jwnꜣ",
        "61443": "Inf.t.stpr.2sgf_Neg.bn jri̯ jwnꜣ",
        "61444": "Inf.t.stpr.3sgm_Neg.bn jri̯ jwnꜣ",
        "61445": "Inf.t.stpr.3sgf_Neg.bn jri̯ jwnꜣ",
        "61446": "Inf.t.stpr.3sg_Neg.bn jri̯ jwnꜣ",
        "61447": "Inf.t.stpr.1pl_Neg.bn jri̯ jwnꜣ",
        "-61447": "Inf.t.stpr.1du_Neg.bn jri̯ jwnꜣ",
        "61448": "Inf.t.stpr.2pl_Neg.bn jri̯ jwnꜣ",
        "-61448": "Inf.t.stpr.2du_Neg.bn jri̯ jwnꜣ",
        "61449": "Inf.t.stpr.3pl_Neg.bn jri̯ jwnꜣ",
        "-61449": "Inf.t.stpr.3du_Neg.bn jri̯ jwnꜣ",
        "61450": "Inf.t_Neg.bn tw= (jwnꜣ)",
        "61451": "Inf.t.stpr.1sg_Neg.bn tw= (jwnꜣ)",
        "61452": "Inf.t.stpr.2sgm_Neg.bn tw= (jwnꜣ)",
        "61453": "Inf.t.stpr.2sgf_Neg.bn tw= (jwnꜣ)",
        "61454": "Inf.t.stpr.3sgm_Neg.bn tw= (jwnꜣ)",
        "61455": "Inf.t.stpr.3sgf_Neg.bn tw= (jwnꜣ)",
        "61456": "Inf.t.stpr.3sg_Neg.bn tw= (jwnꜣ)",
        "61457": "Inf.t.stpr.1pl_Neg.bn tw= (jwnꜣ)",
        "-61457": "Inf.t.stpr.1du_Neg.bn tw= (jwnꜣ)",
        "61458": "Inf.t.stpr.2pl_Neg.bn tw= (jwnꜣ)",
        "-61458": "Inf.t.stpr.2du_Neg.bn tw= (jwnꜣ)",
        "61459": "Inf.t.stpr.3pl_Neg.bn tw= (jwnꜣ)",
        "-61459": "Inf.t.stpr.3du_Neg.bn tw= (jwnꜣ)",
        "61460": "Inf.t_Neg.tm",
        "61461": "Inf.t.stpr.1sg_Neg.tm",
        "61462": "Inf.t.stpr.2sgm_Neg.tm",
        "61463": "Inf.t.stpr.2sgf_Neg.tm",
        "61464": "Inf.t.stpr.3sgm_Neg.tm",
        "61465": "Inf.t.stpr.3sgf_Neg.tm",
        "61466": "Inf.t.stpr.3sg_Neg.tm",
        "61467": "Inf.t.stpr.1pl_Neg.tm",
        "-61467": "Inf.t.stpr.1du_Neg.tm",
        "61468": "Inf.t.stpr.2pl_Neg.tm",
        "-61468": "Inf.t.stpr.2du_Neg.tm",
        "61469": "Inf.t.stpr.3pl_Neg.tm",
        "-61469": "Inf.t.stpr.3du_Neg.tm",
        "61470": "Inf.t_Neg.m-jri̯",
        "61471": "Inf.t.stpr.1sg_Neg.m jri̯",
        "61472": "Inf.t.stpr.2sgm_Neg.m jri̯",
        "61473": "Inf.t.stpr.2sgf_Neg.m jri̯",
        "61474": "Inf.t.stpr.3sgm_Neg.m jri̯",
        "61475": "Inf.t.stpr.3sgf_Neg.m jri̯",
        "61476": "Inf.t.stpr.3sg_Neg.m jri̯",
        "61477": "Inf.t.stpr.1pl_Neg.m jri̯",
        "-61477": "Inf.t.stpr.1du_Neg.m jri̯",
        "61478": "Inf.t.stpr.2pl_Neg.m jri̯",
        "-61478": "Inf.t.stpr.2du_Neg.m jri̯",
        "61479": "Inf.t.stpr.3pl_Neg.m jri̯",
        "-61479": "Inf.t.stpr.3du_Neg.m jri̯",
        "61480": "Inf.t_Neg.nn jw",
        "61481": "Inf.t.stpr.1sg_Neg.nn jw",
        "61482": "Inf.t.stpr.2sgm_Neg.nn jw",
        "61483": "Inf.t.stpr.2sgf_Neg.nn jw",
        "61484": "Inf.t.stpr.3sgm_Neg.nn jw",
        "61485": "Inf.t.stpr.3sgf_Neg.nn jw",
        "61486": "Inf.t.stpr.3sg_Neg.nn jw",
        "61487": "Inf.t.stpr.1pl_Neg.nn jw",
        "-61487": "Inf.t.stpr.1du_Neg.nn jw",
        "61488": "Inf.t.stpr.2pl_Neg.nn jw",
        "-61488": "Inf.t.stpr.2du_Neg.nn jw",
        "61489": "Inf.t.stpr.3pl_Neg.nn jw",
        "-61489": "Inf.t.stpr.3du_Neg.nn jw",
        "61490": "Inf.t_Neg.m",
        "61491": "Inf.t.stpr.1sg_Neg.m",
        "61492": "Inf.t.stpr.2sgm_Neg.m",
        "61493": "Inf.t.stpr.2sgf_Neg.m",
        "61494": "Inf.t.stpr.3sgm_Neg.m",
        "61495": "Inf.t.stpr.3sgf_Neg.m",
        "61496": "Inf.t.stpr.3sg_Neg.m",
        "61497": "Inf.t.stpr.1pl_Neg.m",
        "-61497": "Inf.t.stpr.1du_Neg.m",
        "61498": "Inf.t.stpr.2pl_Neg.m",
        "-61498": "Inf.t.stpr.2du_Neg.m",
        "61499": "Inf.t.stpr.3pl_Neg.m",
        "-61499": "Inf.t.stpr.3du_Neg.m",
        "61510": "Inf.t_Neg.nfr/nfr-n/nfr-pw",
        "61511": "Inf.t.stpr.1sg_Neg.nfr/nfr-n/nfr-pw",
        "61512": "Inf.t.stpr.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "61513": "Inf.t.stpr.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "61514": "Inf.t.stpr.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "61515": "Inf.t.stpr.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "61516": "Inf.t.stpr.3sg_Neg.nfr/nfr-n/nfr-pw",
        "61517": "Inf.t.stpr.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-61517": "Inf.t.stpr.1du_Neg.nfr/nfr-n/nfr-pw",
        "61518": "Inf.t.stpr.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-61518": "Inf.t.stpr.2du_Neg.nfr/nfr-n/nfr-pw",
        "61519": "Inf.t.stpr.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-61519": "Inf.t.stpr.3du_Neg.nfr/nfr-n/nfr-pw",
        "62000": "Compl.inf",
        "62100": "Compl.inf.t",
        "62105": "Compl.inf.t.stpr.3sgf",
        "62200": "Compl.inf.wt",
        "62300": "Compl.inf.jt/yt",
        "62400": "Compl.inf.gem",
        "62500": "Compl.inf.gem.t",
        "63000": "Neg.compl.unspec",
        "63100": "Neg.compl.unmarked",
        "63101": "Neg.compl.unmarked.stpr.1sg",
        "63102": "Neg.compl.unmarked.stpr.2sgm",
        "63104": "Neg.compl.unmarked.stpr.3sgm",
        "63105": "Neg.compl.unmarked.stpr.3sgf",
        "63200": "Neg.compl.w",
        "63300": "Neg.compl.t",
        "63301": "Neg.compl.t.stpr.1sg",
        "63303": "Neg.compl.t.stpr.2sgf",
        "63400": "Neg.compl.gem",
        "63500": "Neg.compl.t.gem",
        "63600": "Neg.compl.w.gem",
        "64000": "Inf_Aux.wn",
        "64001": "Inf.stpr.1sg_Aux.wn",
        "64002": "Inf.stpr.2sgm_Aux.wn",
        "64003": "Inf.stpr.2sgf_Aux.wn",
        "64004": "Inf.stpr.3sgm_Aux.wn",
        "64005": "Inf.stpr.3sgf_Aux.wn",
        "64006": "Inf.stpr.3sg_Aux.wn",
        "64007": "Inf.stpr.1pl_Aux.wn",
        "-64007": "Inf.stpr.1du_Aux.wn",
        "64008": "Inf.stpr.2pl_Aux.wn",
        "-64008": "Inf.stpr.2du_Aux.wn",
        "64009": "Inf.stpr.3pl_Aux.wn",
        "-64009": "Inf.stpr.3du_Aux.wn",
        "64300": "Inf.t_Aux.wn",
        "64301": "Inf.t.stpr.1sg_Aux.wn",
        "64302": "Inf.t.stpr.2sgm_Aux.wn",
        "64303": "Inf.t.stpr.2sgf_Aux.wn",
        "64304": "Inf.t.stpr.3sgm_Aux.wn",
        "64305": "Inf.t.stpr.3sgf_Aux.wn",
        "64306": "Inf.t.stpr.3sg_Aux.wn",
        "64307": "Inf.t.stpr.1pl_Aux.wn",
        "-64307": "Inf.t.stpr.1du_Aux.wn",
        "64308": "Inf.t.stpr.2pl_Aux.wn",
        "-64308": "Inf.t.stpr.2du_Aux.wn",
        "64309": "Inf.t.stpr.3pl_Aux.wn",
        "-64309": "Inf.t.stpr.3du_Aux.wn",
        "65000": "Inf_Aux.ꜥḥꜥ.n",
        "65001": "Inf.stpr.1sg_Aux.ꜥḥꜥ.n",
        "65002": "Inf.stpr.2sgm_Aux.ꜥḥꜥ.n",
        "65003": "Inf.stpr.2sgf_Aux.ꜥḥꜥ.n",
        "65004": "Inf.stpr.3sgm_Aux.ꜥḥꜥ.n",
        "65005": "Inf.stpr.3sgf_Aux.ꜥḥꜥ.n",
        "65006": "Inf.stpr.3sg_Aux.ꜥḥꜥ.n",
        "65007": "Inf.stpr.1pl_Aux.ꜥḥꜥ.n",
        "-65007": "Inf.stpr.1du_Aux.ꜥḥꜥ.n",
        "65008": "Inf.stpr.2pl_Aux.ꜥḥꜥ.n",
        "-65008": "Inf.stpr.2du_Aux.ꜥḥꜥ.n",
        "65009": "Inf.stpr.3pl_Aux.ꜥḥꜥ.n",
        "-65009": "Inf.stpr.3du_Aux.ꜥḥꜥ.n",
        "65300": "Inf.t_Aux.ꜥḥꜥ.n",
        "65301": "Inf.t.stpr.1sg_Aux.ꜥḥꜥ.n",
        "65302": "Inf.t.stpr.2sgm_Aux.ꜥḥꜥ.n",
        "65303": "Inf.t.stpr.2sgf_Aux.ꜥḥꜥ.n",
        "65304": "Inf.t.stpr.3sgm_Aux.ꜥḥꜥ.n",
        "65305": "Inf.t.stpr.3sgf_Aux.ꜥḥꜥ.n",
        "65306": "Inf.t.stpr.3sg_Aux.ꜥḥꜥ.n",
        "65307": "Inf.t.stpr.1pl_Aux.ꜥḥꜥ.n",
        "-65307": "Inf.stpr.1du_Aux.ꜥḥꜥ.n",
        "65308": "Inf.t.stpr.2pl_Aux.ꜥḥꜥ.n",
        "-65308": "Inf.t.stpr.2du_Aux.ꜥḥꜥ.n",
        "65309": "Inf.t.stpr.3pl_Aux.ꜥḥꜥ.n",
        "-65309": "Inf.t.stpr.3du_Aux.ꜥḥꜥ.n",
        "66000": "Inf_Aux.mk",
        "66001": "Inf.stpr.1sg_Aux.mk",
        "66002": "Inf.stpr.2sgm_Aux.mk",
        "66003": "Inf.stpr.2sgf_Aux.mk",
        "66004": "Inf.stpr.3sgm_Aux.mk",
        "66005": "Inf.stpr.3sgf_Aux.mk",
        "66006": "Inf.stpr.3sg_Aux.mk",
        "66007": "Inf.stpr.1pl_Aux.mk",
        "-66007": "Inf.stpr.1du_Aux.mk",
        "66008": "Inf.stpr.2pl_Aux.mk",
        "-66008": "Inf.stpr.2du_Aux.mk",
        "66009": "Inf.stpr.3pl_Aux.mk",
        "-66009": "Inf.stpr.3du_Aux.mk",
        "66300": "Inf.t_Aux.mk",
        "66301": "Inf.t.stpr.1sg_Aux.mk",
        "66302": "Inf.t.stpr.2sgm_Aux.mk",
        "66303": "Inf.t.stpr.2sgf_Aux.mk",
        "66304": "Inf.t.stpr.3sgm_Aux.mk",
        "66305": "Inf.t.stpr.3sgf_Aux.mk",
        "66306": "Inf.t.stpr.3sg_Aux.mk",
        "66307": "Inf.t.stpr.1pl_Aux.mk",
        "-66307": "Inf.t.stpr.1du_Aux.mk",
        "66308": "Inf.t.stpr.2pl_Aux.mk",
        "-66308": "Inf.t.stpr.2du_Aux.mk",
        "66309": "Inf.t.stpr.3pl_Aux.mk",
        "-66309": "Inf.t.stpr.3du_Aux.mk",
        "67000": "Inf_Neg.nn",
        "67001": "Inf.stpr.1sg_Neg.nn",
        "67002": "Inf.stpr.2sgm_Neg.nn",
        "67003": "Inf.stpr.2sgf_Neg.nn",
        "67004": "Inf.stpr.3sgm_Neg.nn",
        "67005": "Inf.stpr.3sgf_Neg.nn",
        "67006": "Inf.stpr.3sg_Neg.nn",
        "67007": "Inf.stpr.1pl_Neg.nn",
        "-67007": "Inf.stpr.1du_Neg.nn",
        "67008": "Inf.stpr.2pl_Neg.nn",
        "-67008": "Inf.stpr.2du_Neg.nn",
        "67009": "Inf.stpr.3pl_Neg.nn",
        "-67009": "Inf.stpr.3du_Neg.nn",
        "67300": "Inf.t_Neg.nn",
        "67301": "Inf.t.stpr.1sg_Neg.nn",
        "67302": "Inf.t.stpr.2sgm_Neg.nn",
        "67303": "Inf.t.stpr.2sgf_Neg.nn",
        "67304": "Inf.t.stpr.3sgm_Neg.nn",
        "67305": "Inf.t.stpr.3sgf_Neg.nn",
        "67306": "Inf.t.stpr.3sg_Neg.nn",
        "67307": "Inf.t.stpr.1pl_Neg.nn",
        "-67307": "Inf.t.stpr.1du_Neg.nn",
        "67308": "Inf.t.stpr.2pl_Neg.nn",
        "-67308": "Inf.t.stpr.2du_Neg.nn",
        "67309": "Inf.t.stpr.3pl_Neg.nn",
        "-67309": "Inf.t.stpr.3du_Neg.nn",
        "68000": "Inf_Aux.wnn",
        "68001": "Inf.stpr.1sg_Aux.wnn",
        "68002": "Inf.stpr.2sgm_Aux.wnn",
        "68003": "Inf.stpr.2sgf_Aux.wnn",
        "68004": "Inf.stpr.3sgm_Aux.wnn",
        "68005": "Inf.stpr.3sgf_Aux.wnn",
        "68006": "Inf.stpr.3sg_Aux.wnn",
        "68007": "Inf.stpr.1pl_Aux.wnn",
        "-68007": "Inf.stpr.1du_Aux.wnn",
        "68008": "Inf.stpr.2pl_Aux.wnn",
        "-68008": "Inf.stpr.2du_Aux.wnn",
        "68009": "Inf.stpr.3pl_Aux.wnn",
        "-68009": "Inf.stpr.3du_Aux.wnn",
        "68300": "Inf.t_Aux.wnn",
        "68301": "Inf.t.stpr.1sg_Aux.wnn",
        "68302": "Inf.t.stpr.2sgm_Aux.wnn",
        "68303": "Inf.t.stpr.2sgf_Aux.wnn",
        "68304": "Inf.t.stpr.3sgm_Aux.wnn",
        "68305": "Inf.t.stpr.3sgf_Aux.wnn",
        "68306": "Inf.t.stpr.3sg_Aux.wnn",
        "68307": "Inf.t.stpr.1pl_Aux.wnn",
        "-68307": "Inf.t.stpr.1du_Aux.wnn",
        "68308": "Inf.t.stpr.2pl_Aux.wnn",
        "-68308": "Inf.t.stpr.2du_Aux.wnn",
        "68309": "Inf.t.stpr.3pl_Aux.wnn",
        "-68309": "Inf.t.stpr.3du_Aux.wnn",
        "69000": "Inf.gem_Aux.jw",
        "69001": "Inf.gem.stpr.1sg",
        "69002": "Inf.gem.stpr.2sgm",
        "69003": "Inf.gem.stpr.2sgf",
        "69004": "Inf.gem.stpr.3sgm",
        "69005": "Inf.gem.stpr.3sgf",
        "69006": "Inf.gem.stpr.3sg",
        "69007": "Inf.gem.stpr.1pl",
        "-69007": "Inf.gem.stpr.1du",
        "69008": "Inf.gem.stpr.2pl",
        "-69008": "Inf.gem.stpr.2du",
        "69009": "Inf.gem.stpr.3pl",
        "-69009": "Inf.gem.stpr.3du",
        "69010": "Inf.gem_Aux.jw",
        "69011": "Inf.gem.stpr.1sg_Aux.jw",
        "69012": "Inf.gem.stpr.2sgm_Aux.jw",
        "69013": "Inf.gem.stpr.2sgf_Aux.jw",
        "69014": "Inf.gem.stpr.3sgm_Aux.jw",
        "69015": "Inf.gem.stpr.3sgf_Aux.jw",
        "69016": "Inf.gem.stpr.3sg_Aux.jw",
        "69017": "Inf.gem.stpr.1pl_Aux.jw",
        "-69017": "Inf.gem.stpr.1du_Aux.jw",
        "69018": "Inf.gem.stpr.2pl_Aux.jw",
        "-69018": "Inf.gem.stpr.2du_Aux.jw",
        "69019": "Inf.gem.stpr.3pl_Aux.jw",
        "-69019": "Inf.gem.stpr.3du_Aux.jw",
        "69020": "Inf.gem_Aux.jri̯",
        "69021": "Inf.gem.stpr.1sg_Aux.jri̯",
        "69022": "Inf.gem.stpr.2sgm_Aux.jri̯",
        "69023": "Inf.gem.stpr.2sgf_Aux.jri̯",
        "69024": "Inf.gem.stpr.3sgm_Aux.jri̯",
        "69025": "Inf.gem.stpr.3sgf_Aux.jri̯",
        "69026": "Inf.gem.stpr.3sg_Aux.jri̯",
        "69027": "Inf.gem.stpr.1pl_Aux.jri̯",
        "-69027": "Inf.gem.stpr.1du_Aux.jri̯",
        "69028": "Inf.gem.stpr.2pl_Aux.jri̯",
        "-69028": "Inf.gem.stpr.2du_Aux.jri̯",
        "69029": "Inf.gem.stpr.3pl_Aux.jri̯",
        "-69029": "Inf.gem.stpr.3du_Aux.jri̯",
        "69030": "Inf.gem_Aux.j.jri̯",
        "69031": "Inf.gem.stpr.1sg_Aux.j.jri̯",
        "69032": "Inf.gem.stpr.2sgm_Aux.j.jri̯",
        "69033": "Inf.gem.stpr.2sgf_Aux.j.jri̯",
        "69034": "Inf.gem.stpr.3sgm_Aux.j.jri̯",
        "69035": "Inf.gem.stpr.3sgf_Aux.j.jri̯",
        "69036": "Inf.gem.stpr.3sg_Aux.j.jri̯",
        "69037": "Inf.gem.stpr.1pl_Aux.j.jri̯",
        "-69037": "Inf.gem.stpr.1du_Aux.j.jri̯",
        "69038": "Inf.gem.stpr.2pl_Aux.j.jri̯",
        "-69038": "Inf.gem.stpr.2du_Aux.j.jri̯",
        "69039": "Inf.gem.stpr.3pl_Aux.j.jri̯",
        "-69039": "Inf.gem.stpr.3du_Aux.j.jri̯",
        "69040": "Inf.gem_Aux.j.jri̯.t",
        "69041": "Inf.gem.stpr.1sg_Aux.j.jri̯.t",
        "69042": "Inf.gem.stpr.2sgm_Aux.j.jri̯.t",
        "69043": "Inf.gem.stpr.2sgf_Aux.j.jri̯.t",
        "69044": "Inf.gem.stpr.3sgm_Aux.j.jri̯.t",
        "69045": "Inf.gem.stpr.3sgf_Aux.j.jri̯.t",
        "69046": "Inf.gem.stpr.3sg_Aux.j.jri̯.t",
        "69047": "Inf.gem.stpr.1pl_Aux.j.jri̯.t",
        "-69047": "Inf.gem.stpr.1du_Aux.j.jri̯.t",
        "69048": "Inf.gem.stpr.2pl_Aux.j.jri̯.t",
        "-69048": "Inf.gem.stpr.2du_Aux.j.jri̯.t",
        "69049": "Inf.gem.stpr.3pl_Aux.j.jri̯.t",
        "-69049": "Inf.gem.stpr.3du_Aux.j.jri̯.t",
        "69050": "Inf.gem_Neg.bwpw",
        "69051": "Inf.gem.stpr.1sg_Neg.bwpw",
        "69052": "Inf.gem.stpr.2sgm_Neg.bwpw",
        "69053": "Inf.gem.stpr.2sgf_Neg.bwpw",
        "69054": "Inf.gem.stpr.3sgm_Neg.bwpw",
        "69055": "Inf.gem.stpr.3sgf_Neg.bwpw",
        "69056": "Inf.gem.stpr.3sg_Neg.bwpw",
        "69057": "Inf.gem.stpr.1pl_Neg.bwpw",
        "-69057": "Inf.gem.stpr.1du_Neg.bwpw",
        "69058": "Inf.gem.stpr.2pl_Neg.bwpw",
        "-69058": "Inf.gem.stpr.2du_Neg.bwpw",
        "69059": "Inf.gem.stpr.3pl_Neg.bwpw",
        "-69059": "Inf.gem.stpr.3du_Neg.bwpw",
        "69060": "Inf.gem_Aux.mtw=",
        "69061": "Inf.gem.stpr.1sg_Aux.mtw=",
        "69062": "Inf.gem.stpr.2sgm_Aux.mtw=",
        "69063": "Inf.gem.stpr.2sgf_Aux.mtw=",
        "69064": "Inf.gem.stpr.3sgm_Aux.mtw=",
        "69065": "Inf.gem.stpr.3sgf_Aux.mtw=",
        "69066": "Inf.gem.stpr.3sg_Aux.mtw=",
        "69067": "Inf.gem.stpr.1pl_Aux.mtw=",
        "-69067": "Inf.gem.stpr.1du_Aux.mtw=",
        "69068": "Inf.gem.stpr.2pl_Aux.mtw=",
        "-69068": "Inf.gem.stpr.2du_Aux.mtw=",
        "69069": "Inf.gem.stpr.3pl_Aux.mtw=",
        "-69069": "Inf.gem.stpr.3du_Aux.mtw=",
        "69070": "Inf.gem_Aux.tw=",
        "69071": "Inf.gem.stpr.1sg_Aux.tw=",
        "69072": "Inf.gem.stpr.2sgm_Aux.tw=",
        "69073": "Inf.gem.stpr.2sgf_Aux.tw=",
        "69074": "Inf.gem.stpr.3sgm_Aux.tw=",
        "69075": "Inf.gem.stpr.3sgf_Aux.tw=",
        "69076": "Inf.gem.stpr.3sg_Aux.tw=",
        "69077": "Inf.gem.stpr.1pl_Aux.tw=",
        "-69077": "Inf.gem.stpr.1du_Aux.tw=",
        "69078": "Inf.gem.stpr.2pl_Aux.tw=",
        "-69078": "Inf.gem.stpr.2du_Aux.tw=",
        "69079": "Inf.gem.stpr.3pl_Aux.tw=",
        "-69079": "Inf.gem.stpr.3du_Aux.tw=",
        "69080": "Inf.gem_Aux.wn.jn",
        "69081": "Inf.gem.gem.stpr.1sg_Aux.wn.jn",
        "69082": "Inf.gem.stpr.2sgm_Aux.wn.jn",
        "69083": "Inf.gem.stpr.2sgf_Aux.wn.jn",
        "69084": "Inf.gem.stpr.3sgm_Aux.wn.jn",
        "69085": "Inf.gem.stpr.3sgf_Aux.wn.jn",
        "69086": "Inf.gem.stpr.3sg_Aux.wn.jn",
        "69087": "Inf.gem.stpr.1pl_Aux.wn.jn",
        "-69087": "Inf.gem.stpr.1du_Aux.wn.jn",
        "69088": "Inf.gem.stpr.2pl_Aux.wn.jn",
        "-69088": "Inf.gem.stpr.2du_Aux.wn.jn",
        "69089": "Inf.gem.stpr.3pl_Aux.wn.jn",
        "-69089": "Inf.gem.stpr.3du_Aux.wn.jn",
        "69090": "Inf.gem_Aux.wn.ḫr",
        "69091": "Inf.gem.stpr.1sg_Aux.wn.ḫr",
        "69092": "Inf.gem.stpr.2sgm_Aux.wn.ḫr",
        "69093": "Inf.gem.stpr.2sgf_Aux.wn.ḫr",
        "69094": "Inf.gem.stpr.3sgm_Aux.wn.ḫr",
        "69095": "Inf.gem.stpr.3sgf_Aux.wn.ḫr",
        "69096": "Inf.gem.stpr.3sg_Aux.wn.ḫr",
        "69097": "Inf.gem.stpr.1pl_Aux.wn.ḫr",
        "-69097": "Inf.gem.stpr.1du_Aux.wn.ḫr",
        "69098": "Inf.gem.stpr.2pl_Aux.wn.ḫr",
        "-69098": "Inf.gem.stpr.2du_Aux.wn.ḫr",
        "69099": "Inf.gem.stpr.3pl_Aux.wn.ḫr",
        "-69099": "Inf.gem.stpr.3du_Aux.wn.ḫr",
        "69100": "Inf.gem_Neg.bw jri̯",
        "69101": "Inf.gem.stpr.1sg_Neg.bw jri̯",
        "69102": "Inf.gem.stpr.2sgm_Neg.bw jri̯",
        "69103": "Inf.gem.stpr.2sgf_Neg.bw jri̯",
        "69104": "Inf.gem.stpr.3sgm_Neg.bw jri̯",
        "69105": "Inf.gem.stpr.3sgf_Neg.bw jri̯",
        "69106": "Inf.gem.stpr.3sg_Neg.bw jri̯",
        "69107": "Inf.gem.stpr.1pl_Neg.bw jri̯",
        "-69107": "Inf.gem.stpr.1du_Neg.bw jri̯",
        "69108": "Inf.gem.stpr.2pl_Neg.bw jri̯",
        "-69108": "Inf.gem.stpr.2du_Neg.bw jri̯",
        "69109": "Inf.gem.stpr.3pl_Neg.bw jri̯",
        "-69109": "Inf.gem.stpr.3du_Neg.bw jri̯",
        "69110": "Inf.gem_Neg.bw j.jri̯.t",
        "69111": "Inf.gem.stpr.1sg_Neg.bw j.jri̯.t",
        "69112": "Inf.gem.stpr.2sgm_Neg.bw j.jri̯.t",
        "69113": "Inf.gem.stpr.2sgf_Neg.bw j.jri̯.t",
        "69114": "Inf.gem.stpr.3sgm_Neg.bw j.jri̯.t",
        "69115": "Inf.gem.stpr.3sgf_Neg.bw j.jri̯.t",
        "69116": "Inf.gem.stpr.3sg_Neg.bw j.jri̯.t",
        "69117": "Inf.gem.stpr.1pl_Neg.bw j.jri̯.t",
        "-69117": "Inf.gem.stpr.1du_Neg.bw j.jri̯.t",
        "69118": "Inf.gem.stpr.2pl_Neg.bw j.jri̯.t",
        "-69118": "Inf.gem.stpr.2du_Neg.bw j.jri̯.t",
        "69119": "Inf.gem.stpr.3pl_Neg.bw j.jri̯.t",
        "-69119": "Inf.gem.stpr.3du_Neg.bw j.jri̯.t",
        "69120": "Inf.gem_Neg.bn jw",
        "69121": "Inf.gem.stpr.1sg_Neg.bn jw",
        "69122": "Inf.gem.stpr.2sgm_Neg.bn jw",
        "69123": "Inf.gem.stpr.2sgf_Neg.bn jw",
        "69124": "Inf.gem.stpr.3sgm_Neg.bn jw",
        "69125": "Inf.gem.stpr.3sgf_Neg.bn jw",
        "69126": "Inf.gem.stpr.3sg_Neg.bn jw",
        "69127": "Inf.gem.stpr.1pl_Neg.bn jw",
        "-69127": "Inf.gem.stpr.1du_Neg.bn jw",
        "69128": "Inf.gem.stpr.2pl_Neg.bn jw",
        "-69128": "Inf.gem.stpr.2du_Neg.bn jw",
        "69129": "Inf.gem.stpr.3pl_Neg.bn jw",
        "-69129": "Inf.gem.stpr.3du_Neg.bn jw",
        "69130": "Inf.gem_Neg.bn jri̯ jwnꜣ",
        "69131": "Inf.gem.stpr.1sg_Neg.bn jri̯ jwnꜣ",
        "69132": "Inf.gem.stpr.2sgm_Neg.bn jri̯ jwnꜣ",
        "69133": "Inf.gem.stpr.2sgf_Neg.bn jri̯ jwnꜣ",
        "69134": "Inf.gem.stpr.3sgm_Neg.bn jri̯ jwnꜣ",
        "69135": "Inf.gem.stpr.3sgf_Neg.bn jri̯ jwnꜣ",
        "69136": "Inf.gem.stpr.3sg_Neg.bn jri̯ jwnꜣ",
        "69137": "Inf.gem.stpr.1pl_Neg.bn jri̯ jwnꜣ",
        "-69137": "Inf.gem.stpr.1du_Neg.bn jri̯ jwnꜣ",
        "69138": "Inf.gem.stpr.2pl_Neg.bn jri̯ jwnꜣ",
        "-69138": "Inf.gem.stpr.2du_Neg.bn jri̯ jwnꜣ",
        "69139": "Inf.gem.stpr.3pl_Neg.bn jri̯ jwnꜣ",
        "-69139": "Inf.gem.stpr.3du_Neg.bn jri̯ jwnꜣ",
        "69140": "Inf.gem_Neg.bn tw= (jwnꜣ)",
        "69141": "Inf.gem.stpr.1sg_Neg.bn tw= (jwnꜣ)",
        "69142": "Inf.gem.stpr.2sgm_Neg.bn tw= (jwnꜣ)",
        "69143": "Inf.gem.stpr.2sgf_Neg.bn tw= (jwnꜣ)",
        "69144": "Inf.gem.stpr.3sgm_Neg.bn tw= (jwnꜣ)",
        "69145": "Inf.gem.stpr.3sgf_Neg.bn tw= (jwnꜣ)",
        "69146": "Inf.gem.stpr.3sg_Neg.bn tw= (jwnꜣ)",
        "69147": "Inf.gem.stpr.1pl_Neg.bn tw= (jwnꜣ)",
        "-69147": "Inf.gem.stpr.1du_Neg.bn tw= (jwnꜣ)",
        "69148": "Inf.gem.stpr.2pl_Neg.bn tw= (jwnꜣ)",
        "-69148": "Inf.gem.stpr.2du_Neg.bn tw= (jwnꜣ)",
        "69149": "Inf.gem.stpr.3pl_Neg.bn tw= (jwnꜣ)",
        "-69149": "Inf.gem.stpr.3du_Neg.bn tw= (jwnꜣ)",
        "69150": "Inf.gem_Neg.tm",
        "69151": "Inf.gem.stpr.1sg_Neg.tm",
        "69152": "Inf.gem.stpr.2sgm_Neg.tm",
        "69153": "Inf.gem.stpr.2sgf_Neg.tm",
        "69154": "Inf.gem.stpr.3sgm_Neg.tm",
        "69155": "Inf.gem.stpr.3sgf_Neg.tm",
        "69156": "Inf.gem.stpr.3sg_Neg.tm",
        "69157": "Inf.gem.stpr.1pl_Neg.tm",
        "-69157": "Inf.gem.stpr.1du_Neg.tm",
        "69158": "Inf.gem.stpr.2pl_Neg.tm",
        "-69158": "Inf.gem.stpr.2du_Neg.tm",
        "69159": "Inf.gem.stpr.3pl_Neg.tm",
        "-69159": "Inf.gem.stpr.3du_Neg.tm",
        "69160": "Inf.gem_Neg.m-jri̯",
        "69161": "Inf.gem.stpr.1sg_Neg.m jri̯",
        "69162": "Inf.gem.stpr.2sgm_Neg.m jri̯",
        "69163": "Inf.gem.stpr.2sgf_Neg.m jri̯",
        "69164": "Inf.gem.stpr.3sgm_Neg.m jri̯",
        "69165": "Inf.gem.stpr.3sgf_Neg.m jri̯",
        "69166": "Inf.gem.stpr.3sg_Neg.m jri̯",
        "69167": "Inf.gem.stpr.1pl_Neg.m jri̯",
        "-69167": "Inf.gem.stpr.1du_Neg.m jri̯",
        "69168": "Inf.gem.stpr.2pl_Neg.m jri̯",
        "-69168": "Inf.gem.stpr.2du_Neg.m jri̯",
        "69169": "Inf.gem.stpr.3pl_Neg.m jri̯",
        "-69169": "Inf.gem.stpr.3du_Neg.m jri̯",
        "69170": "Inf.gem_Neg.nn jw",
        "69171": "Inf.gem.stpr.1sg_Neg.nn jw",
        "69172": "Inf.gem.stpr.2sgm_Neg.nn jw",
        "69173": "Inf.gem.stpr.2sgf_Neg.nn jw",
        "69174": "Inf.gem.stpr.3sgm_Neg.nn jw",
        "69175": "Inf.gem.stpr.3sgf_Neg.nn jw",
        "69176": "Inf.gem.stpr.3sg_Neg.nn jw",
        "69177": "Inf.gem.stpr.1pl_Neg.nn jw",
        "-69177": "Inf.gem.stpr.1du_Neg.nn jw",
        "69178": "Inf.gem.stpr.2pl_Neg.nn jw",
        "-69178": "Inf.gem.stpr.2du_Neg.nn jw",
        "69179": "Inf.gem.stpr.3pl_Neg.nn jw",
        "-69179": "Inf.gem.stpr.3du_Neg.nn jw",
        "69180": "Inf.gem_Neg.m",
        "69181": "Inf.gem.stpr.1sg_Neg.m",
        "69182": "Inf.gem.stpr.2sgm_Neg.m",
        "69183": "Inf.gem.stpr.2sgf_Neg.m",
        "69184": "Inf.gem.stpr.3sgm_Neg.m",
        "69185": "Inf.gem.stpr.3sgf_Neg.m",
        "69186": "Inf.gem.stpr.3sg_Neg.m",
        "69187": "Inf.gem.stpr.1pl_Neg.m",
        "-69187": "Inf.gem.stpr.1du_Neg.m",
        "69188": "Inf.gem.stpr.2pl_Neg.m",
        "-69188": "Inf.gem.stpr.2du_Neg.m",
        "69189": "Inf.gem.stpr.3pl_Neg.m",
        "-69189": "Inf.gem.stpr.3du_Neg.m",
        "69200": "Inf.gem_Neg.nfr/nfr-n/nfr-pw",
        "69201": "Inf.gem.stpr.1sg_Neg.nfr/nfr-n/nfr-pw",
        "69202": "Inf.gem.stpr.2sgm_Neg.nfr/nfr-n/nfr-pw",
        "69203": "Inf.gem.stpr.2sgf_Neg.nfr/nfr-n/nfr-pw",
        "69204": "Inf.gem.stpr.3sgm_Neg.nfr/nfr-n/nfr-pw",
        "69205": "Inf.gem.stpr.3sgf_Neg.nfr/nfr-n/nfr-pw",
        "69206": "Inf.gem.stpr.3sg_Neg.nfr/nfr-n/nfr-pw",
        "69207": "Inf.gem.stpr.1pl_Neg.nfr/nfr-n/nfr-pw",
        "-69207": "Inf.gem.stpr.1du_Neg.nfr/nfr-n/nfr-pw",
        "69208": "Inf.gem.stpr.2pl_Neg.nfr/nfr-n/nfr-pw",
        "-69208": "Inf.gem.stpr.2du_Neg.nfr/nfr-n/nfr-pw",
        "69209": "Inf.gem.stpr.3pl_Neg.nfr/nfr-n/nfr-pw",
        "-69209": "Inf.gem.stpr.3du_Neg.nfr/nfr-n/nfr-pw",
        "69400": "Inf.gem_Aux.wn",
        "69401": "Inf.gem.stpr.1sg_Aux.wn",
        "69402": "Inf.gem.stpr.2sgm_Aux.wn",
        "69403": "Inf.gem.stpr.2sgf_Aux.wn",
        "69404": "Inf.gem.stpr.3sgm_Aux.wn",
        "69405": "Inf.gem.stpr.3sgf_Aux.wn",
        "69406": "Inf.gem.stpr.3sg_Aux.wn",
        "69407": "Inf.gem.stpr.1pl_Aux.wn",
        "-69407": "Inf.gem.stpr.1du_Aux.wn",
        "69408": "Inf.gem.stpr.2pl_Aux.wn",
        "-69408": "Inf.gem.stpr.2du_Aux.wn",
        "69409": "Inf.gem.stpr.3pl_Aux.wn",
        "-69409": "Inf.gem.stpr.3du_Aux.wn",
        "69500": "Inf.gem_Aux.ꜥḥꜥ.n",
        "69501": "Inf.gem.stpr.1sg_Aux.ꜥḥꜥ.n",
        "69502": "Inf.gem.stpr.2sgm_Aux.ꜥḥꜥ.n",
        "69503": "Inf.gem.stpr.2sgf_Aux.ꜥḥꜥ.n",
        "69504": "Inf.gem.stpr.3sgm_Aux.ꜥḥꜥ.n",
        "69505": "Inf.gem.stpr.3sgf_Aux.ꜥḥꜥ.n",
        "69506": "Inf.gem.stpr.3sg_Aux.ꜥḥꜥ.n",
        "69507": "Inf.gem.stpr.1pl_Aux.ꜥḥꜥ.n",
        "-69507": "Inf.gem.stpr.1du_Aux.ꜥḥꜥ.n",
        "69508": "Inf.gem.stpr.2pl_Aux.ꜥḥꜥ.n",
        "-69508": "Inf.gem.stpr.2du_Aux.ꜥḥꜥ.n",
        "69509": "Inf.gem.stpr.3pl_Aux.ꜥḥꜥ.n",
        "-69509": "Inf.gem.stpr.3du_Aux.ꜥḥꜥ.n",
        "69600": "Inf.gem_Aux.mk",
        "69601": "Inf.gem.stpr.1sg_Aux.mk",
        "69602": "Inf.gem.stpr.2sgm_Aux.mk",
        "69603": "Inf.gem.stpr.2sgf_Aux.mk",
        "69604": "Inf.gem.stpr.3sgm_Aux.mk",
        "69605": "Inf.gem.stpr.3sgf_Aux.mk",
        "69606": "Inf.gem.stpr.3sg_Aux.mk",
        "69607": "Inf.gem.stpr.1pl_Aux.mk",
        "-69607": "Inf.gem.stpr.1du_Aux.mk",
        "69608": "Inf.gem.stpr.2pl_Aux.mk",
        "-69608": "Inf.gem.stpr.2du_Aux.mk",
        "69609": "Inf.gem.stpr.3pl_Aux.mk",
        "-69609": "Inf.gem.stpr.3du_Aux.mk",
        "69700": "Inf.gem_Neg.nn",
        "69701": "Inf.gem.stpr.1sg_Neg.nn",
        "69702": "Inf.gem.stpr.2sgm_Neg.nn",
        "69703": "Inf.gem.stpr.2sgf_Neg.nn",
        "69704": "Inf.gem.stpr.3sgm_Neg.nn",
        "69705": "Inf.gem.stpr.3sgf_Neg.nn",
        "69706": "Inf.gem.stpr.3sg_Neg.nn",
        "69707": "Inf.gem.stpr.1pl_Neg.nn",
        "-69707": "Inf.gem.stpr.1du_Neg.nn",
        "69708": "Inf.gem.stpr.2pl_Neg.nn",
        "-69708": "Inf.gem.stpr.2du_Neg.nn",
        "69709": "Inf.gem.stpr.3pl_Neg.nn",
        "-69709": "Inf.gem.stpr.3du_Neg.nn",
        "69800": "Inf.gem_Aux.wnn",
        "69801": "Inf.gem.stpr.1sg_Aux.wnn",
        "69802": "Inf.gem.stpr.2sgm_Aux.wnn",
        "69803": "Inf.gem.stpr.2sgf_Aux.wnn",
        "69804": "Inf.gem.stpr.3sgm_Aux.wnn",
        "69805": "Inf.gem.stpr.3sgf_Aux.wnn",
        "69806": "Inf.gem.stpr.3sg_Aux.wnn",
        "69807": "Inf.gem.stpr.1pl_Aux.wnn",
        "-69807": "Inf.gem.stpr.1du_Aux.wnn",
        "69808": "Inf.gem.stpr.2pl_Aux.wnn",
        "-69808": "Inf.gem.stpr.2du_Aux.wnn",
        "69809": "Inf.gem.stpr.3pl_Aux.wnn",
        "-69809": "Inf.gem.stpr.3du_Aux.wnn",
        "70000": "Noun.sg.stabs",
        "70050": "Noun.sg.stpr.suffx.unspec.",
        "70051": "Noun.sg.stpr.1sg",
        "70052": "Noun.sg.stpr.2sgm",
        "70053": "Noun.sg.stpr.2sgf",
        "70054": "Noun.sg.stpr.3sgm",
        "70055": "Noun.sg.stpr.3sgf",
        "70056": "Noun.sg.stpr.3sg",
        "70057": "Noun.sg.stpr.1pl",
        "-70057": "Noun.sg.stpr.1du",
        "70058": "Noun.sg.stpr.2pl",
        "-70058": "Noun.sg.stpr.2du",
        "70059": "Noun.sg.stpr.3pl",
        "-70059": "Noun.sg.stpr.3du",
        "70060": "Noun.sg.stc",
        "70100": "Noun.pl.stabs",
        "70150": "Noun.pl.stpr.suffx.unspec.",
        "70151": "Noun.pl.stpr.1sg",
        "70152": "Noun.pl.stpr.2sgm",
        "-70152": "Noun.pl.stpr.2sgm_du",
        "70153": "Noun.pl.stpr.2sgf",
        "70154": "Noun.pl.stpr.3sgm",
        "-70154": "Noun.pl.stpr.3sgm_du",
        "70155": "Noun.pl.stpr.3sgf",
        "-70155": "Noun.pl.stpr.3sgf_du",
        "70156": "Noun.pl.stpr.3sg",
        "70157": "Noun.pl.stpr.1pl",
        "-70157": "Noun.pl.stpr.1du",
        "70158": "Noun.pl.stpr.2pl",
        "-70158": "Noun.pl.stpr.2du",
        "70159": "Noun.pl.stpr.3pl",
        "-70159": "Noun.pl.stpr.3du",
        "70160": "Noun.pl.stc",
        "70300": "Noun.du.stabs",
        "70350": "Noun.du.stpr.suffx.unspec.",
        "70351": "Noun.du.stpr.1sg",
        "70352": "Noun.du.stpr.2sgm",
        "-70352": "Noun.du.stpr.2sgm_du",
        "70353": "Noun.du.stpr.2sgf",
        "70354": "Noun.du.stpr.3sgm",
        "-70354": "Noun.du.stpr.3sgm_du",
        "70355": "Noun.du.stpr.3sgf",
        "-70355": "Noun.du.stpr.3sgf_du",
        "70356": "Noun.du.stpr.3sg",
        "70357": "Noun.du.stpr.1pl",
        "-70357": "Noun.du.stpr.1du",
        "70358": "Noun.du.stpr.2pl",
        "-70358": "Noun.du.stpr.2du",
        "70359": "Noun.du.stpr.3pl",
        "-70359": "Noun.du.stpr.3du",
        "70360": "Noun.du.stc",
        "71000": "Adj.unspec.",
        "71010": "Adj.sgm",
        "71020": "Adj.sgf",
        "71030": "Adj.plm",
        "71040": "Adj.plf",
        "71050": "Adj.dum",
        "71060": "Adj.duf",
        "71100": "Adj.dep.pr.pr.unspec.",
        "71115": "Adj.dep.pr.1sg",
        "71116": "Adj.dep.pr.2sgm",
        "71117": "Adj.dep.pr.2sgf",
        "71118": "Adj.dep.pr.3sgm",
        "71119": "Adj.dep.pr.3sgf",
        "71120": "Adj.dep.pr.3sg",
        "71121": "Adj.dep.pr.1pl",
        "71122": "Adj.dep.pr.2pl",
        "71123": "Adj.dep.pr.3pl",
        "71124": "Adj.dep.pr.3pl/st",
        "71200": "Adj.sgm.stpr.suffx.unspec.",
        "71201": "Adj.sgm.stpr.1sg",
        "71202": "Adj.sgm.stpr.2sgm",
        "71203": "Adj.sgm.stpr.2sgf",
        "71204": "Adj.sgm.stpr.3sgm",
        "71205": "Adj.sgm.stpr.3sgf",
        "71206": "Adj.sgm.stpr.3sg",
        "71207": "Adj.sgm.stpr.1pl",
        "-71207": "Adj.sgm.stpr.1du",
        "71208": "Adj.sgm.stpr.2pl",
        "-71208": "Adj.sgm.stpr.2du",
        "71209": "Adj.sgm.stpr.3pl",
        "-71209": "Adj.sgm.stpr.3du",
        "71210": "Adj.sgf.stpr.suffx.unspec.",
        "71211": "Adj.sgf.stpr.1sg",
        "71212": "Adj.sgf.stpr.2sgm",
        "71213": "Adj.sgf.stpr.2sgf",
        "71214": "Adj.sgf.stpr.3sgm",
        "71215": "Adj.sgf.stpr.3sgf",
        "71216": "Adj.sgf.stpr.3sg",
        "71217": "Adj.sgf.stpr.1pl",
        "-71217": "Adj.sgf.stpr.1du",
        "71218": "Adj.sgf.stpr.2pl",
        "-71218": "Adj.sgf.stpr.2du",
        "71219": "Adj.sgf.stpr.3pl",
        "-71219": "Adj.sgf.stpr.3du",
        "71220": "Adj.plm.stpr.suffx.unspec.",
        "71221": "Adj.plm.stpr.1sg",
        "71222": "Adj.plm.stpr.2sgm",
        "71223": "Adj.plm.stpr.2sgf",
        "71224": "Adj.plm.stpr.3sgm",
        "71225": "Adj.plm.stpr.3sgf",
        "71226": "Adj.plm.stpr.3sg",
        "71227": "Adj.plm.stpr.1pl",
        "-71227": "Adj.plm.stpr.1du",
        "71228": "Adj.plm.stpr.2pl",
        "-71228": "Adj.plm.stpr.2du",
        "71229": "Adj.plm.stpr.3pl",
        "-71229": "Adj.plm.stpr.3du",
        "71230": "Adj.plf.stpr.suffx.unspec.",
        "71231": "Adj.plf.stpr.1sg",
        "71232": "Adj.plf.stpr.2sgm",
        "71233": "Adj.plf.stpr.2sgf",
        "71234": "Adj.plf.stpr.3sgm",
        "71235": "Adj.plf.stpr.3sgf",
        "71236": "Adj.plf.stpr.3sg",
        "71237": "Adj.plf.stpr.1pl",
        "-71237": "Adj.plf.stpr.1du",
        "71238": "Adj.plf.stpr.2pl",
        "-71238": "Adj.plf.stpr.2du",
        "71239": "Adj.plf.stpr.3pl",
        "-71239": "Adj.plf.stpr.3du",
        "71240": "Adj.dum.stpr.suffx.unspec.",
        "71241": "Adj.dum.stpr.1sg",
        "71242": "Adj.dum.stpr.2sgm",
        "71243": "Adj.dum.stpr.2sgf",
        "71244": "Adj.dum.stpr.3sgm",
        "71245": "Adj.dum.stpr.3sgf",
        "71246": "Adj.dum.stpr.3sg",
        "71247": "Adj.dum.stpr.1pl",
        "-71247": "Adj.dum.stpr.1du",
        "71248": "Adj.dum.stpr.2pl",
        "-71248": "Adj.dum.stpr.2du",
        "71249": "Adj.dum.stpr.3pl",
        "-71249": "Adj.dum.stpr.3du",
        "71250": "Adj.duf.stpr.suffx.unspec.",
        "71251": "Adj.duf.stpr.1sg",
        "71252": "Adj.duf.stpr.2sgm",
        "71253": "Adj.duf.stpr.2sgf",
        "71254": "Adj.duf.stpr.sgm",
        "71255": "Adj.duf.stpr.3sgf",
        "71256": "Adj.duf.stpr.3sg",
        "71257": "Adj.duf.stpr.1pl",
        "-71257": "Adj.duf.stpr.1du",
        "71258": "Adj.duf.stpr.2pl",
        "-71258": "Adj.duf.stpr.2du",
        "71259": "Adj.duf.stpr.3pl",
        "-71259": "Adj.duf.stpr.3du",
        "71260": "nꜣ.Adj as SC.suffx.unspec.",
        "71261": "nꜣ.Adj as SC.1sg",
        "71262": "nꜣ.Adj as SC.2sgm",
        "71263": "nꜣ.Adj as SC.2sgf",
        "71264": "nꜣ.Adj as SC.3sgm",
        "71265": "nꜣ.Adj as SC.3sgf",
        "71266": "nꜣ.Adj as SC.3sg",
        "71267": "nꜣ.Adj as SC.1pl",
        "-71267": "nꜣ.Adj as SC.1du",
        "71268": "nꜣ.Adj as SC.2pl",
        "-71268": "nꜣ.Adj as SC.2du",
        "71269": "nꜣ.Adj as SC.3pl",
        "-71269": "nꜣ.Adj as SC.3du",
        "71270": "Adj.plm.dep.pr",
        "71280": "Adj.plf.dep.pr",
        "71320": "Adj.f",
        "71500": "Adj.unmarked",
        "71610": "Adj.f.stpr.suffx.unspec.",
        "71611": "Adj.f.stpr.1sg",
        "71612": "Adj.f.stpr.2sgm",
        "71613": "Adj.f.stpr.2sgf",
        "71614": "Adj.f.stpr.3sgm",
        "71615": "Adj.f.stpr.3sgf",
        "71616": "Adj.f.stpr.3sg",
        "71617": "Adj.f.stpr.1pl",
        "-71617": "Adj.f.stpr.1du",
        "71618": "Adj.f.stpr.2pl",
        "-71618": "Adj.f.stpr.2du",
        "71619": "Adj.f.stpr.3pl",
        "-71619": "Adj.f.stpr.3du",
        "72000": "Adv.stpr.suffx.unspec.",
        "72001": "Adv.stpr.1sg",
        "72002": "Adv.stpr.2sgm",
        "72003": "Adv.stpr.2sgf",
        "72004": "Adv.stpr.3sgm",
        "72005": "Adv.stpr.3sgf",
        "72006": "Adv.stpr.3sg",
        "72007": "Adv.stpr.1pl",
        "-72007": "Adv.stpr.1du",
        "72008": "Adv.stpr.2pl",
        "-72008": "Adv.stpr.2du",
        "72009": "Adv.stpr.3pl",
        "-72009": "Adv.stpr.3du",
        "73000": "Adv",
        "74006": "Ord.unspec.stpr.3sg",
        "74010": "Ord.m",
        "74014": "Ord.m.stpr.3sgm",
        "74018": "Ord.m.stpr.2pl",
        "74019": "Ord.m.stpr.3pl",
        "74020": "Ord.f",
        "74024": "Ord.f.stpr.3sgm",
        "74030": "Card.m",
        "74034": "Card.m.stpr.3sgm",
        "74038": "Card.m.stpr.2pl",
        "74039": "Card.m.stpr.3pl",
        "74040": "Card.f",
        "74041": "Card.f.stpr.1sg",
        "74042": "Card.f.stpr.2sgm",
        "74044": "Card.f.stpr.3sgm",
        "74045": "Card.f.stpr.3sgf",
        "80000": "Poss.art.suffx.unspec.",
        "80001": "Poss.art.1sg",
        "80002": "Poss.art.2sgm",
        "80003": "Poss.art.2sgf",
        "80004": "Poss.art.3sgm",
        "80005": "Poss.art.3sgf",
        "80006": "Poss.art.3sg",
        "80007": "Poss.art.1pl",
        "-80007": "Poss.art.1du",
        "80008": "Poss.art.2pl",
        "-80008": "Poss.art.2du",
        "80009": "Poss.art.3pl",
        "-80009": "Poss.art.3du",
        "80100": "Rel.pr.sgm",
        "80200": "Rel.pr.sgf",
        "80201": "Rel.pr.sgf.stpr.1sg",
        "80202": "Rel.pr.sgf.stpr.2sgm",
        "80203": "Rel.pr.sgf.stpr.2sgf",
        "80204": "Rel.pr.sgf.stpr.3sgm",
        "80205": "Rel.pr.sgf.stpr.3sgf",
        "80206": "Rel.pr.sgf.stpr.3sg",
        "80207": "Rel.pr.sgf.stpr.1pl",
        "-80207": "Rel.pr.sgf.stpr.1du",
        "80208": "Rel.pr.sgf.stpr.2pl",
        "-80208": "Rel.pr.sgf.stpr.2du",
        "80209": "Rel.pr.sgf.stpr.3pl",
        "-80209": "Rel.pr.sgf.stpr.3du",
        "80215": "Rel.pr.sgf.dep.pr.1sg",
        "80216": "Rel.pr.sgf.dep.pr.2sgm",
        "80217": "Rel.pr.sgf.dep.pr.2sgf",
        "80218": "Rel.pr.sgf.dep.pr.3sgm",
        "80219": "Rel.pr.sgf.dep.pr.3sgf",
        "80220": "Rel.pr.sgf.dep.pr.3sg",
        "80221": "Rel.pr.sgf.dep.pr.1pl",
        "80222": "Rel.pr.sgf.dep.pr.2pl",
        "80223": "Rel.pr.sgf.dep.pr.3pl",
        "80224": "Rel.pr.sgf.dep.pr.3pl (st)",
        "80300": "Rel.pr.plm",
        "80301": "Rel.pr.plm.stpr.1sg",
        "80302": "Rel.pr.plm.stpr.2sgm",
        "80303": "Rel.pr.plm.stpr.2sgf",
        "80304": "Rel.pr.plm.stpr.3sgm",
        "80305": "Rel.pr.plm.stpr.3sgf",
        "80306": "Rel.pr.plm.stpr.3sg",
        "80307": "Rel.pr.plm.stpr.1pl",
        "-80307": "Rel.pr.plm.stpr.1du",
        "80308": "Rel.pr.plm.stpr.2pl",
        "-80308": "Rel.pr.plm.stpr.2du",
        "80309": "Rel.pr.plm.stpr.3pl",
        "-80309": "Rel.pr.plm.stpr.3du",
        "80315": "Rel.pr.plm.dep.pr.1sg",
        "80316": "Rel.pr.plm.dep.pr.2sgm",
        "80317": "Rel.pr.plm.dep.pr.2sgf",
        "80318": "Rel.pr.plm.dep.pr.3sgm",
        "80319": "Rel.pr.plm.dep.pr.3sgf",
        "80320": "Rel.pr.plm.dep.pr.3sg",
        "80321": "Rel.pr.plm.dep.pr.1pl",
        "80322": "Rel.pr.plm.dep.pr.2pl",
        "80323": "Rel.pr.plm.dep.pr.3pl",
        "80324": "Rel.pr.plm.dep.pr.3pl (st)",
        "80400": "Rel.pr.plf",
        "80401": "Rel.pr.plf.stpr.1sg",
        "80402": "Rel.pr.plf.stpr.2sgm",
        "80403": "Rel.pr.plf.stpr.2sgf",
        "80404": "Rel.pr.plf.stpr.3sgm",
        "80405": "Rel.pr.plf.stpr.3sgf",
        "80406": "Rel.pr.plf.stpr.3sg",
        "80407": "Rel.pr.plf.stpr.1pl",
        "-80407": "Rel.pr.plf.stpr.1du",
        "80408": "Rel.pr.plf.stpr.2pl",
        "-80408": "Rel.pr.plf.stpr.2du",
        "80409": "Rel.pr.plf.stpr.3pl",
        "-80409": "Rel.pr.plf.stpr.3du",
        "80415": "Rel.pr.plf.dep.pr.1sg",
        "80416": "Rel.pr.plf.dep.pr.2sgm",
        "80417": "Rel.pr.plf.dep.pr.2sgf",
        "80418": "Rel.pr.plf.dep.pr.3sgm",
        "80419": "Rel.pr.plf.dep.pr.3sgf",
        "80420": "Rel.pr.plf.dep.pr.3sg",
        "80421": "Rel.pr.plf.dep.pr.1pl",
        "80422": "Rel.pr.plf.dep.pr.2pl",
        "80423": "Rel.pr.plf.dep.pr.3pl",
        "80424": "Rel.pr.plf.dep.pr.3pl (st)",
        "80500": "Rel.pr.dum",
        "80501": "Rel.pr.dum.stpr.1sg",
        "80502": "Rel.pr.dum.stpr.2sgm",
        "80503": "Rel.pr.dum.stpr.2sgf",
        "80504": "Rel.pr.dum.stpr.3sgm",
        "80505": "Rel.pr.dum.stpr.3sgf",
        "80506": "Rel.pr.dum.stpr.3sg",
        "80507": "Rel.pr.dum.stpr.1pl",
        "-80507": "Rel.pr.dum.stpr.1du",
        "80508": "Rel.pr.dum.stpr.2pl",
        "-80508": "Rel.pr.dum.stpr.2du",
        "80509": "Rel.pr.dum.stpr.3pl",
        "-80509": "Rel.pr.dum.stpr.3du",
        "80515": "Rel.pr.dum.dep.pr.1sg",
        "80516": "Rel.pr.dum.dep.pr.2sgm",
        "80517": "Rel.pr.dum.dep.pr.2sgf",
        "80518": "Rel.pr.dum.dep.pr.3sgm",
        "80519": "Rel.pr.dum.dep.pr.3sgf",
        "80520": "Rel.pr.dum.dep.pr.3sg",
        "80521": "Rel.pr.dum.dep.pr.1pl",
        "80522": "Rel.pr.dum.dep.pr.2pl",
        "80523": "Rel.pr.dum.dep.pr.3pl",
        "80524": "Rel.pr.dum.dep.pr.3pl (st)",
        "80600": "Rel.pr.duf",
        "80601": "Rel.pr.duf.stpr.1sg",
        "80602": "Rel.pr.duf.stpr.2sgm",
        "80603": "Rel.pr.duf.stpr.2sgf",
        "80604": "Rel.pr.duf.stpr.3sgm",
        "80605": "Rel.pr.duf.stpr.3sgf",
        "80606": "Rel.pr.duf.stpr.3sg",
        "80607": "Rel.pr.duf.stpr.1pl",
        "-80607": "Rel.pr.duf.stpr.1du",
        "80608": "Rel.pr.duf.stpr.2pl",
        "-80608": "Rel.pr.duf.stpr.2du",
        "80609": "Rel.pr.duf.stpr.3pl",
        "-80609": "Rel.pr.duf.stpr.3du",
        "80615": "Rel.pr.duf.dep.pr.1sg",
        "80616": "Rel.pr.duf.dep.pr.2sgf",
        "80617": "Rel.pr.duf.dep.pr.2sgm",
        "80618": "Rel.pr.duf.dep.pr.3sgf",
        "80619": "Rel.pr.duf.dep.pr.3sgf",
        "80620": "Rel.pr.duf.dep.pr.3sg",
        "80621": "Rel.pr.duf.dep.pr.3pl (st)",
        "80622": "Rel.pr.duf.dep.pr.1pl",
        "80623": "Rel.pr.duf.dep.pr.2pl",
        "80624": "Rel.pr.duf.dep.pr.3pl",
        "81000": "Poss.art",
        "81001": "Rel.pr.unspec.stpr.1sg",
        "81002": "Rel.pr.unspec.stpr.2sgm",
        "81003": "Rel.pr.unspec.stpr.2sgf",
        "81004": "Rel.pr.unspec.stpr.3sgm",
        "81005": "Rel.pr.unspec.stpr.3sgf",
        "81006": "Rel.pr.unspec.stpr.3sg",
        "81007": "Rel.pr.unspec.stpr.1pl",
        "-81007": "Rel.pr.sgm.stpr.1du",
        "81008": "Rel.pr.unspec.stpr.2pl",
        "-81008": "Rel.pr.sgm.stpr.2du",
        "81009": "Rel.pr.unspec.stpr.3pl",
        "-81009": "Rel.pr.sgm.stpr.3du",
        "81015": "Rel.pr.sgm.dep.pr.1sg",
        "81016": "Rel.pr.sgm.dep.pr.2sgm",
        "81017": "Rel.pr.sgm.dep.pr.2sgf",
        "81018": "Rel.pr.sgm.dep.pr.3sgm",
        "81019": "Rel.pr.sgm.dep.pr.3sgf",
        "81020": "Rel.pr.sgm.dep.pr.3sg",
        "81021": "Rel.pr.sgm.dep.pr.1pl",
        "81022": "Rel.pr.sgm.dep.pr.2pl",
        "81023": "Rel.pr.sgm.dep.pr.3pl",
        "81024": "Rel.pr.sgm.dep.pr.3pl (st)",
        "81102": "Rel.pr.sgm.stpr.2sgm",
        "81104": "Rel.pr.sgm.stpr.3sgm",
        "81105": "Rel.pr.sgm.stpr.3sgf",
        "81308": "Rel.pr.plm.stpr.2pl",
        "81409": "Rel.pr.plf.stpr.3pl",
        "82000": "SC.unspec_Neg.bw",
        "82001": "SC.unspec.1sg_Neg.bw",
        "82002": "SC.unspec.2sgm_Neg.bw",
        "82004": "SC.unspec.3sgm_Neg.bw",
        "82005": "SC.unspec.3sgf_Neg.bw",
        "82006": "SC.unspec.3sg_Neg.bw",
        "82007": "SC.unspec.1pl_Neg.bw",
        "82008": "SC.unspec.2pl_Neg.bw",
        "82009": "SC.unspec.3pl_Neg.bw",
        "82020": "SC.act.ngem.nom.subj_Neg.bw",
        "82021": "SC.act.ngem.1sg_Neg.bw",
        "82022": "SC.act.ngem.2sgm_Neg.bw",
        "82023": "SC.act.ngem.2sgf_Neg.bw",
        "82024": "SC.act.ngem.3sgm_Neg.bw",
        "82025": "SC.act.ngem.3sgf_Neg.bw",
        "82026": "SC.act.ngem.3sg_Neg.bw",
        "82027": "SC.act.ngem.1pl_Neg.bw",
        "82028": "SC.act.ngem.2pl_Neg.bw",
        "82029": "SC.act.ngem.3pl_Neg.bw",
        "82030": "SC.act.ngem.1du_Neg.bw",
        "82031": "SC.act.ngem.2du_Neg.bw",
        "82032": "SC.act.ngem.3du_Neg.bw",
        "82040": "SC.pass.ngem.nom.subj_Neg.bw",
        "82041": "SC.pass.ngem.1sg_Neg.bw",
        "82042": "SC.pass.ngem.2sgm_Neg.bw",
        "82043": "SC.pass.ngem.2sgf_Neg.bw",
        "82044": "SC.pass.ngem.3sgm_Neg.bw",
        "82045": "SC.pass.ngem.3sgf_Neg.bw",
        "82046": "SC.pass.ngem.3sg_Neg.bw",
        "82047": "SC.pass.ngem.1pl_Neg.bw",
        "-82047": "SC.pass.ngem.1du_Neg.bw",
        "82048": "SC.pass.ngem.2pl_Neg.bw",
        "-82048": "SC.pass.ngem.2du_Neg.bw",
        "82049": "SC.pass.ngem.3pl_Neg.bw",
        "-82049": "SC.pass.ngem.3du_Neg.bw",
        "82100": "SC.act.gem.nom.subj_Neg.bw",
        "82101": "SC.act.gem.1sg_Neg.bw",
        "82102": "SC.act.gem.2sgm_Neg.bw",
        "82103": "SC.act.gem.2sgf_Neg.bw",
        "82104": "SC.act.gem.3sgm_Neg.bw",
        "82105": "SC.act.gem.3sgf_Neg.bw",
        "82106": "SC.act.gem.3sg_Neg.bw",
        "82107": "SC.act.gem.1pl_Neg.bw",
        "-82107": "SC.act.gem.1du_Neg.bw",
        "82108": "SC.act.gem.2pl_Neg.bw",
        "-82108": "SC.act.gem.2du_Neg.bw",
        "82109": "SC.act.gem.3pl_Neg.bw",
        "-82109": "SC.act.gem.3du_Neg.bw",
        "82120": "SC.pass.gem(redupl).nom.subj_Neg.bw. ",
        "82121": "SC.pass.gem(redupl).1sg_Neg.bw",
        "82122": "SC.pass.gem(redupl).2sgm_Neg.bw",
        "82123": "SC.pass.gem(redupl).2sgf_Neg.bw",
        "82124": "SC.pass.gem(redupl).3sgm_Neg.bw",
        "82125": "SC.pass.gem(redupl).3sgf_Neg.bw",
        "82126": "SC.pass.gem(redupl).3sg_Neg.bw",
        "82127": "SC.pass.gem(redupl).1pl_Neg.bw",
        "-82127": "SC.pass.gem(redupl).1du_Neg.bw",
        "82128": "SC.pass.gem(redupl).2pl_Neg.bw",
        "-82128": "SC.pass.gem(redupl).2du_Neg.bw",
        "82129": "SC.pass.gem(redupl).3pl_Neg.bw",
        "-82129": "SC.pass.gem(redupl).3du_Neg.bw",
        "82140": "SC.act.spec.nom.subj_Neg.bw",
        "82141": "SC.act.spec.1sg_Neg.bw",
        "82142": "SC.act.spec.2sgm_Neg.bw",
        "82143": "SC.act.spec.2sgf_Neg.bw",
        "82144": "SC.act.spec.3sgm_Neg.bw",
        "82145": "SC.act.spec.3sgf_Neg.bw",
        "82146": "SC.act.spec.3sg_Neg.bw",
        "82147": "SC.act.spec.1pl_Neg.bw",
        "-82147": "SC.act.spec.1du_Neg.bw",
        "82148": "SC.act.spec.2pl_Neg.bw",
        "-82148": "SC.act.spec.2du_Neg.bw",
        "82149": "SC.act.spec.3pl_Neg.bw",
        "-82149": "SC.act.spec.3du_Neg.bw",
        "82160": "SC.pass.spec.nom.subj_Neg.bw",
        "82161": "SC.pass.spec.1sg_Neg.bw",
        "82162": "SC.pass.spec.2sgm_Neg.bw",
        "82163": "SC.pass.spec.2sgf_Neg.bw",
        "82164": "SC.pass.spec.3sgm_Neg.bw",
        "82165": "SC.pass.spec.3sgf_Neg.bw",
        "82166": "SC.pass.spec.3sg_Neg.bw",
        "82167": "SC.pass.spec.1pl_Neg.bw",
        "-82167": "SC.pass.spec.1du_Neg.bw",
        "82168": "SC.pass.spec.2pl_Neg.bw",
        "-82168": "SC.pass.spec.2du_Neg.bw",
        "82169": "SC.pass.spec.3pl_Neg.bw",
        "-82169": "SC.pass.spec.3du_Neg.bw",
        "82170": "SC.tw.pass.spec.nom.subj_Neg.bw",
        "82171": "SC.tw.pass.spec.1sg_Neg.bw",
        "82172": "SC.tw.pass.spec.2sgm_Neg.bw",
        "82173": "SC.tw.pass.spec.2sgf_Neg.bw",
        "82174": "SC.tw.pass.spec.3sgm_Neg.bw",
        "82175": "SC.tw.pass.spec.3sgf_Neg.bw",
        "82176": "SC.tw.pass.spec.3sg_Neg.bw",
        "82177": "SC.tw.pass.spec.1pl_Neg.bw",
        "-82177": "SC.tw.pass.spec.1du_Neg.bw",
        "82178": "SC.tw.pass.spec.2pl_Neg.bw",
        "-82178": "SC.tw.pass.spec.2du_Neg.bw",
        "82179": "SC.tw.pass.spec.3pl_Neg.bw",
        "-82179": "SC.tw.pass.spec.3du_Neg.bw",
        "82180": "SC.w.act.ngem.nom.subj_Neg.bw",
        "82181": "SC.w.act.ngem.1sg_Neg.bw",
        "82182": "SC.w.act.ngem.2sgm_Neg.bw",
        "82183": "SC.w.act.ngem.2sgf_Neg.bw",
        "82184": "SC.w.act.ngem.3sgm_Neg.bw",
        "82185": "SC.w.act.ngem.3sgf_Neg.bw",
        "82186": "SC.w.act.ngem.3sg_Neg.bw",
        "82187": "SC.w.act.ngem.1pl_Neg.bw",
        "-82187": "SC.w.act.ngem.1du_Neg.bw",
        "82188": "SC.w.act.ngem.2pl_Neg.bw",
        "-82188": "SC.w.act.ngem.2du_Neg.bw",
        "82189": "SC.w.act.ngem.3pl_Neg.bw",
        "-82189": "SC.w.act.ngem.3du_Neg.bw",
        "82220": "SC.w.act.gem.nom.subj_Neg.bw",
        "82221": "SC.w.act.gem.1sg_Neg.bw",
        "82222": "SC.w.act.gem.2sgm_Neg.bw",
        "82223": "SC.w.act.gem.2sgf_Neg.bw",
        "82224": "SC.w.act.gem.3sgm_Neg.bw",
        "82225": "SC.w.act.gem.3sgf_Neg.bw",
        "82226": "SC.w.act.gem.3sg_Neg.bw",
        "82227": "SC.w.act.gem.1pl_Neg.bw",
        "-82227": "SC.w.act.gem.1du_Neg.bw",
        "82228": "SC.w.act.gem.2pl_Neg.bw",
        "-82228": "SC.w.act.gem.2du_Neg.bw",
        "82229": "SC.w.act.gem.3pl_Neg.bw",
        "-82229": "SC.w.act.gem.3du_Neg.bw",
        "82240": "SC.w.pass.ngem.nom.subj_Neg.bw",
        "82241": "SC.w.pass.ngem.1sg_Neg.bw",
        "82242": "SC.w.pass.ngem.2sgm_Neg.bw",
        "82243": "SC.w.pass.ngem.2sgf_Neg.bw",
        "82244": "SC.w.pass.ngem.3sgm_Neg.bw",
        "82245": "SC.w.pass.ngem.3sgf_Neg.bw",
        "82246": "SC.w.pass.ngem.3sg_Neg.bw",
        "82247": "SC.w.pass.ngem.1pl_Neg.bw",
        "-82247": "SC.w.pass.ngem.1du_Neg.bw",
        "82248": "SC.w.pass.ngem.2pl_Neg.bw",
        "-82248": "SC.w.pass.ngem.2du_Neg.bw",
        "82249": "SC.w.pass.ngem.3pl_Neg.bw",
        "-82249": "SC.w.pass.ngem.3du_Neg.bw",
        "82280": "SC.w.tw.pass.ngem.nom.subj_Neg.bw",
        "82281": "SC.w.tw.pass.ngem.1sg_Neg.bw",
        "82282": "SC.w.tw.pass.ngem.2sgm_Neg.bw",
        "82283": "SC.w.tw.pass.ngem.2sgf_Neg.bw",
        "82284": "SC.w.tw.pass.ngem.3sgm_Neg.bw",
        "82285": "SC.w.tw.pass.ngem.3sgf_Neg.bw",
        "82286": "SC.w.tw.pass.ngem.3sg_Neg.bw",
        "82287": "SC.w.tw.pass.ngem.1pl_Neg.bw",
        "-82287": "SC.w.tw.pass.ngem.1du_Neg.bw",
        "82288": "SC.w.tw.pass.ngem.2pl_Neg.bw",
        "-82288": "SC.w.tw.pass.ngem.2du_Neg.bw",
        "82289": "SC.w.tw.pass.ngem.3pl_Neg.bw",
        "-82289": "SC.w.tw.pass.ngem.3du_Neg.bw",
        "82320": "SC.tw.pass.ngem.nom.subj_Neg.bw",
        "82321": "SC.tw.pass.ngem.1sg_Neg.bw",
        "82322": "SC.tw.pass.ngem.2sgm_Neg.bw",
        "82323": "SC.tw.pass.ngem.2sgf_Neg.bw",
        "82324": "SC.tw.pass.ngem.3sgm_Neg.bw",
        "82325": "SC.tw.pass.ngem.3sgf_Neg.bw",
        "82326": "SC.tw.pass.ngem.3sg_Neg.bw",
        "82327": "SC.tw.pass.ngem.1pl_Neg.bw",
        "-82327": "SC.tw.pass.ngem.1du_Neg.bw",
        "82328": "SC.tw.pass.ngem.2pl_Neg.bw",
        "-82328": "SC.tw.pass.ngem.2du_Neg.bw",
        "82329": "SC.tw.pass.ngem.3pl_Neg.bw",
        "-82329": "SC.tw.pass.ngem.3du_Neg.bw",
        "82360": "SC.tw.pass.gem.nom.subj_Neg.bw",
        "82361": "SC.tw.pass.gem.1sg_Neg.bw",
        "82362": "SC.tw.pass.gem.2sgm_Neg.bw",
        "82363": "SC.tw.pass.gem.2sgf_Neg.bw",
        "82364": "SC.tw.pass.gem.3sgm_Neg.bw",
        "82365": "SC.tw.pass.gem.3sgf_Neg.bw",
        "82366": "SC.tw.pass.gem.3sg_Neg.bw",
        "82367": "SC.tw.pass.gem.1pl_Neg.bw",
        "-82367": "SC.tw.pass.gem.1du_Neg.bw",
        "82368": "SC.tw.pass.gem.2pl_Neg.bw",
        "-82368": "SC.tw.pass.gem.2du_Neg.bw",
        "82369": "SC.tw.pass.gem.3pl_Neg.bw",
        "-82369": "SC.tw.pass.gem.3du_Neg.bw",
        "82380": "SC.n.act.ngem.nom.subj_Neg.bw",
        "82381": "SC.n.act.ngem.1sg_Neg.bw",
        "82382": "SC.n.act.ngem.2sgm_Neg.bw",
        "82383": "SC.n.act.ngem.2sgf_Neg.bw",
        "82384": "SC.n.act.ngem.3sgm_Neg.bw",
        "82385": "SC.n.act.ngem.3sgf_Neg.bw",
        "82386": "SC.n.act.ngem.3sg_Neg.bw",
        "82387": "SC.n.act.ngem.1pl_Neg.bw",
        "-82387": "SC.n.act.ngem.1du_Neg.bw",
        "82388": "SC.n.act.ngem.2pl_Neg.bw",
        "-82388": "SC.n.act.ngem.2du_Neg.bw",
        "82389": "SC.n.act.ngem.3pl_Neg.bw",
        "-82389": "SC.n.act.ngem.3du_Neg.bw",
        "82420": "SC.n.act.gem.nom.subj_Neg.bw",
        "82421": "SC.n.act.gem.1sg_Neg.bw",
        "82422": "SC.n.act.gem.2sgm_Neg.bw",
        "82423": "SC.n.act.gem.2sgf_Neg.bw",
        "82424": "SC.n.act.gem.3sgm_Neg.bw",
        "82425": "SC.n.act.gem.3sgf_Neg.bw",
        "82426": "SC.n.act.gem.3sg_Neg.bw",
        "82427": "SC.n.act.gem.1pl_Neg.bw",
        "-82427": "SC.n.act.gem.1du_Neg.bw",
        "82428": "SC.n.act.gem.2pl_Neg.bw",
        "-82428": "SC.n.act.gem.2du_Neg.bw",
        "82429": "SC.n.act.gem.3pl_Neg.bw",
        "-82429": "SC.n.act.gem.3du_Neg.bw",
        "82430": "SC.n.pass.ngem.nom.subj_Neg.bw",
        "82431": "SC.n.pass.ngem.1sg_Neg.bw",
        "82432": "SC.n.pass.ngem.2sgm_Neg.bw",
        "82433": "SC.n.pass.ngem.2sgf_Neg.bw",
        "82434": "SC.n.pass.ngem.3sgm_Neg.bw",
        "82435": "SC.n.pass.ngem.3sgf_Neg.bw",
        "82436": "SC.n.pass.ngem.3sg_Neg.bw",
        "82437": "SC.n.pass.ngem.1pl_Neg.bw",
        "-82437": "SC.n.pass.ngem.1du_Neg.bw",
        "82438": "SC.n.pass.ngem.2pl_Neg.bw",
        "-82438": "SC.n.pass.ngem.2du_Neg.bw",
        "82439": "SC.n.pass.ngem.3pl_Neg.bw",
        "-82439": "SC.n.pass.ngem.3du_Neg.bw",
        "82440": "SC.n.tw.pass.ngem.nom.subj_Neg.bw",
        "82441": "SC.n.tw.pass.ngem.1sg_Neg.bw",
        "82442": "SC.n.tw.pass.ngem.2sgm_Neg.bw",
        "82443": "SC.n.tw.pass.ngem.2sgf_Neg.bw",
        "82444": "SC.n.tw.pass.ngem.3sgm_Neg.bw",
        "82445": "SC.n.tw.pass.ngem.3sgf_Neg.bw",
        "82446": "SC.n.tw.pass.ngem.3sg_Neg.bw",
        "82447": "SC.n.tw.pass.ngem.1pl_Neg.bw",
        "-82447": "SC.n.tw.pass.ngem.1du_Neg.bw",
        "82448": "SC.n.tw.pass.ngem.2pl_Neg.bw",
        "-82448": "SC.n.tw.pass.ngem.2du_Neg.bw",
        "82449": "SC.n.tw.pass.ngem.3pl_Neg.bw",
        "-82449": "SC.n.tw.pass.ngem.3du_Neg.bw",
        "82480": "SC.n.tw.pass.gem.nom.subj_Neg.bw",
        "82481": "SC.n.tw.pass.gem.1sg_Neg.bw",
        "82482": "SC.n.tw.pass.gem.2sgm_Neg.bw",
        "82483": "SC.n.tw.pass.gem.2sgf_Neg.bw",
        "82484": "SC.n.tw.pass.gem.3sgm_Neg.bw",
        "82485": "SC.n.tw.pass.gem.3sgf_Neg.bw",
        "82486": "SC.n.tw.pass.gem.3sg_Neg.bw",
        "82487": "SC.n.tw.pass.gem.1pl_Neg.bw",
        "-82487": "SC.n.tw.pass.gem.1du_Neg.bw",
        "82488": "SC.n.tw.pass.gem.2pl_Neg.bw",
        "-82488": "SC.n.tw.pass.gem.2du_Neg.bw",
        "82489": "SC.n.tw.pass.gem.3pl_Neg.bw",
        "-82489": "SC.n.tw.pass.gem.3du_Neg.bw",
        "82840": "SC.t.act.ngem.nom.subj_Neg.bw",
        "82841": "SC.t.act.ngem.1sg_Neg.bw",
        "82842": "SC.t.act.ngem.2sgm_Neg.bw",
        "82843": "SC.t.act.ngem.2sgf_Neg.bw",
        "82844": "SC.t.act.ngem.3sgm_Neg.bw",
        "82845": "SC.t.act.ngem.3sgf_Neg.bw",
        "82846": "SC.t.act.ngem.3sg_Neg.bw",
        "82847": "SC.t.act.ngem.1pl_Neg.bw",
        "-82847": "SC.t.act.ngem.1du_Neg.bw",
        "82848": "SC.t.act.ngem.2pl_Neg.bw",
        "-82848": "SC.t.act.ngem.2du_Neg.bw",
        "82849": "SC.t.act.ngem.3pl_Neg.bw",
        "-82849": "SC.t.act.ngem.3du_Neg.bw",
        "82850": "SC.t.act.gem.nom.subj_Neg.bw",
        "82851": "SC.t.act.gem.1sg_Neg.bw",
        "82852": "SC.t.act.gem.2sgm_Neg.bw",
        "82853": "SC.t.act.gem.2sgf_Neg.bw",
        "82854": "SC.t.act.gem.3sgm_Neg.bw",
        "82855": "SC.t.act.gem.3sgf_Neg.bw",
        "82856": "SC.t.act.gem.3sg_Neg.bw",
        "82857": "SC.t.act.gem.1pl_Neg.bw",
        "-82857": "SC.t.act.gem.1du_Neg.bw",
        "82858": "SC.t.act.gem.2pl_Neg.bw",
        "-82858": "SC.t.act.gem.2du_Neg.bw",
        "82859": "SC.t.act.gem.3pl_Neg.bw",
        "-82859": "SC.t.act.gem.3du_Neg.bw",
        "82860": "SC.t.pass.ngem.nom.subj_Neg.bw",
        "82861": "SC.t.pass.ngem.1sg_Neg.bw",
        "82862": "SC.t.pass.ngem.2sgm_Neg.bw",
        "82863": "SC.t.pass.ngem.2sgf_Neg.bw",
        "82864": "SC.t.pass.ngem.3sgm_Neg.bw",
        "82865": "SC.t.pass.ngem.3sgf_Neg.bw",
        "82866": "SC.t.pass.ngem.3sg_Neg.bw",
        "82867": "SC.t.pass.ngem.1pl_Neg.bw",
        "-82867": "SC.t.pass.ngem.1du_Neg.bw",
        "82868": "SC.t.pass.ngem.2pl_Neg.bw",
        "-82868": "SC.t.pass.ngem.2du_Neg.bw",
        "82869": "SC.t.pass.ngem.3pl_Neg.bw",
        "-82869": "SC.t.pass.ngem.3du_Neg.bw",
        "82870": "SC.t.pass.gem.nom.subj_Neg.bw",
        "82871": "SC.t.pass.gem.1sg_Neg.bw",
        "82872": "SC.t.pass.gem.2sgm_Neg.bw",
        "82873": "SC.t.pass.gem.2sgf_Neg.bw",
        "82874": "SC.t.pass.gem.3sgm_Neg.bw",
        "82875": "SC.t.pass.gem.3sgf_Neg.bw",
        "82876": "SC.t.pass.gem.3sg_Neg.bw",
        "82877": "SC.t.pass.gem.1pl_Neg.bw",
        "-82877": "SC.t.pass.gem.1du_Neg.bw",
        "82878": "SC.t.pass.gem.2pl_Neg.bw",
        "-82878": "SC.t.pass.gem.2du_Neg.bw",
        "82879": "SC.t.pass.gem.3pl_Neg.bw",
        "-82879": "SC.t.pass.gem.3du_Neg.bw",
        "82900": "SC.act.ngem.impers_Neg.bw",
        "82910": "SC.pass.ngem.impers_Neg.bw",
        "83001": "SC.unspec.1sg_Neg.bw dj.t",
        "83020": "SC.act.ngem.nom.subj_Neg.bw dj.t",
        "83021": "SC.act.ngem.1sg_Neg.bw dj.t",
        "83022": "SC.act.ngem.2sgm_Neg.bw dj.t",
        "83023": "SC.act.ngem.2sgf_Neg.bw dj.t",
        "83024": "SC.act.ngem.3sgm_Neg.bw dj.t",
        "83025": "SC.act.ngem.3sgf_Neg.bw dj.t",
        "83026": "SC.act.ngem.3sg_Neg.bw dj.t",
        "83027": "SC.act.ngem.1pl_Neg.bw dj.t",
        "-83027": "SC.act.ngem.1du_Neg.bw dj.t",
        "83028": "SC.act.ngem.2pl_Neg.bw dj.t",
        "-83028": "SC.act.ngem.2du_Neg.bw dj.t",
        "83029": "SC.act.ngem.3pl_Neg.bw dj.t",
        "-83029": "SC.act.ngem.3du_Neg.bw dj.t",
        "83040": "SC.pass.ngem.nom.subj_Neg.bw dj.t",
        "83041": "SC.pass.ngem.1sg_Neg.bw dj.t",
        "83042": "SC.pass.ngem.2sgm_Neg.bw dj.t",
        "83043": "SC.pass.ngem.2sgf_Neg.bw dj.t",
        "83044": "SC.pass.ngem.3sgm_Neg.bw dj.t",
        "83045": "SC.pass.ngem.3sgf_Neg.bw dj.t",
        "83046": "SC.pass.ngem.3sg_Neg.bw dj.t",
        "83047": "SC.pass.ngem.1pl_Neg.bw dj.t",
        "-83047": "SC.pass.ngem.1du_Neg.bw dj.t",
        "83048": "SC.pass.ngem.2pl_Neg.bw dj.t",
        "-83048": "SC.pass.ngem.2du_Neg.bw dj.t",
        "83049": "SC.pass.ngem.3pl_Neg.bw dj.t",
        "-83049": "SC.pass.ngem.3du_Neg.bw dj.t",
        "83100": "SC.act.gem.nom.subj_Neg.bw dj.t",
        "83101": "SC.act.gem.1sg_Neg.bw dj.t",
        "83102": "SC.act.gem.2sgm_Neg.bw dj.t",
        "83103": "SC.act.gem.2sgf_Neg.bw dj.t",
        "83104": "SC.act.gem.3sgm_Neg.bw dj.t",
        "83105": "SC.act.gem.3sgf_Neg.bw dj.t",
        "83106": "SC.act.gem.3sg_Neg.bw dj.t",
        "83107": "SC.act.gem.1pl_Neg.bw dj.t",
        "-83107": "SC.act.gem.1du_Neg.bw dj.t",
        "83108": "SC.act.gem.2pl_Neg.bw dj.t",
        "-83108": "SC.act.gem.2du_Neg.bw dj.t",
        "83109": "SC.act.gem.3pl_Neg.bw dj.t",
        "-83109": "SC.act.gem.3du_Neg.bw dj.t",
        "83140": "SC.act.spec.nom.subj_Neg.bw dj.t",
        "83141": "SC.act.spec.1sg_Neg.bw dj.t",
        "83142": "SC.act.spec.2sgm_Neg.bw dj.t",
        "83143": "SC.act.spec.2sgf_Neg.bw dj.t",
        "83144": "SC.act.spec.3sgm_Neg.bw dj.t",
        "83145": "SC.act.spec.3sgf_Neg.bw dj.t",
        "83146": "SC.act.spec.3sg_Neg.bw dj.t",
        "83147": "SC.act.spec.1pl_Neg.bw dj.t",
        "-83147": "SC.act.spec.1du_Neg.bw dj.t",
        "83148": "SC.act.spec.2pl_Neg.bw dj.t",
        "-83148": "SC.act.spec.2du_Neg.bw dj.t",
        "83149": "SC.act.spec.3pl_Neg.bw dj.t",
        "-83149": "SC.act.spec.3du_Neg.bw dj.t",
        "83160": "SC.pass.spec.nom.subj_Neg.bw dj.t",
        "83161": "SC.pass.spec.1sg_Neg.bw dj.t",
        "83162": "SC.pass.spec.2sgm_Neg.bw dj.t",
        "83163": "SC.pass.spec.2sgf_Neg.bw dj.t",
        "83164": "SC.pass.spec.3sgm_Neg.bw dj.t",
        "83165": "SC.pass.spec.3sgf_Neg.bw dj.t",
        "83166": "SC.pass.spec.3sg_Neg.bw dj.t",
        "83167": "SC.pass.spec.1pl_Neg.bw dj.t",
        "-83167": "SC.pass.spec.1du_Neg.bw dj.t",
        "83168": "SC.pass.spec.2pl_Neg.bw dj.t",
        "-83168": "SC.pass.spec.2du_Neg.bw dj.t",
        "83169": "SC.pass.spec.3pl_Neg.bw dj.t",
        "-83169": "SC.pass.spec.3du_Neg.bw dj.t",
        "83170": "SC.tw.pass.spec.nom.subj_Neg.bw dj.t",
        "83171": "SC.tw.pass.spec.1sg_Neg.bw dj.t",
        "83172": "SC.tw.pass.spec.2sgm_Neg.bw dj.t",
        "83173": "SC.tw.pass.spec.2sgf_Neg.bw dj.t",
        "83174": "SC.tw.pass.spec.3sgm_Neg.bw dj.t",
        "83175": "SC.tw.pass.spec.3sgf_Neg.bw dj.t",
        "83176": "SC.tw.pass.spec.3sg_Neg.bw dj.t",
        "83177": "SC.tw.pass.spec.1pl_Neg.bw dj.t",
        "-83177": "SC.tw.pass.spec.1du_Neg.bw dj.t",
        "83178": "SC.tw.pass.spec.2pl_Neg.bw dj.t",
        "-83178": "SC.tw.pass.spec.2du_Neg.bw dj.t",
        "83179": "SC.tw.pass.spec.3pl_Neg.bw dj.t",
        "-83179": "SC.tw.pass.spec.3du_Neg.bw dj.t",
        "83180": "SC.w.act.ngem.nom.subj_Neg.bw dj.t",
        "83181": "SC.w.act.ngem.1sg_Neg.bw dj.t",
        "83182": "SC.w.act.ngem.2sgm_Neg.bw dj.t",
        "83183": "SC.w.act.ngem.2sgf_Neg.bw dj.t",
        "83184": "SC.w.act.ngem.3sgm_Neg.bw dj.t",
        "83185": "SC.w.act.ngem.3sgf_Neg.bw dj.t",
        "83186": "SC.w.act.ngem.3sg_Neg.bw dj.t",
        "83187": "SC.w.act.ngem.1pl_Neg.bw dj.t",
        "-83187": "SC.w.act.ngem.1du_Neg.bw dj.t",
        "83188": "SC.w.act.ngem.2pl_Neg.bw dj.t",
        "-83188": "SC.w.act.ngem.2du_Neg.bw dj.t",
        "83189": "SC.w.act.ngem.3pl_Neg.bw dj.t",
        "-83189": "SC.w.act.ngem.3du_Neg.bw dj.t",
        "83220": "SC.w.act.gem.nom.subj_Neg.bw dj.t",
        "83221": "SC.w.act.gem.1sg_Neg.bw dj.t",
        "83222": "SC.w.act.gem.2sgm_Neg.bw dj.t",
        "83223": "SC.w.act.gem.2sgf_Neg.bw dj.t",
        "83224": "SC.w.act.gem.3sgm_Neg.bw dj.t",
        "83225": "SC.w.act.gem.3sgf_Neg.bw dj.t",
        "83226": "SC.w.act.gem.3sg_Neg.bw dj.t",
        "83227": "SC.w.act.gem.1pl_Neg.bw dj.t",
        "-83227": "SC.w.act.gem.1du_Neg.bw dj.t",
        "83228": "SC.w.act.gem.2pl_Neg.bw dj.t",
        "-83228": "SC.w.act.gem.2du_Neg.bw dj.t",
        "83229": "SC.w.act.gem.3pl_Neg.bw dj.t",
        "-83229": "SC.w.act.gem.3du_Neg.bw dj.t",
        "83240": "SC.w.pass.ngem.nom.subj_Neg.bw dj.t",
        "83241": "SC.w.pass.ngem.1sg_Neg.bw dj.t",
        "83242": "SC.w.pass.ngem.2sgm_Neg.bw dj.t",
        "83243": "SC.w.pass.ngem.2sgf_Neg.bw dj.t",
        "83244": "SC.w.pass.ngem.3sgm_Neg.bw dj.t",
        "83245": "SC.w.pass.ngem.3sgf_Neg.bw dj.t",
        "83246": "SC.w.pass.ngem.3sg_Neg.bw dj.t",
        "83247": "SC.w.pass.ngem.1pl_Neg.bw dj.t",
        "-83247": "SC.w.pass.ngem.1du_Neg.bw dj.t",
        "83248": "SC.w.pass.ngem.2pl_Neg.bw dj.t",
        "-83248": "SC.w.pass.ngem.2du_Neg.bw dj.t",
        "83249": "SC.w.pass.ngem.3pl_Neg.bw dj.t",
        "-83249": "SC.w.pass.ngem.3du_Neg.bw dj.t",
        "83280": "SC.w.tw.pass.ngem.nom.subj_Neg.bw dj.t",
        "83281": "SC.w.tw.pass.ngem.1sg_Neg.bw dj.t",
        "83282": "SC.w.tw.pass.ngem.2sgm_Neg.bw dj.t",
        "83283": "SC.w.tw.pass.ngem.2sgf_Neg.bw dj.t",
        "83284": "SC.w.tw.pass.ngem.3sgm_Neg.bw dj.t",
        "83285": "SC.w.tw.pass.ngem.3sgf_Neg.bw dj.t",
        "83286": "SC.w.tw.pass.ngem.3sg_Neg.bw dj.t",
        "83287": "SC.w.tw.pass.ngem.1pl_Neg.bw dj.t",
        "-83287": "SC.w.tw.pass.ngem.1du_Neg.bw dj.t",
        "83288": "SC.w.tw.pass.ngem.2pl_Neg.bw dj.t",
        "-83288": "SC.w.tw.pass.ngem.2du_Neg.bw dj.t",
        "83289": "SC.w.tw.pass.ngem.3pl_Neg.bw dj.t",
        "-83289": "SC.w.tw.pass.ngem.3du_Neg.bw dj.t",
        "83320": "SC.tw.pass.ngem.nom.subj_Neg.bw",
        "83321": "SC.tw.pass.ngem.1sg_Neg.bw dj.t",
        "83322": "SC.tw.pass.ngem.2sgm_Neg.bw dj.t",
        "83323": "SC.tw.pass.ngem.2sgf_Neg.bw dj.t",
        "83324": "SC.tw.pass.ngem.3sgm_Neg.bw dj.t",
        "83325": "SC.tw.pass.ngem.3sgf_Neg.bw dj.t",
        "83326": "SC.tw.pass.ngem.3sg_Neg.bw dj.t",
        "83327": "SC.tw.pass.ngem.1pl_Neg.bw dj.t",
        "-83327": "SC.tw.pass.ngem.1du_Neg.bw dj.t",
        "83328": "SC.tw.pass.ngem.2pl_Neg.bw dj.t",
        "-83328": "SC.tw.pass.ngem.2du_Neg.bw dj.t",
        "83329": "SC.tw.pass.ngem.3pl_Neg.bw dj.t",
        "-83329": "SC.tw.pass.ngem.3du_Neg.bw dj.t",
        "-83339": "SC.tw.pass.gem.3du_Neg.bw dj.t",
        "83360": "SC.tw.pass.gem.nom.subj_Neg.bw",
        "83361": "SC.tw.pass.gem.1sg_Neg.bw dj.t",
        "83362": "SC.tw.pass.gem.2sgm_Neg.bw dj.t",
        "83363": "SC.tw.pass.gem.2sgf_Neg.bw dj.t",
        "83364": "SC.tw.pass.gem.3sgm_Neg.bw dj.t",
        "83365": "SC.tw.pass.gem.3sgf_Neg.bw dj.t",
        "83366": "SC.tw.pass.gem.3sg_Neg.bw dj.t",
        "83367": "SC.tw.pass.gem.1pl_Neg.bw dj.t",
        "-83367": "SC.tw.pass.gem.1du_Neg.bw dj.t",
        "83368": "SC.tw.pass.gem.2pl_Neg.bw dj.t",
        "-83368": "SC.tw.pass.gem.2du_Neg.bw dj.t",
        "83369": "SC.tw.pass.gem.3pl_Neg.bw dj.t",
        "83380": "SC.n.act.ngem.nom.subj_Neg.bw dj.t",
        "83381": "SC.n.act.ngem.1sg_Neg.bw dj.t",
        "83382": "SC.n.act.ngem.2sgm_Neg.bw dj.t",
        "83383": "SC.n.act.ngem.2sgf_Neg.bw dj.t",
        "83384": "SC.n.act.ngem.3sgm_Neg.bw dj.t",
        "83385": "SC.n.act.ngem.3sgf_Neg.bw dj.t",
        "83386": "SC.n.act.ngem.3sg_Neg.bw dj.t",
        "83387": "SC.n.act.ngem.1pl_Neg.bw dj.t",
        "-83387": "SC.n.act.ngem.1du_Neg.bw dj.t",
        "83388": "SC.n.act.ngem.2pl_Neg.bw dj.t",
        "-83388": "SC.n.act.ngem.2du_Neg.bw dj.t",
        "83389": "SC.n.act.ngem.3pl_Neg.bw dj.t",
        "-83389": "SC.n.act.ngem.3du_Neg.bw dj.t",
        "83420": "SC.n.act.gem.nom.subj_Neg.bw dj.t",
        "83421": "SC.n.act.gem.1sg_Neg.bw dj.t",
        "83422": "SC.n.act.gem.2sgm_Neg.bw dj.t",
        "83423": "SC.n.act.gem.2sgf_Neg.bw dj.t",
        "83424": "SC.n.act.gem.3sgm_Neg.bw dj.t",
        "83425": "SC.n.act.gem.3sgf_Neg.bw dj.t",
        "83426": "SC.n.act.gem.3sg_Neg.bw dj.t",
        "83427": "SC.n.act.gem.1pl_Neg.bw dj.t",
        "-83427": "SC.n.act.gem.1du_Neg.bw dj.t",
        "83428": "SC.n.act.gem.2pl_Neg.bw dj.t",
        "-83428": "SC.n.act.gem.2du_Neg.bw dj.t",
        "83429": "SC.n.act.gem.3pl_Neg.bw dj.t",
        "-83429": "SC.n.act.gem.3du_Neg.bw dj.t",
        "83430": "SC.n.pass.ngem.nom.subj_Neg.bw dj.t",
        "83431": "SC.n.pass.ngem.1sg_Neg.bw dj.t",
        "83432": "SC.n.pass.ngem.2sgm_Neg.bw dj.t",
        "83433": "SC.n.pass.ngem.2sgf_Neg.bw dj.t",
        "83434": "SC.n.pass.ngem.3sgm_Neg.bw dj.t",
        "83435": "SC.n.pass.ngem.3sgf_Neg.bw dj.t",
        "83436": "SC.n.pass.ngem.3sg_Neg.bw dj.t",
        "83437": "SC.n.pass.ngem.1pl_Neg.bw dj.t",
        "-83437": "SC.n.pass.ngem.1du_Neg.bw dj.t",
        "83438": "SC.n.pass.ngem.2pl_Neg.bw dj.t",
        "-83438": "SC.n.pass.ngem.2du_Neg.bw dj.t",
        "83439": "SC.n.pass.ngem.3pl_Neg.bw dj.t",
        "-83439": "SC.n.pass.ngem.3du_Neg.bw dj.t",
        "83440": "SC.n.tw.pass.ngem.nom.subj_Neg.bw dj.t",
        "83441": "SC.n.tw.pass.ngem.1sg_Neg.bw dj.t",
        "83442": "SC.n.tw.pass.ngem.2sgm_Neg.bw dj.t",
        "83443": "SC.n.tw.pass.ngem.2sgf_Neg.bw dj.t",
        "83444": "SC.n.tw.pass.ngem.3sgm_Neg.bw dj.t",
        "83445": "SC.n.tw.pass.ngem.3sgf_Neg.bw dj.t",
        "83446": "SC.n.tw.pass.ngem.3sg_Neg.bw dj.t",
        "83447": "SC.n.tw.pass.ngem.1pl_Neg.bw dj.t",
        "-83447": "SC.n.tw.pass.ngem.1du_Neg.bw dj.t",
        "83448": "SC.n.tw.pass.ngem.2pl_Neg.bw dj.t",
        "-83448": "SC.n.tw.pass.ngem.2du_Neg.bw dj.t",
        "83449": "SC.n.tw.pass.ngem.3pl_Neg.bw dj.t",
        "-83449": "SC.n.tw.pass.ngem.3du_Neg.bw dj.t",
        "83480": "SC.n.tw.pass.gem.nom.subj_Neg.bw dj.t",
        "83481": "SC.n.tw.pass.gem.1sg_Neg.bw dj.t",
        "83482": "SC.n.tw.pass.gem.2sgm_Neg.bw dj.t",
        "83483": "SC.n.tw.pass.gem.2sgf_Neg.bw dj.t",
        "83484": "SC.n.tw.pass.gem.3sgm_Neg.bw dj.t",
        "83485": "SC.n.tw.pass.gem.3sgf_Neg.bw dj.t",
        "83486": "SC.n.tw.pass.gem.3sg_Neg.bw dj.t",
        "83487": "SC.n.tw.pass.gem.1pl_Neg.bw dj.t",
        "-83487": "SC.n.tw.pass.gem.1du_Neg.bw dj.t",
        "83488": "SC.n.tw.pass.gem.2pl_Neg.bw dj.t",
        "-83488": "SC.n.tw.pass.gem.2du_Neg.bw dj.t",
        "83489": "SC.n.tw.pass.gem.3pl_Neg.bw dj.t",
        "-83489": "SC.n.tw.pass.gem.3du_Neg.bw dj.t",
        "83840": "SC.t.act.ngem.nom.subj_Neg.bw dj.t",
        "83841": "SC.t.act.ngem.1sg_Neg.bw dj.t",
        "83842": "SC.t.act.ngem.2sgm_Neg.bw dj.t",
        "83843": "SC.t.act.ngem.2sgf_Neg.bw dj.t",
        "83844": "SC.t.act.ngem.3sgm_Neg.bw dj.t",
        "83845": "SC.t.act.ngem.3sgf_Neg.bw dj.t",
        "83846": "SC.t.act.ngem.3sg_Neg.bw dj.t",
        "83847": "SC.t.act.ngem.1pl_Neg.bw dj.t",
        "-83847": "SC.t.act.ngem.1du_Neg.bw dj.t",
        "83848": "SC.t.act.ngem.2pl_Neg.bw dj.t",
        "-83848": "SC.t.act.ngem.2du_Neg.bw dj.t",
        "83849": "SC.t.act.ngem.3pl_Neg.bw dj.t",
        "-83849": "SC.t.act.ngem.3du_Neg.bw dj.t",
        "83850": "SC.t.act.gem.nom.subj_Neg.bw dj.t",
        "83851": "SC.t.act.gem.1sg_Neg.bw dj.t",
        "83852": "SC.t.act.gem.2sgm_Neg.bw dj.t",
        "83853": "SC.t.act.gem.2sgf_Neg.bw dj.t",
        "83854": "SC.t.act.gem.3sgm_Neg.bw dj.t",
        "83855": "SC.t.act.gem.3sgf_Neg.bw dj.t",
        "83856": "SC.t.act.gem.3sg_Neg.bw dj.t",
        "83857": "SC.t.act.gem.1pl_Neg.bw dj.t",
        "-83857": "SC.t.act.gem.1du_Neg.bw dj.t",
        "83858": "SC.t.act.gem.2pl_Neg.bw dj.t",
        "-83858": "SC.t.act.gem.2du_Neg.bw dj.t",
        "83859": "SC.t.act.gem.3pl_Neg.bw dj.t",
        "-83859": "SC.t.act.gem.3du_Neg.bw dj.t",
        "83860": "SC.t.pass.ngem.nom.subj_Neg.bw dj.t",
        "83861": "SC.t.pass.ngem.1sg_Neg.bw dj.t",
        "83862": "SC.t.pass.ngem.2sgm_Neg.bw dj.t",
        "83863": "SC.t.pass.ngem.2sgf_Neg.bw dj.t",
        "83864": "SC.t.pass.ngem.3sgm_Neg.bw dj.t",
        "83865": "SC.t.pass.ngem.3sgf_Neg.bw dj.t",
        "83866": "SC.t.pass.ngem.3sg_Neg.bw dj.t",
        "83867": "SC.t.pass.ngem.1pl_Neg.bw dj.t",
        "-83867": "SC.t.pass.ngem.1du_Neg.bw dj.t",
        "83868": "SC.t.pass.ngem.2pl_Neg.bw dj.t",
        "-83868": "SC.t.pass.ngem.2du_Neg.bw dj.t",
        "83869": "SC.t.pass.ngem.3pl_Neg.bw dj.t",
        "-83869": "SC.t.pass.ngem.3du_Neg.bw dj.t",
        "83870": "SC.t.pass.gem.nom.subj_Neg.bw dj.t",
        "83871": "SC.t.pass.gem.1sg_Neg.bw dj.t",
        "83872": "SC.t.pass.gem.2sgm_Neg.bw dj.t",
        "83873": "SC.t.pass.gem.2sgf_Neg.bw dj.t",
        "83874": "SC.t.pass.gem.3sgm_Neg.bw dj.t",
        "83875": "SC.t.pass.gem.3sgf_Neg.bw dj.t",
        "83876": "SC.t.pass.gem.3sg_Neg.bw dj.t",
        "83877": "SC.t.pass.gem.1pl_Neg.bw dj.t",
        "-83877": "SC.t.pass.gem.1du_Neg.bw dj.t",
        "83878": "SC.t.pass.gem.2pl_Neg.bw dj.t",
        "-83878": "SC.t.pass.gem.2du_Neg.bw dj.t",
        "83879": "SC.t.pass.gem.3pl_Neg.bw dj.t",
        "-83879": "SC.t.pass.gem.3du_Neg.bw dj.t",
        "84000": "SC.unspec.nom.subj_Neg.bn",
        "84001": "SC.unspec.subj.1sg_Neg.bn",
        "84002": "SC.unspec.2sgm_Neg.bn",
        "84006": "SC.unspec.3sg_Neg.bn",
        "84020": "SC.act.ngem.nom.subj_Neg.bn",
        "184020": "",
        "84021": "SC.act.ngem.1sg_Neg.bn",
        "184021": "",
        "84022": "SC.act.ngem.2sgm_Neg.bn",
        "184022": "",
        "84023": "SC.act.ngem.2sgf_Neg.bn",
        "184023": "",
        "84024": "SC.act.ngem.3sgm_Neg.bn",
        "184024": "",
        "84025": "SC.act.ngem.3sgf_Neg.bn",
        "184025": "",
        "84026": "SC.act.ngem.3sg_Neg.bn",
        "184026": "",
        "84027": "SC.act.ngem.1pl_Neg.bn",
        "-84027": "SC.act.ngem.1du_Neg.bn",
        "184027": "",
        "-184027": "",
        "84028": "SC.act.ngem.2pl_Neg.bn",
        "-84028": "SC.act.ngem.2du_Neg.bn",
        "184028": "",
        "-184028": "",
        "84029": "SC.act.ngem.3pl_Neg.bn",
        "-84029": "SC.act.ngem.3du_Neg.bn",
        "184029": "",
        "-184029": "",
        "84040": "SC.pass.ngem.nom.subj_Neg.bn",
        "84041": "SC.pass.ngem.1sg_Neg.bn",
        "84042": "SC.pass.ngem.2sgm_Neg.bn",
        "84043": "SC.pass.ngem.2sgf_Neg.bn",
        "84044": "SC.pass.ngem.3sgm_Neg.bn",
        "84045": "SC.pass.ngem.3sgf_Neg.bn",
        "84046": "SC.pass.ngem.3sg_Neg.bn",
        "84047": "SC.pass.ngem.1pl_Neg.bn",
        "-84047": "SC.pass.ngem.1du_Neg.bn",
        "84048": "SC.pass.ngem.2pl_Neg.bn",
        "-84048": "SC.pass.ngem.2du_Neg.bn",
        "84049": "SC.pass.ngem.3pl_Neg.bn",
        "-84049": "SC.pass.ngem.3du_Neg.bn",
        "84100": "SC.act.gem.nom.subj_Neg.bn",
        "84101": "SC.act.gem.1sg_Neg.bn",
        "84102": "SC.act.gem.2sgm_Neg.bn",
        "84103": "SC.act.gem.2sgf_Neg.bn",
        "84104": "SC.act.gem.3sgm_Neg.bn",
        "84105": "SC.act.gem.3sgf_Neg.bn",
        "84106": "SC.act.gem.3sg_Neg.bn",
        "84107": "SC.act.gem.1pl_Neg.bn",
        "-84107": "SC.act.gem.1du_Neg.bn",
        "84108": "SC.act.gem.2pl_Neg.bn",
        "-84108": "SC.act.gem.2du_Neg.bn",
        "84109": "SC.act.gem.3pl_Neg.bn",
        "-84109": "SC.act.gem.3du_Neg.bn",
        "84120": "SC.pass.gem.nom.subj_Neg.bn",
        "84121": "SC.pass.gem.1sg_Neg.bn",
        "84122": "SC.pass.gem.2sgm_Neg.bn",
        "84123": "SC.pass.gem.2sgf_Neg.bn",
        "84124": "SC.pass.gem.3sgm_Neg.bn",
        "84125": "SC.pass.gem.3sgf_Neg.bn",
        "84126": "SC.pass.gem.3sg_Neg.bn",
        "84127": "SC.pass.gem.1pl_Neg.bn",
        "-84127": "SC.pass.gem.1du_Neg.bn",
        "84128": "SC.pass.gem.2pl_Neg.bn",
        "-84128": "SC.pass.gem.2du_Neg.bn",
        "84129": "SC.pass.gem.3pl_Neg.bn",
        "-84129": "SC.pass.gem.3du_Neg.bn",
        "84140": "SC.act.spec.nom.subj_Neg.bn",
        "84141": "SC.act.spec.1sg_Neg.bn",
        "84142": "SC.act.spec.2sgm_Neg.bn",
        "84143": "SC.act.spec.2sgf_Neg.bn",
        "84144": "SC.act.spec.3sgm_Neg.bn",
        "84145": "SC.act.spec.3sgf_Neg.bn",
        "84146": "SC.act.spec.3sg_Neg.bn",
        "84147": "SC.act.spec.1pl_Neg.bn",
        "-84147": "SC.act.spec.1du_Neg.bn",
        "84148": "SC.act.spec.2pl_Neg.bn",
        "-84148": "SC.act.spec.2du_Neg.bn",
        "84149": "SC.act.spec.3pl_Neg.bn",
        "-84149": "SC.act.spec.3du_Neg.bn",
        "84160": "SC.pass.spec.nom.subj_Neg.bn",
        "84161": "SC.pass.spec.1sg_Neg.bn",
        "84162": "SC.pass.spec.2sgm_Neg.bn",
        "84163": "SC.pass.spec.2sgf_Neg.bn",
        "84164": "SC.pass.spec.3sgm_Neg.bn",
        "84165": "SC.pass.spec.3sgf_Neg.bn",
        "84166": "SC.pass.spec.3sg_Neg.bn",
        "84167": "SC.pass.spec.1pl_Neg.bn",
        "-84167": "SC.pass.spec.1du_Neg.bn",
        "84168": "SC.pass.spec.2pl_Neg.bn",
        "-84168": "SC.pass.spec.2du_Neg.bn",
        "84169": "SC.pass.spec.3pl_Neg.bn",
        "-84169": "SC.pass.spec.3du_Neg.bn",
        "84170": "SC.tw.pass.spec.nom.subj_Neg.bn",
        "84171": "SC.tw.pass.spec.1sg_Neg.bn",
        "84172": "SC.tw.pass.spec.2sgm_Neg.bn",
        "84173": "SC.tw.pass.spec.2sgf_Neg.bn",
        "84174": "SC.tw.pass.spec.3sgm_Neg.bn",
        "84175": "SC.tw.pass.spec.3sgf_Neg.bn",
        "84176": "SC.tw.pass.spec.3sg_Neg.bn",
        "84177": "SC.tw.pass.spec.1pl_Neg.bn",
        "-84177": "SC.tw.pass.spec.1du_Neg.bn",
        "84178": "SC.tw.pass.spec.2pl_Neg.bn",
        "-84178": "SC.tw.pass.spec.2du_Neg.bn",
        "84179": "SC.tw.pass.spec.3pl_Neg.bn",
        "-84179": "SC.tw.pass.spec.3du_Neg.bn",
        "84180": "SC.w.act.ngem.nom.subj_Neg.bn",
        "84181": "SC.w.act.ngem.1sg_Neg.bn",
        "84182": "SC.w.act.ngem.2sgm_Neg.bn",
        "84183": "SC.w.act.ngem.2sgf_Neg.bn",
        "84184": "SC.w.act.ngem.3sgm_Neg.bn",
        "84185": "SC.w.act.ngem.3sgf_Neg.bn",
        "84186": "SC.w.act.ngem.3sg_Neg.bn",
        "84187": "SC.w.act.ngem.1pl_Neg.bn",
        "-84187": "SC.w.act.ngem.1du_Neg.bn",
        "84188": "SC.w.act.ngem.2pl_Neg.bn",
        "-84188": "SC.w.act.ngem.2du_Neg.bn",
        "84189": "SC.w.act.ngem.3pl_Neg.bn",
        "-84189": "SC.w.act.ngem.3du_Neg.bn",
        "84220": "SC.w.act.gem.nom.subj_Neg.bn",
        "84221": "SC.w.act.gem.1sg_Neg.bn",
        "84222": "SC.w.act.gem.2sgm_Neg.bn",
        "84223": "SC.w.act.gem.2sgf_Neg.bn",
        "84224": "SC.w.act.gem.3sgm_Neg.bn",
        "84225": "SC.w.act.gem.3sgf_Neg.bn",
        "84226": "SC.w.act.gem.3sg_Neg.bn",
        "84227": "SC.w.act.gem.1pl_Neg.bn",
        "-84227": "SC.w.act.gem.1du_Neg.bn",
        "84228": "SC.w.act.gem.2pl_Neg.bn",
        "-84228": "SC.w.act.gem.2du_Neg.bn",
        "84229": "SC.w.act.gem.3pl_Neg.bn",
        "-84229": "SC.w.act.gem.3du_Neg.bn",
        "84240": "SC.w.pass.ngem.nom.subj_Neg.bn",
        "84241": "SC.w.pass.ngem.1sg_Neg.bn",
        "84242": "SC.w.pass.ngem.2sgm_Neg.bn",
        "84243": "SC.w.pass.ngem.2sgf_Neg.bn",
        "84244": "SC.w.pass.ngem.3sgm_Neg.bn",
        "84245": "SC.w.pass.ngem.3sgf_Neg.bn",
        "84246": "SC.w.pass.ngem.3sg_Neg.bn",
        "84247": "SC.w.pass.ngem.1pl_Neg.bn",
        "-84247": "SC.w.pass.ngem.1du_Neg.bn",
        "84248": "SC.w.pass.ngem.2pl_Neg.bn",
        "-84248": "SC.w.pass.ngem.2du_Neg.bn",
        "84249": "SC.w.pass.ngem.3pl_Neg.bn",
        "-84249": "SC.w.pass.ngem.3du_Neg.bn",
        "84280": "SC.w.tw.pass.ngem.nom.subj_Neg.bn",
        "84281": "SC.w.tw.pass.ngem.1sg_Neg.bn",
        "84282": "SC.w.tw.pass.ngem.2sgm_Neg.bn",
        "84283": "SC.w.tw.pass.ngem.2sgf_Neg.bn",
        "84284": "SC.w.tw.pass.ngem.3sgm_Neg.bn",
        "84285": "SC.w.tw.pass.ngem.3sgf_Neg.bn",
        "84286": "SC.w.tw.pass.ngem.3sg_Neg.bn",
        "84287": "SC.w.tw.pass.ngem.1pl_Neg.bn",
        "-84287": "SC.w.tw.pass.ngem.1du_Neg.bn",
        "84288": "SC.w.tw.pass.ngem.2pl_Neg.bn",
        "-84288": "SC.w.tw.pass.ngem.2du_Neg.bn",
        "84289": "SC.w.tw.pass.ngem.3pl_Neg.bn",
        "-84289": "SC.w.tw.pass.ngem.3du_Neg.bn",
        "84320": "SC.tw.pass.ngem.nom.subj_Neg.bn",
        "84321": "SC.tw.pass.ngem.1sg_Neg.bn",
        "84322": "SC.tw.pass.ngem.2sgm_Neg.bn",
        "84323": "SC.tw.pass.ngem.2sgf_Neg.bn",
        "84324": "SC.tw.pass.ngem.3sgm_Neg.bn",
        "84325": "SC.tw.pass.ngem.3sgf_Neg.bn",
        "84326": "SC.tw.pass.ngem.3sg_Neg.bn",
        "84327": "SC.tw.pass.ngem.1pl_Neg.bn",
        "-84327": "SC.tw.pass.ngem.1du_Neg.bn",
        "84328": "SC.tw.pass.ngem.2pl_Neg.bn",
        "-84328": "SC.tw.pass.ngem.2du_Neg.bn",
        "84329": "SC.tw.pass.ngem.3pl_Neg.bn",
        "-84329": "SC.tw.pass.ngem.3du_Neg.bn",
        "84360": "SC.tw.pass.gem.nom.subj_Neg.bn",
        "84361": "SC.tw.pass.gem.1sg_Neg.bn",
        "84362": "SC.tw.pass.gem.2sgm_Neg.bn",
        "84363": "SC.tw.pass.gem.2sgf_Neg.bn",
        "84364": "SC.tw.pass.gem.3sgm_Neg.bn",
        "84365": "SC.tw.pass.gem.3sgf_Neg.bn",
        "84366": "SC.tw.pass.gem.3sg_Neg.bn",
        "84367": "SC.tw.pass.gem.1pl_Neg.bn",
        "-84367": "SC.tw.pass.gem.1du_Neg.bn",
        "84368": "SC.tw.pass.gem.2pl_Neg.bn",
        "-84368": "SC.tw.pass.gem.2du_Neg.bn",
        "84369": "SC.tw.pass.gem.3pl_Neg.bn",
        "-84369": "SC.tw.pass.gem.3du_Neg.bn",
        "84380": "SC.n.act.ngem.nom.subj_Neg.bn",
        "84381": "SC.n.act.ngem.1sg_Neg.bn",
        "84382": "SC.n.act.ngem.2sgm_Neg.bn",
        "84383": "SC.n.act.ngem.2sgf_Neg.bn",
        "84384": "SC.n.act.ngem.3sgm_Neg.bn",
        "84385": "SC.n.act.ngem.3sgf_Neg.bn",
        "84386": "SC.n.act.ngem.3sg_Neg.bn",
        "84387": "SC.n.act.ngem.1pl_Neg.bn",
        "-84387": "SC.n.act.ngem.1du_Neg.bn",
        "84388": "SC.n.act.ngem.2pl_Neg.bn",
        "-84388": "SC.n.act.ngem.2du_Neg.bn",
        "84389": "SC.n.act.ngem.3pl_Neg.bn",
        "-84389": "SC.n.act.ngem.3du_Neg.bn",
        "84420": "SC.n.act.gem.nom.subj_Neg.bn",
        "84421": "SC.n.act.gem.1sg_Neg.bn",
        "84422": "SC.n.act.gem.2sgm_Neg.bn",
        "84423": "SC.n.act.gem.2sgf_Neg.bn",
        "84424": "SC.n.act.gem.3sgm_Neg.bn",
        "84425": "SC.n.act.gem.3sgf_Neg.bn",
        "84426": "SC.n.act.gem.3sg_Neg.bn",
        "84427": "SC.n.act.gem.1pl_Neg.bn",
        "-84427": "SC.n.act.gem.1du_Neg.bn",
        "84428": "SC.n.act.gem.2pl_Neg.bn",
        "-84428": "SC.n.act.gem.2du_Neg.bn",
        "84429": "SC.n.act.gem.3pl_Neg.bn",
        "-84429": "SC.n.act.gem.3du_Neg.bn",
        "84430": "SC.n.pass.ngem.nom.subj_Neg.bn",
        "84431": "SC.n.pass.ngem.1sg_Neg.bn",
        "84432": "SC.n.pass.ngem.2sgm_Neg.bn",
        "84433": "SC.n.pass.ngem.2sgf_Neg.bn",
        "84434": "SC.n.pass.ngem.3sgm_Neg.bn",
        "84435": "SC.n.pass.ngem.3sgf_Neg.bn",
        "84436": "SC.n.pass.ngem.3sg_Neg.bn",
        "84437": "SC.n.pass.ngem.1pl_Neg.bn",
        "-84437": "SC.n.pass.ngem.1du_Neg.bn",
        "84438": "SC.n.pass.ngem.2pl_Neg.bn",
        "-84438": "SC.n.pass.ngem.2du_Neg.bn",
        "84439": "SC.n.pass.ngem.3pl_Neg.bn",
        "-84439": "SC.n.pass.ngem.3du_Neg.bn",
        "84440": "SC.n.tw.pass.ngem.nom.subj_Neg.bn",
        "84441": "SC.n.tw.pass.ngem.1sg_Neg.bn",
        "84442": "SC.n.tw.pass.ngem.2sgm_Neg.bn",
        "84443": "SC.n.tw.pass.ngem.2sgf_Neg.bn",
        "84444": "SC.n.tw.pass.ngem.3sgm_Neg.bn",
        "84445": "SC.n.tw.pass.ngem.3sgf_Neg.bn",
        "84446": "SC.n.tw.pass.ngem.3sg_Neg.bn",
        "84447": "SC.n.tw.pass.ngem.1pl_Neg.bn",
        "-84447": "SC.n.tw.pass.ngem.1du_Neg.bn",
        "84448": "SC.n.tw.pass.ngem.2pl_Neg.bn",
        "-84448": "SC.n.tw.pass.ngem.2du_Neg.bn",
        "84449": "SC.n.tw.pass.ngem.3pl_Neg.bn",
        "-84449": "SC.n.tw.pass.ngem.3du_Neg.bn",
        "84480": "SC.n.tw.pass.gem.nom.subj_Neg.bn",
        "84481": "SC.n.tw.pass.gem.1sg_Neg.bn",
        "84482": "SC.n.tw.pass.gem.2sgm_Neg.bn",
        "84483": "SC.n.tw.pass.gem.2sgf_Neg.bn",
        "84484": "SC.n.tw.pass.gem.3sgm_Neg.bn",
        "84485": "SC.n.tw.pass.gem.3sgf_Neg.bn",
        "84486": "SC.n.tw.pass.gem.3sg_Neg.bn",
        "84487": "SC.n.tw.pass.gem.1pl_Neg.bn",
        "-84487": "SC.n.tw.pass.gem.1du_Neg.bn",
        "84488": "SC.n.tw.pass.gem.2pl_Neg.bn",
        "-84488": "SC.n.tw.pass.gem.2du_Neg.bn",
        "84489": "SC.n.tw.pass.gem.3pl_Neg.bn",
        "-84489": "SC.n.tw.pass.gem.3du_Neg.bn",
        "84840": "SC.t.act.ngem.nom.subj_Neg.bn",
        "84841": "SC.t.act.ngem.1sg_Neg.bn",
        "84842": "SC.t.act.ngem.2sgm_Neg.bn",
        "84843": "SC.t.act.ngem.2sgf_Neg.bn",
        "84844": "SC.t.act.ngem.3sgm_Neg.bn",
        "84845": "SC.t.act.ngem.3sgf_Neg.bn",
        "84846": "SC.t.act.ngem.3sg_Neg.bn",
        "84847": "SC.t.act.ngem.1pl_Neg.bn",
        "-84847": "SC.t.act.ngem.1du_Neg.bn",
        "84848": "SC.t.act.ngem.2pl_Neg.bn",
        "-84848": "SC.t.act.ngem.2du_Neg.bn",
        "84849": "SC.t.act.ngem.3pl_Neg.bn",
        "-84849": "SC.t.act.ngem.3du_Neg.bn",
        "84850": "SC.t.act.gem.nom.subj_Neg.bn",
        "84851": "SC.t.act.gem.1sg_Neg.bn",
        "84852": "SC.t.act.gem.2sgm_Neg.bn",
        "84853": "SC.t.act.gem.2sgf_Neg.bn",
        "84854": "SC.t.act.gem.3sgm_Neg.bn",
        "84855": "SC.t.act.gem.3sgf_Neg.bn",
        "84856": "SC.t.act.gem.3sg_Neg.bn",
        "84857": "SC.t.act.gem.1pl_Neg.bn",
        "-84857": "SC.t.act.gem.1du_Neg.bn",
        "84858": "SC.t.act.gem.2pl_Neg.bn",
        "-84858": "SC.t.act.gem.2du_Neg.bn",
        "84859": "SC.t.act.gem.3pl_Neg.bn",
        "-84859": "SC.t.act.gem.3du_Neg.bn",
        "84860": "SC.t.pass.ngem.nom.subj_Neg.bn",
        "84861": "SC.t.pass.ngem.1sg_Neg.bn",
        "84862": "SC.t.pass.ngem.2sgm_Neg.bn",
        "84863": "SC.t.pass.ngem.2sgf_Neg.bn",
        "84864": "SC.t.pass.ngem.3sgm_Neg.bn",
        "84865": "SC.t.pass.ngem.3sgf_Neg.bn",
        "84866": "SC.t.pass.ngem.3sg_Neg.bn",
        "84867": "SC.t.pass.ngem.1pl_Neg.bn",
        "-84867": "SC.t.pass.ngem.1du_Neg.bn",
        "84868": "SC.t.pass.ngem.2pl_Neg.bn",
        "-84868": "SC.t.pass.ngem.2du_Neg.bn",
        "84869": "SC.t.pass.ngem.3pl_Neg.bn",
        "-84869": "SC.t.pass.ngem.3du_Neg.bn",
        "84870": "SC.t.pass.gem.nom.subj_Neg.bn",
        "84871": "SC.t.pass.gem.1sg_Neg.bn",
        "84872": "SC.t.pass.gem.2sgm_Neg.bn",
        "84873": "SC.t.pass.gem.2sgf_Neg.bn",
        "84874": "SC.t.pass.gem.3sgm_Neg.bn",
        "84875": "SC.t.pass.gem.3sgf_Neg.bn",
        "84876": "SC.t.pass.gem.3sg_Neg.bn",
        "84877": "SC.t.pass.gem.1pl_Neg.bn",
        "-84877": "SC.t.pass.gem.1du_Neg.bn",
        "84878": "SC.t.pass.gem.2pl_Neg.bn",
        "-84878": "SC.t.pass.gem.2du_Neg.bn",
        "84879": "SC.t.pass.gem.3pl_Neg.bn",
        "-84879": "SC.t.pass.gem.3du_Neg.bn",
        "85020": "SC.act.ngem.nom.subj_Neg.m jri̯",
        "85021": "SC.act.ngem.1sg_Neg.m jri̯",
        "85022": "SC.act.ngem.2sgm_Neg.m jri̯",
        "85023": "SC.act.ngem.2sgf_Neg.m jri̯",
        "85024": "SC.act.ngem.3sgm_Neg.m jri̯",
        "85025": "SC.act.ngem.3sgf_Neg.m jri̯",
        "85026": "SC.act.ngem.3sg_Neg.m jri̯",
        "85027": "SC.act.ngem.1pl_Neg.m jri̯",
        "-85027": "SC.act.ngem.1du_Neg.m jri̯",
        "85028": "SC.act.ngem.2pl_Neg.m jri̯",
        "-85028": "SC.act.ngem.2du_Neg.m jri̯",
        "85029": "SC.act.ngem.3pl_Neg.m jri̯",
        "-85029": "SC.act.ngem.3du_Neg.m jri̯",
        "85040": "SC.pass.ngem.nom.subj_Neg.m jri̯",
        "85041": "SC.pass.ngem.1sg_Neg.m jri̯",
        "85042": "SC.pass.ngem.2sgm_Neg.m jri̯",
        "85043": "SC.pass.ngem.2sgf_Neg.m jri̯",
        "85044": "SC.pass.ngem.3sgm_Neg.m jri̯",
        "85045": "SC.pass.ngem.3sgf_Neg.m jri̯",
        "85046": "SC.pass.ngem.3sg_Neg.m jri̯",
        "85047": "SC.pass.ngem.1pl_Neg.m jri̯",
        "-85047": "SC.pass.ngem.1du_Neg.m jri̯",
        "85048": "SC.pass.ngem.2pl_Neg.m jri̯",
        "-85048": "SC.pass.ngem.2du_Neg.m jri̯",
        "85049": "SC.pass.ngem.3pl_Neg.m jri̯",
        "-85049": "SC.pass.ngem.3du_Neg.m jri̯",
        "85100": "SC.act.gem.nom.subj_Neg.m jri̯",
        "85101": "SC.act.gem.1sg_Neg.m jri̯",
        "85102": "SC.act.gem.2sgm_Neg.m jri̯",
        "85103": "SC.act.gem.2sgf_Neg.m jri̯",
        "85104": "SC.act.gem.3sgm_Neg.m jri̯",
        "85105": "SC.act.gem.3sgf_Neg.m jri̯",
        "85106": "SC.act.gem.3sg_Neg.m jri̯",
        "85107": "SC.act.gem.1pl_Neg.m jri̯",
        "-85107": "SC.act.gem.1du_Neg.m jri̯",
        "85108": "SC.act.gem.2pl_Neg.m jri̯",
        "-85108": "SC.act.gem.2du_Neg.m jri̯",
        "85109": "SC.act.gem.3pl_Neg.m jri̯",
        "-85109": "SC.act.gem.3du_Neg.m jri̯",
        "85120": "SC.pass.gem.nom.subj_Neg.m jri̯",
        "85121": "SC.pass.gem.1sg_Neg.m jri̯",
        "85122": "SC.pass.gem.2sgm_Neg.m jri̯",
        "85123": "SC.pass.gem.2sgf_Neg.m jri̯",
        "85124": "SC.pass.gem.3sgm_Neg.m jri̯",
        "85125": "SC.pass.gem.3sgf_Neg.m jri̯",
        "85126": "SC.pass.gem.3sg_Neg.m jri̯",
        "85127": "SC.pass.gem.1pl_Neg.m jri̯",
        "-85127": "SC.pass.gem.1du_Neg.m jri̯",
        "85128": "SC.pass.gem.2pl_Neg.m jri̯",
        "-85128": "SC.pass.gem.2du_Neg.m jri̯",
        "85129": "SC.pass.gem.3pl_Neg.m jri̯",
        "-85129": "SC.pass.gem.3du_Neg.m jri̯",
        "85140": "SC.act.spec.nom.subj_Neg.m jri̯",
        "85141": "SC.act.spec.1sg_Neg.m jri̯",
        "85142": "SC.act.spec.2sgm_Neg.m jri̯",
        "85143": "SC.act.spec.2sgf_Neg.m jri̯",
        "85144": "SC.act.spec.3sgm_Neg.m jri̯",
        "85145": "SC.act.spec.3sgf_Neg.m jri̯",
        "85146": "SC.act.spec.3sg_Neg.m jri̯",
        "85147": "SC.act.spec.1pl_Neg.m jri̯",
        "-85147": "SC.act.spec.1du_Neg.m jri̯",
        "85148": "SC.act.spec.2pl_Neg.m jri̯",
        "-85148": "SC.act.spec.2du_Neg.m jri̯",
        "85149": "SC.act.spec.3pl_Neg.m jri̯",
        "-85149": "SC.act.spec.3du_Neg.m jri̯",
        "85160": "SC.pass.spec.nom.subj_Neg.m jri̯",
        "85161": "SC.pass.spec.1sg_Neg.m jri̯",
        "85162": "SC.pass.spec.2sgm_Neg.m jri̯",
        "85163": "SC.pass.spec.2sgf_Neg.m jri̯",
        "85164": "SC.pass.spec.3sgm_Neg.m jri̯",
        "85165": "SC.pass.spec.3sgf_Neg.m jri̯",
        "85166": "SC.pass.spec.3sg_Neg.m jri̯",
        "85167": "SC.pass.spec.1pl_Neg.m jri̯",
        "-85167": "SC.pass.spec.1du_Neg.m jri̯",
        "85168": "SC.pass.spec.2pl_Neg.m jri̯",
        "-85168": "SC.pass.spec.2du_Neg.m jri̯",
        "85169": "SC.pass.spec.3pl_Neg.m jri̯",
        "-85169": "SC.pass.spec.3du_Neg.m jri̯",
        "85170": "SC.tw.pass.spec.nom.subj_Neg.m jri̯",
        "85171": "SC.tw.pass.spec.1sg_Neg.m jri̯",
        "85172": "SC.tw.pass.spec.2sgm_Neg.m jri̯",
        "85173": "SC.tw.pass.spec.2sgf_Neg.m jri̯",
        "85174": "SC.tw.pass.spec.3sgm_Neg.m jri̯",
        "85175": "SC.tw.pass.spec.3sgf_Neg.m jri̯",
        "85176": "SC.tw.pass.spec.3sg_Neg.m jri̯",
        "85177": "SC.tw.pass.spec.1pl_Neg.m jri̯",
        "-85177": "SC.tw.pass.spec.1du_Neg.m jri̯",
        "85178": "SC.tw.pass.spec.2pl_Neg.m jri̯",
        "-85178": "SC.tw.pass.spec.2du_Neg.m jri̯",
        "85179": "SC.tw.pass.spec.3pl_Neg.m jri̯",
        "-85179": "SC.tw.pass.spec.3du_Neg.m jri̯",
        "85180": "SC.w.act.ngem.nom.subj_Neg.m jri̯",
        "85181": "SC.w.act.ngem.1sg_Neg.m jri̯",
        "85182": "SC.w.act.ngem.2sgm_Neg.m jri̯",
        "85183": "SC.w.act.ngem.2sgf_Neg.m jri̯",
        "85184": "SC.w.act.ngem.3sgm_Neg.m jri̯",
        "85185": "SC.w.act.ngem.3sgf_Neg.m jri̯",
        "85186": "SC.w.act.ngem.3sg_Neg.m jri̯",
        "85187": "SC.w.act.ngem.1pl_Neg.m jri̯",
        "-85187": "SC.w.act.ngem.1du_Neg.m jri̯",
        "85188": "SC.w.act.ngem.2pl_Neg.m jri̯",
        "-85188": "SC.w.act.ngem.2du_Neg.m jri̯",
        "85189": "SC.w.act.ngem.3pl_Neg.m jri̯",
        "-85189": "SC.w.act.ngem.3du_Neg.m jri̯",
        "85220": "SC.w.act.gem.nom.subj_Neg.m jri̯",
        "85221": "SC.w.act.gem.1sg_Neg.m jri̯",
        "85222": "SC.w.act.gem.2sgm_Neg.m jri̯",
        "85223": "SC.w.act.gem.2sgf_Neg.m jri̯",
        "85224": "SC.w.act.gem.3sgm_Neg.m jri̯",
        "85225": "SC.w.act.gem.3sgf_Neg.m jri̯",
        "85226": "SC.w.act.gem.3sg_Neg.m jri̯",
        "85227": "SC.w.act.gem.1pl_Neg.m jri̯",
        "-85227": "SC.w.act.gem.1du_Neg.m jri̯",
        "85228": "SC.w.act.gem.2pl_Neg.m jri̯",
        "-85228": "SC.w.act.gem.2du_Neg.m jri̯",
        "85229": "SC.w.act.gem.3pl_Neg.m jri̯",
        "-85229": "SC.w.act.gem.3du_Neg.m jri̯",
        "85240": "SC.w.pass.ngem.nom.subj_Neg.m jri̯",
        "85241": "SC.w.pass.ngem.1sg_Neg.m jri̯",
        "85242": "SC.w.pass.ngem.2sgm_Neg.m jri̯",
        "85243": "SC.w.pass.ngem.2sgf_Neg.m jri̯",
        "85244": "SC.w.pass.ngem.3sgm_Neg.m jri̯",
        "85245": "SC.w.pass.ngem.3sgf_Neg.m jri̯",
        "85246": "SC.w.pass.ngem.3sg_Neg.m jri̯",
        "85247": "SC.w.pass.ngem.1pl_Neg.m jri̯",
        "-85247": "SC.w.pass.ngem.1du_Neg.m jri̯",
        "85248": "SC.w.pass.ngem.2pl_Neg.m jri̯",
        "-85248": "SC.w.pass.ngem.2du_Neg.m jri̯",
        "85249": "SC.w.pass.ngem.3pl_Neg.m jri̯",
        "-85249": "SC.w.pass.ngem.3du_Neg.m jri̯",
        "85280": "SC.w.tw.pass.ngem.nom.subj_Neg.m jri̯",
        "85281": "SC.w.tw.pass.ngem.1sg_Neg.m jri̯",
        "85282": "SC.w.tw.pass.ngem.2sgm_Neg.m jri̯",
        "85283": "SC.w.tw.pass.ngem.2sgf_Neg.m jri̯",
        "85284": "SC.w.tw.pass.ngem.3sgm_Neg.m jri̯",
        "85285": "SC.w.tw.pass.ngem.3sgf_Neg.m jri̯",
        "85286": "SC.w.tw.pass.ngem.3sg_Neg.m jri̯",
        "85287": "SC.w.tw.pass.ngem.1pl_Neg.m jri̯",
        "-85287": "SC.w.tw.pass.ngem.1du_Neg.m jri̯",
        "85288": "SC.w.tw.pass.ngem.2pl_Neg.m jri̯",
        "-85288": "SC.w.tw.pass.ngem.2du_Neg.m jri̯",
        "85289": "SC.w.tw.pass.ngem.3pl_Neg.m jri̯",
        "-85289": "SC.w.tw.pass.ngem.3du_Neg.m jri̯",
        "85320": "SC.tw.pass.ngem.nom.subj_Neg.m jri̯",
        "85321": "SC.tw.pass.ngem.1sg_Neg.m jri̯",
        "85322": "SC.tw.pass.ngem.2sgm_Neg.m jri̯",
        "85323": "SC.tw.pass.ngem.2sgf_Neg.m jri̯",
        "85324": "SC.tw.pass.ngem.3sgm_Neg.m jri̯",
        "85325": "SC.tw.pass.ngem.3sgf_Neg.m jri̯",
        "85326": "SC.tw.pass.ngem.3sg_Neg.m jri̯",
        "85327": "SC.tw.pass.ngem.1pl_Neg.m jri̯",
        "-85327": "SC.tw.pass.ngem.1du_Neg.m jri̯",
        "85328": "SC.tw.pass.ngem.2pl_Neg.m jri̯",
        "-85328": "SC.tw.pass.ngem.2du_Neg.m jri̯",
        "85329": "SC.tw.pass.ngem.3pl_Neg.m jri̯",
        "-85329": "SC.tw.pass.ngem.3du_Neg.m jri̯",
        "85360": "SC.tw.pass.gem.nom.subj_Neg.m jri̯",
        "85361": "SC.tw.pass.gem.1sg_Neg.m jri̯",
        "85362": "SC.tw.pass.gem.2sgm_Neg.m jri̯",
        "85363": "SC.tw.pass.gem.2sgf_Neg.m jri̯",
        "85364": "SC.tw.pass.gem.3sgm_Neg.m jri̯",
        "85365": "SC.tw.pass.gem.3sgf_Neg.m jri̯",
        "85366": "SC.tw.pass.gem.3sg_Neg.m jri̯",
        "85367": "SC.tw.pass.gem.1pl_Neg.m jri̯",
        "-85367": "SC.tw.pass.gem.1du_Neg.m jri̯",
        "85368": "SC.tw.pass.gem.2pl_Neg.m jri̯",
        "-85368": "SC.tw.pass.gem.2du_Neg.m jri̯",
        "85369": "SC.tw.pass.gem.3pl_Neg.m jri̯",
        "-85369": "SC.tw.pass.gem.3du_Neg.m jri̯",
        "85380": "SC.n.act.ngem.nom.subj_Neg.m jri̯",
        "85381": "SC.n.act.ngem.1sg_Neg.m jri̯",
        "85382": "SC.n.act.ngem.2sgm_Neg.m jri̯",
        "85383": "SC.n.act.ngem.2sgf_Neg.m jri̯",
        "85384": "SC.n.act.ngem.3sgm_Neg.m jri̯",
        "85385": "SC.n.act.ngem.3sgf_Neg.m jri̯",
        "85386": "SC.n.act.ngem.3sg_Neg.m jri̯",
        "85387": "SC.n.act.ngem.1pl_Neg.m jri̯",
        "-85387": "SC.n.act.ngem.1du_Neg.m jri̯",
        "85388": "SC.n.act.ngem.2pl_Neg.m jri̯",
        "-85388": "SC.n.act.ngem.2du_Neg.m jri̯",
        "85389": "SC.n.act.ngem.3pl_Neg.m jri̯",
        "-85389": "SC.n.act.ngem.3du_Neg.m jri̯",
        "85420": "SC.n.act.gem.nom.subj_Neg.m jri̯",
        "85421": "SC.n.act.gem.1sg_Neg.m jri̯",
        "85422": "SC.n.act.gem.2sgm_Neg.m jri̯",
        "85423": "SC.n.act.gem.2sgf_Neg.m jri̯",
        "85424": "SC.n.act.gem.3sgm_Neg.m jri̯",
        "85425": "SC.n.act.gem.3sgf_Neg.m jri̯",
        "85426": "SC.n.act.gem.3sg_Neg.m jri̯",
        "85427": "SC.n.act.gem.1pl_Neg.m jri̯",
        "-85427": "SC.n.act.gem.1du_Neg.m jri̯",
        "85428": "SC.n.act.gem.2pl_Neg.m jri̯",
        "-85428": "SC.n.act.gem.2du_Neg.m jri̯",
        "85429": "SC.n.act.gem.3pl_Neg.m jri̯",
        "-85429": "SC.n.act.gem.3du_Neg.m jri̯",
        "85430": "SC.n.pass.ngem.nom.subj_Neg.m jri̯",
        "85431": "SC.n.pass.ngem.1sg_Neg.m jri̯",
        "85432": "SC.n.pass.ngem.2sgm_Neg.m jri̯",
        "85433": "SC.n.pass.ngem.2sgf_Neg.m jri̯",
        "85434": "SC.n.pass.ngem.3sgm_Neg.m jri̯",
        "85435": "SC.n.pass.ngem.3sgf_Neg.m jri̯",
        "85436": "SC.n.pass.ngem.3sg_Neg.m jri̯",
        "85437": "SC.n.pass.ngem.1pl_Neg.m jri̯",
        "-85437": "SC.n.pass.ngem.1du_Neg.m jri̯",
        "85438": "SC.n.pass.ngem.2pl_Neg.m jri̯",
        "-85438": "SC.n.pass.ngem.2du_Neg.m jri̯",
        "85439": "SC.n.pass.ngem.3pl_Neg.m jri̯",
        "-85439": "SC.n.pass.ngem.3du_Neg.m jri̯",
        "85440": "SC.n.tw.pass.ngem.nom.subj_Neg.m jri̯",
        "85441": "SC.n.tw.pass.ngem.1sg_Neg.m jri̯",
        "85442": "SC.n.tw.pass.ngem.2sgm_Neg.m jri̯",
        "85443": "SC.n.tw.pass.ngem.2sgf_Neg.m jri̯",
        "85444": "SC.n.tw.pass.ngem.3sgm_Neg.m jri̯",
        "85445": "SC.n.tw.pass.ngem.3sgf_Neg.m jri̯",
        "85446": "SC.n.tw.pass.ngem.3sg_Neg.m jri̯",
        "85447": "SC.n.tw.pass.ngem.1pl_Neg.m jri̯",
        "-85447": "SC.n.tw.pass.ngem.1du_Neg.m jri̯",
        "85448": "SC.n.tw.pass.ngem.2pl_Neg.m jri̯",
        "-85448": "SC.n.tw.pass.ngem.2du_Neg.m jri̯",
        "85449": "SC.n.tw.pass.ngem.3pl_Neg.m jri̯",
        "-85449": "SC.n.tw.pass.ngem.3du_Neg.m jri̯",
        "85480": "SC.n.tw.pass.gem.nom.subj_Neg.m jri̯",
        "85481": "SC.n.tw.pass.gem.1sg_Neg.m jri̯",
        "85482": "SC.n.tw.pass.gem.2sgm_Neg.m jri̯",
        "85483": "SC.n.tw.pass.gem.2sgf_Neg.m jri̯",
        "85484": "SC.n.tw.pass.gem.3sgm_Neg.m jri̯",
        "85485": "SC.n.tw.pass.gem.3sgf_Neg.m jri̯",
        "85486": "SC.n.tw.pass.gem.3sg_Neg.m jri̯",
        "85487": "SC.n.tw.pass.gem.1pl_Neg.m jri̯",
        "-85487": "SC.n.tw.pass.gem.1du_Neg.m jri̯",
        "85488": "SC.n.tw.pass.gem.2pl_Neg.m jri̯",
        "-85488": "SC.n.tw.pass.gem.2du_Neg.m jri̯",
        "85489": "SC.n.tw.pass.gem.3pl_Neg.m jri̯",
        "-85489": "SC.n.tw.pass.gem.3du_Neg.m jri̯",
        "85840": "SC.t.act.ngem.nom.subj_Neg.m jri̯",
        "85841": "SC.t.act.ngem.1sg_Neg.m jri̯",
        "85842": "SC.t.act.ngem.2sgm_Neg.m jri̯",
        "85843": "SC.t.act.ngem.2sgf_Neg.m jri̯",
        "85844": "SC.t.act.ngem.3sgm_Neg.m jri̯",
        "85845": "SC.t.act.ngem.3sgf_Neg.m jri̯",
        "85846": "SC.t.act.ngem.3sg_Neg.m jri̯",
        "85847": "SC.t.act.ngem.1pl_Neg.m jri̯",
        "-85847": "SC.t.act.ngem.1du_Neg.m jri̯",
        "85848": "SC.t.act.ngem.2pl_Neg.m jri̯",
        "-85848": "SC.t.act.ngem.2du_Neg.m jri̯",
        "85849": "SC.t.act.ngem.3pl_Neg.m jri̯",
        "-85849": "SC.t.act.ngem.3du_Neg.m jri̯",
        "85850": "SC.t.act.gem.nom.subj_Neg.m jri̯",
        "85851": "SC.t.act.gem.1sg_Neg.m jri̯",
        "85852": "SC.t.act.gem.2sgm_Neg.m jri̯",
        "85853": "SC.t.act.gem.2sgf_Neg.m jri̯",
        "85854": "SC.t.act.gem.3sgm_Neg.m jri̯",
        "85855": "SC.t.act.gem.3sgf_Neg.m jri̯",
        "85856": "SC.t.act.gem.3sg_Neg.m jri̯",
        "85857": "SC.t.act.gem.1pl_Neg.m jri̯",
        "-85857": "SC.t.act.gem.1du_Neg.m jri̯",
        "85858": "SC.t.act.gem.2pl_Neg.m jri̯",
        "-85858": "SC.t.act.gem.2du_Neg.m jri̯",
        "85859": "SC.t.act.gem.3pl_Neg.m jri̯",
        "-85859": "SC.t.act.gem.3du_Neg.m jri̯",
        "85860": "SC.t.pass.ngem.nom.subj_Neg.m jri̯",
        "85861": "SC.t.pass.ngem.1sg_Neg.m jri̯",
        "85862": "SC.t.pass.ngem.2sgm_Neg.m jri̯",
        "85863": "SC.t.pass.ngem.2sgf_Neg.m jri̯",
        "85864": "SC.t.pass.ngem.3sgm_Neg.m jri̯",
        "85865": "SC.t.pass.ngem.3sgf_Neg.m jri̯",
        "85866": "SC.t.pass.ngem.3sg_Neg.m jri̯",
        "85867": "SC.t.pass.ngem.1pl_Neg.m jri̯",
        "-85867": "SC.t.pass.ngem.1du_Neg.m jri̯",
        "85868": "SC.t.pass.ngem.2pl_Neg.m jri̯",
        "-85868": "SC.t.pass.ngem.2du_Neg.m jri̯",
        "85869": "SC.t.pass.ngem.3pl_Neg.m jri̯",
        "-85869": "SC.t.pass.ngem.3du_Neg.m jri̯",
        "85870": "SC.t.pass.gem.nom.subj_Neg.m jri̯",
        "85871": "SC.t.pass.gem.1sg_Neg.m jri̯",
        "85872": "SC.t.pass.gem.2sgm_Neg.m jri̯",
        "85873": "SC.t.pass.gem.2sgf_Neg.m jri̯",
        "85874": "SC.t.pass.gem.3sgm_Neg.m jri̯",
        "85875": "SC.t.pass.gem.3sgf_Neg.m jri̯",
        "85876": "SC.t.pass.gem.3sg_Neg.m jri̯",
        "85877": "SC.t.pass.gem.1pl_Neg.m jri̯",
        "-85877": "SC.t.pass.gem.1du_Neg.m jri̯",
        "85878": "SC.t.pass.gem.2pl_Neg.m jri̯",
        "-85878": "SC.t.pass.gem.2du_Neg.m jri̯",
        "85879": "SC.t.pass.gem.3pl_Neg.m jri̯",
        "-85879": "SC.t.pass.gem.3du_Neg.m jri̯",
        "85910": "SC.pass.ngem.impers_Neg.m jri̯",
        "86000": "SC.unspec.nom.subj_Neg.m dj",
        "86004": "SC.unspec.3sgm_Neg.m dj",
        "86005": "SC.unspec.3sgf_Neg.m dj",
        "86006": "SC.unspec.3sg_Neg.m dj",
        "86020": "SC.act.ngem.nom.subj_Neg.m dj",
        "86021": "SC.act.ngem.1sg_Neg.m dj",
        "86022": "SC.act.ngem.2sgm_Neg.m dj",
        "86023": "SC.act.ngem.2sgf_Neg.m dj",
        "86024": "SC.act.ngem.3sgm_Neg.m dj",
        "86025": "SC.act.ngem.3sgf_Neg.m dj",
        "86026": "SC.act.ngem.3sg_Neg.m dj",
        "86027": "SC.act.ngem.1pl_Neg.m dj",
        "-86027": "SC.act.ngem.1du_Neg.m dj",
        "86028": "SC.act.ngem.2pl_Neg.m dj",
        "-86028": "SC.act.ngem.2du_Neg.m dj",
        "86029": "SC.act.ngem.3pl_Neg.m dj",
        "-86029": "SC.act.ngem.3du_Neg.m dj",
        "86040": "SC.pass.ngem.nom.subj_Neg.m dj",
        "86041": "SC.pass.ngem.1sg_Neg.m dj",
        "86042": "SC.pass.ngem.2sgm_Neg.m dj",
        "86043": "SC.pass.ngem.2sgf_Neg.m dj",
        "86044": "SC.pass.ngem.3sgm_Neg.m dj",
        "86045": "SC.pass.ngem.3sgf_Neg.m dj",
        "86046": "SC.pass.ngem.3sg_Neg.m dj",
        "86047": "SC.pass.ngem.1pl_Neg.m dj",
        "-86047": "SC.pass.ngem.1du_Neg.m dj",
        "86048": "SC.pass.ngem.2pl_Neg.m dj",
        "-86048": "SC.pass.ngem.2du_Neg.m dj",
        "86049": "SC.pass.ngem.3pl_Neg.m dj",
        "-86049": "SC.pass.ngem.3du_Neg.m dj",
        "86100": "SC.act.gem.nom.subj_Neg.m dj",
        "86101": "SC.act.gem.1sg_Neg.m dj",
        "86102": "SC.act.gem.2sgm_Neg.m dj",
        "86103": "SC.act.gem.2sgf_Neg.m dj",
        "86104": "SC.act.gem.3sgm_Neg.m dj",
        "86105": "SC.act.gem.3sgf_Neg.m dj",
        "86106": "SC.act.gem.3sg_Neg.m dj",
        "86107": "SC.act.gem.1pl_Neg.m dj",
        "-86107": "SC.act.gem.1du_Neg.m dj",
        "86108": "SC.act.gem.2pl_Neg.m dj",
        "-86108": "SC.act.gem.2du_Neg.m dj",
        "86109": "SC.act.gem.3pl_Neg.m dj",
        "-86109": "SC.act.gem.3du_Neg.m dj",
        "86120": "SC.pass.gem.nom.subj_Neg.m dj",
        "86121": "SC.pass.gem.1sg_Neg.m dj",
        "86122": "SC.pass.gem.2sgm_Neg.m dj",
        "86123": "SC.pass.gem.2sgf_Neg.m dj",
        "86124": "SC.pass.gem.3sgm_Neg.m dj",
        "86125": "SC.pass.gem.3sgf_Neg.m dj",
        "86126": "SC.pass.gem.3sg_Neg.m dj",
        "86127": "SC.pass.gem.1pl_Neg.m dj",
        "-86127": "SC.pass.gem.1du_Neg.m dj",
        "86128": "SC.pass.gem.2pl_Neg.m dj",
        "-86128": "SC.pass.gem.2du_Neg.m dj",
        "86129": "SC.pass.gem.3pl_Neg.m dj",
        "-86129": "SC.pass.gem.3du_Neg.m dj",
        "86140": "SC.act.spec.nom.subj_Neg.m dj",
        "86141": "SC.act.spec.1sg_Neg.m dj",
        "86142": "SC.act.spec.2sgm_Neg.m dj",
        "86143": "SC.act.spec.2sgf_Neg.m dj",
        "86144": "SC.act.spec.3sgm_Neg.m dj",
        "86145": "SC.act.spec.3sgf_Neg.m dj",
        "86146": "SC.act.spec.3sg_Neg.m dj",
        "86147": "SC.act.spec.1pl_Neg.m dj",
        "-86147": "SC.act.spec.1du_Neg.m dj",
        "86148": "SC.act.spec.2pl_Neg.m dj",
        "-86148": "SC.act.spec.2du_Neg.m dj",
        "86149": "SC.act.spec.3pl_Neg.m dj",
        "-86149": "SC.act.spec.3du_Neg.m dj",
        "86160": "SC.pass.spec.nom.subj_Neg.m dj",
        "86161": "SC.pass.spec.1sg_Neg.m dj",
        "86162": "SC.pass.spec.2sgm_Neg.m dj",
        "86163": "SC.pass.spec.2sgf_Neg.m dj",
        "86164": "SC.pass.spec.3sgm_Neg.m dj",
        "86165": "SC.pass.spec.3sgf_Neg.m dj",
        "86166": "SC.pass.spec.3sg_Neg.m dj",
        "86167": "SC.pass.spec.1pl_Neg.m dj",
        "-86167": "SC.pass.spec.1du_Neg.m dj",
        "86168": "SC.pass.spec.2pl_Neg.m dj",
        "-86168": "SC.pass.spec.2du_Neg.m dj",
        "86169": "SC.pass.spec.3pl_Neg.m dj",
        "-86169": "SC.pass.spec.3du_Neg.m dj",
        "86170": "SC.tw.pass.spec.nom.subj_Neg.m dj",
        "86171": "SC.tw.pass.spec.1sg_Neg.m dj",
        "86172": "SC.tw.pass.spec.2sgm_Neg.m dj",
        "86173": "SC.tw.pass.spec.2sgf_Neg.m dj",
        "86174": "SC.tw.pass.spec.3sgm_Neg.m dj",
        "86175": "SC.tw.pass.spec.3sgf_Neg.m dj",
        "86176": "SC.tw.pass.spec.3sg_Neg.m dj",
        "86177": "SC.tw.pass.spec.1pl_Neg.m dj",
        "-86177": "SC.tw.pass.spec.1du_Neg.m dj",
        "86178": "SC.tw.pass.spec.2pl_Neg.m dj",
        "-86178": "SC.tw.pass.spec.2du_Neg.m dj",
        "86179": "SC.tw.pass.spec.3pl_Neg.m dj",
        "-86179": "SC.tw.pass.spec.3du_Neg.m dj",
        "86180": "SC.w.act.ngem.nom.subj_Neg.m dj",
        "86181": "SC.w.act.ngem.1sg_Neg.m dj",
        "86182": "SC.w.act.ngem.2sgm_Neg.m dj",
        "86183": "SC.w.act.ngem.2sgf_Neg.m dj",
        "86184": "SC.w.act.ngem.3sgm_Neg.m dj",
        "86185": "SC.w.act.ngem.3sgf_Neg.m dj",
        "86186": "SC.w.act.ngem.3sg_Neg.m dj",
        "86187": "SC.w.act.ngem.1pl_Neg.m dj",
        "-86187": "SC.w.act.ngem.1du_Neg.m dj",
        "86188": "SC.w.act.ngem.2pl_Neg.m dj",
        "-86188": "SC.w.act.ngem.2du_Neg.m dj",
        "86189": "SC.w.act.ngem.3pl_Neg.m dj",
        "-86189": "SC.w.act.ngem.3du_Neg.m dj",
        "86220": "SC.w.act.gem.nom.subj_Neg.m dj",
        "86221": "SC.w.act.gem.1sg_Neg.m dj",
        "86222": "SC.w.act.gem.2sgm_Neg.m dj",
        "86223": "SC.w.act.gem.2sgf_Neg.m dj",
        "86224": "SC.w.act.gem.3sgm_Neg.m dj",
        "86225": "SC.w.act.gem.3sgf_Neg.m dj",
        "86226": "SC.w.act.gem.3sg_Neg.m dj",
        "86227": "SC.w.act.gem.1pl_Neg.m dj",
        "-86227": "SC.w.act.gem.1du_Neg.m dj",
        "86228": "SC.w.act.gem.2pl_Neg.m dj",
        "-86228": "SC.w.act.gem.2du_Neg.m dj",
        "86229": "SC.w.act.gem.3pl_Neg.m dj",
        "-86229": "SC.w.act.gem.3du_Neg.m dj",
        "86240": "SC.w.pass.ngem.nom.subj_Neg.m dj",
        "86241": "SC.w.pass.ngem.1sg_Neg.m dj",
        "86242": "SC.w.pass.ngem.2sgm_Neg.m dj",
        "86243": "SC.w.pass.ngem.2sgf_Neg.m dj",
        "86244": "SC.w.pass.ngem.3sgm_Neg.m dj",
        "86245": "SC.w.pass.ngem.3sgf_Neg.m dj",
        "86246": "SC.w.pass.ngem.3sg_Neg.m dj",
        "86247": "SC.w.pass.ngem.1pl_Neg.m dj",
        "-86247": "SC.w.pass.ngem.1du_Neg.m dj",
        "86248": "SC.w.pass.ngem.2pl_Neg.m dj",
        "-86248": "SC.w.pass.ngem.2du_Neg.m dj",
        "86249": "SC.w.pass.ngem.3pl_Neg.m dj",
        "-86249": "SC.w.pass.ngem.3du_Neg.m dj",
        "86280": "SC.w.tw.pass.ngem.nom.subj_Neg.m dj",
        "86281": "SC.w.tw.pass.ngem.1sg_Neg.m dj",
        "86282": "SC.w.tw.pass.ngem.2sgm_Neg.m dj",
        "86283": "SC.w.tw.pass.ngem.2sgf_Neg.m dj",
        "86284": "SC.w.tw.pass.ngem.3sgm_Neg.m dj",
        "86285": "SC.w.tw.pass.ngem.3sgf_Neg.m dj",
        "86286": "SC.w.tw.pass.ngem.3sg_Neg.m dj",
        "86287": "SC.w.tw.pass.ngem.1pl_Neg.m dj",
        "-86287": "SC.w.tw.pass.ngem.1du_Neg.m dj",
        "86288": "SC.w.tw.pass.ngem.2pl_Neg.m dj",
        "-86288": "SC.w.tw.pass.ngem.2du_Neg.m dj",
        "86289": "SC.w.tw.pass.ngem.3pl_Neg.m dj",
        "-86289": "SC.w.tw.pass.ngem.3du_Neg.m dj",
        "86320": "SC.tw.pass.ngem.nom.subj_Neg.m dj",
        "86321": "SC.tw.pass.ngem.1sg_Neg.m dj",
        "86322": "SC.tw.pass.ngem.2sgm_Neg.m dj",
        "86323": "SC.tw.pass.ngem.2sgf_Neg.m dj",
        "86324": "SC.tw.pass.ngem.3sgm_Neg.m dj",
        "86325": "SC.tw.pass.ngem.3sgf_Neg.m dj",
        "86326": "SC.tw.pass.ngem.3sg_Neg.m dj",
        "86327": "SC.tw.pass.ngem.1pl_Neg.m dj",
        "-86327": "SC.tw.pass.ngem.1du_Neg.m dj",
        "86328": "SC.tw.pass.ngem.2pl_Neg.m dj",
        "-86328": "SC.tw.pass.ngem.2du_Neg.m dj",
        "86329": "SC.tw.pass.ngem.3pl_Neg.m dj",
        "-86329": "SC.tw.pass.ngem.3du_Neg.m dj",
        "86360": "SC.tw.pass.gem.nom.subj_Neg.m dj",
        "86361": "SC.tw.pass.gem.1sg_Neg.m dj",
        "86362": "SC.tw.pass.gem.2sgm_Neg.m dj",
        "86363": "SC.tw.pass.gem.2sgf_Neg.m dj",
        "86364": "SC.tw.pass.gem.3sgm_Neg.m dj",
        "86365": "SC.tw.pass.gem.3sgf_Neg.m dj",
        "86366": "SC.tw.pass.gem.3sg_Neg.m dj",
        "86367": "SC.tw.pass.gem.1pl_Neg.m dj",
        "-86367": "SC.tw.pass.gem.1du_Neg.m dj",
        "86368": "SC.tw.pass.gem.2pl_Neg.m dj",
        "-86368": "SC.tw.pass.gem.2du_Neg.m dj",
        "86369": "SC.tw.pass.gem.3pl_Neg.m dj",
        "-86369": "SC.tw.pass.gem.3du_Neg.m dj",
        "86380": "SC.n.act.ngem.nom.subj_Neg.m dj",
        "86381": "SC.n.act.ngem.1sg_Neg.m dj",
        "86382": "SC.n.act.ngem.2sgm_Neg.m dj",
        "86383": "SC.n.act.ngem.2sgf_Neg.m dj",
        "86384": "SC.n.act.ngem.3sgm_Neg.m dj",
        "86385": "SC.n.act.ngem.3sgf_Neg.m dj",
        "86386": "SC.n.act.ngem.3sg_Neg.m dj",
        "86387": "SC.n.act.ngem.1pl_Neg.m dj",
        "-86387": "SC.n.act.ngem.1du_Neg.m dj",
        "86388": "SC.n.act.ngem.2pl_Neg.m dj",
        "-86388": "SC.n.act.ngem.2du_Neg.m dj",
        "86389": "SC.n.act.ngem.3pl_Neg.m dj",
        "-86389": "SC.n.act.ngem.3du_Neg.m dj",
        "86420": "SC.n.act.gem.nom.subj_Neg.m dj",
        "86421": "SC.n.act.gem.1sg_Neg.m dj",
        "86422": "SC.n.act.gem.2sgm_Neg.m dj",
        "86423": "SC.n.act.gem.2sgf_Neg.m dj",
        "86424": "SC.n.act.gem.3sgm_Neg.m dj",
        "86425": "SC.n.act.gem.3sgf_Neg.m dj",
        "86426": "SC.n.act.gem.3sg_Neg.m dj",
        "86427": "SC.n.act.gem.1pl_Neg.m dj",
        "-86427": "SC.n.act.gem.1du_Neg.m dj",
        "86428": "SC.n.act.gem.2pl_Neg.m dj",
        "-86428": "SC.n.act.gem.2du_Neg.m dj",
        "86429": "SC.n.act.gem.3pl_Neg.m dj",
        "-86429": "SC.n.act.gem.3du_Neg.m dj",
        "86430": "SC.n.pass.ngem.nom.subj_Neg.m dj",
        "86431": "SC.n.pass.ngem.1sg_Neg.m dj",
        "86432": "SC.n.pass.ngem.2sgm_Neg.m dj",
        "86433": "SC.n.pass.ngem.2sgf_Neg.m dj",
        "86434": "SC.n.pass.ngem.3sgm_Neg.m dj",
        "86435": "SC.n.pass.ngem.3sgf_Neg.m dj",
        "86436": "SC.n.pass.ngem.3sg_Neg.m dj",
        "86437": "SC.n.pass.ngem.1pl_Neg.m dj",
        "-86437": "SC.n.pass.ngem.1du_Neg.m dj",
        "86438": "SC.n.pass.ngem.2pl_Neg.m dj",
        "-86438": "SC.n.pass.ngem.2du_Neg.m dj",
        "86439": "SC.n.pass.ngem.3pl_Neg.m dj",
        "-86439": "SC.n.pass.ngem.3du_Neg.m dj",
        "86440": "SC.n.tw.pass.ngem.nom.subj_Neg.m dj",
        "86441": "SC.n.tw.pass.ngem.1sg_Neg.m dj",
        "86442": "SC.n.tw.pass.ngem.2sgm_Neg.m dj",
        "86443": "SC.n.tw.pass.ngem.2sgf_Neg.m dj",
        "86444": "SC.n.tw.pass.ngem.3sgm_Neg.m dj",
        "86445": "SC.n.tw.pass.ngem.3sgf_Neg.m dj",
        "86446": "SC.n.tw.pass.ngem.3sg_Neg.m dj",
        "86447": "SC.n.tw.pass.ngem.1pl_Neg.m dj",
        "-86447": "SC.n.tw.pass.ngem.1du_Neg.m dj",
        "86448": "SC.n.tw.pass.ngem.2pl_Neg.m dj",
        "-86448": "SC.n.tw.pass.ngem.2du_Neg.m dj",
        "86449": "SC.n.tw.pass.ngem.3pl_Neg.m dj",
        "-86449": "SC.n.tw.pass.ngem.3du_Neg.m dj",
        "86480": "SC.n.tw.pass.gem.nom.subj_Neg.m dj",
        "86481": "SC.n.tw.pass.gem.1sg_Neg.m dj",
        "86482": "SC.n.tw.pass.gem.2sgm_Neg.m dj",
        "86483": "SC.n.tw.pass.gem.2sgf_Neg.m dj",
        "86484": "SC.n.tw.pass.gem.3sgm_Neg.m dj",
        "86485": "SC.n.tw.pass.gem.3sgf_Neg.m dj",
        "86486": "SC.n.tw.pass.gem.3sg_Neg.m dj",
        "86487": "SC.n.tw.pass.gem.1pl_Neg.m dj",
        "-86487": "SC.n.tw.pass.gem.1du_Neg.m dj",
        "86488": "SC.n.tw.pass.gem.2pl_Neg.m dj",
        "-86488": "SC.n.tw.pass.gem.2du_Neg.m dj",
        "86489": "SC.n.tw.pass.gem.3pl_Neg.m dj",
        "-86489": "SC.n.tw.pass.gem.3du_Neg.m dj",
        "86840": "SC.t.act.ngem.nom.subj_Neg.m dj",
        "86841": "SC.t.act.ngem.1sg_Neg.m dj",
        "86842": "SC.t.act.ngem.2sgm_Neg.m dj",
        "86843": "SC.t.act.ngem.2sgf_Neg.m dj",
        "86844": "SC.t.act.ngem.3sgm_Neg.m dj",
        "86845": "SC.t.act.ngem.3sgf_Neg.m dj",
        "86846": "SC.t.act.ngem.3sg_Neg.m dj",
        "86847": "SC.t.act.ngem.1pl_Neg.m dj",
        "-86847": "SC.t.act.ngem.1du_Neg.m dj",
        "86848": "SC.t.act.ngem.2pl_Neg.m dj",
        "-86848": "SC.t.act.ngem.2du_Neg.m dj",
        "86849": "SC.t.act.ngem.3pl_Neg.m dj",
        "-86849": "SC.t.act.ngem.3du_Neg.m dj",
        "86850": "SC.t.act.gem.nom.subj_Neg.m dj",
        "86851": "SC.t.act.gem.1sg_Neg.m dj",
        "86852": "SC.t.act.gem.2sgm_Neg.m dj",
        "86853": "SC.t.act.gem.2sgf_Neg.m dj",
        "86854": "SC.t.act.gem.3sgm_Neg.m dj",
        "86855": "SC.t.act.gem.3sgf_Neg.m dj",
        "86856": "SC.t.act.gem.3sg_Neg.m dj",
        "86857": "SC.t.act.gem.1pl_Neg.m dj",
        "-86857": "SC.t.act.gem.1du_Neg.m dj",
        "86858": "SC.t.act.gem.2pl_Neg.m dj",
        "-86858": "SC.t.act.gem.2du_Neg.m dj",
        "86859": "SC.t.act.gem.3pl_Neg.m dj",
        "-86859": "SC.t.act.gem.3du_Neg.m dj",
        "86860": "SC.t.pass.ngem.nom.subj_Neg.m dj",
        "86861": "SC.t.pass.ngem.1sg_Neg.m dj",
        "86862": "SC.t.pass.ngem.2sgm_Neg.m dj",
        "86863": "SC.t.pass.ngem.2sgf_Neg.m dj",
        "86864": "SC.t.pass.ngem.3sgm_Neg.m dj",
        "86865": "SC.t.pass.ngem.3sgf_Neg.m dj",
        "86866": "SC.t.pass.ngem.3sg_Neg.m dj",
        "86867": "SC.t.pass.ngem.1pl_Neg.m dj",
        "-86867": "SC.t.pass.ngem.1du_Neg.m dj",
        "86868": "SC.t.pass.ngem.2pl_Neg.m dj",
        "-86868": "SC.t.pass.ngem.2du_Neg.m dj",
        "86869": "SC.t.pass.ngem.3pl_Neg.m dj",
        "-86869": "SC.t.pass.ngem.3du_Neg.m dj",
        "86870": "SC.t.pass.gem.nom.subj_Neg.m dj",
        "86871": "SC.t.pass.gem.1sg_Neg.m dj",
        "86872": "SC.t.pass.gem.2sgm_Neg.m dj",
        "86873": "SC.t.pass.gem.2sgf_Neg.m dj",
        "86874": "SC.t.pass.gem.3sgm_Neg.m dj",
        "86875": "SC.t.pass.gem.3sgf_Neg.m dj",
        "86876": "SC.t.pass.gem.3sg_Neg.m dj",
        "86877": "SC.t.pass.gem.1pl_Neg.m dj",
        "-86877": "SC.t.pass.gem.1du_Neg.m dj",
        "86878": "SC.t.pass.gem.2pl_Neg.m dj",
        "-86878": "SC.t.pass.gem.2du_Neg.m dj",
        "86879": "SC.t.pass.gem.3pl_Neg.m dj",
        "-86879": "SC.t.pass.gem.3du_Neg.m dj",
        "86900": "SC.act.ngem.impers_Neg.m dj",
        "87001": "SC.unspec.1sg_Neg.m jri̯ dj.t",
        "87020": "SC.pass.gem.nom.subj_Neg.m jri̯ dj.t",
        "87021": "SC.pass.gem.1sg_Neg.m jri̯ dj.t",
        "87022": "SC.act.ngem.2sgm_Neg.m jri̯ dj.t",
        "87023": "SC.act.ngem.2sgf_Neg.m jri̯ dj.t",
        "87024": "SC.act.ngem.3sgm_Neg.m jri̯ dj.t",
        "87025": "SC.act.ngem.3sgf_Neg.m jri̯ dj.t",
        "87026": "SC.act.ngem.3sg_Neg.m jri̯ dj.t",
        "87027": "SC.act.ngem.1pl_Neg.m jri̯ dj.t",
        "-87027": "SC.act.ngem.1du_Neg.m jri̯ dj.t",
        "87028": "SC.act.ngem.2pl_Neg.m jri̯ dj.t",
        "-87028": "SC.act.ngem.2du_Neg.m jri̯ dj.t",
        "87029": "SC.act.ngem.3pl_Neg.m jri̯ dj.t",
        "-87029": "SC.act.ngem.3du_Neg.m jri̯ dj.t",
        "87040": "SC.pass.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87041": "SC.pass.ngem.1sg_Neg.m jri̯ dj.t",
        "87042": "SC.pass.ngem.2sgm_Neg.m jri̯ dj.t",
        "87043": "SC.pass.ngem.2sgf_Neg.m jri̯ dj.t",
        "87044": "SC.pass.ngem.3sgm_Neg.m jri̯ dj.t",
        "87045": "SC.pass.ngem.3sgf_Neg.m jri̯ dj.t",
        "87046": "SC.pass.ngem.3sg_Neg.m jri̯ dj.t",
        "87047": "SC.pass.ngem.1pl_Neg.m jri̯ dj.t",
        "-87047": "SC.pass.ngem.1du_Neg.m jri̯ dj.t",
        "87048": "SC.pass.ngem.2pl_Neg.m jri̯ dj.t",
        "-87048": "SC.pass.ngem.2du_Neg.m jri̯ dj.t",
        "87049": "SC.pass.ngem.3pl_Neg.m jri̯ dj.t",
        "-87049": "SC.pass.ngem.3du_Neg.m jri̯ dj.t",
        "87100": "SC.act.gem.nom.subj_Neg.m jri̯ dj.t",
        "87101": "SC.act.gem.1sg_Neg.m jri̯ dj.t",
        "87102": "SC.act.gem.2sgm_Neg.m jri̯ dj.t",
        "87103": "SC.act.gem.2sgf_Neg.m jri̯ dj.t",
        "87104": "SC.act.gem.3sgm_Neg.m jri̯ dj.t",
        "87105": "SC.act.gem.3sgf_Neg.m jri̯ dj.t",
        "87106": "SC.act.gem.3sg_Neg.m jri̯ dj.t",
        "87107": "SC.act.gem.1pl_Neg.m jri̯ dj.t",
        "-87107": "SC.act.gem.1du_Neg.m jri̯ dj.t",
        "87108": "SC.act.gem.2pl_Neg.m jri̯ dj.t",
        "-87108": "SC.act.gem.2du_Neg.m jri̯ dj.t",
        "87109": "SC.act.gem.3pl_Neg.m jri̯ dj.t",
        "-87109": "SC.act.gem.3du_Neg.m jri̯ dj.t",
        "87120": "SC.pass.gem.nom.subj_Neg.m jri̯ dj.t",
        "87121": "SC.pass.gem.1sg_Neg.m jri̯ dj.t",
        "87122": "SC.pass.gem.2sgm_Neg.m jri̯ dj.t",
        "87123": "SC.pass.gem.2sgf_Neg.m jri̯ dj.t",
        "87124": "SC.pass.gem.3sgm_Neg.m jri̯ dj.t",
        "87125": "SC.pass.gem.3sgf_Neg.m jri̯ dj.t",
        "87126": "SC.pass.gem.3sg_Neg.m jri̯ dj.t",
        "87127": "SC.pass.gem.1pl_Neg.m jri̯ dj.t",
        "-87127": "SC.pass.gem.1du_Neg.m jri̯ dj.t",
        "87128": "SC.pass.gem.2pl_Neg.m jri̯ dj.t",
        "-87128": "SC.pass.gem.2du_Neg.m jri̯ dj.t",
        "87129": "SC.pass.gem.3pl_Neg.m jri̯ dj.t",
        "-87129": "SC.pass.gem.3du_Neg.m jri̯ dj.t",
        "87140": "SC.act.spec.nom.subj_Neg.m jri̯ dj.t",
        "87141": "SC.act.spec.1sg_Neg.m jri̯ dj.t",
        "87142": "SC.act.spec.2sgm_Neg.m jri̯ dj.t",
        "87143": "SC.act.spec.2sgf_Neg.m jri̯ dj.t",
        "87144": "SC.act.spec.3sgm_Neg.m jri̯ dj.t",
        "87145": "SC.act.spec.3sgf_Neg.m jri̯ dj.t",
        "87146": "SC.act.spec.3sg_Neg.m jri̯ dj.t",
        "87147": "SC.act.spec.1pl_Neg.m jri̯ dj.t",
        "-87147": "SC.act.spec.1du_Neg.m jri̯ dj.t",
        "87148": "SC.act.spec.2pl_Neg.m jri̯ dj.t",
        "-87148": "SC.act.spec.2du_Neg.m jri̯ dj.t",
        "87149": "SC.act.spec.3pl_Neg.m jri̯ dj.t",
        "-87149": "SC.act.spec.3du_Neg.m jri̯ dj.t",
        "87160": "SC.pass.spec.nom.subj_Neg.m jri̯ dj.t",
        "87161": "SC.pass.spec.1sg_Neg.m jri̯ dj.t",
        "87162": "SC.pass.spec.2sgm_Neg.m jri̯ dj.t",
        "87163": "SC.pass.spec.2sgf_Neg.m jri̯ dj.t",
        "87164": "SC.pass.spec.3sgm_Neg.m jri̯ dj.t",
        "87165": "SC.pass.spec.3sgf_Neg.m jri̯ dj.t",
        "87166": "SC.pass.spec.3sg_Neg.m jri̯ dj.t",
        "87167": "SC.pass.spec.1pl_Neg.m jri̯ dj.t",
        "-87167": "SC.pass.spec.1du_Neg.m jri̯ dj.t",
        "87168": "SC.pass.spec.2pl_Neg.m jri̯ dj.t",
        "-87168": "SC.pass.spec.2du_Neg.m jri̯ dj.t",
        "87169": "SC.pass.spec.3pl_Neg.m jri̯ dj.t",
        "-87169": "SC.pass.spec.3du_Neg.m jri̯ dj.t",
        "87170": "SC.tw.pass.spec.nom.subj_Neg.m jri̯ dj.t",
        "87171": "SC.tw.pass.spec.1sg_Neg.m jri̯ dj.t",
        "87172": "SC.tw.pass.spec.2sgm_Neg.m jri̯ dj.t",
        "87173": "SC.tw.pass.spec.2sgf_Neg.m jri̯ dj.t",
        "87174": "SC.tw.pass.spec.3sgm_Neg.m jri̯ dj.t",
        "87175": "SC.tw.pass.spec.3sgf_Neg.m jri̯ dj.t",
        "87176": "SC.tw.pass.spec.3sg_Neg.m jri̯ dj.t",
        "87177": "SC.tw.pass.spec.1pl_Neg.m jri̯ dj.t",
        "-87177": "SC.tw.pass.spec.1du_Neg.m jri̯ dj.t",
        "87178": "SC.tw.pass.spec.2pl_Neg.m jri̯ dj.t",
        "-87178": "SC.tw.pass.spec.2du_Neg.m jri̯ dj.t",
        "87179": "SC.tw.pass.spec.3pl_Neg.m jri̯ dj.t",
        "-87179": "SC.tw.pass.spec.3du_Neg.m jri̯ dj.t",
        "87180": "SC.w.act.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87181": "SC.w.act.ngem.1sg_Neg.m jri̯ dj.t",
        "87182": "SC.w.act.ngem.2sgm_Neg.m jri̯ dj.t",
        "87183": "SC.w.act.ngem.2sgf_Neg.m jri̯ dj.t",
        "87184": "SC.w.act.ngem.3sgm_Neg.m jri̯ dj.t",
        "87185": "SC.w.act.ngem.3sgf_Neg.m jri̯ dj.t",
        "87186": "SC.w.act.ngem.3sg_Neg.m jri̯ dj.t",
        "87187": "SC.w.act.ngem.1pl_Neg.m jri̯ dj.t",
        "-87187": "SC.w.act.ngem.1du_Neg.m jri̯ dj.t",
        "87188": "SC.w.act.ngem.2pl_Neg.m jri̯ dj.t",
        "-87188": "SC.w.act.ngem.2du_Neg.m jri̯ dj.t",
        "87189": "SC.w.act.ngem.3pl_Neg.m jri̯ dj.t",
        "-87189": "SC.w.act.ngem.3du_Neg.m jri̯ dj.t",
        "87220": "SC.w.act.gem.nom.subj_Neg.m jri̯ dj.t",
        "87221": "SC.w.act.gem.1sg_Neg.m jri̯ dj.t",
        "87222": "SC.w.act.gem.2sgm_Neg.m jri̯ dj.t",
        "87223": "SC.w.act.gem.2sgf_Neg.m jri̯ dj.t",
        "87224": "SC.w.act.gem.3sgm_Neg.m jri̯ dj.t",
        "87225": "SC.w.act.gem.3sgf_Neg.m jri̯ dj.t",
        "87226": "SC.w.act.gem.3sg_Neg.m jri̯ dj.t",
        "87227": "SC.w.act.gem.1pl_Neg.m jri̯ dj.t",
        "-87227": "SC.w.act.gem.1du_Neg.m jri̯ dj.t",
        "87228": "SC.w.act.gem.2pl_Neg.m jri̯ dj.t",
        "-87228": "SC.w.act.gem.2du_Neg.m jri̯ dj.t",
        "87229": "SC.w.act.gem.3pl_Neg.m jri̯ dj.t",
        "-87229": "SC.w.act.gem.3du_Neg.m jri̯ dj.t",
        "87240": "SC.w.pass.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87241": "SC.w.pass.ngem.1sg_Neg.m jri̯ dj.t",
        "87242": "SC.w.pass.ngem.2sgm_Neg.m jri̯ dj.t",
        "87243": "SC.w.pass.ngem.2sgf_Neg.m jri̯ dj.t",
        "87244": "SC.w.pass.ngem.3sgm_Neg.m jri̯ dj.t",
        "87245": "SC.w.pass.ngem.3sgf_Neg.m jri̯ dj.t",
        "87246": "SC.w.pass.ngem.3sg_Neg.m jri̯ dj.t",
        "87247": "SC.w.pass.ngem.1pl_Neg.m jri̯ dj.t",
        "-87247": "SC.w.pass.ngem.1du_Neg.m jri̯ dj.t",
        "87248": "SC.w.pass.ngem.2pl_Neg.m jri̯ dj.t",
        "-87248": "SC.w.pass.ngem.2du_Neg.m jri̯ dj.t",
        "87249": "SC.w.pass.ngem.3pl_Neg.m jri̯ dj.t",
        "-87249": "SC.w.pass.ngem.3du_Neg.m jri̯ dj.t",
        "87280": "SC.w.tw.pass.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87281": "SC.w.tw.pass.ngem.1sg_Neg.m jri̯ dj.t",
        "87282": "SC.w.tw.pass.ngem.2sgm_Neg.m jri̯ dj.t",
        "87283": "SC.w.tw.pass.ngem.2sgf_Neg.m jri̯ dj.t",
        "87284": "SC.w.tw.pass.ngem.3sgm_Neg.m jri̯ dj.t",
        "87285": "SC.w.tw.pass.ngem.3sgf_Neg.m jri̯ dj.t",
        "87286": "SC.w.tw.pass.ngem.3sg_Neg.m jri̯ dj.t",
        "87287": "SC.w.tw.pass.ngem.1pl_Neg.m jri̯ dj.t",
        "-87287": "SC.w.tw.pass.ngem.1du_Neg.m jri̯ dj.t",
        "87288": "SC.w.tw.pass.ngem.2pl_Neg.m jri̯ dj.t",
        "-87288": "SC.w.tw.pass.ngem.2du_Neg.m jri̯ dj.t",
        "87289": "SC.w.tw.pass.ngem.3pl_Neg.m jri̯ dj.t",
        "-87289": "SC.w.tw.pass.ngem.3du_Neg.m jri̯ dj.t",
        "87320": "SC.tw.pass.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87321": "SC.tw.pass.ngem.1sg_Neg.m jri̯ dj.t",
        "87322": "SC.tw.pass.ngem.2sgm_Neg.m jri̯ dj.t",
        "87323": "SC.tw.pass.ngem.2sgf_Neg.m jri̯ dj.t",
        "87324": "SC.tw.pass.ngem.3sgm_Neg.m jri̯ dj.t",
        "87325": "SC.tw.pass.ngem.3sgf_Neg.m jri̯ dj.t",
        "87326": "SC.tw.pass.ngem.3sg_Neg.m jri̯ dj.t",
        "87327": "SC.tw.pass.ngem.1pl_Neg.m jri̯ dj.t",
        "-87327": "SC.tw.pass.ngem.1du_Neg.m jri̯ dj.t",
        "87328": "SC.tw.pass.ngem.2pl_Neg.m jri̯ dj.t",
        "-87328": "SC.tw.pass.ngem.2du_Neg.m jri̯ dj.t",
        "87329": "SC.tw.pass.ngem.3pl_Neg.m jri̯ dj.t",
        "-87329": "SC.tw.pass.ngem.3du_Neg.m jri̯ dj.t",
        "87360": "SC.tw.pass.gem.nom.subj_Neg.m jri̯ dj.t",
        "87361": "SC.tw.pass.gem.1sg_Neg.m jri̯ dj.t",
        "87362": "SC.tw.pass.gem.2sgm_Neg.m jri̯ dj.t",
        "87363": "SC.tw.pass.gem.2sgf_Neg.m jri̯ dj.t",
        "87364": "SC.tw.pass.gem.3sgm_Neg.m jri̯ dj.t",
        "87365": "SC.tw.pass.gem.3sgf_Neg.m jri̯ dj.t",
        "87366": "SC.tw.pass.gem.3sg_Neg.m jri̯ dj.t",
        "87367": "SC.tw.pass.gem.1pl_Neg.m jri̯ dj.t",
        "-87367": "SC.tw.pass.gem.1du_Neg.m jri̯ dj.t",
        "87368": "SC.tw.pass.gem.2pl_Neg.m jri̯ dj.t",
        "-87368": "SC.tw.pass.gem.2du_Neg.m jri̯ dj.t",
        "87369": "SC.tw.pass.gem.3pl_Neg.m jri̯ dj.t",
        "-87369": "SC.tw.pass.gem.3du_Neg.m jri̯ dj.t",
        "87380": "SC.n.act.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87381": "SC.n.act.ngem.1sg_Neg.m jri̯ dj.t",
        "87382": "SC.n.act.ngem.2sgm_Neg.m jri̯ dj.t",
        "87383": "SC.n.act.ngem.2sgf_Neg.m jri̯ dj.t",
        "87384": "SC.n.act.ngem.3sgm_Neg.m jri̯ dj.t",
        "87385": "SC.n.act.ngem.3sgf_Neg.m jri̯ dj.t",
        "87386": "SC.n.act.ngem.3sg_Neg.m jri̯ dj.t",
        "87387": "SC.n.act.ngem.1pl_Neg.m jri̯ dj.t",
        "-87387": "SC.n.act.ngem.1du_Neg.m jri̯ dj.t",
        "87388": "SC.n.act.ngem.2pl_Neg.m jri̯ dj.t",
        "-87388": "SC.n.act.ngem.2du_Neg.m jri̯ dj.t",
        "87389": "SC.n.act.ngem.3pl_Neg.m jri̯ dj.t",
        "-87389": "SC.n.act.ngem.3du_Neg.m jri̯ dj.t",
        "87420": "SC.n.act.gem.nom.subj_Neg.m jri̯ dj.t",
        "87421": "SC.n.act.gem.1sg_Neg.m jri̯ dj.t",
        "87422": "SC.n.act.gem.2sgm_Neg.m jri̯ dj.t",
        "87423": "SC.n.act.gem.2sgf_Neg.m jri̯ dj.t",
        "87424": "SC.n.act.gem.3sgm_Neg.m jri̯ dj.t",
        "87425": "SC.n.act.gem.3sgf_Neg.m jri̯ dj.t",
        "87426": "SC.n.act.gem.3sg_Neg.m jri̯ dj.t",
        "87427": "SC.n.act.gem.1pl_Neg.m jri̯ dj.t",
        "-87427": "SC.n.act.gem.1du_Neg.m jri̯ dj.t",
        "87428": "SC.n.act.gem.2pl_Neg.m jri̯ dj.t",
        "-87428": "SC.n.act.gem.2du_Neg.m jri̯ dj.t",
        "87429": "SC.n.act.gem.3pl_Neg.m jri̯ dj.t",
        "-87429": "SC.n.act.gem.3du_Neg.m jri̯ dj.t",
        "87430": "SC.n.pass.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87431": "SC.n.pass.ngem.1sg_Neg.m jri̯ dj.t",
        "87432": "SC.n.pass.ngem.2sgm_Neg.m jri̯ dj.t",
        "87433": "SC.n.pass.ngem.2sgf_Neg.m jri̯ dj.t",
        "87434": "SC.n.pass.ngem.3sgm_Neg.m jri̯ dj.t",
        "87435": "SC.n.pass.ngem.3sgf_Neg.m jri̯ dj.t",
        "87436": "SC.n.pass.ngem.3sg_Neg.m jri̯ dj.t",
        "87437": "SC.n.pass.ngem.1pl_Neg.m jri̯ dj.t",
        "-87437": "SC.n.pass.ngem.1du_Neg.m jri̯ dj.t",
        "87438": "SC.n.pass.ngem.2pl_Neg.m jri̯ dj.t",
        "-87438": "SC.n.pass.ngem.2du_Neg.m jri̯ dj.t",
        "87439": "SC.n.pass.ngem.3pl_Neg.m jri̯ dj.t",
        "-87439": "SC.n.pass.ngem.3du_Neg.m jri̯ dj.t",
        "87440": "SC.n.tw.pass.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87441": "SC.n.tw.pass.ngem.1sg_Neg.m jri̯ dj.t",
        "87442": "SC.n.tw.pass.ngem.2sgm_Neg.m jri̯ dj.t",
        "87443": "SC.n.tw.pass.ngem.2sgf_Neg.m jri̯ dj.t",
        "87444": "SC.n.tw.pass.ngem.3sgm_Neg.m jri̯ dj.t",
        "87445": "SC.n.tw.pass.ngem.3sgf_Neg.m jri̯ dj.t",
        "87446": "SC.n.tw.pass.ngem.3sg_Neg.m jri̯ dj.t",
        "87447": "SC.n.tw.pass.ngem.1pl_Neg.m jri̯ dj.t",
        "-87447": "SC.n.tw.pass.ngem.1du_Neg.m jri̯ dj.t",
        "87448": "SC.n.tw.pass.ngem.2pl_Neg.m jri̯ dj.t",
        "-87448": "SC.n.tw.pass.ngem.2du_Neg.m jri̯ dj.t",
        "87449": "SC.n.tw.pass.ngem.3pl_Neg.m jri̯ dj.t",
        "-87449": "SC.n.tw.pass.ngem.3du_Neg.m jri̯ dj.t",
        "87480": "SC.n.tw.pass.gem.nom.subj_Neg.m jri̯ dj.t",
        "87481": "SC.n.tw.pass.gem.1sg_Neg.m jri̯ dj.t",
        "87482": "SC.n.tw.pass.gem.2sgm_Neg.m jri̯ dj.t",
        "87483": "SC.n.tw.pass.gem.2sgf_Neg.m jri̯ dj.t",
        "87484": "SC.n.tw.pass.gem.3sgm_Neg.m jri̯ dj.t",
        "87485": "SC.n.tw.pass.gem.3sgf_Neg.m jri̯ dj.t",
        "87486": "SC.n.tw.pass.gem.3sg_Neg.m jri̯ dj.t",
        "87487": "SC.n.tw.pass.gem.1pl_Neg.m jri̯ dj.t",
        "-87487": "SC.n.tw.pass.gem.1du_Neg.m jri̯ dj.t",
        "87488": "SC.n.tw.pass.gem.2pl_Neg.m jri̯ dj.t",
        "-87488": "SC.n.tw.pass.gem.2du_Neg.m jri̯ dj.t",
        "87489": "SC.n.tw.pass.gem.3pl_Neg.m jri̯ dj.t",
        "-87489": "SC.n.tw.pass.gem.3du_Neg.m jri̯ dj.t",
        "87840": "SC.t.act.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87841": "SC.t.act.ngem.1sg_Neg.m jri̯ dj.t",
        "87842": "SC.t.act.ngem.2sgm_Neg.m jri̯ dj.t",
        "87843": "SC.t.act.ngem.2sgf_Neg.m jri̯ dj.t",
        "87844": "SC.t.act.ngem.3sgm_Neg.m jri̯ dj.t",
        "87845": "SC.t.act.ngem.3sgf_Neg.m jri̯ dj.t",
        "87846": "SC.t.act.ngem.3sg_Neg.m jri̯ dj.t",
        "87847": "SC.t.act.ngem.1pl_Neg.m jri̯ dj.t",
        "-87847": "SC.t.act.ngem.1du_Neg.m jri̯ dj.t",
        "87848": "SC.t.act.ngem.2pl_Neg.m jri̯ dj.t",
        "-87848": "SC.t.act.ngem.2du_Neg.m jri̯ dj.t",
        "87849": "SC.t.act.ngem.3pl_Neg.m jri̯ dj.t",
        "-87849": "SC.t.act.ngem.3du_Neg.m jri̯ dj.t",
        "87850": "SC.t.act.gem.nom.subj_Neg.m jri̯ dj.t",
        "87851": "SC.t.act.gem.1sg_Neg.m jri̯ dj.t",
        "87852": "SC.t.act.gem.2sgm_Neg.m jri̯ dj.t",
        "87853": "SC.t.act.gem.2sgf_Neg.m jri̯ dj.t",
        "87854": "SC.t.act.gem.3sgm_Neg.m jri̯ dj.t",
        "87855": "SC.t.act.gem.3sgf_Neg.m jri̯ dj.t",
        "87856": "SC.t.act.gem.3sg_Neg.m jri̯ dj.t",
        "87857": "SC.t.act.gem.1pl_Neg.m jri̯ dj.t",
        "-87857": "SC.t.act.gem.1du_Neg.m jri̯ dj.t",
        "87858": "SC.t.act.gem.2pl_Neg.m jri̯ dj.t",
        "-87858": "SC.t.act.gem.2du_Neg.m jri̯ dj.t",
        "87859": "SC.t.act.gem.3pl_Neg.m jri̯ dj.t",
        "-87859": "SC.t.act.gem.3du_Neg.m jri̯ dj.t",
        "87860": "SC.t.pass.ngem.nom.subj_Neg.m jri̯ dj.t",
        "87861": "SC.t.pass.ngem.1sg_Neg.m jri̯ dj.t",
        "87862": "SC.t.pass.ngem.2sgm_Neg.m jri̯ dj.t",
        "87863": "SC.t.pass.ngem.2sgf_Neg.m jri̯ dj.t",
        "87864": "SC.t.pass.ngem.3sgm_Neg.m jri̯ dj.t",
        "87865": "SC.t.pass.ngem.3sgf_Neg.m jri̯ dj.t",
        "87866": "SC.t.pass.ngem.3sg_Neg.m jri̯ dj.t",
        "87867": "SC.t.pass.ngem.1pl_Neg.m jri̯ dj.t",
        "-87867": "SC.t.pass.ngem.1du_Neg.m jri̯ dj.t",
        "87868": "SC.t.pass.ngem.2pl_Neg.m jri̯ dj.t",
        "-87868": "SC.t.pass.ngem.2du_Neg.m jri̯ dj.t",
        "87869": "SC.t.pass.ngem.3pl_Neg.m jri̯ dj.t",
        "-87869": "SC.t.pass.ngem.3du_Neg.m jri̯ dj.t",
        "87870": "SC.t.pass.gem.nom.subj_Neg.m jri̯ dj.t",
        "87871": "SC.t.pass.gem.1sg_Neg.m jri̯ dj.t",
        "87872": "SC.t.pass.gem.2sgm_Neg.m jri̯ dj.t",
        "87873": "SC.t.pass.gem.2sgf_Neg.m jri̯ dj.t",
        "87874": "SC.t.pass.gem.3sgm_Neg.m jri̯ dj.t",
        "87875": "SC.t.pass.gem.3sgf_Neg.m jri̯ dj.t",
        "87876": "SC.t.pass.gem.3sg_Neg.m jri̯ dj.t",
        "87877": "SC.t.pass.gem.1pl_Neg.m jri̯ dj.t",
        "-87877": "SC.t.pass.gem.1du_Neg.m jri̯ dj.t",
        "87878": "SC.t.pass.gem.2pl_Neg.m jri̯ dj.t",
        "-87878": "SC.t.pass.gem.2du_Neg.m jri̯ dj.t",
        "87879": "SC.t.pass.gem.3pl_Neg.m jri̯ dj.t",
        "-87879": "SC.t.pass.gem.3du_Neg.m jri̯ dj.t",
        "90000": "Admir.partcl.wj",
        "91000": "Verbal.adj.=3sgm",
        "91010": "Verbal.adj.=3sgf",
        "91020": "Verbal.adj.=3pl",
        "-91020": "Verbal.adj.=3du",
        "91030": "Verbal.adj",
        "93000": "Prep.stpr.suffx.unspec.",
        "93001": "Prep.stpr.1sg",
        "93002": "Prep.stpr.2sgm",
        "-93002": "Prep.stpr.2sgm_du",
        "93003": "Prep.stpr.2sgf ",
        "-93004": "Prep.stpr.3sgm_du ",
        "93004": "Prep.stpr.3sgm ",
        "93005": "Prep.stpr.3sgf ",
        "-93005": "Prep.stpr.3sgf_du",
        "93006": "Prep.stpr.3sg ",
        "93007": "Prep.stpr.1pl",
        "-93007": "Prep.stpr.1du",
        "93008": "Prep.stpr.2pl",
        "-93008": "Prep.stpr.2du",
        "93009": "Prep.stpr.3pl",
        "-93009": "Prep.stpr.3du ",
        "93100": "Prep.stpr.",
        "94000": "Partcl.stpr.suffx.unspec.",
        "94001": "Partcl.stpr.1sg ",
        "94002": "Partcl.stpr.2sgm",
        "-94002": "Partcl.stpr.2sgm_du",
        "94003": "Partcl.stpr.2sgf ",
        "94004": "Partcl.stpr.3sgm ",
        "-94004": "Partcl.stpr.3sgm_du",
        "94005": "Partcl.stpr.3sgf ",
        "-94005": "Partcl.stpr.3sgf_du",
        "94006": "Partcl.stpr.3sg ",
        "94007": "Partcl.stpr.1pl",
        "94008": "Partcl.stpr.2pl",
        "94009": "Partcl.stpr.3pl",
        "94010": "Partcl.stpr.1du",
        "94011": "Partcl.stpr.2du",
        "94012": "Partcl.stpr.3du ",
        "94015": "Partcl.stc.1sg",
        "94016": "Partcl.stc.2sgm",
        "94017": "Partcl.stc.2sgf",
        "94018": "Partcl.stc.3sgm",
        "94019": "Partcl.stc.3sgf",
        "94020": "Partcl.stc.3sg",
        "94021": "Partcl.stc.1pl",
        "94022": "Partcl.stc.2pl",
        "94023": "Partcl.stc.3pl",
        "94024": "Partcl.stc.3pl",
        "94100": "Partcl.stpr/stc",
        "96000": "Aux.",
        "96010": "Aux.others+Verb",
        "96020": "Aux.jw_(Prep)+Verb",
        "96030": "Aux.jri̯_(Prep)+Verb",
        "96040": "Aux.j.jri̯_(Prep)+Verb",
        "96050": "Aux.j.jri̯.t_(Prep)+Verb",
        "96060": "Aux.ꜥḥꜥ.n_(Prep)+Verb",
        "96070": "Aux.wn_(Prep)+Verb",
        "96080": "Aux.wnn_(Prep)+Verb",
        "96090": "Aux.wn.jn_(Prep)+Verb",
        "96100": "Aux.bwpw_(Prep)+Verb",
        "96110": "Aux.mtw=_(Prep)+Verb",
        "96120": "Aux.tw=_(Prep)+Verb",
        "96200": "Aux.jw.stpr.suffx.unspec_adv/Verb",
        "96201": "Aux.jw.stpr.1sg_adv/Verb",
        "96202": "Aux.jw.stpr.2sgm_adv/Verb",
        "96203": "Aux.jw.stpr.2sgf_adv/Verb",
        "96204": "Aux.jw.stpr.3sgm_adv/Verb",
        "96205": "Aux.jw.stpr.3sgf_adv/Verb",
        "96206": "Aux.jw.stpr.3sg_adv/Verb",
        "96207": "Aux.jw.stpr.1pl_adv/Verb",
        "-96207": "Aux.jw.stpr.1du_adv/Verb",
        "96208": "Aux.jw.stpr.2pl_adv/Verb",
        "-96208": "Aux.jw.stpr.2du_adv/Verb",
        "96209": "Aux.jw.stpr.3pl_adv/Verb",
        "-96209": "Aux.jw.stpr.3du_adv/Verb",
        "96300": "Aux.stpr.suffx.unspec.",
        "96301": "Aux.stpr.1sg",
        "96302": "Aux.stpr.2sgm",
        "96303": "Aux.stpr.2sgf",
        "96304": "Aux.stpr.3sgm",
        "96305": "Aux.stpr.3sgf",
        "96306": "Aux.stpr.3sg",
        "96307": "Aux.stpr.1pl",
        "-96307": "Aux.stpr.1du",
        "96308": "Aux.stpr.2pl",
        "-96308": "Aux.stpr.2du",
        "96309": "Aux.stpr.3pl",
        "-96309": "Aux.stpr.3du",
        "96310": "Aux.jw.stpr.suffx.unspec_(Prep)_Verb",
        "96311": "Aux.jw.stpr.1sg_(Prep)_Verb",
        "96312": "Aux.jw.stpr.2sgm_(Prep)_Verb",
        "96313": "Aux.jw.stpr.2sgf_(Prep)_Verb",
        "96314": "Aux.jw.stpr.3sgm_(Prep)_Verb",
        "96315": "Aux.jw.stpr.3sgf_(Prep)_Verb",
        "96316": "Aux.jw.stpr.3sg_(Prep)_Verb",
        "96317": "Aux.jw.stpr.1pl_(Prep)_Verb",
        "-96317": "Aux.jw.stpr.1du_(Prep)_Verb",
        "96318": "Aux.jw.stpr.2pl_(Prep)_Verb",
        "-96318": "Aux.jw.stpr.2du_(Prep)_Verb",
        "96319": "Aux.jw.stpr.3pl_(Prep)_Verb",
        "-96319": "Aux.jw.stpr.3du_(Prep)_Verb",
        "96320": "Aux.jri̯.stpr.suffx.unspec_(Prep)_Verb",
        "96321": "Aux.jri̯.stpr.1sg_(Prep)_Verb",
        "96322": "Aux.jri̯.stpr.2sgm_(Prep)_Verb",
        "96323": "Aux.jri̯.stpr.2sgf_(Prep)_Verb",
        "96324": "Aux.jri̯.stpr.3sgm_(Prep)_Verb",
        "96325": "Aux.jri̯.stpr.3sgf_(Prep)_Verb",
        "96326": "Aux.jri̯.stpr.3sg_(Prep)_Verb",
        "96327": "Aux.jri̯.stpr.1pl_(Prep)_Verb",
        "-96327": "Aux.jri̯.stpr.1du_(Prep)_Verb",
        "96328": "Aux.jri̯.stpr.2pl_(Prep)_Verb",
        "-96328": "Aux.jri̯.stpr.2du_(Prep)_Verb",
        "96329": "Aux.jri̯.stpr.3pl_(Prep)_Verb",
        "-96329": "Aux.jri̯.stpr.3du_(Prep)_Verb",
        "96330": "Aux.j.jri̯.stpr.suffx.unspec_(Prep)_Verb",
        "96331": "Aux.j.jri̯.stpr.1sg_(Prep)_Verb",
        "96332": "Aux.j.jri̯.stpr.2sgm_(Prep)_Verb",
        "96333": "Aux.j.jri̯.stpr.2sgf_(Prep)_Verb",
        "96334": "Aux.j.jri̯.stpr.3sgm_(Prep)_Verb",
        "96335": "Aux.j.jri̯.stpr.3sgf_(Prep)_Verb",
        "96336": "Aux.j.jri̯.stpr.3sg_(Prep)_Verb",
        "96337": "Aux.j.jri̯.stpr.1pl_(Prep)_Verb",
        "-96337": "Aux.j.jri̯.stpr.1du_(Prep)_Verb",
        "96338": "Aux.j.jri̯.stpr.2pl_(Prep)_Verb",
        "-96338": "Aux.j.jri̯.stpr.2du_(Prep)_Verb",
        "96339": "Aux.j.jri̯.stpr.3pl_(Prep)_Verb",
        "-96339": "Aux.j.jri̯.stpr.3du_(Prep)_Verb",
        "96340": "Aux.j.jri̯.t.stpr.suffx.unspec_(Prep)_Verb",
        "96341": "Aux.j.jri̯.t.stpr.1sg_(Prep)_Verb",
        "96342": "Aux.j.jri̯.t.stpr.2sgm_(Prep)_Verb",
        "96343": "Aux.j.jri̯.t.stpr.2sgf_(Prep)_Verb",
        "96344": "Aux.j.jri̯.t.stpr.3sgm_(Prep)_Verb",
        "96345": "Aux.j.jri̯.t.stpr.3sgf_(Prep)_Verb",
        "96346": "Aux.j.jri̯.t.stpr.3sg_(Prep)_Verb",
        "96347": "Aux.j.jri̯.t.stpr.1pl_(Prep)_Verb",
        "-96347": "Aux.j.jri̯.t.stpr.1du_(Prep)_Verb",
        "96348": "Aux.j.jri̯.t.stpr.2pl_(Prep)_Verb",
        "-96348": "Aux.j.jri̯.t.stpr.2du_(Prep)_Verb",
        "96349": "Aux.j.jri̯.t.stpr.3pl_(Prep)_Verb",
        "-96349": "Aux.j.jri̯.t.stpr.3du_(Prep)_Verb",
        "96350": "Aux.ꜥḥꜥ.n.stpr.suffx.unspec_(Prep)_Verb",
        "96351": "Aux.ꜥḥꜥ.n.stpr.1sg_(Prep)_Verb",
        "96352": "Aux.ꜥḥꜥ.n.stpr.2sgm_(Prep)_Verb",
        "96353": "Aux.ꜥḥꜥ.n.stpr.2sgf_(Prep)_Verb",
        "96354": "Aux.ꜥḥꜥ.n.stpr.3sgm_(Prep)_Verb",
        "96355": "Aux.ꜥḥꜥ.n.stpr.3sgf_(Prep)_Verb",
        "96356": "Aux.ꜥḥꜥ.n.stpr.3sg_(Prep)_Verb",
        "96357": "Aux.ꜥḥꜥ.n.stpr.1pl_(Prep)_Verb",
        "-96357": "Aux.ꜥḥꜥ.n.stpr.1du_(Prep)_Verb",
        "96358": "Aux.ꜥḥꜥ.n.stpr.2pl_(Prep)_Verb",
        "-96358": "Aux.ꜥḥꜥ.n.stpr.2du_(Prep)_Verb",
        "96359": "Aux.ꜥḥꜥ.n.stpr.3pl_(Prep)_Verb",
        "-96359": "Aux.ꜥḥꜥ.n.stpr.3du_(Prep)_Verb",
        "96360": "Aux.wn.stpr.suffx.unspec_(Prep)_Verb",
        "96361": "Aux.wn.stpr.1sg_(Prep)_Verb",
        "96362": "Aux.wn.stpr.2sgm_(Prep)_Verb",
        "96363": "Aux.wn.stpr.2sgf_(Prep)_Verb",
        "96364": "Aux.wn.stpr.3sgm_(Prep)_Verb",
        "96365": "Aux.wn.stpr.3sgf_(Prep)_Verb",
        "96366": "Aux.wn.stpr.3sg_(Prep)_Verb",
        "96367": "Aux.wn.stpr.1pl_(Prep)_Verb",
        "-96367": "Aux.wn.stpr.1du_(Prep)_Verb",
        "96368": "Aux.wn.stpr.2pl_(Prep)_Verb",
        "-96368": "Aux.wn.stpr.2du_(Prep)_Verb",
        "96369": "Aux.wn.stpr.3pl_(Prep)_Verb",
        "-96369": "Aux.wn.stpr.3du_(Prep)_Verb",
        "96370": "Aux.wnn.stpr.suffx.unspec_(Prep)_Verb",
        "96371": "Aux.wnn.stpr.1sg_(Prep)_Verb",
        "96372": "Aux.wnn.stpr.2sgm_(Prep)_Verb",
        "96373": "Aux.wnn.stpr.2sgf_(Prep)_Verb",
        "96374": "Aux.wnn.stpr.3sgm_(Prep)_Verb",
        "96375": "Aux.wnn.stpr.3sgf_(Prep)_Verb",
        "96376": "Aux.wnn.stpr.3sg_(Prep)_Verb",
        "96377": "Aux.wnn.stpr.1pl_(Prep)_Verb",
        "-96377": "Aux.wnn.stpr.1du_(Prep)_Verb",
        "96378": "Aux.wnn.stpr.2pl_(Prep)_Verb",
        "-96378": "Aux.wnn.stpr.2du_(Prep)_Verb",
        "96379": "Aux.wnn.stpr.3pl_(Prep)_Verb",
        "-96379": "Aux.wnn.stpr.3du_(Prep)_Verb",
        "96380": "Aux.wn.jn.stpr.suffx.unspec_(Prep)_Verb",
        "96381": "Aux.wn.jn.stpr.1sg_(Prep)_Verb",
        "96382": "Aux.wn.jn.stpr.2sgm_(Prep)_Verb",
        "96383": "Aux.wn.jn.stpr.2sgf_(Prep)_Verb",
        "96384": "Aux.wn.jn.stpr.3sgm_(Prep)_Verb",
        "96385": "Aux.wn.jn.stpr.3sgf_(Prep)_Verb",
        "96386": "Aux.wn.jn.stpr.3sg_(Prep)_Verb",
        "96387": "Aux.wn.jn.stpr.1pl_(Prep)_Verb",
        "-96387": "Aux.wn.jn.stpr.1du_(Prep)_Verb",
        "96388": "Aux.wn.jn.stpr.2pl_(Prep)_Verb",
        "-96388": "Aux.wn.jn.stpr.2du_(Prep)_Verb",
        "96389": "Aux.wn.jn.stpr.3pl_(Prep)_Verb",
        "-96389": "Aux.wn.jn.stpr.3du_(Prep)_Verb",
        "96400": "Aux.bwpw.stpr.suffx.unspec_(Prep)_Verb",
        "96401": "Aux.bwpw.stpr.1sg_(Prep)_Verb",
        "96402": "Aux.bwpw.stpr.2sgm_(Prep)_Verb",
        "96403": "Aux.bwpw.stpr.2sgf_(Prep)_Verb",
        "96404": "Aux.bwpw.stpr.3sgm_(Prep)_Verb",
        "96405": "Aux.bwpw.stpr.3sgf_(Prep)_Verb",
        "96406": "Aux.bwpw.stpr.3sg_(Prep)_Verb",
        "96407": "Aux.bwpw.stpr.1pl_(Prep)_Verb",
        "-96407": "Aux.bwpw.stpr.1du_(Prep)_Verb",
        "96408": "Aux.bwpw.stpr.2pl_(Prep)_Verb",
        "-96408": "Aux.bwpw.stpr.2du_(Prep)_Verb",
        "96409": "Aux.bwpw.stpr.3pl_(Prep)_Verb",
        "-96409": "Aux.bwpw.stpr.3du_(Prep)_Verb",
        "96410": "Aux.mtw=.stpr.suffx.unspec_(Prep)_Verb",
        "96411": "Aux.mtw=.stpr.1sg_(Prep)_Verb",
        "96412": "Aux.mtw=.stpr.2sgm_(Prep)_Verb",
        "96413": "Aux.mtw=.stpr.2sgf_(Prep)_Verb",
        "96414": "Aux.mtw=.stpr.3sgm_(Prep)_Verb",
        "96415": "Aux.mtw=.stpr.3sgf_(Prep)_Verb",
        "96416": "Aux.mtw=.stpr.3sg_(Prep)_Verb",
        "96417": "Aux.mtw=.stpr.1pl_(Prep)_Verb",
        "-96417": "Aux.mtw=.stpr.1du_(Prep)_Verb",
        "96418": "Aux.mtw=.stpr.2pl_(Prep)_Verb",
        "-96418": "Aux.mtw=.stpr.2du_(Prep)_Verb",
        "96419": "Aux.mtw=.stpr.3pl_(Prep)_Verb",
        "-96419": "Aux.mtw=.stpr.3du_(Prep)_Verb",
        "96420": "Aux.tw=.stpr.suffx.unspec_(Prep)_Verb",
        "96421": "Aux.tw=.stpr.1sg_(Prep)_Verb",
        "96422": "Aux.tw=.stpr.2sgm_(Prep)_Verb",
        "96423": "Aux.tw=.stpr.2sgf_(Prep)_Verb",
        "96424": "Aux.tw=.stpr.3sgm_(Prep)_Verb",
        "96425": "Aux.tw=.stpr.3sgf_(Prep)_Verb",
        "96426": "Aux.tw=.stpr.3sg_(Prep)_Verb",
        "96427": "Aux.tw=.stpr.1pl_(Prep)_Verb",
        "-96427": "Aux.tw=.stpr.1du_(Prep)_Verb",
        "96428": "Aux.tw=.stpr.2pl_(Prep)_Verb",
        "-96428": "Aux.tw=.stpr.2du_(Prep)_Verb",
        "96429": "Aux.tw=.stpr.3pl_(Prep)_Verb",
        "-96429": "Aux.tw=.stpr.3du_(Prep)_Verb",
        "96430": "Aux.wn.ḫr.stpr.suffx.unspec_(Prep)_Verb",
        "96431": "Aux.wn.ḫr.stpr.1sg_(Prep)_Verb",
        "96432": "Aux.wn.ḫr.stpr.2sgm_(Prep)_Verb",
        "96433": "Aux.wn.ḫr.stpr.2sgf_(Prep)_Verb",
        "96434": "Aux.wn.ḫr.stpr.3sgm_(Prep)_Verb",
        "96435": "Aux.wn.ḫr.stpr.3sgf_(Prep)_Verb",
        "96436": "Aux.wn.ḫr.stpr.3sg_(Prep)_Verb",
        "96437": "Aux.wn.ḫr.stpr.1pl_(Prep)_Verb",
        "-96437": "Aux.wn.ḫr.stpr.1du_(Prep)_Verb",
        "96438": "Aux.wn.ḫr.stpr.2pl_(Prep)_Verb",
        "-96438": "Aux.wn.ḫr.stpr.2du_(Prep)_Verb",
        "96439": "Aux.wn.ḫr.stpr.3pl_(Prep)_Verb",
        "-96439": "Aux.wn.ḫr.stpr.3du_(Prep)_Verb"
        }
    verbal = dict.get(flexcode)
    if verbal:
        return verbal
    else:
        return "(unresolved code: "+flexcode+")" 

def lingGlossFromLemmaID(lemmaID):
    dict = {
        "10030": "-1sg",
        "10050": "-3sg.m",
        "10060": "-3sg.m",
        "10070": "-1pl",
        "10090": "-3sg.f",
        "10100": "-3pl",
        "10110": "-2sg.m",
        "10120": "-2sg.f",
        "10130": "-2pl",
        "27490": "1pl",
        "27940": "1sg",
        "42370": "-3pl",
        "44000": "=1sg",
        "80016": "=1pl",
        "90020": "3sg.m",
        "90080": "3.sg.f",
        "90120": "2sg.m",
        "90160": "2sg.f",
        "127770": "=3.sg.f",
        "129490": "=3sg.m",
        "130830": "3sg.m",
        "136190": "=3pl",
        "147350": "=3sg.c",
        "163890": "=2sg.m",
        "170100": "-3sg.c",
        "172370": "-2pl",
        "174900": "=2sg.m",
        "175050": "2sg.m",
        "175640": "=2sg.f",
        "175650": "=2pl",
        "400960": "=3pl",
        "600625": "2sg.m",
        "600627": "3sg.m",
        "600628": "3.sg.f",
        "851173": "-3.sg.f",
        "851177": "=2du",
        "851182": "=2sg.m2sg.f",
        "851183": "=2sg.c",
        "851184": "=3sg.c",
        "851185": "=3sg.c",
        "851187": "=2pl",
        "851193": "2sg.m",
        "851195": "3sg.m",
        "851199": "3pl",
        "851200": "1sg",
        "851201": "2sg.m",
        "851203": "3sg.m",
        "851204": "3.sg.f",
        "851205": "3.sg.f",
        "851206": "3sg.c",
        "851209": "3pl",
        "851657": "-3pl",
        "851878": "3sg.m",
        "851879": "3.sg.f",
        "851880": "2sg.m",
        "851881": "2sg.f",
        "853880": "=3.sg.f",
        "859326": "3.sg.f",
        "859327": "=3.sg.f",
        "d1172": "-3pl",
        "d1173": "=1sg",
        "d1925": "ART.poss:m.sg",
        "d2193": "-3sg.m",
        "d2866": "-1pl",
        "d300": "-1sg",
        "d3021": "ART.poss:pl",
        "d4934": "-3sg.f",
        "d4936": "=3sg.c",
        "d5105": "-3pl",
        "d5701": "=3pl",
        "d5705": "3pl",
        "d5706": "=3pl",
        "d582": "1pl.poss",
        "d590": "1sg",
        "d6496": "-2sg.m",
        "d6972": "-2sg.f",
        "d7044": "ART.poss:f.sg",
        "d7316": "-2pl",
        "d7332": "=2pl",
        "d7333": "2pl",
        "dm156": "-3sg.m",
        "dm2089": "ART.poss:m.sg",
        "dm2393": "-3pl",
        "dm2475": "=1sg",
        "dm2685": "2sg.f",
        "dm2804": "-2sg.m",
        "dm3593": "m.sg:poss-",
        "dm382": "-3sg.f",
        "dm3873": "1sg.poss",
        "dm3986": "f.sg:poss-" }
    if lemmaID != '':
        lingGloss = dict.get(lemmaID)
    
    if lingGloss:
        return lingGloss
    else:
        return ''        


def stateFromSuffix (flexcode):
    stateFlex = flexcode % 10 # letzte Ziffer isolieren
    if stateFlex == 0: state = '' # sta, stc or unknown
    else: state = ':stpr' # stpr 
    return state
    
def lingGlossFromPOS(pos, sub_pos):
    dictPOS = {
        "adjective": "ADJ",
        "adverb": "ADV",
        "entity_name": "N",
        "epitheton_title": "N",
        "interjection": "INTJ",
        "numeral": "NUM",
        "particle": "PTCL",
        "preposition": "PREP",
        "pronoun": "PRON",
        "root": "ROOT",
        "substantive": "N",
        "undefined": "(undefined)",
        "verb": "V",
        "non valid lemma": "(invalid)"}

    dictSubPOS = {
        "animal_name": "PROPN",
        "artifact_name": "PROPN",
        "cardinal": "NUM.card",
        "demonstrative_pronoun": "DEM",
        "epith_god": "DIVN",
        "epith_king": "ROYLN",
        "gods_name": "DIVN",
        "interrogative_pronoun": "Q",
        "kings_name": "ROYLN",
        "nisbe_adjective_preposition": "PREP-adjz",
        "nisbe_adjective_substantive": "N-adjz",
        "ordinal": "NUM.ord",
        "org_name": "PROPN",
        "particle_enclitic": "=PTCL",
        "particle_nonenclitic": "PTCL",
        "person_name": "PERSN",
        "personal_pronoun": "PRO",
        "place_name": "TOPN",
        "prepositional_adverb": "PREP\\advz",
        "relative_pronoun": "REL",
        "substantive_fem": "N.f",
        "substantive_masc": "N.m",
        "title": "TITL",
        "verb_2-gem": "V",
        "verb_2-lit": "V",
        "verb_3-gem": "V",
        "verb_3-inf": "V",
        "verb_3-lit": "V",
        "verb_4-inf": "V",
        "verb_4-lit": "V",
        "verb_5-inf": "V",
        "verb_5-lit": "V",
        "verb_6-lit": "V",
        "verb_caus_2-gem": "V",
        "verb_caus_2-lit": "V",
        "verb_caus_3-gem": "V",
        "verb_caus_3-inf": "V",
        "verb_caus_3-lit": "V",
        "verb_caus_4-inf": "V",
        "verb_caus_4-lit": "V",
        "verb_caus_5-lit": "V",
        "verb_irr": "V" }
    
    if sub_pos != '':
        lingGloss = dictSubPOS.get(sub_pos)
        if lingGloss:
            return lingGloss
    if pos != '':
        lingGloss = dictPOS.get(pos)
        if lingGloss != '':
            return lingGloss
        
    return ''
    
def defaultFlexFromPOS(pos, sub_pos):
    dictPOS = {
        "adjective": "ADJ:m.sg",
        "adverb": "ADV",
        "entity_name": "N",
        "epitheton_title": "N",
        "interjection": "INTJ",
        "numeral": "NUM",
        "particle": "PTCL",
        "preposition": "PREP",
        "pronoun": "PRON",
        "root": "ROOT",
        "substantive": "N.m:sg",
        "undefined": "(undefined)",
        "verb": "V",
        "non valid lemma": "(invalid)"}

    dictSubPOS = {
        "animal_name": "PROPN",
        "artifact_name": "PROPN",
        "cardinal": "NUM.card",
        "demonstrative_pronoun": "DEM",
        "epith_god": "DIVN",
        "epith_king": "ROYLN",
        "gods_name": "DIVN",
        "interrogative_pronoun": "Q",
        "kings_name": "ROYLN",
        "nisbe_adjective_preposition": "PREP-adjz:m.sg",
        "nisbe_adjective_substantive": "N-adjz:m.sg",
        "ordinal": "NUM.ord:m.sg",
        "org_name": "PROPN",
        "particle_enclitic": "=PTCL",
        "particle_nonenclitic": "PTCL",
        "person_name": "PERSN",
        "personal_pronoun": "PRO",
        "place_name": "TOPN",
        "prepositional_adverb": "PREP\\advz",
        "relative_pronoun": "REL:m.sg",
        "substantive_fem": "N.f:sg",
        "substantive_masc": "N.m:sg",
        "title": "TITL",
        "verb_2-gem": "V",
        "verb_2-lit": "V",
        "verb_3-gem": "V",
        "verb_3-inf": "V",
        "verb_3-lit": "V",
        "verb_4-inf": "V",
        "verb_4-lit": "V",
        "verb_5-inf": "V",
        "verb_5-lit": "V",
        "verb_6-lit": "V",
        "verb_caus_2-gem": "V",
        "verb_caus_2-lit": "V",
        "verb_caus_3-gem": "V",
        "verb_caus_3-inf": "V",
        "verb_caus_3-lit": "V",
        "verb_caus_4-inf": "V",
        "verb_caus_4-lit": "V",
        "verb_caus_5-lit": "V",
        "verb_irr": "V" }
    
    if sub_pos != '':
        lingGloss = dictSubPOS.get(sub_pos)
        if lingGloss:
            return lingGloss
    if pos != '':
        lingGloss = dictPOS.get(pos)
        if lingGloss:
            return lingGloss
    
    return ''
    
def stemType (sub_pos):
    if     sub_pos == 'verb_3-inf' \
        or sub_pos == 'verb_irr' \
        or sub_pos == 'verb_4-inf' \
        or sub_pos == 'verb_5-inf' \
        or sub_pos == 'verb_caus_3-inf' \
        or sub_pos == 'verb_caus_4-inf': 
        return 'inf'
    elif   sub_pos == 'verb_2-gem' \
        or sub_pos == 'verb_3-gem' \
        or sub_pos == 'verb_caus_2-gem' \
        or sub_pos == 'verb_caus_3-gem': 
        return 'gem'
    elif   sub_pos == 'verb_2-lit' \
        or sub_pos == 'verb_3-lit' \
        or sub_pos == 'verb_4-lit' \
        or sub_pos == 'verb_5-lit' \
        or sub_pos == 'verb_6-lit' \
        or sub_pos == 'verb_caus_2-lit' \
        or sub_pos == 'verb_caus_3-lit' \
        or sub_pos == 'verb_caus_4-lit' \
        or sub_pos == 'verb_caus_5-lit': 
        return 'strong'
    return ''
    
@register.filter(is_safe=True)
def computeLingGlossing(flexcode, lemmaID):
    logFile = None # kein Error Log ausgeben
    pos ='' # im mockup noch nicht verfügbar
    sub_pos ='' # im mockup noch nicht verfügbar
    
    # ling. Glossierung aus LemmaID (Pronomina, u.a)
    glossing = lingGlossFromLemmaID(lemmaID)
    if glossing != '':
        return glossing
    
    # ling. Glossierung aus flexcode
    glossing = ''
    try:
        flexcode = int(flexcode)
    except ValueError:
        if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid flexcode [no number]: '+flexcode)
        return '(invalid code)'
    
    if flexcode >= 0:
        algSign = 1
    else:
        algSign = 0
        flexcode = abs(flexcode) 
        
    flex = flexcode % 100000 #Negationsstelle x00000 abschneiden
        
    # Status-Codes
    if (flexcode >= 0) and (flexcode <= 9): 
        glossing = lingGlossFromPOS(pos, sub_pos)
        #if flexcode == 0: glossing += '(flex: unedited)'
        #elif flexcode == 1: glossing += '(flex: ?)'
        #elif flexcode == 2: glossing += '(flex: ?)'
        #elif flexcode == 3: glossing += '(flex: not specified)'
        #elif flexcode == 4: glossing += '(flex: unclear)'
        #elif flexcode == 5: glossing += '(flex: problematic)'
        #elif flexcode == 9: glossing += '(flex: to be reviewed)'
        if flexcode == 3:
            glossing = defaultFlexFromPOS(pos, sub_pos)
        if glossing == '': 
            if flexcode == 0: glossing = '(unedited)'
            elif flexcode == 1: glossing = '(?)'
            elif flexcode == 2: glossing = '(?)'
            elif flexcode == 3: glossing = '—'
            elif flexcode == 4: glossing = '(unclear)'
            elif flexcode == 5: glossing = '(problematic)'
            elif flexcode == 9: glossing = '(to be reviewed)'            
            
    # Suffixkonjugation
    elif ((flex // 10000) == 1) or (((flex // 1000) >= 82) and ((flex // 1000) <= 87)):
        glossing = 'V\\tam'
        flex = flex % 10000 # auf 4 Stellen beschneiden, SK-Info weg
        #if (flex // 1000) == 1: # präf.SK 
        #    glossing = 'tam:'+glossing
        flex = flex % 1000 # auf 3 Stellen beschneiden, aux.-Info weg
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        
        #SK-Formen
        flex = flex // 10 # letzte Stelle beschneiden
        skForm = ''
        if   flex ==  0: # 1x00x, "SK" (unterspezifiziert)
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified suffix conjugation flexcode (form, xxx00x): '+str(flexcode))
        elif flex ==  2: skForm = '.act' # 10020, "SK.akt.kzl"
        elif flex ==  4: skForm = '.pass' # 10040, "SK.pass.kzl"
        elif flex == 10: 
            skForm = '.act' # 10100, "SK.akt.gem"
            if stemType(sub_pos) == 'inf': # jrr
                glossing = 'V~ipfv'
        elif flex == 12: 
            skForm = '.pass' # 10120, "SK.pass.gem=redupl"
            if stemType(sub_pos) == 'strong' \
                or stemType(sub_pos) == 'inf': # sDmm, nDrr; https://wikis.hu-berlin.de/ancientegyptian/%C2%A780
                glossing = 'V~post'
        elif flex == 14: skForm = '.act' # 10140, "SK.akt.spez"
        elif flex == 16: skForm = '.pass' # 10160, "SK.pass.spez"
        elif flex == 17: skForm = '-pass' # 10170, "SK.tw-pass.spez"
        elif flex == 18: skForm = '.act' # 10180, "SK.w-.akt.kzl"
        elif flex == 20: skForm = '.act' # 10200, "Sk.w-.akt.kurz", ##obsolete
        elif flex == 22: skForm = '.act' # 10220, "Sk.w-.akt.gem"
        elif flex == 24: skForm = '.pass' # 10240, "SK.w-.pass.kzl"
        elif flex == 28: skForm = '-pass' # 10280, "SK.w-.tw-pass.kzl"
        elif flex == 30: skForm = '-pass' # 10300, "SK.w-.tw-pass.kurz", ##obsolete
        elif flex == 32: skForm = '-pass' # 10320, "SK.tw-pass.kzl"
        elif flex == 36: 
            skForm = '-pass' # 10360, "SK.tw-pass.gem"
            if stemType(sub_pos) == 'inf': # jrr.tw
                glossing = 'V~ipfv'
        elif flex == 38: skForm = '.act-ant' # 10380, "SK.n-.akt.kzl"
        elif flex == 40: skForm = '.act-ant' # 10400, "SK.n-.akt.kurz", ##obsolete
        elif flex == 42: skForm = '.act-ant' # 10420, "SK.n-.akt.gem"
        elif flex == 44: skForm = '-ant-pass' # 10440, "SK.n-.tw-pass.kzl"
        elif flex == 48: skForm = '-ant-pass' # 10480, "SK.n-.tw-pass.gem"
        elif flex == 50: skForm = '.act-cnsv' # 10500, "SK.jn-.akt.kzl"
        elif flex == 54: skForm = '.act-cnsv' # 10540, "SK.jn-.akt.gem"
        elif flex == 56: skForm = '-cnsv-pass' # 10560, "SK.jn-.tw-pass.kzl"
        elif flex == 57: skForm = '-cnsv-pass' # 10570 , "SK.jn-.tw-pass.kzl.unpersönl."
        elif flex == 60: skForm = '.act-oblv' # 10600, "SK.ḫr-.akt.kzl"
        elif flex == 61: skForm = '.act' # 10610, "ḫr SK.akt.kzl"
        elif flex == 64: skForm = '.act-oblv' # 10640, "SK.ḫr-.akt.gem"
        elif flex == 65: skForm = '.act' # 10650, "ḫr SK akt.gem"
        elif flex == 66: skForm = '-oblv-pass' # 10660, "SK.ḫr-.tw-pass.kzl"
        elif flex == 67: skForm = '-pass' # 10670, "ḫr SK-tw.pass.kzl"
        elif flex == 70: skForm = '-oblv-pass' # 10700, "SK.ḫr-.tw-pass.gem"
        elif flex == 71: skForm = '-pass' # 10710, "ḫr SK-tw.pass.gem"
        elif flex == 72: skForm = '.act-post' # 10720, "SK.kꜣ-.akt.kzl"
        elif flex == 73: skForm = '.act' # 10730, "kꜣ SK.akt.kzl"
        elif flex == 76: skForm = '.act-post' # 10760, "SK.kꜣ-.akt.gem"
        elif flex == 77: skForm = '.act' # 10770, "kꜣ SK. akt.gem. "
        elif flex == 78: skForm = '-post-pass' # 10780, "SK.kꜣ-.tw-pass.kzl"
        elif flex == 79: skForm = '-pass' # 10790, "kꜣ SK.-tw-pass.kzl."
        elif flex == 82: skForm = '-post-pass' # 10820, "SK.kꜣ-.tw-pass.gem"
        elif flex == 83: skForm = '-pass' # 10830, "k3 SK.-tw-pass.gem"
        elif flex == 84: skForm = '.act-compl' # 10840, "SK.t-.akt.kzl."
        elif flex == 85: skForm = '.act-compl' # 10850, "SK.t-.akt.gem"
        elif flex == 86: skForm = '.pass-compl' # 10860, "SK.t-.pass.kzl"
        elif flex == 87: skForm = '.pass-compl' # 10870, "SK.t-.pass.gem"
        elif flex == 90: skForm = '.act' # 10900, "SK.akt.kzl.unpersönl."
        elif flex == 91: skForm = '.pass' # 10910, "SK.pass.kzl.unpersönl."
        elif flex == 92: 
            skForm = '.act' # 10920, "SK.akt.gem.unpersönl."
            if stemType(sub_pos) == 'inf': # jrr
                glossing = 'V~ipfv'
        elif flex == 93: 
            skForm = '.pass' # 10930, "SK.pass.gem.unpersönl."
            if stemType(sub_pos) == 'strong' \
                or stemType(sub_pos) == 'inf': # sDmm, nDrr; https://wikis.hu-berlin.de/ancientegyptian/%C2%A780
                glossing = 'V~post'
        elif flex == 80: skForm = '.act-ant' # 10800, "SK.n-akt.kzl.unpersönl."
        elif flex == 81: skForm = '-ant-pass' # 10810, "SK.n-tw.pass.kzl.unpersönl. "
        elif flex == 94: skForm = '.pass' # 10940, "SK.unpersönl.w-pass."
        elif flex == 95: skForm = '-pass' # 10950, "SK.tw-pass.kzl.unpersönl."
        elif flex == 96: skForm = '-pass' # 10960, "SK.tw-pass.gem.unpersönl."
        elif flex == 19: skForm = '-pass' # 10190 , "SK.tw-pass.spez.unpersönl."
        elif flex == 97: skForm = '.act' # 10970 , "SK.akt.spez.unpersönl."
        elif flex == 98: skForm = '.pass' # 10980 , "SK.pass.spez.unpersönl."
        elif flex == 99: skForm = '.act-compl' # 10990 , "SK.t-akt.kzl.unpersönl."
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid suffix conjugation flexcode (form, pattern xxxXXx): '+str(flexcode))
        glossing += skForm + state
        
        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif (pos == 'adjective' and str(sub_pos) == 'nan'):
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
            
    # Resultative
    elif (flex // 10000) == 2:
        glossing = 'V\\res'
        flex = flex % 10000 # auf 4 Stellen beschneiden, PsP-Info weg
        #if (flex // 1000) == 1: # präf.PsP 
        #    glossing = 'tam:'+glossing
        if (flex // 1000) > 7: # ungültig 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid resultative flexcode (pattern x2[0-7]xxx): '+str(flexcode))
            
        flex = flex % 1000 # auf 3 Stellen beschneiden, Stamm- & einige aux-Info weg
        flex = flex // 10 # letzte Stelle abschneiden, weitere aux-Info weg
        
        form = ''
        if   flex ==  0: # 2x00x, "psp" (unterspezifiziert)
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified resultative form (ending, pattern x2x00x): '+str(flexcode))
        elif flex ==  1: form = '-1sg' # 20010, "psp.sg1"
        elif flex ==  2: form = '-2sg.m' # 20020, "psp.sg2m"
        elif flex ==  3: form = '-2sg.f' # 20030, "psp.sg2f"
        elif flex ==  4: form = '-3sg.m' # 20040, "psp.sg3m"
        elif flex == 34: form = '-3sg' # 20040, "psp.sg3"
        elif flex ==  5: form = '-3sg.f' # 20050, "psp.sg3f"
        elif flex ==  6: form = '-1pl' # 20060, "psp.pl1"
        elif flex ==  7: form = '-2pl' # 20070, "psp.pl2"
        elif flex ==  8: form = '-3pl.m' # 20080, "psp.pl3m"
        elif flex == 38: form = '-3pl' # 20080, "psp.pl3"
        elif flex ==  9: form = '-3pl.f' # 20090, "psp.pl3f"
        elif flex == 10: form = '-2du' # 20100, "psp.du2"
        elif flex == 11: form = '-3du.m' # 20110, "psp.du3m"
        elif flex == 31: form = '-3du' # 20110, "psp.du3"
        elif flex == 12: form = '-3du.f' # 20120, "psp.du3f"
        elif flex == 13: form = '-1du' # 20130, "psp.du1"
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid resultative flexcode (ending, pattern x2x[1-13/31/34/38]x): '+str(flexcode))
        glossing += form
        
        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined' \
            or (pos == 'adjective' and str(sub_pos) == 'nan'):
                pass # ok
        elif (pos == 'epitheton_title' and str(sub_pos) != 'title') \
            or (pos == 'adverb' and str(sub_pos) == 'nan'):
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
 
    # Partizip
    elif (flex // 10000) == 3:
        glossing = 'V\\ptcp'
        flex = flex % 10000 # auf 4 Stellen beschneiden, PsP-Info weg

        if (flex // 1000) == 1: # gem.Partizip 
            if stemType(sub_pos) == 'inf':
                glossing = 'V~ptcp.distr'
        #elif (flex // 1000) == 2: # präf.Partizip 
        #    if str(sub_pos) == 'verb_2-lit': # j.rx.w, https://wikis.hu-berlin.de/ancientegyptian/%C2%A797
        #        glossing = 'V\\ptcp.distr' # wegen nägy. nicht immer korrekt
        elif (flex // 1000) > 2: # ungültig 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid participle flexcode (pattern x3[0-2]xxx): '+str(flexcode))        
        flex = flex % 1000 # auf 3 Stellen beschneiden, Stamm-Info weg
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg
        
        ptcpForm = ''
        if   flex ==  0: # 3x00x, "partz" (unterspezifiziert)
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified participle flexcode (genus verbi/number/gender, pattern x3x00x): '+str(flexcode))
        elif flex ==  1: ptcpForm = '.act.m.sg' # 30010, "partz.akt.sgm"
        elif flex ==  2: ptcpForm = '.act.f.sg' # 30020, "partz.akt.sgf"
        elif flex == 32: ptcpForm = '.act.f' # 30320, "partz.akt.sg"
        elif flex ==  3: ptcpForm = '.act.m.pl' # 30030, "partz.akt.plm"
        elif flex ==  4: ptcpForm = '.act.f.pl' # 30040, "partz.akt.plf"
        elif flex ==  5: ptcpForm = '.act.m.du' # 30050, "partz.akt.dum"
        elif flex ==  6: ptcpForm = '.act.f.du' # 30060, "partz.akt.duf"
        elif flex ==  7: ptcpForm = '.pass.m.sg' # 30070, "partz.pass.sgm"
        elif flex ==  8: ptcpForm = '.pass.f.sg' # 30080, "partz.pass.sgf"
        elif flex == 38: ptcpForm = '.pass.f' # 30380, "partz.pass.sg"
        elif flex ==  9: ptcpForm = '.pass.m.pl' # 30090, "partz.pass.plm"
        elif flex == 10: ptcpForm = '.pass.f.pl' # 30100, "partz.pass.plf"
        elif flex == 11: ptcpForm = '.pass.m.du' # 30110, "partz.pass.dum"
        elif flex == 12: ptcpForm = '.pass.f.du' # 30120, "partz.pass.duf"
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid participle flexcode (genus verbi/number/gender, pattern x3x[1-12/32/38]x): '+str(flexcode))
        glossing += ptcpForm + state

        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined' :
                pass # ok
        elif (pos == 'adjective' and str(sub_pos) == 'nan') \
            or pos == 'substantive' \
            or pos == 'entity_name'\
            or pos == 'epitheton_title':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        
    # Relativform
    elif (flex // 10000) == 4:
        glossing = 'V\\rel'
        flex = flex % 10000 # auf 4 Stellen beschneiden, Relf.-Info weg
        
        stem = ''
        if (flex // 1000) == 1: # gem.Partizip 
            if stemType(sub_pos) == 'inf':
                stem = 'redupl'
        #elif (flex // 1000) == 2: # präf. 
        #    glossing = 'tam:'+glossing
        elif (flex // 1000) > 2: # ungültig 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid participle flexcode (pattern x4[0-2]xxx): '+str(flexcode))        
        flex = flex % 1000 # auf 3 Stellen beschneiden, Stamm-Info weg
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stellen abschneiden, state-Info weg
        
        relForm = ''
        tam = ''
        if   flex ==  0: # 4x00x, "rel" (unterspezifiziert)
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified relafive form flexcode (number/gender/tempus, pattern x4x00x): '+str(flexcode))
        elif flex ==  1: 
            relForm = '.m.sg-ant' # 40010, "rel.f.n-.sgm" ### ipfv-Kombi nicht als Warnung abgefangen
            tam = 'ant'
        elif flex == 31: 
            relForm = '.m-ant' # 40310, "rel.f.n-.m"
            tam = 'ant'
        elif flex ==  2: 
            relForm = '.f.sg-ant' # 40020, "rel.f.n-.sgf"
            tam = 'ant'
        elif flex == 32: 
            relForm = '.f-ant' # 40320, "rel.f.n-.sg"
            tam = 'ant'
        elif flex ==  3: 
            relForm = '.m.pl-ant' # 40030, "rel.f n-.plm"
            tam = 'ant'
        elif flex ==  4: 
            relForm = '.f.pl-ant' # 40040, "rel.f.n-.plf"
            tam = 'ant'
        elif flex ==  5: 
            relForm = '.m.du-ant' # 40050, "rel.f.n-.dum"
            tam = 'ant'
        elif flex ==  6: 
            relForm = '.f.du-ant' # 40060, "rel.f.n-.duf"
            tam = 'ant'
        elif flex ==  7: relForm = '.m.sg' # 40070, "rel.f.sgm"
        elif flex ==  8: relForm = '.f.sg' # 40080, "rel.f.sgf"
        elif flex == 38: relForm = '.f' # 40080, "rel.f.f"
        elif flex ==  9: relForm = '.m.pl' # 40090, "rel.f.plm"
        elif flex == 10: relForm = '.f.pl' # 40100, "rel.f.plf"
        elif flex == 11: relForm = '.m.du' # 40110, "rel.f.dum"
        elif flex == 12: relForm = '.f.du' # 40120, "rel.f.duf"
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid relafive form flexcode (number/gender/tempus, pattern x4x[1-12/31/32/38]x): '+str(flexcode))

        if stem == 'redupl':
            if tam != 'ant':
                glossing = 'V~rel.ipfv'
            else:
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Anterior relative form with reduplicating stem ('+str(sub_pos)+')<>'+glossing)
        
        glossing += relForm + state

        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined' :
                pass # ok
        elif (pos == 'adjective' and str(sub_pos) == 'nan') \
            or pos == 'substantive' \
            or pos == 'entity_name'\
            or pos == 'epitheton_title' :
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
 
    # Imperativ
    elif (flex // 10000) == 5:
        glossing = 'V\\imp'
        flex = flex % 10000 # auf 4 Stellen beschneiden, Imp.-Info weg
        #if (flex // 1000) == 1: # präf. 
        #    glossing = 'tam:'+glossing
        if (flex // 1000) > 2: # ungültig 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid imperative flexcode (pattern 5[0-2]xxx): '+str(flexcode))        
        flex = flex % 1000 # auf 3 Stellen beschneiden, Stamm-Info weg
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stellen abschneiden, state-Info weg
        
        form = ''
        if flex == 0: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified imperative flexcode (pattern 5x0xx): '+str(flexcode))
        elif flex == 1: form = '.sg' # 50010, "imp.sg"
        elif flex == 2: form = '.pl' # 50020, "imp.pl"
        elif flex == 3: form = '.du' # 50030, "imp.du"
        elif flex == 4: form = '' # 50040, "jmj.tw=" ENG §357
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid imperative flexcode (pattern 5x[1-4]xx): '+str(flexcode))
        glossing += form + state    
        
        # Check POS compatibility
        if     pos == 'verb'  \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif (pos == 'particle' and str(sub_pos) != 'particle_enclitic') \
            or pos == 'interjection':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Nominale Verbalformen
    elif (flex // 1000) == 60:
        glossing = 'V'
        flex = flex % 1000 # auf 3 Stellen beschneiden, NomVf.-Info weg      
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg
        
        if flex % 10 > 0:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid nominal verb form flexcode (pattern 7xx[1-5]x): '+str(flexcode))
        flex = flex // 10 # letzte Stelle abschneiden
            
        form = ''
        if   flex == 0: 
            form = '\\nmlz/advz' # 60000, "subst/adv.verbf" (!unterspezifiziert)
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Underspecified nominal/adverbial verb form flexcode (pattern 7x0xx): '+str(flexcode))
        elif flex == 1: form = '\\nmlz.m' # 60100, "verbalnomen.kzl"
        elif flex == 2: form = '\\nmlz.m' # 60200, "verbalnomen.endg w/j"
        elif flex == 3: form = '\\nmlz.f' # 60300, "verbalnomen.endg. t"
        elif flex == 4: form = '\\nmlz.f' # 60400, "verbalnomen.endg. wt/jt"
        elif flex == 5: form = '\\nmlz' # 60500, "verbalnomen gem"
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid nominal verb form flexcode (pattern 7x[1-5]xx): '+str(flexcode))
        glossing += form + state  

        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif (pos == 'adverb' and str(sub_pos) != 'prepositional_adverb') \
            or pos == 'substantive':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        
    # Komplementsinfinitive
    elif (flex // 1000) == 62:
        glossing = 'V\\adv.inf'
        flex = flex % 1000 # auf 3 Stellen beschneiden, KomplInf-Info weg      
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg
        
        if flex % 10 > 0:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid complementary infinitive flexcode (pattern 62x0x): '+str(flexcode))
        flex = flex // 10 # letzte Stelle abschneiden
            
        form = ''
        if flex == 0: # 62000, "kompl.inf." (unterspezifiziert)
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified(?) complementary infinitive flexcode (pattern 620?xx): '+str(flexcode))
        elif flex == 1: form = '.f' # 62100, "kompl.inf.endg.t"
        elif flex == 2: form = '.f' # 62200, "kompl.inf.endg.wt"
        elif flex == 3: form = '.f' # 62300, "kompl.inf.jt/yt"
        elif flex == 4: form = '.m' # 62400, "kompl.inf.gem."
        elif flex == 5: form = '.f' # 62500, "kompl.inf.gem.endg.t"
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid complementary infinitive flexcode (pattern 62[1-5]0x): '+str(flexcode))
        glossing += form + state  

        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'substantive':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Negativkomplement
    elif (flex // 1000) == 63:
        glossing = 'V\\advz'
        flex = flex % 1000 # auf 3 Stellen beschneiden, NegKompl-Info weg      
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg
        
        if flex % 10 > 0:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid negative complement flexcode (pattern 63x0x): '+str(flexcode))
        flex = flex // 10 # letzte Stelle abschneiden
            
        form = ''
        if flex == 0: # 63000, "neg.kompl" (unterspezifiziert)
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified negative complement flexcode (pattern 630xx): '+str(flexcode))
        elif flex == 1: form = '' # 63100, "neg.kompl.kzl"
        elif flex == 2: form = '' # 63200, "neg.kompl.endg.w"
        elif flex == 3: form = '' # 63300, "neg.kompl.endg.t"
        elif flex == 4: form = '' # 63400, "neg.kompl.gem"
        elif flex == 5: form = '' # 63500, "neg.kompl.gem.endg.t"
        elif flex == 6: form = '' # 63600, "neg.kompl.gem.endg.w"
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid negative complement flexcode (pattern 63[1-6]0x): '+str(flexcode))
        glossing += form + state  
        
        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Infinitive
    elif (flex // 1000) == 61 or (((flex // 1000) >= 64) and ((flex // 1000) <= 69)):
        glossing = 'V\\inf'
        flex = flex % 1000 # auf 3 Stellen beschneiden, NegKompl-Info weg      
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        glossing += state 
        
        #nicht existierende Codes nicht abgefangen

        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'substantive':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Substantive
    elif (flex // 1000) == 70:
        glossing = 'N'
        flex = flex % 1000 # auf 3 Stellen beschneiden, KomplInf-Info weg   
        
        #Status
        stateFlex = flex % 100 // 10 # vorletzte Stelle isolieren
        state = ''
        if stateFlex == 0: state = '' # sta oder unbekannt 
        elif stateFlex == 5: state = ':stpr' # stpr
        elif stateFlex == 6: state = ':stc' # stc 
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid substantive flexcode (state; pattern 70x[0/5/6]x): '+str(flexcode))
        
        #Suffixe
        stateFlex = flex % 10 # letzte Ziffer isolieren
        if stateFlex != 0: # stpr
            if state != ':stpr': 
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Erroneous substantive stat.pr. flex code [state] (pattern 70x5x): '+str(flexcode))
                state = ':stpr'
        flex = flex // 100 # letzte beiden Stelle abschneiden, state-Info weg
        
        form = ''
        if flex == 0: form = ':sg' # sg
        elif flex == 1: form = ':pl' # pl
        elif flex == 3: form = ':du' # du
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid substantive flexcode (number; pattern 70[0/1/3]xx): '+str(flexcode))

        gender = ''
        if pos == 'substantive':
            if sub_pos == 'substantive_masc': gender ='.m'
            elif sub_pos == 'substantive_fem': gender ='.f'
            else:
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified substantive form: no gender on noun ('+str(flexcode)+'): ' + glossing + gender + form + state)               
        
        glossing += gender + form + state  

        # Check POS compatibility
        if     pos == 'substantive' \
            or pos == 'entity_name' \
            or pos == 'epitheton_title' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'verb' \
            or pos == 'adjective' \
            or pos == 'pronoun' \
            or pos == 'numeral' \
            or pos == 'preposition' :
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Adjektive
    elif (flex // 1000) == 71:
        glossing = 'ADJ'
        if sub_pos == "nisbe_adjective_preposition":
            glossing = "PREP-adjz"
        elif sub_pos == "nisbe_adjective_substantive":
            glossing = "N-adjz"
        flex = flex % 1000 # auf 3 Stellen beschneiden, Adj-Info weg     
                
        #Status
        stateFlex = flex // 100 # erste Ziffer isolieren
        
        form = ''
        state = ''
        if stateFlex == 0: 
            state = '' # sta oder unbekannt 
            flex = flex // 10 # erste beiden Ziffern isolieren ; ACHTUNG: Schenkels Neuerungen noch nicht berücksichtgt
            
            if flex == 0: 
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified adjective flexcode (number/gender; pattern 71000): '+str(flexcode))
            elif flex == 1: form = ':m.sg' # 
            elif flex == 2: form = ':f.sg' # 
            elif flex == 3: form = ':m.pl' # 
            elif flex == 4: form = ':f.pl' # 
            elif flex == 5: form = ':m.du' # 
            elif flex == 6: form = ':f.du' # 
            else: 
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid adjective flexcode (number/gender; pattern 710[1-6]0): '+str(flexcode))

            if flexcode % 10 != 0:
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid adjective flexcode (Suffix without stat.pr.; pattern 711[0/1?-5/6?]0): '+str(flexcode))
        elif stateFlex == 1: 
            state = '' # "stc", eigentlich Kompositum, z.B. ni-sw 
            
            #enklitische Pronomina
            abhFlex = flex % 100 # letzte zwei Ziffern isolieren
            if abhFlex == 0: state = '' # 
            elif ((abhFlex >= 1) and (abhFlex <= 9)): 
                state = ':stpr' # stpr  
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid adjective flexcode (suffix pronoun instead of dep. pronoun; pattern 711[15-24]): '+str(flexcode))
            elif ((abhFlex >= 15) and (abhFlex <= 24)): state = '' # "stc"  
            else:
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid adjective flexcode (pronoun; pattern 711[15-24]): '+str(flexcode))
        elif stateFlex == 2: 
            state = ':stpr' # stpr redundant
            flex = flex // 10 # erste beiden Ziffern isolieren ; ACHTUNG: Schenkels Neuerungen noch nicht berücksichtgt

            if flex == 20: form = ':m.sg' # sic, verwirrend, dass bei 0 beginnend
            elif flex == 21: form = ':f.sg' # 
            elif flex == 22: form = ':m.pl' # 
            elif flex == 23: form = ':f.pl' # 
            elif flex == 24: form = ':m.du' # 
            elif flex == 25: form = ':f.du' # 
            elif flex == 26: # 71260, "adj. in SK m. Präfix nꜣ (Einerstelle Suffixpr.) / Spätzeit [nꜣ:nfr=f]
                glossing = 'vblz-ADJ'
            else: 
                if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid adjective flexcode (number/gender; pattern 712[0-6]x): '+str(flexcode))

            #Suffixe
            state = stateFromSuffix (flexcode)
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid adjective flexcode (number/gender; pattern 71[0-2][0-6]x): '+str(flexcode))
        flex = flex % 10 # erste Stelle abschneiden, state-Info weg
        glossing += form + state  

        # Check POS compatibility
        if     pos == 'adjective' \
            or pos == 'pronoun' \
            or pos == 'numeral' \
            or (pos == 'epitheton_title' and str(sub_pos) != 'title') \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'substantive' \
            or pos == 'entity_name' \
            or pos == 'epitheton_title' \
            or pos == 'preposition' \
            or pos == 'verb':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        
    # Adverbien
    elif (flex // 1000) == 72:
        glossing = 'ADV'
        flex = flex % 1000 # auf 3 Stellen beschneiden, NegKompl-Info weg      
        
        #Suffixe
        state = ''
        stateFlex = flex % 10 # letzte Ziffer isolieren
        if stateFlex == 0: state = ':stpr' # st.pr. aber Suffix zerstört ## verwirrend 
        else: state = ':stpr' # stpr  
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg        
        
        if flex != 0:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid adverbial flexcode (pattern 7200x): '+str(flexcode))
            
        glossing += state  
        
        # Check POS compatibility
        if     pos == 'adverb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'adjective' \
            or (pos == 'epitheton_title' and sub_pos != 'title') \
            or pos == 'preposition':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
          
    # Zahlen
    elif (flex // 1000) == 74:
        glossing = 'NUM'
        flex = flex % 1000 # auf 3 Stellen beschneiden, NegKompl-Info weg      
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg        
                
        form = ''
        subtype = ''
        if flex == 0: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified number form (pattern 7400x): '+str(flexcode))
        elif flex == 1: 
            form = '.ord:sg.m' # immer sg?
            subtype = 'ordinal'
        elif flex == 2: 
            form = '.ord:sg.f' # immer sg?
            subtype = 'ordinal'
        elif flex == 3: 
            form = '.card:m' # wa, snwi 
            subtype = 'cardinal'
        elif flex == 4: 
            form = '.card:f' # wa.t, sn.ti 
            subtype = 'cardinal'
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid number form (pattern 740[1-4]x): '+str(flexcode))
        glossing += form + state  

        # Check POS compatibility
        if     (pos == 'numeral' and str(sub_pos) == 'nan') \
            or str(sub_pos) == subtype \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'numeral' \
            or pos == 'substantive' \
            or pos == 'adjective' \
            or pos == 'epitheton_title':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        
    # Possessivartikel
    elif (flex // 100) == 800:
        glossing = 'ART.poss'
        flex = flex % 100 # auf 2 Stellen beschneiden, Possartikel-Info weg      
        
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg        
                
        if flex != 0: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid possessive article flexcode (pattern 8000x): '+str(flexcode))
        glossing += state       

        # Check POS compatibility
        if     (pos == 'pronoun' and str(sub_pos) == 'nan') \
            or str(sub_pos) == 'demonstrative_pronoun' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'substantive' \
            or str(sub_pos) == 'personal_pronoun' \
            or (pos == 'adjective' and str(sub_pos) == 'nan'):
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Relativpronomina
    elif ((flex // 100) >= 801) and ((flex // 1000) <= 81):
        glossing = 'PRON.rel'
        flex = flex % 10000 # auf 4 Stellen beschneiden, RelPron-Info weg      
        
        #Suffixe und enklitische Pronomina
        state = ''
        stateFlex = flex % 100 # letzte zwei Ziffern isolieren
        if stateFlex == 0: state = '' # 
        elif ((stateFlex >= 1) and (stateFlex <= 9)): state = ':stpr' # stpr  
        elif ((stateFlex >= 15) and (stateFlex <= 24)): state = '' # abh. Pronomen / "stc"  
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid relative pronoun flexcode (pronoun, pattern 8xx0x / 8xx15-24): '+str(flexcode))
        flex = flex // 100 # letzte zwei Stellen abschneiden, state-Info weg        
                
        form = ''
        if   flex ==  0: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified(?) relative pronoun form (pattern 8[0-1][1?-4]xx): '+str(flexcode))
        elif flex ==  1: form = ':m.sg' #  
        elif flex ==  2: form = ':f.sg' #  
        elif flex ==  3: form = ':m.pl' # 
        elif flex ==  4: form = ':f.pl' # 
        elif flex == 10: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Underspecified relative pronoun form (pattern 8[0-1][1?-4]xx): '+str(flexcode))
        elif flex == 11: form = ':m.sg' #  
        elif flex == 12: form = ':f.sg' #  
        elif flex == 13: form = ':m.pl' # 
        elif flex == 14: form = ':f.pl' # 
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid relative pronoun flexcode (gender/number, pattern 8[0-1][1-4]xx): '+str(flexcode))
        glossing += form + state  

        # Check POS compatibility
        if    (pos == 'pronoun' and str(sub_pos) == 'relative_pronoun') \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif  (pos == 'pronoun' and str(sub_pos) == 'nan') \
            or pos == 'substantive' \
            or pos == 'entity_name' \
            or (pos == 'adjective' and str(sub_pos) == 'nan') \
            or (pos == 'particle' and str(sub_pos) != 'particle_enclitic') \
            or str(sub_pos) == 'nisbe_adjective_preposition':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Admirativsuffix
    elif (flex // 1000) == 90:
        glossing = 'ADJ-excl'
        flex = flex % 1000 # auf 3 Stellen beschneiden, Possartikel-Info weg          
                
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg        

        if flex != 0: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid admirativ suffix flexcode (pattern 9000x): '+str(flexcode))
        glossing += state

        # Check POS compatibility
        if     pos == 'adjective' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'verb':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        
    # sdm.tj.fj
    elif (flex // 100) == 910:
        glossing = 'V:ptcp.post'
        flex = flex % 100 # auf 2 Stellen beschneiden, Verbaladj-Info weg              

        form = ''
        if   flex ==  0: form = '-m.sg' #  
        elif flex == 10: form = '-f.sg' #  
        elif flex == 20: form = '-m.pl' # 
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid posterior participle flexcode (pattern 910[0-2]0): '+str(flexcode))
        glossing += form
        
        # Check POS compatibility
        if     pos == 'verb' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif (pos == 'adjective' and str(sub_pos) == 'nan'):
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
         
    # Präpositionen
    elif (flex // 100) == 930:
        glossing = 'PREP'
        flex = flex % 100 # auf 2 Stellen beschneiden, Possartikel-Info weg          
                
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg        

        if flex != 0: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid preposition flexcode (pattern 9300x): '+str(flexcode))
        glossing += state
        
        # Check POS compatibility
        if     pos == 'preposition' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif (pos == 'particle' and str(sub_pos) != 'particle_nonenclitic') \
            or str(sub_pos) == 'nisbe_adjective_preposition' \
            or str(sub_pos) == 'prepositional_adverb' \
            or pos == 'adverb' \
            or pos == 'adjective' \
            or pos == 'substantive' \
            or pos == 'entity_name' \
            or pos == 'epitheton_title' :
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
         
    # Partikeln
    elif (flex // 100) == 940:
        glossing = 'PTCL'
        flex = flex % 100 # auf 2 Stellen beschneiden, Particle-Info weg          
                
        #Suffixe und enklitische Pronomina
        state = ''
        stateFlex = flex % 100 # letzte zwei Ziffern isolieren
        if stateFlex == 0: state = '' # 
        elif ((stateFlex >= 1) and (stateFlex <= 9)): state = ':stpr' # stpr  
        elif ((stateFlex >= 15) and (stateFlex <= 24)): state = '' # "stc"  
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid particle flexcode (pronoun; pattern 9400x, 94015-24): '+str(flexcode))

        glossing += state
        
        # Check POS compatibility
        if     pos == 'particle' \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'adverb' \
            or pos == 'interjection' \
            or pos == 'preposition' \
            or str(sub_pos) == 'interrogative_pronoun':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)

    # Auxilliar
    elif (flex // 1000) == 96:
        glossing = 'AUX'
        flex = flex % 1000 # auf 3 Stellen beschneiden, Aux-Info weg          
                
        #Suffixe
        state = stateFromSuffix (flexcode)
        flex = flex // 10 # letzte Stelle abschneiden, state-Info weg  
        
        form = ''
        if flex == 20: form = '' # (unspezifiziert)
        elif ((flex >= 30) and (flex <= 38)): form = '' # 
        elif ((flex >= 40) and (flex <= 43)): form = '' # 
        else: 
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Invalid auxilliary flexcode (form, pattern 7620x, 7630x-43x):'+str(flexcode))
        glossing += form + state 
        
        # Check POS compatibility
        #####warum tauch aux nicht in den pos/sub_pos auf??
        if     pos == 'verb' \
            or (pos == 'particle' and str(sub_pos) != 'particle_enclitic') \
            or pos == 'non valid lemma' \
            or pos == 'undefined':
                pass # ok
        elif pos == 'preposition':
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\t'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tWarning: Suspicious POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
        else:
            if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Invalid POS<>flexcode combination: '+pos+'('+str(sub_pos)+')<>'+glossing)
    
    else:
        #unresolved
        glossing = lingGlossFromPOS(pos, sub_pos)
        if glossing == '': 
            glossing = '(unresolved)'
        if logFile: logFile.write('\n'+pos+'\t'+str(sub_pos)+'\t'+str(flexcode)+'\tError: Unhandled flex code: '+str(flexcode))

    return glossing
    
    
#### Kilani Unicode Hieroglyphs Mockup
# First Function - replaces sign codes, keeps control characters

@register.filter(is_safe=True)
def MdC_Unicode_withLatinControlChars(wordToParse):

    wordToParse = wordToParse.replace("-", "£-£").replace(":", "£:£").replace("*", "£*£").replace("(", "£(£").replace(
        "£)£", "").replace("£&£", "")

    signsToParse = wordToParse.split("£")

    signsParsed = replaceGardiner(signsToParse)

    wordParsed = "".join(signsParsed)

    return wordParsed

#- - - - - - - - - - - -

# Second Function - replaces sign codes, removes control characters

@register.filter(is_safe=True)
def MdC_Unicode_noControlChars(wordToParse):

    wordToParse = wordToParse.replace("-", "£-£").replace(":", "£:£").replace("*", "£*£").replace("(", "£(£").replace(
        "£)£", "").replace("£&£", "")

    signsToParse = wordToParse.split("£")

    signsParsed = replaceGardiner(signsToParse)

    wordToParse = "".join(signsParsed)

    wordParsed = wordToParse.replace("-", "").replace(":", "").replace("*", "").replace("(", "").replace(")", "").replace("&", "")
    wordParsed = wordParsed.replace("§", "(").replace("$", ")")

    return wordParsed

#- - - - - - - - - - - -

# Third Function - replaces sign codes, removes control characters, insert the breaking-ligature character (u

@register.filter(is_safe=True)
def MdC_Unicode_noControlChars_WithBreakLigChar(wordToParse):

    wordToParse = wordToParse.replace("-", "£-£").replace(":", "£:£").replace("*", "£*£").replace("(", "£(£").replace("£)£", "").replace("£&£", "")

    signsToParse = wordToParse.split("£")

    signsParsed = replaceGardiner(signsToParse)

    wordToParse = "".join(signsParsed)

    wordParsed = wordToParse.replace("-", u"\u200B").replace(":", "").replace("*", "").replace("(", "").replace(")", "").replace("&", "")
    wordParsed = wordParsed.replace("§", "(").replace("$", ")")

    return wordParsed






#============================

#============================


def replaceGardiner (signs):

    for i in range (0, len(signs)):
        if signs[i] == 'Z16h':
            signs[i] = '𓐌'
        elif signs[i] == 'Z16g':
            signs[i] = '𓐋'
        elif signs[i] == 'Z16f':
            signs[i] = '𓐊'
        elif signs[i] == 'Z16e':
            signs[i] = '𓐉'
        elif signs[i] == 'Z16d':
            signs[i] = '𓐈'
        elif signs[i] == 'Z16c':
            signs[i] = '𓐇'
        elif signs[i] == 'Z16b':
            signs[i] = '𓐆'
        elif signs[i] == 'Z16a':
            signs[i] = '𓐅'
        elif signs[i] == 'Z16':
            signs[i] = '𓐄'
        elif signs[i] == 'Z15i':
            signs[i] = '𓐃'
        elif signs[i] == 'Z15h':
            signs[i] = '𓐂'
        elif signs[i] == 'Z15g':
            signs[i] = '𓐁'
        elif signs[i] == 'Z15f':
            signs[i] = '𓐀'
        elif signs[i] == 'Z15e':
            signs[i] = '𓏿'
        elif signs[i] == 'Z15d':
            signs[i] = '𓏾'
        elif signs[i] == 'Z15c':
            signs[i] = '𓏽'
        elif signs[i] == 'Z15b':
            signs[i] = '𓏼'
        elif signs[i] == 'Z15a':
            signs[i] = '𓏻'
        elif signs[i] == 'Z15':
            signs[i] = '𓏺'
        elif signs[i] == 'Z14':
            signs[i] = '𓏹'
        elif signs[i] == 'Z13':
            signs[i] = '𓏸'
        elif signs[i] == 'Z12':
            signs[i] = '𓏷'
        elif signs[i] == 'Z11':
            signs[i] = '𓏶'
        elif signs[i] == 'Z10':
            signs[i] = '𓏵'
        elif signs[i] == 'Z9':
            signs[i] = '𓏴'
        elif signs[i] == 'Z8':
            signs[i] = '𓏳'
        elif signs[i] == 'Z7':
            signs[i] = '𓏲'
        elif signs[i] == 'Z6':
            signs[i] = '𓏱'
        elif signs[i] == 'Z5A':
            signs[i] = '𓏰'
        elif signs[i] == 'Z5':
            signs[i] = '𓏯'
        elif signs[i] == 'Z4a':
            signs[i] = '𓏮'
        elif signs[i] == 'Z4':
            signs[i] = '𓏭'
        elif signs[i] == 'Z3b':
            signs[i] = '𓏬'
        elif signs[i] == 'Z3A':
            signs[i] = '𓏫'
        elif signs[i] == 'Z3':
            signs[i] = '𓏪'
        elif signs[i] == 'Z2d':
            signs[i] = '𓏩'
        elif signs[i] == 'Z2c':
            signs[i] = '𓏨'
        elif signs[i] == 'Z2b':
            signs[i] = '𓏧'
        elif signs[i] == 'Z2a':
            signs[i] = '𓏦'
        elif signs[i] == 'Z2':
            signs[i] = '𓏥'
        elif signs[i] == 'Z1':
            signs[i] = '𓏤'
        elif signs[i] == 'Y8':
            signs[i] = '𓏣'
        elif signs[i] == 'Y7':
            signs[i] = '𓏢'
        elif signs[i] == 'Y6':
            signs[i] = '𓏡'
        elif signs[i] == 'Y5':
            signs[i] = '𓏠'
        elif signs[i] == 'Y4':
            signs[i] = '𓏟'
        elif signs[i] == 'Y3':
            signs[i] = '𓏞'
        elif signs[i] == 'Y2':
            signs[i] = '𓏝'
        elif signs[i] == 'Y1a':
            signs[i] = '𓏜'
        elif signs[i] == 'Y1':
            signs[i] = '𓏛'
        elif signs[i] == 'X8a':
            signs[i] = '𓏚'
        elif signs[i] == 'X8':
            signs[i] = '𓏙'
        elif signs[i] == 'X7':
            signs[i] = '𓏘'
        elif signs[i] == 'X6a':
            signs[i] = '𓏗'
        elif signs[i] == 'X6':
            signs[i] = '𓏖'
        elif signs[i] == 'X5':
            signs[i] = '𓏕'
        elif signs[i] == 'X4b':
            signs[i] = '𓏔'
        elif signs[i] == 'X4a':
            signs[i] = '𓏓'
        elif signs[i] == 'X4':
            signs[i] = '𓏒'
        elif signs[i] == 'X3':
            signs[i] = '𓏑'
        elif signs[i] == 'X2':
            signs[i] = '𓏐'
        elif signs[i] == 'X1':
            signs[i] = '𓏏'
        elif signs[i] == 'W25':
            signs[i] = '𓏎'
        elif signs[i] == 'W24a':
            signs[i] = '𓏍'
        elif signs[i] == 'W24':
            signs[i] = '𓏌'
        elif signs[i] == 'W23':
            signs[i] = '𓏋'
        elif signs[i] == 'W22':
            signs[i] = '𓏊'
        elif signs[i] == 'W21':
            signs[i] = '𓏉'
        elif signs[i] == 'W20':
            signs[i] = '𓏈'
        elif signs[i] == 'W19':
            signs[i] = '𓏇'
        elif signs[i] == 'W18a':
            signs[i] = '𓏆'
        elif signs[i] == 'W18':
            signs[i] = '𓏅'
        elif signs[i] == 'W17a':
            signs[i] = '𓏄'
        elif signs[i] == 'W17':
            signs[i] = '𓏃'
        elif signs[i] == 'W16':
            signs[i] = '𓏂'
        elif signs[i] == 'W15':
            signs[i] = '𓏁'
        elif signs[i] == 'W14a':
            signs[i] = '𓏀'
        elif signs[i] == 'W14':
            signs[i] = '𓎿'
        elif signs[i] == 'W13':
            signs[i] = '𓎾'
        elif signs[i] == 'W12':
            signs[i] = '𓎽'
        elif signs[i] == 'W11':
            signs[i] = '𓎼'
        elif signs[i] == 'W10a':
            signs[i] = '𓎻'
        elif signs[i] == 'W10':
            signs[i] = '𓎺'
        elif signs[i] == 'W9a':
            signs[i] = '𓎹'
        elif signs[i] == 'W9':
            signs[i] = '𓎸'
        elif signs[i] == 'W8':
            signs[i] = '𓎷'
        elif signs[i] == 'W7':
            signs[i] = '𓎶'
        elif signs[i] == 'W6':
            signs[i] = '𓎵'
        elif signs[i] == 'W5':
            signs[i] = '𓎴'
        elif signs[i] == 'W4':
            signs[i] = '𓎳'
        elif signs[i] == 'W3a':
            signs[i] = '𓎲'
        elif signs[i] == 'W3':
            signs[i] = '𓎱'
        elif signs[i] == 'W2':
            signs[i] = '𓎰'
        elif signs[i] == 'W1':
            signs[i] = '𓎯'
        elif signs[i] == 'V40a':
            signs[i] = '𓎮'
        elif signs[i] == 'V40':
            signs[i] = '𓎭'
        elif signs[i] == 'V39':
            signs[i] = '𓎬'
        elif signs[i] == 'V38':
            signs[i] = '𓎫'
        elif signs[i] == 'V37a':
            signs[i] = '𓎪'
        elif signs[i] == 'V37':
            signs[i] = '𓎩'
        elif signs[i] == 'V36':
            signs[i] = '𓎨'
        elif signs[i] == 'V35':
            signs[i] = '𓎧'
        elif signs[i] == 'V34':
            signs[i] = '𓎦'
        elif signs[i] == 'V33a':
            signs[i] = '𓎥'
        elif signs[i] == 'V33':
            signs[i] = '𓎤'
        elif signs[i] == 'V32':
            signs[i] = '𓎣'
        elif signs[i] == 'V31a':
            signs[i] = '𓎢'
        elif signs[i] == 'V31':
            signs[i] = '𓎡'
        elif signs[i] == 'V30a':
            signs[i] = '𓎠'
        elif signs[i] == 'V30':
            signs[i] = '𓎟'
        elif signs[i] == 'V29a':
            signs[i] = '𓎞'
        elif signs[i] == 'V29':
            signs[i] = '𓎝'
        elif signs[i] == 'V28a':
            signs[i] = '𓎜'
        elif signs[i] == 'V28':
            signs[i] = '𓎛'
        elif signs[i] == 'V27':
            signs[i] = '𓎚'
        elif signs[i] == 'V26':
            signs[i] = '𓎙'
        elif signs[i] == 'V25':
            signs[i] = '𓎘'
        elif signs[i] == 'V24':
            signs[i] = '𓎗'
        elif signs[i] == 'V23a':
            signs[i] = '𓎖'
        elif signs[i] == 'V23':
            signs[i] = '𓎕'
        elif signs[i] == 'V22':
            signs[i] = '𓎔'
        elif signs[i] == 'V21':
            signs[i] = '𓎓'
        elif signs[i] == 'V20l':
            signs[i] = '𓎒'
        elif signs[i] == 'V20k':
            signs[i] = '𓎑'
        elif signs[i] == 'V20j':
            signs[i] = '𓎐'
        elif signs[i] == 'V20i':
            signs[i] = '𓎏'
        elif signs[i] == 'V20h':
            signs[i] = '𓎎'
        elif signs[i] == 'V20g':
            signs[i] = '𓎍'
        elif signs[i] == 'V20f':
            signs[i] = '𓎌'
        elif signs[i] == 'V20e':
            signs[i] = '𓎋'
        elif signs[i] == 'V20d':
            signs[i] = '𓎊'
        elif signs[i] == 'V20c':
            signs[i] = '𓎉'
        elif signs[i] == 'V20b':
            signs[i] = '𓎈'
        elif signs[i] == 'V20a':
            signs[i] = '𓎇'
        elif signs[i] == 'V20':
            signs[i] = '𓎆'
        elif signs[i] == 'V19':
            signs[i] = '𓎅'
        elif signs[i] == 'V18':
            signs[i] = '𓎄'
        elif signs[i] == 'V17':
            signs[i] = '𓎃'
        elif signs[i] == 'V16':
            signs[i] = '𓎂'
        elif signs[i] == 'V15':
            signs[i] = '𓎁'
        elif signs[i] == 'V14':
            signs[i] = '𓎀'
        elif signs[i] == 'V13':
            signs[i] = '𓍿'
        elif signs[i] == 'V12b':
            signs[i] = '𓍾'
        elif signs[i] == 'V12a':
            signs[i] = '𓍽'
        elif signs[i] == 'V12':
            signs[i] = '𓍼'
        elif signs[i] == 'V11c':
            signs[i] = '𓍻'
        elif signs[i] == 'V11b':
            signs[i] = '𓍺'
        elif signs[i] == 'V11a':
            signs[i] = '𓍹'
        elif signs[i] == 'V11':
            signs[i] = '𓍸'
        elif signs[i] == 'V10':
            signs[i] = '𓍷'
        elif signs[i] == 'V9':
            signs[i] = '𓍶'
        elif signs[i] == 'V8':
            signs[i] = '𓍵'
        elif signs[i] == 'V7b':
            signs[i] = '𓍴'
        elif signs[i] == 'V7a':
            signs[i] = '𓍳'
        elif signs[i] == 'V7':
            signs[i] = '𓍲'
        elif signs[i] == 'V6':
            signs[i] = '𓍱'
        elif signs[i] == 'V5':
            signs[i] = '𓍰'
        elif signs[i] == 'V4':
            signs[i] = '𓍯'
        elif signs[i] == 'V3':
            signs[i] = '𓍮'
        elif signs[i] == 'V2a':
            signs[i] = '𓍭'
        elif signs[i] == 'V2':
            signs[i] = '𓍬'
        elif signs[i] == 'V1i':
            signs[i] = '𓍫'
        elif signs[i] == 'V1h':
            signs[i] = '𓍪'
        elif signs[i] == 'V1g':
            signs[i] = '𓍩'
        elif signs[i] == 'V1f':
            signs[i] = '𓍨'
        elif signs[i] == 'V1e':
            signs[i] = '𓍧'
        elif signs[i] == 'V1d':
            signs[i] = '𓍦'
        elif signs[i] == 'V1c':
            signs[i] = '𓍥'
        elif signs[i] == 'V1b':
            signs[i] = '𓍤'
        elif signs[i] == 'V1a':
            signs[i] = '𓍣'
        elif signs[i] == 'V1':
            signs[i] = '𓍢'
        elif signs[i] == 'U42':
            signs[i] = '𓍡'
        elif signs[i] == 'U41':
            signs[i] = '𓍠'
        elif signs[i] == 'U40':
            signs[i] = '𓍟'
        elif signs[i] == 'U39':
            signs[i] = '𓍞'
        elif signs[i] == 'U38':
            signs[i] = '𓍝'
        elif signs[i] == 'U37':
            signs[i] = '𓍜'
        elif signs[i] == 'U36':
            signs[i] = '𓍛'
        elif signs[i] == 'U35':
            signs[i] = '𓍚'
        elif signs[i] == 'U34':
            signs[i] = '𓍙'
        elif signs[i] == 'U33':
            signs[i] = '𓍘'
        elif signs[i] == 'U32a':
            signs[i] = '𓍗'
        elif signs[i] == 'U32':
            signs[i] = '𓍖'
        elif signs[i] == 'U31':
            signs[i] = '𓍕'
        elif signs[i] == 'U30':
            signs[i] = '𓍔'
        elif signs[i] == 'U29a':
            signs[i] = '𓍓'
        elif signs[i] == 'U29':
            signs[i] = '𓍒'
        elif signs[i] == 'U28':
            signs[i] = '𓍑'
        elif signs[i] == 'U27':
            signs[i] = '𓍐'
        elif signs[i] == 'U26':
            signs[i] = '𓍏'
        elif signs[i] == 'U25':
            signs[i] = '𓍎'
        elif signs[i] == 'U24':
            signs[i] = '𓍍'
        elif signs[i] == 'U23a':
            signs[i] = '𓍌'
        elif signs[i] == 'U23':
            signs[i] = '𓍋'
        elif signs[i] == 'U22':
            signs[i] = '𓍊'
        elif signs[i] == 'U21':
            signs[i] = '𓍉'
        elif signs[i] == 'U20':
            signs[i] = '𓍈'
        elif signs[i] == 'U19':
            signs[i] = '𓍇'
        elif signs[i] == 'U18':
            signs[i] = '𓍆'
        elif signs[i] == 'U17':
            signs[i] = '𓍅'
        elif signs[i] == 'U16':
            signs[i] = '𓍄'
        elif signs[i] == 'U15':
            signs[i] = '𓍃'
        elif signs[i] == 'U14':
            signs[i] = '𓍂'
        elif signs[i] == 'U13':
            signs[i] = '𓍁'
        elif signs[i] == 'U12':
            signs[i] = '𓍀'
        elif signs[i] == 'U11':
            signs[i] = '𓌿'
        elif signs[i] == 'U10':
            signs[i] = '𓌾'
        elif signs[i] == 'U9':
            signs[i] = '𓌽'
        elif signs[i] == 'U8':
            signs[i] = '𓌼'
        elif signs[i] == 'U7':
            signs[i] = '𓌻'
        elif signs[i] == 'U6b':
            signs[i] = '𓌺'
        elif signs[i] == 'U6a':
            signs[i] = '𓌹'
        elif signs[i] == 'U6':
            signs[i] = '𓌸'
        elif signs[i] == 'U5':
            signs[i] = '𓌷'
        elif signs[i] == 'U4':
            signs[i] = '𓌶'
        elif signs[i] == 'U3':
            signs[i] = '𓌵'
        elif signs[i] == 'U2':
            signs[i] = '𓌴'
        elif signs[i] == 'U1':
            signs[i] = '𓌳'
        elif signs[i] == 'T36':
            signs[i] = '𓌲'
        elif signs[i] == 'T35':
            signs[i] = '𓌱'
        elif signs[i] == 'T34':
            signs[i] = '𓌰'
        elif signs[i] == 'T33a':
            signs[i] = '𓌯'
        elif signs[i] == 'T33':
            signs[i] = '𓌮'
        elif signs[i] == 'T32a':
            signs[i] = '𓌭'
        elif signs[i] == 'T32':
            signs[i] = '𓌬'
        elif signs[i] == 'T31':
            signs[i] = '𓌫'
        elif signs[i] == 'T30':
            signs[i] = '𓌪'
        elif signs[i] == 'T29':
            signs[i] = '𓌩'
        elif signs[i] == 'T28':
            signs[i] = '𓌨'
        elif signs[i] == 'T27':
            signs[i] = '𓌧'
        elif signs[i] == 'T26':
            signs[i] = '𓌦'
        elif signs[i] == 'T25':
            signs[i] = '𓌥'
        elif signs[i] == 'T24':
            signs[i] = '𓌤'
        elif signs[i] == 'T23':
            signs[i] = '𓌣'
        elif signs[i] == 'T22':
            signs[i] = '𓌢'
        elif signs[i] == 'T21':
            signs[i] = '𓌡'
        elif signs[i] == 'T20':
            signs[i] = '𓌠'
        elif signs[i] == 'T19':
            signs[i] = '𓌟'
        elif signs[i] == 'T18':
            signs[i] = '𓌞'
        elif signs[i] == 'T17':
            signs[i] = '𓌝'
        elif signs[i] == 'T16a':
            signs[i] = '𓌜'
        elif signs[i] == 'T16':
            signs[i] = '𓌛'
        elif signs[i] == 'T15':
            signs[i] = '𓌚'
        elif signs[i] == 'T14':
            signs[i] = '𓌙'
        elif signs[i] == 'T13':
            signs[i] = '𓌘'
        elif signs[i] == 'T12':
            signs[i] = '𓌗'
        elif signs[i] == 'T11a':
            signs[i] = '𓌖'
        elif signs[i] == 'T11':
            signs[i] = '𓌕'
        elif signs[i] == 'T10':
            signs[i] = '𓌔'
        elif signs[i] == 'T9a':
            signs[i] = '𓌓'
        elif signs[i] == 'T9':
            signs[i] = '𓌒'
        elif signs[i] == 'T8a':
            signs[i] = '𓌑'
        elif signs[i] == 'T8':
            signs[i] = '𓌐'
        elif signs[i] == 'T7a':
            signs[i] = '𓌏'
        elif signs[i] == 'T7':
            signs[i] = '𓌎'
        elif signs[i] == 'T6':
            signs[i] = '𓌍'
        elif signs[i] == 'T5':
            signs[i] = '𓌌'
        elif signs[i] == 'T4':
            signs[i] = '𓌋'
        elif signs[i] == 'T3a':
            signs[i] = '𓌊'
        elif signs[i] == 'T3':
            signs[i] = '𓌉'
        elif signs[i] == 'T2':
            signs[i] = '𓌈'
        elif signs[i] == 'T1':
            signs[i] = '𓌇'
        elif signs[i] == 'S46':
            signs[i] = '𓌆'
        elif signs[i] == 'S45':
            signs[i] = '𓌅'
        elif signs[i] == 'S44':
            signs[i] = '𓌄'
        elif signs[i] == 'S43':
            signs[i] = '𓌃'
        elif signs[i] == 'S42':
            signs[i] = '𓌂'
        elif signs[i] == 'S41':
            signs[i] = '𓌁'
        elif signs[i] == 'S40':
            signs[i] = '𓌀'
        elif signs[i] == 'S39':
            signs[i] = '𓋿'
        elif signs[i] == 'S38':
            signs[i] = '𓋾'
        elif signs[i] == 'S37':
            signs[i] = '𓋽'
        elif signs[i] == 'S36':
            signs[i] = '𓋼'
        elif signs[i] == 'S35a':
            signs[i] = '𓋻'
        elif signs[i] == 'S35':
            signs[i] = '𓋺'
        elif signs[i] == 'S34':
            signs[i] = '𓋹'
        elif signs[i] == 'S33':
            signs[i] = '𓋸'
        elif signs[i] == 'S32':
            signs[i] = '𓋷'
        elif signs[i] == 'S31':
            signs[i] = '𓋶'
        elif signs[i] == 'S30':
            signs[i] = '𓋵'
        elif signs[i] == 'S29':
            signs[i] = '𓋴'
        elif signs[i] == 'S28':
            signs[i] = '𓋳'
        elif signs[i] == 'S27':
            signs[i] = '𓋲'
        elif signs[i] == 'S26b':
            signs[i] = '𓋱'
        elif signs[i] == 'S26a':
            signs[i] = '𓋰'
        elif signs[i] == 'S26':
            signs[i] = '𓋯'
        elif signs[i] == 'S25':
            signs[i] = '𓋮'
        elif signs[i] == 'S24':
            signs[i] = '𓋭'
        elif signs[i] == 'S23':
            signs[i] = '𓋬'
        elif signs[i] == 'S22':
            signs[i] = '𓋫'
        elif signs[i] == 'S21':
            signs[i] = '𓋪'
        elif signs[i] == 'S20':
            signs[i] = '𓋩'
        elif signs[i] == 'S19':
            signs[i] = '𓋨'
        elif signs[i] == 'S18':
            signs[i] = '𓋧'
        elif signs[i] == 'S17a':
            signs[i] = '𓋦'
        elif signs[i] == 'S17':
            signs[i] = '𓋥'
        elif signs[i] == 'S16':
            signs[i] = '𓋤'
        elif signs[i] == 'S15':
            signs[i] = '𓋣'
        elif signs[i] == 'S14b':
            signs[i] = '𓋢'
        elif signs[i] == 'S14a':
            signs[i] = '𓋡'
        elif signs[i] == 'S14':
            signs[i] = '𓋠'
        elif signs[i] == 'S13':
            signs[i] = '𓋟'
        elif signs[i] == 'S12':
            signs[i] = '𓋞'
        elif signs[i] == 'S11':
            signs[i] = '𓋝'
        elif signs[i] == 'S10':
            signs[i] = '𓋜'
        elif signs[i] == 'S9':
            signs[i] = '𓋛'
        elif signs[i] == 'S8':
            signs[i] = '𓋚'
        elif signs[i] == 'S7':
            signs[i] = '𓋙'
        elif signs[i] == 'S6a':
            signs[i] = '𓋘'
        elif signs[i] == 'S6':
            signs[i] = '𓋗'
        elif signs[i] == 'S5':
            signs[i] = '𓋖'
        elif signs[i] == 'S4':
            signs[i] = '𓋕'
        elif signs[i] == 'S3':
            signs[i] = '𓋔'
        elif signs[i] == 'S2a':
            signs[i] = '𓋓'
        elif signs[i] == 'S2':
            signs[i] = '𓋒'
        elif signs[i] == 'S1':
            signs[i] = '𓋑'
        elif signs[i] == 'R29':
            signs[i] = '𓋐'
        elif signs[i] == 'R28':
            signs[i] = '𓋏'
        elif signs[i] == 'R27':
            signs[i] = '𓋎'
        elif signs[i] == 'R26':
            signs[i] = '𓋍'
        elif signs[i] == 'R25':
            signs[i] = '𓋌'
        elif signs[i] == 'R24':
            signs[i] = '𓋋'
        elif signs[i] == 'R23':
            signs[i] = '𓋊'
        elif signs[i] == 'R22':
            signs[i] = '𓋉'
        elif signs[i] == 'R21':
            signs[i] = '𓋈'
        elif signs[i] == 'R20':
            signs[i] = '𓋇'
        elif signs[i] == 'R19':
            signs[i] = '𓋆'
        elif signs[i] == 'R18':
            signs[i] = '𓋅'
        elif signs[i] == 'R17':
            signs[i] = '𓋄'
        elif signs[i] == 'R16a':
            signs[i] = '𓋃'
        elif signs[i] == 'R16':
            signs[i] = '𓋂'
        elif signs[i] == 'R15':
            signs[i] = '𓋁'
        elif signs[i] == 'R14':
            signs[i] = '𓋀'
        elif signs[i] == 'R13':
            signs[i] = '𓊿'
        elif signs[i] == 'R12':
            signs[i] = '𓊾'
        elif signs[i] == 'R11':
            signs[i] = '𓊽'
        elif signs[i] == 'R10a':
            signs[i] = '𓊼'
        elif signs[i] == 'R10':
            signs[i] = '𓊻'
        elif signs[i] == 'R9':
            signs[i] = '𓊺'
        elif signs[i] == 'R8':
            signs[i] = '𓊹'
        elif signs[i] == 'R7':
            signs[i] = '𓊸'
        elif signs[i] == 'R6':
            signs[i] = '𓊷'
        elif signs[i] == 'R5':
            signs[i] = '𓊶'
        elif signs[i] == 'R4':
            signs[i] = '𓊵'
        elif signs[i] == 'R3b':
            signs[i] = '𓊴'
        elif signs[i] == 'R3a':
            signs[i] = '𓊳'
        elif signs[i] == 'R3':
            signs[i] = '𓊲'
        elif signs[i] == 'R2a':
            signs[i] = '𓊱'
        elif signs[i] == 'R2':
            signs[i] = '𓊰'
        elif signs[i] == 'R1':
            signs[i] = '𓊯'
        elif signs[i] == 'Q7':
            signs[i] = '𓊮'
        elif signs[i] == 'Q6':
            signs[i] = '𓊭'
        elif signs[i] == 'Q5':
            signs[i] = '𓊬'
        elif signs[i] == 'Q4':
            signs[i] = '𓊫'
        elif signs[i] == 'Q3':
            signs[i] = '𓊪'
        elif signs[i] == 'Q2':
            signs[i] = '𓊩'
        elif signs[i] == 'Q1':
            signs[i] = '𓊨'
        elif signs[i] == 'P11':
            signs[i] = '𓊧'
        elif signs[i] == 'P10':
            signs[i] = '𓊦'
        elif signs[i] == 'P9':
            signs[i] = '𓊥'
        elif signs[i] == 'P8':
            signs[i] = '𓊤'
        elif signs[i] == 'P7':
            signs[i] = '𓊣'
        elif signs[i] == 'P6':
            signs[i] = '𓊢'
        elif signs[i] == 'P5':
            signs[i] = '𓊡'
        elif signs[i] == 'P4':
            signs[i] = '𓊠'
        elif signs[i] == 'P3a':
            signs[i] = '𓊟'
        elif signs[i] == 'P3':
            signs[i] = '𓊞'
        elif signs[i] == 'P2':
            signs[i] = '𓊝'
        elif signs[i] == 'P1a':
            signs[i] = '𓊜'
        elif signs[i] == 'P1':
            signs[i] = '𓊛'
        elif signs[i] == 'O51':
            signs[i] = '𓊚'
        elif signs[i] == 'O5b':
            signs[i] = '𓊙'
        elif signs[i] == 'O5a':
            signs[i] = '𓊘'
        elif signs[i] == 'O50':
            signs[i] = '𓊗'
        elif signs[i] == 'O49':
            signs[i] = '𓊖'
        elif signs[i] == 'O48':
            signs[i] = '𓊕'
        elif signs[i] == 'O47':
            signs[i] = '𓊔'
        elif signs[i] == 'O46':
            signs[i] = '𓊓'
        elif signs[i] == 'O45':
            signs[i] = '𓊒'
        elif signs[i] == 'O44':
            signs[i] = '𓊑'
        elif signs[i] == 'O43':
            signs[i] = '𓊐'
        elif signs[i] == 'O42':
            signs[i] = '𓊏'
        elif signs[i] == 'O41':
            signs[i] = '𓊎'
        elif signs[i] == 'O40':
            signs[i] = '𓊍'
        elif signs[i] == 'O39':
            signs[i] = '𓊌'
        elif signs[i] == 'O38':
            signs[i] = '𓊋'
        elif signs[i] == 'O37':
            signs[i] = '𓊊'
        elif signs[i] == 'O36d':
            signs[i] = '𓊉'
        elif signs[i] == 'O36c':
            signs[i] = '𓊈'
        elif signs[i] == 'O36b':
            signs[i] = '𓊇'
        elif signs[i] == 'O36a':
            signs[i] = '𓊆'
        elif signs[i] == 'O36':
            signs[i] = '𓊅'
        elif signs[i] == 'O35':
            signs[i] = '𓊄'
        elif signs[i] == 'O34':
            signs[i] = '𓊃'
        elif signs[i] == 'O33a':
            signs[i] = '𓊂'
        elif signs[i] == 'O33':
            signs[i] = '𓊁'
        elif signs[i] == 'O32':
            signs[i] = '𓊀'
        elif signs[i] == 'O31':
            signs[i] = '𓉿'
        elif signs[i] == 'O3a':
            signs[i] = '𓉾'
        elif signs[i] == 'O30':
            signs[i] = '𓉽'
        elif signs[i] == 'O29a':
            signs[i] = '𓉼'
        elif signs[i] == 'O29':
            signs[i] = '𓉻'
        elif signs[i] == 'O28':
            signs[i] = '𓉺'
        elif signs[i] == 'O27':
            signs[i] = '𓉹'
        elif signs[i] == 'O26':
            signs[i] = '𓉸'
        elif signs[i] == 'O25a':
            signs[i] = '𓉷'
        elif signs[i] == 'O25':
            signs[i] = '𓉶'
        elif signs[i] == 'O24a':
            signs[i] = '𓉵'
        elif signs[i] == 'O24':
            signs[i] = '𓉴'
        elif signs[i] == 'O23':
            signs[i] = '𓉳'
        elif signs[i] == 'O22':
            signs[i] = '𓉲'
        elif signs[i] == 'O21':
            signs[i] = '𓉱'
        elif signs[i] == 'O2a':
            signs[i] = '𓉰'
        elif signs[i] == 'O20':
            signs[i] = '𓉯'
        elif signs[i] == 'O19a':
            signs[i] = '𓉮'
        elif signs[i] == 'O19':
            signs[i] = '𓉭'
        elif signs[i] == 'O18':
            signs[i] = '𓉬'
        elif signs[i] == 'O17':
            signs[i] = '𓉫'
        elif signs[i] == 'O16':
            signs[i] = '𓉪'
        elif signs[i] == 'O15':
            signs[i] = '𓉩'
        elif signs[i] == 'O14':
            signs[i] = '𓉨'
        elif signs[i] == 'O13':
            signs[i] = '𓉧'
        elif signs[i] == 'O12':
            signs[i] = '𓉦'
        elif signs[i] == 'O11':
            signs[i] = '𓉥'
        elif signs[i] == 'O10c':
            signs[i] = '𓉤'
        elif signs[i] == 'O10b':
            signs[i] = '𓉣'
        elif signs[i] == 'O10a':
            signs[i] = '𓉢'
        elif signs[i] == 'O10':
            signs[i] = '𓉡'
        elif signs[i] == 'O9':
            signs[i] = '𓉠'
        elif signs[i] == 'O8':
            signs[i] = '𓉟'
        elif signs[i] == 'O7':
            signs[i] = '𓉞'
        elif signs[i] == 'O6f':
            signs[i] = '𓉝'
        elif signs[i] == 'O6e':
            signs[i] = '𓉜'
        elif signs[i] == 'O6d':
            signs[i] = '𓉛'
        elif signs[i] == 'O6c':
            signs[i] = '𓉚'
        elif signs[i] == 'O6b':
            signs[i] = '𓉙'
        elif signs[i] == 'O6a':
            signs[i] = '𓉘'
        elif signs[i] == 'O6':
            signs[i] = '𓉗'
        elif signs[i] == 'O5a':
            signs[i] = '𓉖'
        elif signs[i] == 'O5':
            signs[i] = '𓉕'
        elif signs[i] == 'O4':
            signs[i] = '𓉔'
        elif signs[i] == 'O3':
            signs[i] = '𓉓'
        elif signs[i] == 'O2':
            signs[i] = '𓉒'
        elif signs[i] == 'O1a':
            signs[i] = '𓉑'
        elif signs[i] == 'O1':
            signs[i] = '𓉐'
        elif signs[i] == 'NU22a':
            signs[i] = '𓉏'
        elif signs[i] == 'NU22':
            signs[i] = '𓉎'
        elif signs[i] == 'NU21':
            signs[i] = '𓉍'
        elif signs[i] == 'NU20':
            signs[i] = '𓉌'
        elif signs[i] == 'NU19':
            signs[i] = '𓉋'
        elif signs[i] == 'NU18a':
            signs[i] = '𓉊'
        elif signs[i] == 'NU18':
            signs[i] = '𓉉'
        elif signs[i] == 'NU17':
            signs[i] = '𓉈'
        elif signs[i] == 'NU16':
            signs[i] = '𓉇'
        elif signs[i] == 'NU15':
            signs[i] = '𓉆'
        elif signs[i] == 'NU14':
            signs[i] = '𓉅'
        elif signs[i] == 'NU13':
            signs[i] = '𓉄'
        elif signs[i] == 'NU12':
            signs[i] = '𓉃'
        elif signs[i] == 'NU11a':
            signs[i] = '𓉂'
        elif signs[i] == 'NU11':
            signs[i] = '𓉁'
        elif signs[i] == 'NU1a':
            signs[i] = '𓉀'
        elif signs[i] == 'NU10':
            signs[i] = '𓈿'
        elif signs[i] == 'NU9':
            signs[i] = '𓈾'
        elif signs[i] == 'NU8':
            signs[i] = '𓈽'
        elif signs[i] == 'NU7':
            signs[i] = '𓈼'
        elif signs[i] == 'NU6':
            signs[i] = '𓈻'
        elif signs[i] == 'NU5':
            signs[i] = '𓈺'
        elif signs[i] == 'NU4':
            signs[i] = '𓈹'
        elif signs[i] == 'NU3':
            signs[i] = '𓈸'
        elif signs[i] == 'NU2':
            signs[i] = '𓈷'
        elif signs[i] == 'NU1':
            signs[i] = '𓈶'
        elif signs[i] == 'NL20':
            signs[i] = '𓈵'
        elif signs[i] == 'NL19':
            signs[i] = '𓈴'
        elif signs[i] == 'NL18':
            signs[i] = '𓈳'
        elif signs[i] == 'NL17a':
            signs[i] = '𓈲'
        elif signs[i] == 'NL17':
            signs[i] = '𓈱'
        elif signs[i] == 'NL16':
            signs[i] = '𓈰'
        elif signs[i] == 'NL15':
            signs[i] = '𓈯'
        elif signs[i] == 'NL14':
            signs[i] = '𓈮'
        elif signs[i] == 'NL13':
            signs[i] = '𓈭'
        elif signs[i] == 'NL12':
            signs[i] = '𓈬'
        elif signs[i] == 'NL11':
            signs[i] = '𓈫'
        elif signs[i] == 'NL10':
            signs[i] = '𓈪'
        elif signs[i] == 'NL9':
            signs[i] = '𓈩'
        elif signs[i] == 'NL8':
            signs[i] = '𓈨'
        elif signs[i] == 'NL7':
            signs[i] = '𓈧'
        elif signs[i] == 'NL6':
            signs[i] = '𓈦'
        elif signs[i] == 'NL5a':
            signs[i] = '𓈥'
        elif signs[i] == 'NL5':
            signs[i] = '𓈤'
        elif signs[i] == 'NL4':
            signs[i] = '𓈣'
        elif signs[i] == 'NL3':
            signs[i] = '𓈢'
        elif signs[i] == 'NL2':
            signs[i] = '𓈡'
        elif signs[i] == 'NL1':
            signs[i] = '𓈠'
        elif signs[i] == 'N42':
            signs[i] = '𓈟'
        elif signs[i] == 'N41':
            signs[i] = '𓈞'
        elif signs[i] == 'N40':
            signs[i] = '𓈝'
        elif signs[i] == 'N39':
            signs[i] = '𓈜'
        elif signs[i] == 'N38':
            signs[i] = '𓈛'
        elif signs[i] == 'N37a':
            signs[i] = '𓈚'
        elif signs[i] == 'N37':
            signs[i] = '𓈙'
        elif signs[i] == 'N36':
            signs[i] = '𓈘'
        elif signs[i] == 'N35a':
            signs[i] = '𓈗'
        elif signs[i] == 'N35':
            signs[i] = '𓈖'
        elif signs[i] == 'N34a':
            signs[i] = '𓈕'
        elif signs[i] == 'N34':
            signs[i] = '𓈔'
        elif signs[i] == 'N33a':
            signs[i] = '𓈓'
        elif signs[i] == 'N33':
            signs[i] = '𓈒'
        elif signs[i] == 'N32':
            signs[i] = '𓈑'
        elif signs[i] == 'N31':
            signs[i] = '𓈐'
        elif signs[i] == 'N30':
            signs[i] = '𓈏'
        elif signs[i] == 'N29':
            signs[i] = '𓈎'
        elif signs[i] == 'N28':
            signs[i] = '𓈍'
        elif signs[i] == 'N27':
            signs[i] = '𓈌'
        elif signs[i] == 'N26':
            signs[i] = '𓈋'
        elif signs[i] == 'N25a':
            signs[i] = '𓈊'
        elif signs[i] == 'N25':
            signs[i] = '𓈉'
        elif signs[i] == 'N24':
            signs[i] = '𓈈'
        elif signs[i] == 'N23':
            signs[i] = '𓈇'
        elif signs[i] == 'N22':
            signs[i] = '𓈆'
        elif signs[i] == 'N21':
            signs[i] = '𓈅'
        elif signs[i] == 'N20':
            signs[i] = '𓈄'
        elif signs[i] == 'N19':
            signs[i] = '𓈃'
        elif signs[i] == 'N18b':
            signs[i] = '𓈂'
        elif signs[i] == 'N18a':
            signs[i] = '𓈁'
        elif signs[i] == 'N18':
            signs[i] = '𓈀'
        elif signs[i] == 'N17':
            signs[i] = '𓇿'
        elif signs[i] == 'N16':
            signs[i] = '𓇾'
        elif signs[i] == 'N15':
            signs[i] = '𓇽'
        elif signs[i] == 'N14':
            signs[i] = '𓇼'
        elif signs[i] == 'N13':
            signs[i] = '𓇻'
        elif signs[i] == 'N12':
            signs[i] = '𓇺'
        elif signs[i] == 'N11':
            signs[i] = '𓇹'
        elif signs[i] == 'N10':
            signs[i] = '𓇸'
        elif signs[i] == 'N9':
            signs[i] = '𓇷'
        elif signs[i] == 'N8':
            signs[i] = '𓇶'
        elif signs[i] == 'N7':
            signs[i] = '𓇵'
        elif signs[i] == 'N6':
            signs[i] = '𓇴'
        elif signs[i] == 'N5':
            signs[i] = '𓇳'
        elif signs[i] == 'N4':
            signs[i] = '𓇲'
        elif signs[i] == 'N3':
            signs[i] = '𓇱'
        elif signs[i] == 'N2':
            signs[i] = '𓇰'
        elif signs[i] == 'N1':
            signs[i] = '𓇯'
        elif signs[i] == 'M44':
            signs[i] = '𓇮'
        elif signs[i] == 'M43':
            signs[i] = '𓇭'
        elif signs[i] == 'M42':
            signs[i] = '𓇬'
        elif signs[i] == 'M41':
            signs[i] = '𓇫'
        elif signs[i] == 'M40a':
            signs[i] = '𓇪'
        elif signs[i] == 'M40':
            signs[i] = '𓇩'
        elif signs[i] == 'M39':
            signs[i] = '𓇨'
        elif signs[i] == 'M38':
            signs[i] = '𓇧'
        elif signs[i] == 'M37':
            signs[i] = '𓇦'
        elif signs[i] == 'M36':
            signs[i] = '𓇥'
        elif signs[i] == 'M35':
            signs[i] = '𓇤'
        elif signs[i] == 'M34':
            signs[i] = '𓇣'
        elif signs[i] == 'M33b':
            signs[i] = '𓇢'
        elif signs[i] == 'M33a':
            signs[i] = '𓇡'
        elif signs[i] == 'M33':
            signs[i] = '𓇠'
        elif signs[i] == 'M32':
            signs[i] = '𓇟'
        elif signs[i] == 'M31a':
            signs[i] = '𓇞'
        elif signs[i] == 'M31':
            signs[i] = '𓇝'
        elif signs[i] == 'M30':
            signs[i] = '𓇜'
        elif signs[i] == 'M29':
            signs[i] = '𓇛'
        elif signs[i] == 'M28a':
            signs[i] = '𓇚'
        elif signs[i] == 'M28':
            signs[i] = '𓇙'
        elif signs[i] == 'M27':
            signs[i] = '𓇘'
        elif signs[i] == 'M26':
            signs[i] = '𓇗'
        elif signs[i] == 'M25':
            signs[i] = '𓇖'
        elif signs[i] == 'M24a':
            signs[i] = '𓇕'
        elif signs[i] == 'M24':
            signs[i] = '𓇔'
        elif signs[i] == 'M23':
            signs[i] = '𓇓'
        elif signs[i] == 'M22a':
            signs[i] = '𓇒'
        elif signs[i] == 'M22':
            signs[i] = '𓇑'
        elif signs[i] == 'M21':
            signs[i] = '𓇐'
        elif signs[i] == 'M20':
            signs[i] = '𓇏'
        elif signs[i] == 'M19':
            signs[i] = '𓇎'
        elif signs[i] == 'M18':
            signs[i] = '𓇍'
        elif signs[i] == 'M17a':
            signs[i] = '𓇌'
        elif signs[i] == 'M17':
            signs[i] = '𓇋'
        elif signs[i] == 'M16a':
            signs[i] = '𓇊'
        elif signs[i] == 'M16':
            signs[i] = '𓇉'
        elif signs[i] == 'M15a':
            signs[i] = '𓇈'
        elif signs[i] == 'M15':
            signs[i] = '𓇇'
        elif signs[i] == 'M14':
            signs[i] = '𓇆'
        elif signs[i] == 'M13':
            signs[i] = '𓇅'
        elif signs[i] == 'M12h':
            signs[i] = '𓇄'
        elif signs[i] == 'M12g':
            signs[i] = '𓇃'
        elif signs[i] == 'M12f':
            signs[i] = '𓇂'
        elif signs[i] == 'M12e':
            signs[i] = '𓇁'
        elif signs[i] == 'M12d':
            signs[i] = '𓇀'
        elif signs[i] == 'M12c':
            signs[i] = '𓆿'
        elif signs[i] == 'M12b':
            signs[i] = '𓆾'
        elif signs[i] == 'M12a':
            signs[i] = '𓆽'
        elif signs[i] == 'M12':
            signs[i] = '𓆼'
        elif signs[i] == 'M11':
            signs[i] = '𓆻'
        elif signs[i] == 'M10a':
            signs[i] = '𓆺'
        elif signs[i] == 'M10':
            signs[i] = '𓆹'
        elif signs[i] == 'M9':
            signs[i] = '𓆸'
        elif signs[i] == 'M8':
            signs[i] = '𓆷'
        elif signs[i] == 'M7':
            signs[i] = '𓆶'
        elif signs[i] == 'M6':
            signs[i] = '𓆵'
        elif signs[i] == 'M5':
            signs[i] = '𓆴'
        elif signs[i] == 'M4':
            signs[i] = '𓆳'
        elif signs[i] == 'M3a':
            signs[i] = '𓆲'
        elif signs[i] == 'M3':
            signs[i] = '𓆱'
        elif signs[i] == 'M2':
            signs[i] = '𓆰'
        elif signs[i] == 'M1b':
            signs[i] = '𓆯'
        elif signs[i] == 'M1a':
            signs[i] = '𓆮'
        elif signs[i] == 'M1':
            signs[i] = '𓆭'
        elif signs[i] == 'L8':
            signs[i] = '𓆬'
        elif signs[i] == 'L7':
            signs[i] = '𓆫'
        elif signs[i] == 'L6a':
            signs[i] = '𓆪'
        elif signs[i] == 'L6':
            signs[i] = '𓆩'
        elif signs[i] == 'L5':
            signs[i] = '𓆨'
        elif signs[i] == 'L4':
            signs[i] = '𓆧'
        elif signs[i] == 'L3':
            signs[i] = '𓆦'
        elif signs[i] == 'L2a':
            signs[i] = '𓆥'
        elif signs[i] == 'L2':
            signs[i] = '𓆤'
        elif signs[i] == 'L1':
            signs[i] = '𓆣'
        elif signs[i] == 'K8':
            signs[i] = '𓆢'
        elif signs[i] == 'K7':
            signs[i] = '𓆡'
        elif signs[i] == 'K6':
            signs[i] = '𓆠'
        elif signs[i] == 'K5':
            signs[i] = '𓆟'
        elif signs[i] == 'K4':
            signs[i] = '𓆞'
        elif signs[i] == 'K3':
            signs[i] = '𓆝'
        elif signs[i] == 'K2':
            signs[i] = '𓆜'
        elif signs[i] == 'K1':
            signs[i] = '𓆛'
        elif signs[i] == 'I15':
            signs[i] = '𓆚'
        elif signs[i] == 'I14':
            signs[i] = '𓆙'
        elif signs[i] == 'I13':
            signs[i] = '𓆘'
        elif signs[i] == 'I12':
            signs[i] = '𓆗'
        elif signs[i] == 'I11a':
            signs[i] = '𓆖'
        elif signs[i] == 'I11':
            signs[i] = '𓆕'
        elif signs[i] == 'I1a':
            signs[i] = '𓆔'
        elif signs[i] == 'I10':
            signs[i] = '𓆓'
        elif signs[i] == 'I9a':
            signs[i] = '𓆒'
        elif signs[i] == 'I9':
            signs[i] = '𓆑'
        elif signs[i] == 'I8':
            signs[i] = '𓆐'
        elif signs[i] == 'I7':
            signs[i] = '𓆏'
        elif signs[i] == 'I6':
            signs[i] = '𓆎'
        elif signs[i] == 'I5a':
            signs[i] = '𓆍'
        elif signs[i] == 'I5':
            signs[i] = '𓆌'
        elif signs[i] == 'I4':
            signs[i] = '𓆋'
        elif signs[i] == 'I3':
            signs[i] = '𓆊'
        elif signs[i] == 'I2':
            signs[i] = '𓆉'
        elif signs[i] == 'I1':
            signs[i] = '𓆈'
        elif signs[i] == 'H8':
            signs[i] = '𓆇'
        elif signs[i] == 'H7':
            signs[i] = '𓆆'
        elif signs[i] == 'H6a':
            signs[i] = '𓆅'
        elif signs[i] == 'H6':
            signs[i] = '𓆄'
        elif signs[i] == 'H5':
            signs[i] = '𓆃'
        elif signs[i] == 'H4':
            signs[i] = '𓆂'
        elif signs[i] == 'H3':
            signs[i] = '𓆁'
        elif signs[i] == 'H2':
            signs[i] = '𓆀'
        elif signs[i] == 'H1':
            signs[i] = '𓅿'
        elif signs[i] == 'G54':
            signs[i] = '𓅾'
        elif signs[i] == 'G53':
            signs[i] = '𓅽'
        elif signs[i] == 'G52':
            signs[i] = '𓅼'
        elif signs[i] == 'G51':
            signs[i] = '𓅻'
        elif signs[i] == 'G50':
            signs[i] = '𓅺'
        elif signs[i] == 'G49':
            signs[i] = '𓅹'
        elif signs[i] == 'G48':
            signs[i] = '𓅸'
        elif signs[i] == 'G47':
            signs[i] = '𓅷'
        elif signs[i] == 'G46':
            signs[i] = '𓅶'
        elif signs[i] == 'G45a':
            signs[i] = '𓅵'
        elif signs[i] == 'G45':
            signs[i] = '𓅴'
        elif signs[i] == 'G44':
            signs[i] = '𓅳'
        elif signs[i] == 'G43a':
            signs[i] = '𓅲'
        elif signs[i] == 'G43':
            signs[i] = '𓅱'
        elif signs[i] == 'G42':
            signs[i] = '𓅰'
        elif signs[i] == 'G41':
            signs[i] = '𓅯'
        elif signs[i] == 'G40':
            signs[i] = '𓅮'
        elif signs[i] == 'G39':
            signs[i] = '𓅭'
        elif signs[i] == 'G38':
            signs[i] = '𓅬'
        elif signs[i] == 'G37a':
            signs[i] = '𓅫'
        elif signs[i] == 'G37':
            signs[i] = '𓅪'
        elif signs[i] == 'G36a':
            signs[i] = '𓅩'
        elif signs[i] == 'G36':
            signs[i] = '𓅨'
        elif signs[i] == 'G35':
            signs[i] = '𓅧'
        elif signs[i] == 'G34':
            signs[i] = '𓅦'
        elif signs[i] == 'G33':
            signs[i] = '𓅥'
        elif signs[i] == 'G32':
            signs[i] = '𓅤'
        elif signs[i] == 'G31':
            signs[i] = '𓅣'
        elif signs[i] == 'G30':
            signs[i] = '𓅢'
        elif signs[i] == 'G29':
            signs[i] = '𓅡'
        elif signs[i] == 'G28':
            signs[i] = '𓅠'
        elif signs[i] == 'G27':
            signs[i] = '𓅟'
        elif signs[i] == 'G26a':
            signs[i] = '𓅞'
        elif signs[i] == 'G26':
            signs[i] = '𓅝'
        elif signs[i] == 'G25':
            signs[i] = '𓅜'
        elif signs[i] == 'G24':
            signs[i] = '𓅛'
        elif signs[i] == 'G23':
            signs[i] = '𓅚'
        elif signs[i] == 'G22':
            signs[i] = '𓅙'
        elif signs[i] == 'G21':
            signs[i] = '𓅘'
        elif signs[i] == 'G20a':
            signs[i] = '𓅗'
        elif signs[i] == 'G20':
            signs[i] = '𓅖'
        elif signs[i] == 'G19':
            signs[i] = '𓅕'
        elif signs[i] == 'G18':
            signs[i] = '𓅔'
        elif signs[i] == 'G17':
            signs[i] = '𓅓'
        elif signs[i] == 'G16':
            signs[i] = '𓅒'
        elif signs[i] == 'G15':
            signs[i] = '𓅑'
        elif signs[i] == 'G14':
            signs[i] = '𓅐'
        elif signs[i] == 'G13':
            signs[i] = '𓅏'
        elif signs[i] == 'G12':
            signs[i] = '𓅎'
        elif signs[i] == 'G11a':
            signs[i] = '𓅍'
        elif signs[i] == 'G11':
            signs[i] = '𓅌'
        elif signs[i] == 'G10':
            signs[i] = '𓅋'
        elif signs[i] == 'G9':
            signs[i] = '𓅊'
        elif signs[i] == 'G8':
            signs[i] = '𓅉'
        elif signs[i] == 'G7b':
            signs[i] = '𓅈'
        elif signs[i] == 'G7a':
            signs[i] = '𓅇'
        elif signs[i] == 'G7':
            signs[i] = '𓅆'
        elif signs[i] == 'G6a':
            signs[i] = '𓅅'
        elif signs[i] == 'G6':
            signs[i] = '𓅄'
        elif signs[i] == 'G5':
            signs[i] = '𓅃'
        elif signs[i] == 'G4':
            signs[i] = '𓅂'
        elif signs[i] == 'G3':
            signs[i] = '𓅁'
        elif signs[i] == 'G2':
            signs[i] = '𓅀'
        elif signs[i] == 'G1':
            signs[i] = '𓄿'
        elif signs[i] == 'F53':
            signs[i] = '𓄾'
        elif signs[i] == 'F52':
            signs[i] = '𓄽'
        elif signs[i] == 'F51c':
            signs[i] = '𓄼'
        elif signs[i] == 'F51b':
            signs[i] = '𓄻'
        elif signs[i] == 'F51a':
            signs[i] = '𓄺'
        elif signs[i] == 'F51':
            signs[i] = '𓄹'
        elif signs[i] == 'F50':
            signs[i] = '𓄸'
        elif signs[i] == 'F49':
            signs[i] = '𓄷'
        elif signs[i] == 'F48':
            signs[i] = '𓄶'
        elif signs[i] == 'F47a':
            signs[i] = '𓄵'
        elif signs[i] == 'F47':
            signs[i] = '𓄴'
        elif signs[i] == 'F46a':
            signs[i] = '𓄳'
        elif signs[i] == 'F46':
            signs[i] = '𓄲'
        elif signs[i] == 'F45a':
            signs[i] = '𓄱'
        elif signs[i] == 'F45':
            signs[i] = '𓄰'
        elif signs[i] == 'F44':
            signs[i] = '𓄯'
        elif signs[i] == 'F43':
            signs[i] = '𓄮'
        elif signs[i] == 'F42':
            signs[i] = '𓄭'
        elif signs[i] == 'F41':
            signs[i] = '𓄬'
        elif signs[i] == 'F40':
            signs[i] = '𓄫'
        elif signs[i] == 'F39':
            signs[i] = '𓄪'
        elif signs[i] == 'F38a':
            signs[i] = '𓄩'
        elif signs[i] == 'F38':
            signs[i] = '𓄨'
        elif signs[i] == 'F37a':
            signs[i] = '𓄧'
        elif signs[i] == 'F37':
            signs[i] = '𓄦'
        elif signs[i] == 'F36':
            signs[i] = '𓄥'
        elif signs[i] == 'F35':
            signs[i] = '𓄤'
        elif signs[i] == 'F34':
            signs[i] = '𓄣'
        elif signs[i] == 'F33':
            signs[i] = '𓄢'
        elif signs[i] == 'F32':
            signs[i] = '𓄡'
        elif signs[i] == 'F31a':
            signs[i] = '𓄠'
        elif signs[i] == 'F31':
            signs[i] = '𓄟'
        elif signs[i] == 'F30':
            signs[i] = '𓄞'
        elif signs[i] == 'F29':
            signs[i] = '𓄝'
        elif signs[i] == 'F28':
            signs[i] = '𓄜'
        elif signs[i] == 'F27':
            signs[i] = '𓄛'
        elif signs[i] == 'F26':
            signs[i] = '𓄚'
        elif signs[i] == 'F25':
            signs[i] = '𓄙'
        elif signs[i] == 'F24':
            signs[i] = '𓄘'
        elif signs[i] == 'F23':
            signs[i] = '𓄗'
        elif signs[i] == 'F22':
            signs[i] = '𓄖'
        elif signs[i] == 'F21a':
            signs[i] = '𓄕'
        elif signs[i] == 'F21':
            signs[i] = '𓄔'
        elif signs[i] == 'F20':
            signs[i] = '𓄓'
        elif signs[i] == 'F19':
            signs[i] = '𓄒'
        elif signs[i] == 'F18':
            signs[i] = '𓄑'
        elif signs[i] == 'F17':
            signs[i] = '𓄐'
        elif signs[i] == 'F16':
            signs[i] = '𓄏'
        elif signs[i] == 'F15':
            signs[i] = '𓄎'
        elif signs[i] == 'F14':
            signs[i] = '𓄍'
        elif signs[i] == 'F13a':
            signs[i] = '𓄌'
        elif signs[i] == 'F13':
            signs[i] = '𓄋'
        elif signs[i] == 'F12':
            signs[i] = '𓄊'
        elif signs[i] == 'F11':
            signs[i] = '𓄉'
        elif signs[i] == 'F10':
            signs[i] = '𓄈'
        elif signs[i] == 'F9':
            signs[i] = '𓄇'
        elif signs[i] == 'F8':
            signs[i] = '𓄆'
        elif signs[i] == 'F7':
            signs[i] = '𓄅'
        elif signs[i] == 'F6':
            signs[i] = '𓄄'
        elif signs[i] == 'F5':
            signs[i] = '𓄃'
        elif signs[i] == 'F4':
            signs[i] = '𓄂'
        elif signs[i] == 'F3':
            signs[i] = '𓄁'
        elif signs[i] == 'F2':
            signs[i] = '𓄀'
        elif signs[i] == 'F1a':
            signs[i] = '𓃿'
        elif signs[i] == 'F1':
            signs[i] = '𓃾'
        elif signs[i] == 'E38':
            signs[i] = '𓃽'
        elif signs[i] == 'E37':
            signs[i] = '𓃼'
        elif signs[i] == 'E36':
            signs[i] = '𓃻'
        elif signs[i] == 'E34a':
            signs[i] = '𓃺'
        elif signs[i] == 'E34':
            signs[i] = '𓃹'
        elif signs[i] == 'E33':
            signs[i] = '𓃸'
        elif signs[i] == 'E32':
            signs[i] = '𓃷'
        elif signs[i] == 'E31':
            signs[i] = '𓃶'
        elif signs[i] == 'E30':
            signs[i] = '𓃵'
        elif signs[i] == 'E29':
            signs[i] = '𓃴'
        elif signs[i] == 'E28a':
            signs[i] = '𓃳'
        elif signs[i] == 'E28':
            signs[i] = '𓃲'
        elif signs[i] == 'E27':
            signs[i] = '𓃱'
        elif signs[i] == 'E26':
            signs[i] = '𓃰'
        elif signs[i] == 'E25':
            signs[i] = '𓃯'
        elif signs[i] == 'E24':
            signs[i] = '𓃮'
        elif signs[i] == 'E23':
            signs[i] = '𓃭'
        elif signs[i] == 'E22':
            signs[i] = '𓃬'
        elif signs[i] == 'E21':
            signs[i] = '𓃫'
        elif signs[i] == 'E2a':
            signs[i] = '𓃪'
        elif signs[i] == 'E20':
            signs[i] = '𓃩'
        elif signs[i] == 'E19':
            signs[i] = '𓃨'
        elif signs[i] == 'E18':
            signs[i] = '𓃧'
        elif signs[i] == 'E17a':
            signs[i] = '𓃦'
        elif signs[i] == 'E17':
            signs[i] = '𓃥'
        elif signs[i] == 'E16a':
            signs[i] = '𓃤'
        elif signs[i] == 'E16':
            signs[i] = '𓃣'
        elif signs[i] == 'E15':
            signs[i] = '𓃢'
        elif signs[i] == 'E14':
            signs[i] = '𓃡'
        elif signs[i] == 'E13':
            signs[i] = '𓃠'
        elif signs[i] == 'E12':
            signs[i] = '𓃟'
        elif signs[i] == 'E11':
            signs[i] = '𓃞'
        elif signs[i] == 'E10':
            signs[i] = '𓃝'
        elif signs[i] == 'E9a':
            signs[i] = '𓃜'
        elif signs[i] == 'E9':
            signs[i] = '𓃛'
        elif signs[i] == 'E8a':
            signs[i] = '𓃚'
        elif signs[i] == 'E8':
            signs[i] = '𓃙'
        elif signs[i] == 'E7':
            signs[i] = '𓃘'
        elif signs[i] == 'E6':
            signs[i] = '𓃗'
        elif signs[i] == 'E5':
            signs[i] = '𓃖'
        elif signs[i] == 'E4':
            signs[i] = '𓃕'
        elif signs[i] == 'E3':
            signs[i] = '𓃔'
        elif signs[i] == 'E2':
            signs[i] = '𓃓'
        elif signs[i] == 'E1':
            signs[i] = '𓃒'
        elif signs[i] == 'D67h':
            signs[i] = '𓃑'
        elif signs[i] == 'D67g':
            signs[i] = '𓃐'
        elif signs[i] == 'D67f':
            signs[i] = '𓃏'
        elif signs[i] == 'D67e':
            signs[i] = '𓃎'
        elif signs[i] == 'D67d':
            signs[i] = '𓃍'
        elif signs[i] == 'D67c':
            signs[i] = '𓃌'
        elif signs[i] == 'D67b':
            signs[i] = '𓃋'
        elif signs[i] == 'D67a':
            signs[i] = '𓃊'
        elif signs[i] == 'D67':
            signs[i] = '𓃉'
        elif signs[i] == 'D66':
            signs[i] = '𓃈'
        elif signs[i] == 'D65':
            signs[i] = '𓃇'
        elif signs[i] == 'D64':
            signs[i] = '𓃆'
        elif signs[i] == 'D63':
            signs[i] = '𓃅'
        elif signs[i] == 'D62':
            signs[i] = '𓃄'
        elif signs[i] == 'D61':
            signs[i] = '𓃃'
        elif signs[i] == 'D60':
            signs[i] = '𓃂'
        elif signs[i] == 'D59':
            signs[i] = '𓃁'
        elif signs[i] == 'D58':
            signs[i] = '𓃀'
        elif signs[i] == 'D57':
            signs[i] = '𓂿'
        elif signs[i] == 'D56':
            signs[i] = '𓂾'
        elif signs[i] == 'D55':
            signs[i] = '𓂽'
        elif signs[i] == 'D54a':
            signs[i] = '𓂼'
        elif signs[i] == 'D54':
            signs[i] = '𓂻'
        elif signs[i] == 'D53':
            signs[i] = '𓂺'
        elif signs[i] == 'D52a':
            signs[i] = '𓂹'
        elif signs[i] == 'D52':
            signs[i] = '𓂸'
        elif signs[i] == 'D51':
            signs[i] = '𓂷'
        elif signs[i] == 'D50i':
            signs[i] = '𓂶'
        elif signs[i] == 'D50h':
            signs[i] = '𓂵'
        elif signs[i] == 'D50g':
            signs[i] = '𓂴'
        elif signs[i] == 'D50f':
            signs[i] = '𓂳'
        elif signs[i] == 'D50e':
            signs[i] = '𓂲'
        elif signs[i] == 'D50d':
            signs[i] = '𓂱'
        elif signs[i] == 'D50c':
            signs[i] = '𓂰'
        elif signs[i] == 'D50b':
            signs[i] = '𓂯'
        elif signs[i] == 'D50a':
            signs[i] = '𓂮'
        elif signs[i] == 'D50':
            signs[i] = '𓂭'
        elif signs[i] == 'D49':
            signs[i] = '𓂬'
        elif signs[i] == 'D48a':
            signs[i] = '𓂫'
        elif signs[i] == 'D48':
            signs[i] = '𓂪'
        elif signs[i] == 'D47':
            signs[i] = '𓂩'
        elif signs[i] == 'D46a':
            signs[i] = '𓂨'
        elif signs[i] == 'D46':
            signs[i] = '𓂧'
        elif signs[i] == 'D45':
            signs[i] = '𓂦'
        elif signs[i] == 'D44':
            signs[i] = '𓂥'
        elif signs[i] == 'D43':
            signs[i] = '𓂤'
        elif signs[i] == 'D42':
            signs[i] = '𓂣'
        elif signs[i] == 'D41':
            signs[i] = '𓂢'
        elif signs[i] == 'D40':
            signs[i] = '𓂡'
        elif signs[i] == 'D39':
            signs[i] = '𓂠'
        elif signs[i] == 'D38':
            signs[i] = '𓂟'
        elif signs[i] == 'D37':
            signs[i] = '𓂞'
        elif signs[i] == 'D36':
            signs[i] = '𓂝'
        elif signs[i] == 'D35':
            signs[i] = '𓂜'
        elif signs[i] == 'D34a':
            signs[i] = '𓂛'
        elif signs[i] == 'D34':
            signs[i] = '𓂚'
        elif signs[i] == 'D33':
            signs[i] = '𓂙'
        elif signs[i] == 'D32':
            signs[i] = '𓂘'
        elif signs[i] == 'D31a':
            signs[i] = '𓂗'
        elif signs[i] == 'D31':
            signs[i] = '𓂖'
        elif signs[i] == 'D30':
            signs[i] = '𓂕'
        elif signs[i] == 'D29':
            signs[i] = '𓂔'
        elif signs[i] == 'D28':
            signs[i] = '𓂓'
        elif signs[i] == 'D27a':
            signs[i] = '𓂒'
        elif signs[i] == 'D27':
            signs[i] = '𓂑'
        elif signs[i] == 'D26':
            signs[i] = '𓂐'
        elif signs[i] == 'D25':
            signs[i] = '𓂏'
        elif signs[i] == 'D24':
            signs[i] = '𓂎'
        elif signs[i] == 'D23':
            signs[i] = '𓂍'
        elif signs[i] == 'D22':
            signs[i] = '𓂌'
        elif signs[i] == 'D21':
            signs[i] = '𓂋'
        elif signs[i] == 'D20':
            signs[i] = '𓂊'
        elif signs[i] == 'D19':
            signs[i] = '𓂉'
        elif signs[i] == 'D18':
            signs[i] = '𓂈'
        elif signs[i] == 'D17':
            signs[i] = '𓂇'
        elif signs[i] == 'D16':
            signs[i] = '𓂆'
        elif signs[i] == 'D15':
            signs[i] = '𓂅'
        elif signs[i] == 'D14':
            signs[i] = '𓂄'
        elif signs[i] == 'D13':
            signs[i] = '𓂃'
        elif signs[i] == 'D12':
            signs[i] = '𓂂'
        elif signs[i] == 'D11':
            signs[i] = '𓂁'
        elif signs[i] == 'D10':
            signs[i] = '𓂀'
        elif signs[i] == 'D9':
            signs[i] = '𓁿'
        elif signs[i] == 'D8a':
            signs[i] = '𓁾'
        elif signs[i] == 'D8':
            signs[i] = '𓁽'
        elif signs[i] == 'D7':
            signs[i] = '𓁼'
        elif signs[i] == 'D6':
            signs[i] = '𓁻'
        elif signs[i] == 'D5':
            signs[i] = '𓁺'
        elif signs[i] == 'D4':
            signs[i] = '𓁹'
        elif signs[i] == 'D3':
            signs[i] = '𓁸'
        elif signs[i] == 'D2':
            signs[i] = '𓁷'
        elif signs[i] == 'D1':
            signs[i] = '𓁶'
        elif signs[i] == 'C24':
            signs[i] = '𓁵'
        elif signs[i] == 'C23':
            signs[i] = '𓁴'
        elif signs[i] == 'C22':
            signs[i] = '𓁳'
        elif signs[i] == 'C21':
            signs[i] = '𓁲'
        elif signs[i] == 'C20':
            signs[i] = '𓁱'
        elif signs[i] == 'C19':
            signs[i] = '𓁰'
        elif signs[i] == 'C18':
            signs[i] = '𓁯'
        elif signs[i] == 'C17':
            signs[i] = '𓁮'
        elif signs[i] == 'C16':
            signs[i] = '𓁭'
        elif signs[i] == 'C15':
            signs[i] = '𓁬'
        elif signs[i] == 'C14':
            signs[i] = '𓁫'
        elif signs[i] == 'C13':
            signs[i] = '𓁪'
        elif signs[i] == 'C12':
            signs[i] = '𓁩'
        elif signs[i] == 'C11':
            signs[i] = '𓁨'
        elif signs[i] == 'C10a':
            signs[i] = '𓁧'
        elif signs[i] == 'C10':
            signs[i] = '𓁦'
        elif signs[i] == 'C9':
            signs[i] = '𓁥'
        elif signs[i] == 'C8':
            signs[i] = '𓁤'
        elif signs[i] == 'C7':
            signs[i] = '𓁣'
        elif signs[i] == 'C6':
            signs[i] = '𓁢'
        elif signs[i] == 'C5':
            signs[i] = '𓁡'
        elif signs[i] == 'C4':
            signs[i] = '𓁠'
        elif signs[i] == 'C3':
            signs[i] = '𓁟'
        elif signs[i] == 'C2c':
            signs[i] = '𓁞'
        elif signs[i] == 'C2b':
            signs[i] = '𓁝'
        elif signs[i] == 'C2a':
            signs[i] = '𓁜'
        elif signs[i] == 'C2':
            signs[i] = '𓁛'
        elif signs[i] == 'C1':
            signs[i] = '𓁚'
        elif signs[i] == 'B9':
            signs[i] = '𓁙'
        elif signs[i] == 'B8':
            signs[i] = '𓁘'
        elif signs[i] == 'B7':
            signs[i] = '𓁗'
        elif signs[i] == 'B6':
            signs[i] = '𓁖'
        elif signs[i] == 'B5a':
            signs[i] = '𓁕'
        elif signs[i] == 'B5':
            signs[i] = '𓁔'
        elif signs[i] == 'B4':
            signs[i] = '𓁓'
        elif signs[i] == 'B3':
            signs[i] = '𓁒'
        elif signs[i] == 'B2':
            signs[i] = '𓁑'
        elif signs[i] == 'B1':
            signs[i] = '𓁐'
        elif signs[i] == 'Aa32':
            signs[i] = '𓐮'
        elif signs[i] == 'Aa31':
            signs[i] = '𓐭'
        elif signs[i] == 'Aa30':
            signs[i] = '𓐬'
        elif signs[i] == 'Aa29':
            signs[i] = '𓐫'
        elif signs[i] == 'Aa28':
            signs[i] = '𓐪'
        elif signs[i] == 'Aa27':
            signs[i] = '𓐩'
        elif signs[i] == 'Aa26':
            signs[i] = '𓐨'
        elif signs[i] == 'Aa25':
            signs[i] = '𓐧'
        elif signs[i] == 'Aa24':
            signs[i] = '𓐦'
        elif signs[i] == 'Aa23':
            signs[i] = '𓐥'
        elif signs[i] == 'Aa22':
            signs[i] = '𓐤'
        elif signs[i] == 'Aa21':
            signs[i] = '𓐣'
        elif signs[i] == 'Aa20':
            signs[i] = '𓐢'
        elif signs[i] == 'Aa19':
            signs[i] = '𓐡'
        elif signs[i] == 'Aa18':
            signs[i] = '𓐠'
        elif signs[i] == 'Aa17':
            signs[i] = '𓐟'
        elif signs[i] == 'Aa16':
            signs[i] = '𓐞'
        elif signs[i] == 'Aa15':
            signs[i] = '𓐝'
        elif signs[i] == 'Aa14':
            signs[i] = '𓐜'
        elif signs[i] == 'Aa13':
            signs[i] = '𓐛'
        elif signs[i] == 'Aa12':
            signs[i] = '𓐚'
        elif signs[i] == 'Aa11':
            signs[i] = '𓐙'
        elif signs[i] == 'Aa10':
            signs[i] = '𓐘'
        elif signs[i] == 'Aa9':
            signs[i] = '𓐗'
        elif signs[i] == 'Aa8':
            signs[i] = '𓐖'
        elif signs[i] == 'Aa7b':
            signs[i] = '𓐕'
        elif signs[i] == 'Aa7a':
            signs[i] = '𓐔'
        elif signs[i] == 'Aa7':
            signs[i] = '𓐓'
        elif signs[i] == 'Aa6':
            signs[i] = '𓐒'
        elif signs[i] == 'Aa5':
            signs[i] = '𓐑'
        elif signs[i] == 'Aa4':
            signs[i] = '𓐐'
        elif signs[i] == 'Aa3':
            signs[i] = '𓐏'
        elif signs[i] == 'Aa2':
            signs[i] = '𓐎'
        elif signs[i] == 'Aa1':
            signs[i] = '𓐍'
        elif signs[i] == 'A70':
            signs[i] = '𓁏'
        elif signs[i] == 'A69':
            signs[i] = '𓁎'
        elif signs[i] == 'A68':
            signs[i] = '𓁍'
        elif signs[i] == 'A67':
            signs[i] = '𓁌'
        elif signs[i] == 'A66':
            signs[i] = '𓁋'
        elif signs[i] == 'A65':
            signs[i] = '𓁊'
        elif signs[i] == 'A64':
            signs[i] = '𓁉'
        elif signs[i] == 'A63':
            signs[i] = '𓁈'
        elif signs[i] == 'A62':
            signs[i] = '𓁇'
        elif signs[i] == 'A61':
            signs[i] = '𓁆'
        elif signs[i] == 'A60':
            signs[i] = '𓁅'
        elif signs[i] == 'A59':
            signs[i] = '𓁄'
        elif signs[i] == 'A58':
            signs[i] = '𓁃'
        elif signs[i] == 'A57':
            signs[i] = '𓁂'
        elif signs[i] == 'A56':
            signs[i] = '𓁁'
        elif signs[i] == 'A55':
            signs[i] = '𓁀'
        elif signs[i] == 'A54':
            signs[i] = '𓀿'
        elif signs[i] == 'A53':
            signs[i] = '𓀾'
        elif signs[i] == 'A52':
            signs[i] = '𓀽'
        elif signs[i] == 'A51':
            signs[i] = '𓀼'
        elif signs[i] == 'A50':
            signs[i] = '𓀻'
        elif signs[i] == 'A49':
            signs[i] = '𓀺'
        elif signs[i] == 'A48':
            signs[i] = '𓀹'
        elif signs[i] == 'A47':
            signs[i] = '𓀸'
        elif signs[i] == 'A46':
            signs[i] = '𓀷'
        elif signs[i] == 'A45a':
            signs[i] = '𓀶'
        elif signs[i] == 'A45':
            signs[i] = '𓀵'
        elif signs[i] == 'A44':
            signs[i] = '𓀴'
        elif signs[i] == 'A43a':
            signs[i] = '𓀳'
        elif signs[i] == 'A43':
            signs[i] = '𓀲'
        elif signs[i] == 'A42a':
            signs[i] = '𓀱'
        elif signs[i] == 'A42':
            signs[i] = '𓀰'
        elif signs[i] == 'A41':
            signs[i] = '𓀯'
        elif signs[i] == 'A4a':
            signs[i] = '𓀮'
        elif signs[i] == 'A40':
            signs[i] = '𓀭'
        elif signs[i] == 'A39':
            signs[i] = '𓀬'
        elif signs[i] == 'A38':
            signs[i] = '𓀫'
        elif signs[i] == 'A37':
            signs[i] = '𓀪'
        elif signs[i] == 'A36':
            signs[i] = '𓀩'
        elif signs[i] == 'A35':
            signs[i] = '𓀨'
        elif signs[i] == 'A34':
            signs[i] = '𓀧'
        elif signs[i] == 'A33':
            signs[i] = '𓀦'
        elif signs[i] == 'A32a':
            signs[i] = '𓀥'
        elif signs[i] == 'A32':
            signs[i] = '𓀤'
        elif signs[i] == 'A31':
            signs[i] = '𓀣'
        elif signs[i] == 'A30':
            signs[i] = '𓀢'
        elif signs[i] == 'A29':
            signs[i] = '𓀡'
        elif signs[i] == 'A28':
            signs[i] = '𓀠'
        elif signs[i] == 'A27':
            signs[i] = '𓀟'
        elif signs[i] == 'A26':
            signs[i] = '𓀞'
        elif signs[i] == 'A25':
            signs[i] = '𓀝'
        elif signs[i] == 'A24':
            signs[i] = '𓀜'
        elif signs[i] == 'A23':
            signs[i] = '𓀛'
        elif signs[i] == 'A22':
            signs[i] = '𓀚'
        elif signs[i] == 'A21':
            signs[i] = '𓀙'
        elif signs[i] == 'A20':
            signs[i] = '𓀘'
        elif signs[i] == 'A19':
            signs[i] = '𓀗'
        elif signs[i] == 'A18':
            signs[i] = '𓀖'
        elif signs[i] == 'A17a':
            signs[i] = '𓀕'
        elif signs[i] == 'A17':
            signs[i] = '𓀔'
        elif signs[i] == 'A16':
            signs[i] = '𓀓'
        elif signs[i] == 'A15':
            signs[i] = '𓀒'
        elif signs[i] == 'A14a':
            signs[i] = '𓀑'
        elif signs[i] == 'A14':
            signs[i] = '𓀐'
        elif signs[i] == 'A13':
            signs[i] = '𓀏'
        elif signs[i] == 'A12':
            signs[i] = '𓀎'
        elif signs[i] == 'A11':
            signs[i] = '𓀍'
        elif signs[i] == 'A10':
            signs[i] = '𓀌'
        elif signs[i] == 'A9':
            signs[i] = '𓀋'
        elif signs[i] == 'A8':
            signs[i] = '𓀊'
        elif signs[i] == 'A7':
            signs[i] = '𓀉'
        elif signs[i] == 'A6b':
            signs[i] = '𓀈'
        elif signs[i] == 'A6a':
            signs[i] = '𓀇'
        elif signs[i] == 'A6':
            signs[i] = '𓀆'
        elif signs[i] == 'A5a':
            signs[i] = '𓀅'
        elif signs[i] == 'A5':
            signs[i] = '𓀄'
        elif signs[i] == 'A4':
            signs[i] = '𓀃'
        elif signs[i] == 'A3':
            signs[i] = '𓀂'
        elif signs[i] == 'A2':
            signs[i] = '𓀁'
        elif signs[i] == 'A1':
            signs[i] = '𓀀'
        elif signs[i] == 'O':
            signs[i] = '°'
        elif signs[i] == '[':
            signs[i] = '['
        elif signs[i] == ']':
            signs[i] = ']'
        else:
            if not signs[i] == "-" and not signs[i] == ":" and not signs[i] == "*" and not signs[i] == "(" and not signs[i] == ")":
                signs[i] = "§" + signs[i] + "$"


    
    return signs