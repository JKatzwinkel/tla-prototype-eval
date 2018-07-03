from django.urls import path

from . import views

urlpatterns = [
        path('details/<str:thsobj_id>', views.details),
        path('search', views.search),
        path('', views.list)
        ]
