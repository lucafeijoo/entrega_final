from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from Accounts.forms import UserRegisterForm

def login_request(request):

        if request.method == "POST":
                form = AuthenticationForm(request, data = request.POST)

                if form.is_valid():
                        usuario = form.cleaned_data.get("username")
                        contra = form.cleaned_data.get("password")

                        user = authenticate(username=usuario, password=contra)

                        if user is not None:
                                login(request, user)
                                return render(request, "my_app/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                        else:
                                return render(request, "Accounts/login.html", {"mensaje":"Error, datos erroneos"})
                else:
                                return render(request, "Accounts/login.html", {"mensaje":"Error, formulario erroneo"})
        form = AuthenticationForm()
        
        return render(request, "Accounts/login.html", {"form":form})


def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "my_app/inicio.html", {"mensaje": "Usuario creado correctamente"})
        else:
            mensaje = 'Error en el registro'
    formulario = UserRegisterForm()
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "Accounts/register.html", context=context)