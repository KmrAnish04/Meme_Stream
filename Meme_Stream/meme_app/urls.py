from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      
    path('stream', views.stream, name='stream'),      
    path('openForm', views.openForm, name='openForm'),      
    path('submitMeme', views.submitMeme, name='submitMeme'),      
    path('openEditForm', views.openEditForm, name='openEditForm'),
    path('editMeme', views.editMeme, name='editMeme')
]