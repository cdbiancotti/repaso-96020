from django.urls import path
from usuarios.views import iniciar_sesion, registro, perfil, editar_perfil, CambiarContrasenia, mensajes, crear_mensaje, detalle_mensaje
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/contrasenia/', CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='usuarios/sesion_cerrada.html'), name='cerrar_sesion'),
    path('mensajes/', mensajes, name='mensajes'),
    path('mensajes/crear/', crear_mensaje, name='crear_mensaje'),
    path('mensajes/<id_msj>/', detalle_mensaje, name='detalle_mensaje'),
]
