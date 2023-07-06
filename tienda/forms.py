from django import forms
from .models import Autor, Contacto, Libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError
from django.core.validators import RegexValidator


from django import forms
from tienda.models import Contacto

class ContactoForm(forms.ModelForm):
    # Validaciones
    nombre = forms.CharField(min_length=5, max_length=20)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        if len(mensaje) < 10:
            raise forms.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return mensaje

    class Meta:
        model = Contacto
        fields = ["nombre", "email", "mensaje"]


        """ incluye todo lo del modelo """
 




class LibroForm(forms.ModelForm):
    #validaciones
    nombre = forms.CharField(min_length=3, max_length=30)
    isbn = forms.IntegerField(min_value=2, max_value=400000)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
  
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Libro.objects.filter(nombre__iexact=nombre).exists()
    
        if existe:
          raise ValidationError("Este nombre ya existe")
        return nombre



    class Meta:
        model = Libro
        fields = '__all__'

class CustomUserCeationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


class RegistroForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=20, required=True)
    primer_nombre = forms.CharField(max_length=25, required=True)
    apellido = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)     

def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data['nombre_usuario']
        if User.objects.filter(nombre_usuario=nombre_usuario).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return nombre_usuario

def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError("El correo electrónico debe contener el símbolo '@'.")
        return email


##form autor 
class AutorForm(forms.ModelForm):
    #validaciones
    idAutor = forms.IntegerField(min_value=2, max_value=400000)
    nombre = forms.CharField(min_length=3, max_length=30)
    
    
  
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Autor.objects.filter(nombre__iexact=nombre).exists()
    
        if existe:
          raise ValidationError("Este nombre ya existe")
        return nombre
    
    
    class Meta:
        model = Autor
        fields = ["idAutor", "nombre"]