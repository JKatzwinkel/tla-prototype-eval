from django.urls import path

from . import views

urlpatterns = [
    path('', views.help),
    path('bts-glossings', views.BTSglossings),
    path('ling-glossings', views.lingGlossings),
]

