from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class IniciarSesion(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    
class CrearUsuario(UserCreationForm):
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': '',
            'email': '',
        }
        labels = {
            'username': 'Usuario',
            'email': 'Email',
        }
        
class EditarPerfil(UserChangeForm):
    password = None
    biografia = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'biografia']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }
        
class CambiarContraseniaFormulario(PasswordChangeForm):
    old_password = forms.CharField(label='Contrasenia Vieja', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Contrasenia Nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contrasenia Nueva', widget=forms.PasswordInput)