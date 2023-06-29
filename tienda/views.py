from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, LibroForm, CustomUserCeationForm
from .models import Carrito, Libro
from .carrito import Carrito
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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

def productos1(request):
    return render(request, 'tienda/productos1.html')

def carrito(request):
    return render(request, 'tienda/carrito.html')

def Nosotros(request):
    return render(request, 'tienda/Nosotros.html')

def Login(request):
    return render(request, 'tienda/Login.html')

def productos(request):
    libros = Libro.objects.all()
    data ={
        'libros': libros
    }
    return render(request, 'tienda/productos.html',data)

def Registro(request):
    return render(request, 'tienda/Registro.html')
def fantasia(request):
    libros = Libro.objects.all()
    data ={
        'libros': libros
    }
    return render(request, 'tienda/fantasia.html',data)

def RomanceClasico(request):
    libros = Libro.objects.all()
    data ={
        'libros': libros
    }
    return render(request, 'tienda/RomanceClasico.html',data)

""" agregar, modificar, listar """

""" agregar """
@permission_required('tienda.add_libro')
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
@permission_required('tienda.view_libro')
def libroList(request):
    libros = Libro.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(libros, 5)
        libros = paginator.page(page)
    except:
        raise Http404

    contexto={
        'entity':libros,
        'paginator': paginator
    }
    return render(request, 'tienda/Libros/listar.html',contexto)

""" Modificar """
@permission_required('tienda.change_libro')
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
@permission_required('tienda.delete_libro')
def eliminarLibro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="libroList")

def registro(request):
    data = {
        'form': CustomUserCeationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCeationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has Registrado Correctamente")
            return redirect(to="Inicio")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)



###carritoo
def tienda(request):
    productos = Libro.objects.all()
    return render(request, "carrito.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Libro.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Libro.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Libro.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos")