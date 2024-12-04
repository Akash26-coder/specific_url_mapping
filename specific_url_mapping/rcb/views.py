from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Kohli</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>virat</h1>')