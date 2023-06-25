from django import forms
from .models import Contacto, Libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    #validaciones

    nombre = forms.CharField(min_length=3, max_length=30)
    
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo","tipoConsulta", "mensaje"]

        """ incluye todo lo del modelo """
        fields = '__all__'

class LibroForm(forms.ModelForm):
    #validaciones
    nombre = forms.CharField(min_length=3, max_length=30)
    isbn = forms.IntegerField(min_value=2, max_value=400000)
    imagen = forms.ImageField(required=False)
  
    class Meta:
        model = Libro
        fields = '__all__'

class CustomUserCeationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]