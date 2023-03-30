from django import forms
from .models import Propietario,Vehiculo,Placa,Oficina

class PropietarioForm(forms.ModelForm):
    apPaterno = forms.CharField(label="Apellido Paterno")
    apMaterno = forms.CharField(label="Apellido Materno")

    class Meta:
        model = Propietario
        fields = ["RFC","nombre","apPaterno","apMaterno","apMaterno","email","CURP","calle","colonia","municipio","CP","edad"]

class PlacaForm(forms.ModelForm):
    class Meta:
        model = Placa
        fields =["numero","numTC","vehiculo","propietario","estatus","oficina"]

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields =["nombre","ciudad","telefono"]

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields =["NIV","noMotor","marca","linea","modelo"]