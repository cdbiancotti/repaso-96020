from django.urls import path
from paletas.views import listado, crear, detalle, ActualizarPaleta, BorrarPaleta

app_name = 'paletas'

urlpatterns = [
    path('listado/', listado, name='listado'),
    path('crear/', crear, name='crear'),
    path('<id>/', detalle, name='detalle'),
    path('<pk>/actualizar/', ActualizarPaleta.as_view(), name='actualizar'),
    path('<pk>/borrar/', BorrarPaleta.as_view(), name='borrar'),
]
