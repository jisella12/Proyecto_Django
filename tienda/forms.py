from django import forms
from .models import Contacto, Libro

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo","tipoConsulta", "mensaje"]

        """ incluye todo lo del modelo """
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'