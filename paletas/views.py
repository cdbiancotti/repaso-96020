from django.shortcuts import render, redirect
from paletas.models import Paletas
from paletas.forms import FormularioPaleta, FormularioBusqueda
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def listado(request):
    
    formulario = FormularioBusqueda(request.GET)
    if formulario.is_valid():
        paletas = Paletas.objects.filter(marca__icontains=formulario.cleaned_data.get('marca'))
    else:
        paletas = Paletas.objects.all()
    return render(request, 'paletas/listado.html', {'paletas': paletas, 'formulario': formulario})

@login_required
def crear(request):
    
    if request.method == "POST":
        formulario = FormularioPaleta(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('paletas:listado')
    else:
        formulario = FormularioPaleta()
        
    return render(request, 'paletas/crear.html', {'formulario': formulario})

def detalle(request, id):
    paleta = Paletas.objects.get(id=id)
    return render(request, 'paletas/detalle.html', {'paleta': paleta})


class BorrarPaleta(LoginRequiredMixin, DeleteView):
    model = Paletas
    template_name = "paletas/borrar.html"
    success_url = reverse_lazy('paletas:listado')

class ActualizarPaleta(LoginRequiredMixin, UpdateView):
    model = Paletas
    template_name = "paletas/actualizar.html"
    success_url = reverse_lazy('paletas:listado')
    # fields = "__all__" # ['campo1', 'campo2', etc]
    form_class = FormularioPaleta
