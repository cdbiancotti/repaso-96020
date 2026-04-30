from django import forms
from paletas.models import Paletas

class FormularioPaleta(forms.ModelForm):
    
    class Meta:
        model = Paletas
        fields = "__all__"
        
class FormularioBusqueda(forms.Form):
    marca = forms.CharField(max_length=30, required=False)