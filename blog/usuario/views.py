from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import EditarUsuarioForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate

# Create your views here.




class RegistrarUsuario(CreateView):
    template_name = 'usuario/registrar.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        usuario = form.save(commit=False)  
        usuario.is_staff = False 
        usuario.is_superuser = False  
        usuario.save()  
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
    

@login_required
def usuario_show(request):
     return render(request, 'usuario/usuario_show.html', {'user': request.user})

@login_required
def usuario_edit(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid():
            # Verifica si se quiere cambiar la contraseña
            password_old = form.cleaned_data.get('password_old')
            password_new = form.cleaned_data.get('password_new')

            if password_old and password_new:
                # Autentica con la contraseña actual
                user = authenticate(username=usuario.username, password=password_old)
                if user:
                    # Si la autenticación es exitosa, cambia la contraseña
                    usuario.set_password(password_new)
                    usuario.save()
                    update_session_auth_hash(request, usuario)  # Mantiene la sesión activa
                    messages.success(request, 'Tu contraseña ha sido actualizada exitosamente.')
                else:
                    messages.error(request, 'La contraseña actual es incorrecta.')
                    return redirect('usuario_edit')

            else:
                # Solo guardar la imagen
                form.save()
                messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')

            return redirect('usuario_show')
    else:
        form = EditarUsuarioForm(instance=usuario)

    return render(request, 'usuario/usuario_edit.html', {'form': form})