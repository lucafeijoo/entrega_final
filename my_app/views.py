from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):

<<<<<<< HEAD
        return HttpResponse("vista inicio")
=======
        return render(request, "my_app/base.html")
>>>>>>> f78d110 (Hecho el static y la plantilla base)

def nosotros(request):

        return render (request, "proyectofinal/nosotros.html")

def blogs(request):

        return HttpResponse("vista blogs")