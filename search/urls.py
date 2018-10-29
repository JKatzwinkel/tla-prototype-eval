from django.urls import path

from search import views

urlpatterns = [
        path('', views.search),
        path('dict', views.search_dict),
        ]
