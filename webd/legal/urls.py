from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.contact),
    path('imprint', views.imprint),
    path('privacy-policy', views.privacyPolicy),
]

