from django.shortcuts import render

# Inclui a classe HttpResponse
from django.http import HttpResponse

# Define uma function view chamada index
def index(request):
    return HttpResponse('Olá Django - index')

# Define uma function view chamada ola.
def ola(request):
    return HttpResponse('Olá Django')
