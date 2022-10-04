from unicodedata import name
from django.urls import path
from my_app import views

urlpatterns = [

    path("", views.inicio, name = "inicio"),
    path("inicio/", views.inicio),
    path("nosotros/", views.nosotros, name = "nosotros"),
    path("blogs/", views.BlogList.as_view(), name = "blogs"),
    path('crear/', views.crear_blog, name="crear"),
    path('sabermas/<int:pk>/', views.BlogDetail.as_view(), name="sabermas"),
    path('modificar/<int:pk>/', views.BlogUpdate.as_view(), name="modificar"),
    path('eliminar/<int:pk>/', views.BlogDelete.as_view(), name="eliminar"),
    
]