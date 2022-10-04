from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):

        return render (request, "my_app/inicio.html")

def nosotros(request):

        return render (request, "my_app/nosotros.html")

def blogs(request):

        return render (request, "my_app/blogs.html")


def login_request(request):

        if request.method == "POST":
                form = AuthenticationForm(request, data = request.POST)

                if form.is_valid():
                        usuario = form.cleaned.data.get("username")
                        contra = form.cleaned.data.get("password")

                        user = authenticate(username=usuario, password=contra)

                        if user is not None:
                                login(request, user)
                                return render(request, "my_app/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                        else:
                                return render(request, "my_app/inicio.html", {"mensaje":"Error, datos erroneos"})
                else:
                                return render(request, "my_app/inicio.html", {"mensaje":"Error, formulario erroneo"})
        form = AuthenticationForm()
        
        return render(request, "my_app/inicio.html", {"form":form})

