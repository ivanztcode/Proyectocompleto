from django.shortcuts import render

# Create your views here.
def usuariosHome(request):
    return render(request,"usuariosHome.html")