from django import forms
from .models import Citamedica

class Formulariocita(forms.ModelForm):
    class Meta:
        model=Citamedica
        fields= '__all__'