from django.shortcuts import render
from .models import Post
from .models import Comentario
from .models import Categoria
from django.utils import timezone
from django.http import Http404

# from django.http import HttpResponse



def index(request):
    ultimosPosts = Post.objects.all().order_by('fecha_publicacion').reverse()[:3]
    categorias_con_post = Categoria.obtener_categorias_ordenadas_por_numero_de_posts()
    return render(request, 'index.html', {
        'ultimosPosts': ultimosPosts,
        'postPorCategoria': categorias_con_post})

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