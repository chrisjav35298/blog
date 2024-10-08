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
# from django.contrib import admin
# from django.urls import path
# from myblog.views import *


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('posts/', lista_posts, name='lista_posts'),
#     path('', index, name='index'),

  

    
# ]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myblog.views import lista_posts, index, post_detalle
from contacto import views as contacto_views 
from usuario.views import RegistrarUsuario, LoginUsuario, LogoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', lista_posts, name='lista_posts'),
    path('', index, name='index'),
    path('detalle/<int:id>/', post_detalle, name='post_detalle'),
    path('contacto/', contacto_views.contacto, name='contacto'),
    path('contacto/exito/', contacto_views.contacto_exito, name='contacto_exito'),
    path('registro/', RegistrarUsuario.as_view(), name='registrar'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
