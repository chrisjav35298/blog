from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Count

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=200)
    contenido = models.TextField(default='Contenido por defecto')  
    imagen = models.ImageField(null=True, blank=True, upload_to='img/posts')  
    fecha_creacion = models.DateTimeField(default=timezone.now)  
    fecha_publicacion = models.DateField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name='posts')

    def publicar(self):
        self.fecha_publicacion = timezone.now().date()  
        self.save()

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    @classmethod
    def obtener_categorias_ordenadas_por_numero_de_posts(cls):
        return cls.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')
    
    @classmethod
    def obtener_posts_ordenados_por_categorias(cls):
        return Post.objects.select_related('categorias').order_by('categorias__nombre')

    
class Comentario(models.Model):
    cuerpo_comentario = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)  
    aprobado = models.BooleanField(default=False)
    post = models.ForeignKey('Post', related_name='comentarios', on_delete=models.CASCADE)
    autor_comentario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def aprobar_comentario(self):
        self.aprobado = True
        self.save()

    def __str__(self):
        return f'Comentario de {self.autor_comentario} en {self.post}'
