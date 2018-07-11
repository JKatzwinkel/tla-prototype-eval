from django.urls import path

from . import views

urlpatterns = [
        path('details/<str:obj_id>', views.details),
        path('search', views.search),
        ]
