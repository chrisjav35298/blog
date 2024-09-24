from django.shortcuts import render

from django.http import HttpResponse


def home_view(request):
    context = {'mensaje': 'INFORMATORIO ' }
    return HttpResponse(f" hola {context['mensaje']}")
# Create your views here.

def index(request):
    return render(request, 'inicio.html')