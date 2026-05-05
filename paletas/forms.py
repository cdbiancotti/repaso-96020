from django import forms
from paletas.models import Paleta

class FormularioPaleta(forms.ModelForm):
    
    class Meta:
        model = Paleta
        fields = "__all__"
        
class FormularioBusqueda(forms.Form):
    marca = forms.CharField(max_length=30, required=False)