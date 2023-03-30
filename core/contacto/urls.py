from django.urls import path, include
from contacto import views

urlpatterns = [
   path("",views.contactoHome,name="homeContacto"),
   path("form/",views.contactoForm,name="formContacto"),
]
