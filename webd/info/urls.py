from django.urls import path

from . import views

urlpatterns = [
    path('introduction', views.introduction),
    path('project', views.project),
    path('collaboration', views.collaboration),
    path('licence', views.licence),
    path('dictionary', views.dictionary),
    path('text-corpus', views.textCorpus),
    path('extras', views.extras),
]

