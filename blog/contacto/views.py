from django.shortcuts import render, redirect
from .form import ContactoForm

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
