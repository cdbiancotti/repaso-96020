from django.shortcuts import render
from paletas.models import Paletas

def listado(request):
    paletas = Paletas.objects.all()
    return render(request, 'paletas/listado.html', {'paletas': paletas})