#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from escuela.models import Universidad, Pais, Continente

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class UniversidadForm(ModelForm):
    class Meta:
        model = Universidad

class PaisForm(ModelForm):
    class Meta:
        model = Pais

class ContinenteForm(ModelForm):
    class Meta:
        model = Continente