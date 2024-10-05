from django import forms
from .models import MensajeContacto  # Importa el modelo

class ContactoForm(forms.ModelForm):  # Cambia a ModelForm
    class Meta:
        model = MensajeContacto  # Especifica el modelo
        fields = ['nombre', 'email', 'mensaje']  # Campos que quieres incluir
