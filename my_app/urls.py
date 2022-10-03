from unicodedata import name
from django.urls import path
from my_app import views

urlpatterns = [

    path("", views.inicio, name = "inicio"),
    path("inicio/", views.inicio),
    path("nosotros/", views.nosotros, name = "nosotros"),
    path("blogs/", views.blogs, name = "blogs"),
    path("otros/", views.otros, name = "otros"),
    path("mascota/", views.mascotas, name = "mascotas"),
    # path("login/", views.login_request, name = "Login"),
    
]