from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      
    path('openForm', views.openForm, name='openForm'),      
    path('submitMeme', views.submitMeme, name='submitMeme'),      
]