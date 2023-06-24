from django.shortcuts import render
from .forms import ContactoForm, LibroForm
from .models import Libro
# Create your views here.


def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Enviado"
        else:
            data["form"] = formulario

    return render(request, 'tienda/contacto.html',data)

def Inicio(request):
    context={}
    return render(request, 'tienda/Inicio.html', context)

def Nosotros(request):
    return render(request, 'tienda/Nosotros.html')

def carro(request):
    return render(request, 'tienda/carro.html')

def Login(request):
    return render(request, 'tienda/Login.html')

def productos(request):
    return render(request, 'tienda/productos.html',)

def Registro(request):
    return render(request, 'tienda/Registro.html')
def fantasia(request):
    return render(request, 'tienda/fantasia.html')

def RomanceClasico(request):
    return render(request, 'tienda/RomanceClasico.html')


""" agregar, modificar, listar """
def AgregarLibro(request):
    data = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Guardado Correctamente"
        else:
            data ["form"] = formulario

    return render(request, 'tienda/Libros/agregar.html',data)

def libroList(request):
    libros = Libro.objects.all()
    contexto={
        'libros':libros
    }
    return render(request, 'tienda/Libros/listar.html',contexto)

