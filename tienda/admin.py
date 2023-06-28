from django.contrib import admin
from .models import Autor, Libro, Contacto
from .forms import LibroForm
# Register your models here.

class LibroAdmin(admin.ModelAdmin): 
    form = LibroForm 






admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Contacto)
