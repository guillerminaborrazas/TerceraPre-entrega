from django.http import HttpResponse
from django.template import loader

def inicio(reuqest):
    return HttpResponse("Inicio")
