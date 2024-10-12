from django import forms
from .models import MensajeContacto  

class ContactoForm(forms.ModelForm):  
    class Meta:
        model = MensajeContacto  
        fields = ['nombre', 'email', 'mensaje']  
