from django.db import models
from django.contrib.auth.models import User

class UsuarioInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)


class Mensaje(models.Model):
    motivo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msj_enviados")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msj_recibidos")