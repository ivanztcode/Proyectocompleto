from django.urls import path, include
from registro import views

urlpatterns = [
   path("",views.registroHome,name="homeRegistro"),
   path("oficina/",views.registroOficina,name="formOficina"),
   path("placa/",views.registroPlaca,name="formPlaca"),
   path("propietario/",views.registroPropietario,name="formPropietario"),
   path("vehiculo/",views.registroVehiculo,name="formVehiculo"),
   path("logout/",views.exit,name="exit"),
   path("register/",views.register,name="register"),

]
