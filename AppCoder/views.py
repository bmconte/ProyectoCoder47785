from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    curso.save()

    return HttpResponse(curso.nombre)
