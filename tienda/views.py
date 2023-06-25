from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, LibroForm
from .models import Libro
from django.contrib import messages
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

""" agregar """

def AgregarLibro(request):
    data = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Registrado")
        else:
            data ["form"] = formulario

    return render(request, 'tienda/Libros/agregar.html',data)

""" Listar """

def libroList(request):
    libros = Libro.objects.all()
    contexto={
        'libros':libros
    }
    return render(request, 'tienda/Libros/listar.html',contexto)

""" Modificar """
def modificarLibro(request, id):

    libro = get_object_or_404(Libro, id=id)
    data = {
        'form': LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="libroList")
        else:
            data ["form"] = formulario
    return render(request, 'tienda/Libros/modificar.html',data)

""" Eliminar """
def eliminarLibro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="libroList")