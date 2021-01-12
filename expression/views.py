from django.shortcuts import render, redirect
from home.models import LevelClear

# Create your views here.
def expression_view(request):
    if LevelClear.objects.get(name='expression').cleared:
        return render(request, 'expression/main.html')
    else:
        return redirect('/hangman/expression')