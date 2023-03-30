from django.urls import path, include
from usuarios import views

urlpatterns = [
   path("",views.usuariosHome,name="homeUsuarios"),
]
