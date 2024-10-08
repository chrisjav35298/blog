from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Categoria
from .models import Comentario




admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
