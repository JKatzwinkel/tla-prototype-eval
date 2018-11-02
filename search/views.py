from django.shortcuts import render
from django.views.decorators.http import require_http_methods

WORD_CLASSES = {
        "substantive": [
          "substantive_masc",
          "substantive_fem"],
        "particle": [
          "particle_enclitic",
          "particle_nonenclitic"],
        "root": [
          "substantive_fem"],
        "pronoun": [
          "personal_pronoun",
          "demonstrative_pronoun",
          "interrogative_pronoun",
          "relative_pronoun"],
        "numeral": [
          "cardinal",
          "ordinal"],
        "adverb": [
          "prepositional_adverb"],
        "preposition": None,
        "adjective": [
          "nisbe_adjective_preposition",
          "nisbe_adjective_substantive"],
        "epitheton_title": [
          "epith_king",
          "epith_god",
          "title"],
        "entity_name": [
          "place_name",
          "org_name",
          "person_name",
          "animal_name",
          "gods_name",
          "artifact_name",
          "kings_name"],
        "undefined": [
          "gods_name",
          "substantive_masc"],
        "verb": [
          "verb_caus_3-inf",
          "verb_5-inf",
          "verb_3-lit",
          "verb_3-inf",
          "verb_6-lit",
          "verb_caus_3-gem",
          "verb_5-lit",
          "verb_2-gem",
          "verb_caus_4-lit",
          "verb_caus_2-gem",
          "verb_4-lit",
          "verb_caus_5-lit",
          "verb_caus_3-lit",
          "verb_3-gem",
          "verb_caus_2-lit",
          "verb_irr",
          "verb_4-inf",
          "verb_caus_4-inf",
          "verb_2-lit"],
        "interjection": None}


@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    return render(request, 'search/index.html',
            {
                'word_classes': WORD_CLASSES,
                }
            )


@require_http_methods(["GET"])
def search_dict(request):
    params = request.GET.copy()
    print(params)
    return render(request, 'search/dict.html', {})

# Create your views here.
