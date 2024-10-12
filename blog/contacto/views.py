from django.shortcuts import render, redirect
from .form import ContactoForm
from .models import MensajeContacto

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('contacto_exito')
    else:
        form = ContactoForm()

    return render(request, 'contacto/contacto_form.html', {'form': form})

def contacto_exito(request):
    return render(request, 'contacto/contacto_exito.html')




@login_required  
def lista_mensajes_contacto(request):
    if not request.user.is_superuser:  
        return HttpResponseForbidden("No tienes permiso para realizar esta acción.")
    
    mensajes = MensajeContacto.objects.all().order_by('-fecha_envio') 
    return render(request, 'contacto/contacto_list.html', {'mensajes': mensajes})