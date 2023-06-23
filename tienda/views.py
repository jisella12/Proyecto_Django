from django.shortcuts import render
from .forms import ContactoForm
# Create your views here.
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

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'tienda/contacto.html',data)