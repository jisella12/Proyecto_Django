from django.urls import path 
from .views import AgregarAutor, Inicio, Nosotros,  Login, contactoList, productos, Registro, contacto, AgregarLibro, libroList, fantasia, RomanceClasico, modificarLibro, eliminarLibro,  registro, carrito



urlpatterns = [
    path('Inicio/', Inicio, name='Inicio'), 
    path('Nosotros/', Nosotros, name='Nosotros'),
    path('Login/', Login, name='Login'), 
    path('productos/', productos, name='productos'), 
    path('Registro/', Registro, name='Registro'), 
    path('contacto/', contacto, name='contacto'), 
    path('agregar-libro/', AgregarLibro, name='agregar'), 
    path('libroList/', libroList, name='libroList'), 
    path('fantasia/', fantasia, name='fantasia'), 
    path('RomanceClasico/', RomanceClasico, name='RomanceClasico'), 
    path('modificarLibro/<int:id>/', modificarLibro, name='modificarLibro'),

    path('eliminarLibro/<id>/', eliminarLibro, name='eliminarLibro'), 
    path('registro/', registro, name='registro'), 
    path('carrito/', carrito, name='carrito'),
    path('agregar-Autor/', AgregarAutor, name='agregarAutor'), 
    path('contactoList/', contactoList, name='contactoList'), 






]