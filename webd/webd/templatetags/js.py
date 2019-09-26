from django.utils.safestring import mark_safe
from django.template import Library
#from django.utils.http import urlencode

import json

register = Library()

@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))
    
@register.filter(is_safe=True)
def niceRelationName(name):
    if name == 'root':
        name = 'Roots'
    elif name == 'rootOf':
        name = 'Root of'
    elif name == 'predecessor':
        name = 'Predecessors'
    elif name == 'successor':
        name = 'Successors'
    elif name == 'referencing':
        name = 'Substitutes for following obsolete lemmata'        
    elif name == 'referencedBy':
        name = 'Substituted by'        
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
