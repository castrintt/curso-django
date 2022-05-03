from django.shortcuts import render
from django.http import HttpResponse as response


def home(request):
    return render(request, 'recipes/home.html', context={
        'name':'igor'
    })

def contato(request):
    return response(request,'recipes/contato.html')

def sobre(request):
    return response('SOBRE 1')
