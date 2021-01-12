from django.urls import path
from .views import meme_view

app_name = 'memes'
urlpatterns = [
    path('', meme_view, name='meme'),
]