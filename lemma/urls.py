from django.urls import path

from . import views

urlpatterns = [
        path('details/<str:lemma_id>', views.details),
        ]
