from unicodedata import name
from django.urls import path
from Accounts import views

urlpatterns = [

path('login/', views.login_request, name = "Login"),
path('register/', views.register, name = "Registro"),

]