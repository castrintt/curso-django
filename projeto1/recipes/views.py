from django.shortcuts import render
from django.http import HttpResponse as response


def home(request):
    return response('HOME 1')

def contato(request):
    return response('CONTATO 1')

def sobre(request):
    return response('SOBRE 1')