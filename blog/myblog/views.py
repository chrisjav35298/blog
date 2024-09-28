from django.shortcuts import render
from .models import Post
from django.utils import timezone
# from django.http import HttpResponse



# def home_view(request):
#     context = {'mensaje': 'INFORMATORIO ' }
#     return HttpResponse(f" hola {context['mensaje']}")
# # Create your views here.

# def index(request):
#     return render(request, 'inicio.html')

def lista_posts(request):
    posts = Post.objects.order_by('fecha_publicacion')
    return render(request, 'posts.html',{'posts':posts})