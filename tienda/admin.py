from django.contrib import admin
from .models import Autor, Libro, Contacto
# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Contacto)