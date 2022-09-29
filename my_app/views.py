from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):

        return HttpResponse("vista inicio")

def nosotros(request):

        return render (request, "proyectofinal/nosotros.html")

def blogs(request):

        return HttpResponse("vista blogs")