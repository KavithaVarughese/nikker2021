from django.shortcuts import render, redirect
from home.models import LevelClear

# Create your views here.
def mail_view(request):
    if LevelClear.objects.get(name='mail').cleared:
        return render(request, 'mail/main.html')
    else:
        return redirect('/hangman/mail')