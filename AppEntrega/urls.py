from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('', inicio),
    path('clientes/', clientes, name="Clientes"),
    path('proveedores/', proveedores, name='Proveedores'),
    path('articulos/', articulos, name='Articulos'),
    path('servicios/', servicios, name='Servicios'),
    path('setCliente/', setCliente, name="Agregar Clientes"),
    path('setProveedor/', setProveedor, name="Agregar Proveedores"),
    path('setArticulo/', setArticulo, name="Agregar Articulos"),
    path('setServicio/', setServicio, name="Agregar Servicios"),


]