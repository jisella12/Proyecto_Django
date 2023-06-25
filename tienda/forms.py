from django import forms
from .models import Contacto, Libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CustomUserCeationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]