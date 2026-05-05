from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='imagenes_paletas', null=True, blank=True)
    
    def __str__(self):
        return f"Paleta {self.pk}: marca {self.marca} - precio {self.precio}"