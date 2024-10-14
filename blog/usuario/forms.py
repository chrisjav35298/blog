from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import Usuario



class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username','first_name', 'last_name', 'password1', 'password2','email','imagen']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)



class EditarUsuarioForm(forms.ModelForm):
    password_old = forms.CharField(
        label="Contraseña Actual",
        widget=forms.PasswordInput,
        required=False
    )
    password_new = forms.CharField(
        label="Nueva Contraseña",
        widget=forms.PasswordInput,
        required=False
    )
    password_new_confirm = forms.CharField(
        label="Confirmar Nueva Contraseña",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = Usuario
        fields = ('imagen', 'password_old', 'password_new', 'password_new_confirm')

    def clean(self):
        cleaned_data = super().clean()
        password_new = cleaned_data.get("password_new")
        password_new_confirm = cleaned_data.get("password_new_confirm")
        password_old = cleaned_data.get("password_old")

        if password_new or password_new_confirm:
            # Verifica si se ha ingresado la contraseña actual
            if not password_old:
                raise forms.ValidationError("Debes ingresar la contraseña actual para cambiarla.")

            # Verifica que las contraseñas nuevas coincidan
            if password_new != password_new_confirm:
                raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
    

class EditarUsuarioStaffForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'is_staff', 'is_active']
        labels = {
            'is_staff': 'Colaborador',
            'is_active': 'Activo'
        }
        widgets = {
            'is_staff': forms.CheckboxInput(),
            'is_active': forms.CheckboxInput(),
        }