from django.urls import path

from . import views

urlpatterns = [
        path('lemma/<str:lemma_id>', views.lemma_details_page),
        ]
