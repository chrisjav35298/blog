from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'usuario/registrar.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')  # Redirige al login después de registrarse

    def form_valid(self, form):
        usuario = form.save(commit=False)  # No guardar aún en la base de datos
        usuario.is_staff = False  # No es un staff
        usuario.is_superuser = False  # No es un superusuario
        usuario.save()  # Ahora guarda el usuario en la base de datos
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        
        # return super().form_valid(form)

        return redirect('login')
    
class LoginUsuario(LoginView):
    template_name = 'usuario/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('index')

class LogoutUsuario(LogoutView):
    template_name = 'usuario/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')
        return reverse('index')
    

