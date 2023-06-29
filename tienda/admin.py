from django.contrib import admin
from .models import Autor, Libro, Contacto, ElementoCarrito, Carrito
from .forms import LibroForm
# Register your models here.

class LibroAdmin(admin.ModelAdmin): 
    form = LibroForm 






admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Contacto)
admin.site.register(ElementoCarrito)
admin.site.register(Carrito)
