from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>ruturaj</h1>')

def vice_captain(request):
    return HttpResponse('<h1>jadeja</h1>')