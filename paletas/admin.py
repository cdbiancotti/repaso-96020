from django.contrib import admin
from paletas.models import Paletas


# admin.site.register(Paletas)

class PaletaAdminModel(admin.ModelAdmin):
    list_filter = ['marca']
    list_display = ['marca', 'precio']



admin.site.register(Paletas, PaletaAdminModel)