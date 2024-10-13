from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .models import Comentario
from .models import Categoria
from django.utils import timezone
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CategoriaForm
from django.http import HttpResponseForbidden
from .forms import ComentarioForm 
from django.contrib import messages
from datetime import datetime
from usuario.models import Usuario  




def es_admin(user):
    return user.is_superuser

# def index(request):
#     ultimosPosts = Post.objects.filter(fecha_publicacion__isnull=False).order_by('-fecha_publicacion')[:4]
#     categorias_con_post = Categoria.obtener_categorias_ordenadas_por_numero_de_posts()
#     return render(request, 'index.html', {
#         'ultimosPosts': ultimosPosts,
#         'postPorCategoria': categorias_con_post})

def index(request):
    categoria_id = request.GET.get('categoria')
    autor_id = request.GET.get('autor')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    categorias = Categoria.objects.all()
    autores = Usuario.objects.all()  

    ultimosPosts = Post.objects.filter(fecha_publicacion__isnull=False)

    if categoria_id:
        ultimosPosts = ultimosPosts.filter(categorias__id=categoria_id)

    if autor_id:
        ultimosPosts = ultimosPosts.filter(autor__id=autor_id)

    if fecha_desde:
        ultimosPosts = ultimosPosts.filter(fecha_publicacion__gte=datetime.strptime(fecha_desde, '%Y-%m-%d'))

    if fecha_hasta:
        ultimosPosts = ultimosPosts.filter(fecha_publicacion__lte=datetime.strptime(fecha_hasta, '%Y-%m-%d'))

    categorias_con_post = Categoria.obtener_categorias_ordenadas_por_numero_de_posts()

    return render(request, 'index.html', {
        'ultimosPosts': ultimosPosts,
        'categorias': categorias,
        'autores': autores,
        'postPorCategoria': categorias_con_post
    })




# hay que usar para paginar
# def lista_posts(request):
#     posts = Post.objects.all()  # Obtén todos los posts
#     paginator = Paginator(posts, 5)  # Muestra 5 posts por página

#     page_number = request.GET.get('page')  # Obtén el número de página de la URL
#     page_obj = paginator.get_page(page_number)  # Obtén el objeto de la página actual

#     return render(request, 'mi_template.html', {'page_obj': page_obj})



def post_detalle(request, id):
    post = get_object_or_404(Post, id=id)
    comentarios = post.comentarios.filter(aprobado=True)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)  # Instanciar el formulario con los datos POST

        if form.is_valid():  # Validar el formulario
            comentario = form.save(commit=False)  # No guardar aún
            comentario.post = post  # Asignar el post
            comentario.autor_comentario = request.user  # Asignar el usuario actual
            comentario.save()  # Ahora guardar el comentario
            return redirect('post_detalle', id=post.id)

    else:
        form = ComentarioForm()  # Crear un formulario vacío en caso de un GET

    context = {
        "Post": post,
        "comentarios": comentarios,
        "form": form,  # Pasar el formulario al contexto
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


def almacenar_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  # Asigna el post al comentario
            comentario.autor_comentario = request.user  # Asigna el usuario actual
            comentario.save()  # Guarda el comentario
            messages.success(request, 'Tu comentario ha sido enviado con éxito.')
            return redirect('post_detalle', id=post.id)
    else:
        form = ComentarioForm()  # Crea un formulario vacío para GET

    context = {
        'form': form,
        'post': post,
        
    }
    return render(request, 'comentario_form.html', context)


# relacionado a crud del Postfrom django.shortcuts import render, redirect
from .forms import PostForm

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user 
            post.save()
            form.save_m2m()  
            return redirect('post_list')  
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

# def editar_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list') 
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'post_edit.html', {'form': form})

def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # Si el checkbox "publicar" está presente, establece la fecha de publicación
            if request.POST.get('publicar'):
                post.fecha_publicacion = timezone.now().date()  # Establece la fecha actual
            else:
                post.fecha_publicacion = request.POST.get('fecha_publicacion')  # Mantiene la fecha ingresada
            form.save()
            return redirect('post_list') 
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  
    return render(request, 'post_delete.html', {'post': post})


def lista_posts(request):
    posts = Post.objects.order_by('-fecha_publicacion')
    print(posts)  # Esto te permitirá ver en la consola los posts que estás obteniendo
    return render(request, 'post_list.html', {'posts': posts})
