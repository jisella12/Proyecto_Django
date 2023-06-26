from django import forms
from .models import Contacto, Libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validator import MaxSizeFileValidator
from .validator import ValidationError 

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
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=1500000)

def clena_nombre(self):
    nombre = self.cleaned_data["nombre"]
    existe = Libro.objects.filter(nombre__iexact=nombre).exists()
    if existe:
        raise ValidationError("Este nombre Existe")
    else:
        return nombre 
  
    class Meta:
        model = Libro
        fields = '__all__'

class CustomUserCeationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]