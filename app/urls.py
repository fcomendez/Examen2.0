from django.urls import path
from .views import productos, carrito

urlpatterns = [
    path('', productos, name="productos"),
    path('carrito/', carrito, name="carrito"),
]
