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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', lista_posts, name='lista_posts'),
    path('', index, name='index'),
    path('detalle/<int:id>/', post_detalle, name='post_detalle'),
    path('contacto/', contacto_views.contacto, name='contacto'),
    path('contacto/exito/', contacto_views.contacto_exito, name='contacto_exito'),

]

if settings.DEBUG:  # Esto asegura que solo se sirvan archivos de medios en modo desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
