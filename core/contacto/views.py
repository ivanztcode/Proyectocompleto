from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


# Create your views here.

def contactoHome(request):
    return render (request,"contactoHome.html")



def contactoForm(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect (reverse("formContacto")+"?ok")

        else:
            return redirect (reverse("formContacto")+"?error")
    return render (request,"contactoForm.html",{"form":contact_form})