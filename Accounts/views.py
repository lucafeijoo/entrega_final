from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from Accounts.forms import UserRegisterForm,UserUpdateForm

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


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('Login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('editar_usuario')
    template_name = 'Accounts/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user