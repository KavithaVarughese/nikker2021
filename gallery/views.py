from django.shortcuts import render, redirect
from home.models import LevelClear

# Create your views here.
def collage_view(request):
    if LevelClear.objects.get(name='gallery').cleared:
        return render(request, 'gallery/collage.html')
    else:
        return redirect('/hangman/gallery')
