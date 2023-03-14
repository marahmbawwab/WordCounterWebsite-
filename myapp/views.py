from django.shortcuts import render
from django.http import HttpResponse
from . import urls
# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'noor'})


def countword(request):
    words = request.GET['text']
    Count = len(words.split())  # split words by space
    return render(request, 'counter.html', {'count': Count, 'text': words})
