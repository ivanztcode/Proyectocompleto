from django.shortcuts import render, redirect
from .forms import PropietarioForm, PlacaForm, OficinaForm,VehiculoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.

def registroHome(request):
    return render(request,"registroHome.html")

@login_required
def registroOficina(request):
    oficina_form = OficinaForm()
    if request.method == "POST":
        oficina_form = OficinaForm(data=request.POST)
        if oficina_form.is_valid():
            oficina_form.save()
            return redirect(reverse("formOficina")+"?ok")
        else:
            return redirect(reverse("formOficina")+"?error")
    return render(request,"registroOficina.html",{"form":oficina_form})

@login_required
def registroPlaca(request):
    placa_form = PlacaForm()
    if request.method == "POST":
        placa_form = PlacaForm(data=request.POST)
        if placa_form.is_valid():
            placa_form.save()
            return redirect(reverse("registroPlaca")+"?ok")
        else:
            return redirect(reverse("registroPlaca")+"?error")
    return render (request,"registroPlaca.html",{"form":placa_form})

@login_required
def registroPropietario(request):
    propietario_form = PropietarioForm()
    if request.method =="POST":
        propietario_form = PropietarioForm(data= request.POST)
        if propietario_form.is_valid():
            propietario_form.save()
            return redirect(reverse("registroPropietario")+"?ok")
        else:
            return redirect(reverse("registroPropietario")+"?error")
    return render (request,"registroPropietario.html",{"form":propietario_form})

@login_required
def registroVehiculo(request):
    vehiculo_form = VehiculoForm()
    if request.method =="POST":
        vehiculo_form = VehiculoForm(data= request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect(reverse("registroVehiculo")+"ok")
        else:
            return redirect(reverse("registroVehiculo")+"error")
    return render (request,"registroVehiculo.html",{"form":vehiculo_form})


def exit(request):
    logout(request)
    return redirect ("index")

def register (request):
    data={
        "form": forms.CustomUserCreationForm()
    }
    return render (request,"registration/register.html",data)
