from django import forms
from django.contrib.admin import widgets
from models import *


class CicloForm(forms.ModelForm):
    clave = forms.CharField(widget=widgets.AdminTextInputWidget())
    fecha_revision = forms.DateField(widget=widgets.AdminDateWidget())
    observacion = forms.CharField(max_length=255, required=False, widget=widgets.AdminTextareaWidget())

    class Meta:
        model = Ciclo
        fields = ['clave', 'fecha_revision', 'observacion', 'status']


class DimensionForm(forms.ModelForm):
    dimension = forms.CharField(widget=widgets.AdminTextInputWidget())

    class Meta:
        model = Dimension
        fields = ['dimension']


class ObjetivoForm(forms.ModelForm):
    ciclo = forms.CharField(max_length=10, widget=widgets.AdminTextInputWidget())
    objetivo = forms.CharField(widget=widgets.AdminTextareaWidget())

    class Meta:
        model = Objetivo
        fields = '__all__'


class ProyectoForm(forms.ModelForm):
    adjunto = forms.FileField(required=False)
    titulo = forms.CharField(widget=widgets.AdminTextareaWidget())
    fecha_plazo = forms.DateField(widget=widgets.AdminDateWidget())
    indicador = forms.CharField(max_length=20, widget=widgets.AdminTextInputWidget(), required=False)

    class Meta:
        model = Proyecto
        fields = '__all__'