from django.http import HttpResponse
from django.shortcuts import render
from my_app.forms import mascotas
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):

        return render (request, "my_app/inicio.html")

def nosotros(request):

        return render (request, "my_app/nosotros.html")

def blogs(request):

        return render (request, "my_app/blogs.html")

def otros(request):

        return render (request, "my_app/otros.html")


def otros(request):

        return render (request, "my_app/otros.html")


def mascotas(request):
        if request.method == "POST":
                data_form = request.POST
                mascota = mascotas(nombre=data_form["nombre"], especie=data_form["especie"], edad=data_form["edad"])
                mascota.save
                return render(request, "my_app/inicio.html")

        return render (request, "my_app/mascota.html" )


# def login_request(request):

#         if request.method == "POST":
#                 form = AuthenticationForm(request, data = request.POST)

#                 if form.is_valid():
#                         usuario = form.cleaned.data.get("username")
#                         contra = form.cleaned.data.get("password")

#                         user = authenticate(username=usuario, password=contra)

#                         if user is not None:
#                                 login(request, user)
#                                 return render(request, "my_app/inicio.html", {"mensaje":f"bienvenido {usuario}"})
#                         else:
#                                 return render(request, "my_app/inicio.html", {"mensaje":"error"})
#                 else:
#                                 return render(request, "my_app/inicio.html", {"mensaje":"error dos"})
#         form = AuthenticationForm()
#         return render(request, "my_app/inicio.html", {"form":form})

