from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import *
from AppEntrega.forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppEntrega/inicio.html")
def clientes(request):
    return render(request, "AppEntrega/clientes.html")
def proveedores(request):
    return render(request, "AppEntrega/proveedores.html")
def articulos(request):
    return render(request, "AppEntrega/articulos.html")
def servicios(request):
    return render(request, "AppEntrega/servicios.html")

def setCliente(request):
    if request.method == "POST":
 
            miFormulario = formSetCliente(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(nombre =informacion["nombre"], apellido =informacion["apellido"], email = informacion["email"])
                  cliente.save()
                  miFormulario = formSetCliente
                  return render(request, "AppEntrega/setCliente.html", {"miFormulario": miFormulario})
    else:
            miFormulario = formSetCliente
 
    return render(request, "AppEntrega/setCliente.html", {"miFormulario": miFormulario})

def setProveedor(request):
    if request.method == "POST":
 
            miFormulario = formSetProveedor(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  proveedor = Proveedor(nombre =informacion["nombre"], RUT =informacion["RUT"], email = informacion["email"])
                  proveedor.save()
                  miFormulario = formSetProveedor
                  return render(request, "AppEntrega/setProveedor.html", {"miFormulario": miFormulario})
    else:
            miFormulario = formSetProveedor
 
    return render(request, "AppEntrega/setProveedor.html", {"miFormulario": miFormulario})

def setArticulo(request):
    if request.method == "POST":
 
            miFormulario = formSetArticulo(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  articulo = Articulo(nombre =informacion["nombre"], nro=informacion["nro"], precio = informacion["precio"], vendedor= informacion["vendedor"])
                  articulo.save()
                  miFormulario = formSetArticulo
                  return render(request, "AppEntrega/setArticulo.html", {"miFormulario": miFormulario})
    else:
            miFormulario = formSetArticulo
 
    return render(request, "AppEntrega/setArticulo.html", {"miFormulario": miFormulario})

def setServicio(request):
    if request.method == "POST":
 
            miFormulario = formSetServicio(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  servicio = Servicio(descripcion=informacion["descripcion"], proveedor=informacion["proveedor"], precio=informacion["precio"])
                  servicio.save()
                  miFormulario = formSetServicio
                  return render(request, "AppEntrega/setServicio.html", {"miFormulario": miFormulario})
    else:
            miFormulario = formSetServicio
 
    return render(request, "AppEntrega/setServicio.html", {"miFormulario": miFormulario})