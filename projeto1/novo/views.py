from django.shortcuts import render
from django.http import HttpResponse as response

def home_novo(request):
    return response('NOVO HOME')

def sobre_novo(request):
    return response('NOVO SOBRE')

def contato_novo(request):
    return response('NOVO CONTATO')


# Create your views here.
