from django.urls import path 
from . import views

urlpatterns = [
    path('Inicio', views.Inicio, name='Inicio'), 
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('carro', views.carro, name='carro'),
    path('Login', views.Login, name='Login'), 
    path('productos', views.productos, name='productos'), 
    path('Registro', views.Registro, name='Registro'), 
    path('contacto', views.contacto, name='contacto'), 

]