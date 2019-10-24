from django.urls import path

from . import views

urlpatterns = [
    path('', views.help),
    path('bts-glossings', views.BTSglossings),
    path('ling-glossings', views.lingGlossings),
    path('search', views.helpSearch),
    path('dict', views.helpDict),
    path('lemma', views.helpLemma),
    path('occurrences', views.helpOccurrences),
]

