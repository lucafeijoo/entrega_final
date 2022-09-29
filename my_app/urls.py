from django.urls import path
from my_app import views

urlpatterns = [

    path("inicio", views.inicio),
    path("nosotros", views.nosotros),
    path("blogs", views.blogs),
    
]