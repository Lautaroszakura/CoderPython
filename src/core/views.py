from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde Django")

def saludar_con_etiqueta(request):
    return HttpResponse('<h1>Este es el titulo de mi App</h1>') #Las funciones van con __

def index(request):
    return render(request, 'core/index.html') #render 