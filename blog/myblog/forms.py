from django import forms
from .models import Categoria
from .models import Comentario
from .models import Post



class CategoriaForm(forms.ModelForm): 
    class Meta:
        model = Categoria  
        fields = ['nombre']  



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpo_comentario']  
        widgets = {
            'cuerpo_comentario': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí...', 'required': True}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'titulo', 'resumen', 'contenido', 'imagen', 'categorias']
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(),
        }