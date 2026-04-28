from django.db import models

class Paletas(models.Model):
    marca = models.CharField(max_length=30)
    precio = models.FloatField()
    
    def __str__(self):
        return f"Paleta {self.pk}: marca {self.marca} - precio {self.precio}"