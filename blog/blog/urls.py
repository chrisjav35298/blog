"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# Importación de vistas basadas en funciones
from myblog.views import (
    lista_posts,
    index,
    post_detalle,
    categoria,
    lista_categorias,
    editar_categoria,
    eliminar_categoria,
    crear_post,
    editar_post,
    eliminar_post
)

from contacto import views as contacto_views
from usuario.views import (
    RegistrarUsuario,
    LoginUsuario,
    LogoutUsuario,
    usuario_edit,
    usuario_show,
    usuario_list,
    usuario_staff_edit,
    usuario_update
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas para publicaciones y crud post
    
    path('', index, name='index'),
    path('detalle/<int:id>/', post_detalle, name='post_detalle'),
    path('post/', crear_post, name='post_new'),
    path('posts/', lista_posts, name='post_list'),
    path('post/<int:id>/editar/', editar_post, name='post_edit'),
    path('post/<int:id>/eliminar/', eliminar_post, name='post_delete'),

    # Rutas para contacto
    path('contacto/', contacto_views.contacto, name='contacto'),
    path('contacto/exito/', contacto_views.contacto_exito, name='contacto_exito'),
    path('contacto/list/', contacto_views.lista_mensajes_contacto, name='contacto_list'),

    # Rutas para usuario
    path('registro/', RegistrarUsuario.as_view(), name='registrar'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),
    path('usuario/editar/', usuario_edit, name='usuario_edit'),
    path('usuario/perfil/', usuario_show, name='usuario_show'),
    path('usuario/list/', usuario_list, name='usuario_list'),
    path('usuario/editar/staff/<int:id>/', usuario_staff_edit, name='usuario_staff_edit'),
    path('usuario/update/', usuario_update, name='usuario_update'),


    # Rutas para categorías
    path('categoria/', categoria, name='categoria_new'),
    path('categorias/', lista_categorias, name='categoria_list'),
    path('categoria/editar/<int:id>/', editar_categoria, name='categoria_edit'),
    path('categoria/eliminar/<int:id>/', eliminar_categoria, name='categoria_delete'),
]

# Configuración para manejar archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
