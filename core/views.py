from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'https://abre.ai/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'https://abre.ai/turing-pic'}
    ]
    return render(request, 'index.html', {'speakers': speakers})

def speaker_detail(request):
    return HttpResponse()