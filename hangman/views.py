from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Phrase
from home.models import LevelClear


@csrf_exempt
def hangman(request, urlname):
    if LevelClear.objects.get(name=urlname).cleared:
        return redirect('/'+urlname)
    if request.method == 'POST':
        puzzle = Phrase.objects.get(pk=request.POST['id'])
        if request.POST['submitted_letter']:
            if request.POST['submitted_letter'] not in puzzle.phrase:
                if puzzle.wrong_tries < 7:
                    puzzle.wrong_tries = puzzle.wrong_tries + 1
                    puzzle.save()
                if puzzle.wrong_tries == 7:
                    return HttpResponse(json.dumps({'progress': request.POST['progress'], 'id': request.POST['id'], 'failed': 'true', 'image_idx': puzzle.wrong_tries}))
                return HttpResponse(json.dumps({'progress': request.POST['progress'], 'id': request.POST['id'], 'image_idx': puzzle.wrong_tries}))
            else:
                if puzzle.wrong_tries == 7:
                    return HttpResponse(json.dumps({'progress': request.POST['progress'], 'id': request.POST['id'], 'failed': 'true', 'image_idx': puzzle.wrong_tries}))
                progress = request.POST['progress']
                return_string = ''
                for i in range(len(puzzle.phrase)):
                    if puzzle.phrase[i] == request.POST['submitted_letter']:
                        return_string += request.POST['submitted_letter']
                    else:
                        return_string += progress[i]
                if return_string == puzzle.phrase :
                    puzzle.success = True
                    puzzle.save()
                    LevelClear.objects.filter(name=urlname).update(cleared=True)
                    return HttpResponse(json.dumps({'progress': return_string, 'id': request.POST['id'], 'success': 'true', 'image_idx': puzzle.wrong_tries, 'url' :'/'+urlname}))
                return HttpResponse(json.dumps({'progress': return_string, 'id': request.POST['id'], 'image_idx': puzzle.wrong_tries}))
    elif request.method == 'GET':
        qs = Phrase.objects.filter(success=False).update(wrong_tries=0)
        qs = Phrase.objects.filter(success=False)
        if qs.count() == 0:
            return redirect('/')
        return_string = ''
        for i in qs[0].phrase:
            if i == ' ':
                return_string += ' '
            else:
                return_string += '*'
        return render(request, 'hangman/index.html', {'progress': return_string, 'id': qs[0].pk, 'image_idx': '0'})
