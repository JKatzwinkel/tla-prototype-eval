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
def fixForRES(mdc):
    if mdc:
        mdc = mdc.replace('[', '"["')
        mdc = mdc.replace(']', '"]"')
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
        transl = transl.replace('.du', ':DU')
        transl = transl.replace('.pl', ':PL')
        transl = transl.replace(',', '.')
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
        "epitheton_title": "title / epitheton",
        "interjection": "interjection",
        "numeral": "numeral",
        "particle": "particle",
        "preposition": "preposition",
        "pronoun": "pronoun",
        "root": "root",
        "substantive": "noun",
        "undefined": "(unfedined)",
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
        "verb_irr": "jrr" }
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
