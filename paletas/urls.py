from django.urls import path
from paletas.views import listado

app_name = 'paletas'

urlpatterns = [
    path('listado/', listado, name='listado'),
]
