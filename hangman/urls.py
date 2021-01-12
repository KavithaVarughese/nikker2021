from django.urls import path
from .views import hangman

urlpatterns = [
    path('hangman/<slug:urlname>', hangman, name='hangman'),
]
