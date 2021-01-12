from django.shortcuts import render, redirect
from home.models import LevelClear

# Create your views here.
def meme_view(request):
    if LevelClear.objects.get(name='memes').cleared:
        return render(request, 'memes/main.html');
    else:
        return redirect('/hangman/memes');