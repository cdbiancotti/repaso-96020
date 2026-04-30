from django.shortcuts import render, redirect
from usuarios.forms import IniciarSesion, CrearUsuario, EditarPerfil, CambiarContraseniaFormulario
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuarios.models import UsuarioInfo

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = IniciarSesion(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            login(request, usuario)
            
            UsuarioInfo.objects.get_or_create(user=usuario)
            
            return redirect('home:home')
    else: 
        formulario = IniciarSesion()
    
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registro(request):
    
    if request.method == "POST":
        formulario = CrearUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:iniciar_sesion')
    else:
        formulario = CrearUsuario()
        
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {})

@login_required
def editar_perfil(request):
    
    usuario_info = request.user.usuarioinfo
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            
            usuario_info.biografia = formulario.cleaned_data.get('biografia')
            
            usuario_info.save()
            formulario.save()
            return redirect('usuarios:perfil')
    else:
        formulario = EditarPerfil(instance=request.user, initial={'biografia': usuario_info.biografia})
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('usuarios:perfil')
    form_class = CambiarContraseniaFormulario