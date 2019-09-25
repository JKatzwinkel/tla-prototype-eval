from django.utils.safestring import mark_safe
from django.template import Library

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
