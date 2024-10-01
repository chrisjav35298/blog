from django.shortcuts import render
from .models import Post
from .models import Comentario
from django.utils import timezone
# from django.http import HttpResponse



# def home_view(request):
#     context = {'mensaje': 'INFORMATORIO ' }
#     return HttpResponse(f" hola {context['mensaje']}")
# # Create your views here.

# def index(request):
#     return render(request, 'inicio.html')

def index(request):
    ultimosPosts = Post.objects.all().order_by('fecha_publicacion').reverse()[:3]
    return render(request, 'index.html',{'ultimosPosts':ultimosPosts})

def lista_posts(request):
    posts = Post.objects.all().order_by('fecha_publicacion')
    return render(request, 'posts.html',{'posts':posts})

def post_detalle(request, id):
    try:
        data = Post.objects.get(id=id)  
        comentarios = Comentario.objects.filter(aprobado=True)
    except Post.DoesNotExist:
        raise Http404('El post no se encuentra.')

    context = {
        "Post": data,
        "comentarios": comentarios
    }

    return render(request, 'show.html', context)