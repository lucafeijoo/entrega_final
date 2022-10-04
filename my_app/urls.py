from unicodedata import name
from django.urls import path
from my_app import views

urlpatterns = [

    path("", views.inicio, name = "inicio"),
    path("inicio/", views.inicio),
    path("nosotros/", views.nosotros, name = "nosotros"),
    path("blogs/", views.blogs, name = "blogs"),
    
]