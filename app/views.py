from django.shortcuts import redirect, render
from .models import Producto
# Create your views here.

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

def carrito(request):
    return render(request, 'app/carrito.html')


