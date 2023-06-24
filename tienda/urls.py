from django.urls import path 
from .views import Inicio, Nosotros, carro, Login, productos, Registro, contacto, AgregarLibro, listar_libro

urlpatterns = [
    path('Inicio/', Inicio, name='Inicio'), 
    path('Nosotros/', Nosotros, name='Nosotros'),
    path('carro/', carro, name='carro'),
    path('Login/', Login, name='Login'), 
    path('productos/', productos, name='productos'), 
    path('Registro/', Registro, name='Registro'), 
    path('contacto/', contacto, name='contacto'), 
    path('agregar-libro/', AgregarLibro, name='agregar'), 
    path('listar-libro/', listar_libro, name='listar'), 
]