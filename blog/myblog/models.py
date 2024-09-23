from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=200)
    contenido = models.TextField(default='Contenido por defecto')  # TextField does not need max_length
    imagen = models.ImageField(null=True, blank=True, upload_to='img/posts')  # Move upload_to here
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Remove ()
    fecha_publicacion = models.DateField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name='posts')

    def publicar(self):
        self.fecha_publicacion = timezone.now().date()  # Ensure it is a date object
        self.save()

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    cuerpo_comentario = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)  # Remove ()
    aprobado = models.BooleanField(default=False)
    post = models.ForeignKey('Post', related_name='comentarios', on_delete=models.CASCADE)
    autor_comentario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def aprobar_comentario(self):
        self.aprobado = True
        self.save()

    def __str__(self):
        return f'Comentario de {self.autor_comentario} en {self.post}'
