from django.urls import path 
from .views import Inicio, Nosotros, carro, Login, productos, Registro, contacto

urlpatterns = [
    path('Inicio/', Inicio, name='Inicio'), 
    path('Nosotros/', Nosotros, name='Nosotros'),
    path('carro/', carro, name='carro'),
    path('Login/', Login, name='Login'), 
    path('productos/', productos, name='productos'), 
    path('Registro/', Registro, name='Registro'), 
    path('contacto/', contacto, name='contacto'), 
    


]