from django.contrib import admin

from tienda.forms import LibroForm
from .models import Autor, Libro, Contacto


class LibroAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo" "autor"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["autor", "nuevo"]
    list_per_page = 5
    form = LibroForm



# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Contacto)