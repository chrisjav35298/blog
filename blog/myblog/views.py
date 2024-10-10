from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .models import Comentario
from .models import Categoria
from django.utils import timezone
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .form import CategoriaForm
from django.http import HttpResponseForbidden




def es_admin(user):
    return user.is_superuser

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



def categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('categoria_list')  
    else:
        form = CategoriaForm()

    return render(request, 'categoria_new.html', {'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()  
    return render(request, 'categoria_list.html', {'categorias': categorias})

def editar_categoria(request, id):
    if not request.user.is_superuser:  
        return HttpResponseForbidden("No tienes permiso para realizar esta acción.")
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categoria_edit.html', {'form': form})


def eliminar_categoria(request, id):
    if not request.user.is_superuser: 
        return HttpResponseForbidden("No tienes permiso para realizar esta acción.")
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    
    return render(request, 'categoria_delete.html', {'categoria': categoria})