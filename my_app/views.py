from typing import Dict
from urllib import request
from my_app.models import Blog
from my_app.forms import BlogForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def inicio(request):

        return render (request, "my_app/inicio.html")


def nosotros(request):

        return render (request, "my_app/nosotros.html")


class BlogList(ListView):
    model = Blog
    template_name = "my_app/blogs.html"


class BlogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')


@login_required
def crear_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)

        if form.is_valid():
            blog = form.save()
            blog.autor = request.user
            blog.save()
            return redirect(reverse('blogs'))
    
    else:
        
        form = BlogForm()
    
    return render(request, "my_app/form_blogs.html", {"form": form})


class BlogUpdate(LoginRequiredMixin,UpdateView):
    model = Blog
    success_url = reverse_lazy('blogs')
    fields  = [  'titulo', 'subtitulo', 'cuerpo']


class BlogDetail(DetailView):
    model = Blog
    template_name = "my_app/blogs_sabermas.html"