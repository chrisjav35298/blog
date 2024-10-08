from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'usuario/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inica sesión.')
        form.save()

        return redirect('login')
    
class LoginUsuario(LoginView):
    template_name = 'usuario/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('lista_posts')

class LogoutUsuario(LogoutView):
    template_name = 'usuario/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')
        return reverse('usuario/logout')
    

