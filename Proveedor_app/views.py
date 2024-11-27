from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.

def inicio_vistaProveedores(request):
    losproveedores = Proveedores.objects.all()

    return render(request,"gestionarProveedores.html",{"misproveedores":losproveedores})



def registrarProveedores(request):
    id_proveedor = request.POST["txtidproveedor"]
    nombre = request.POST["txtnombreproveedor"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    c_electronico = request.POST["txtcorreo"]
    stock = request.POST["txtstock"]

    guardarproveedor = Proveedores.objects.create(id_proveedor=id_proveedor, nombre=nombre,
                                              direccion=direccion, telefono=telefono, c_electronico=c_electronico, stock=stock)

    return redirect("proveedores")

def seleccionarProveedores(request, id_proveedor):
    proveedores = Proveedores.objects.get(id_proveedor = id_proveedor)

    return render(request,"editarProveedores.html",{"misproveedores":proveedores})


def editarProveedores(request):
    id_proveedor = request.POST["txtidproveedor"]
    nombre = request.POST["txtnombreproveedor"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    c_electronico = request.POST["txtcorreo"]
    stock = request.POST["txtstock"]

    proveedores = Proveedores.objects.get(id_proveedor = id_proveedor)
    proveedores.nombre = nombre
    proveedores.direccion = direccion
    proveedores.telefono = telefono
    proveedores.c_electronico = c_electronico
    proveedores.stock = stock

    proveedores.save()

    return redirect("proveedores")


def borrarProveedores(request, id_proveedor):
    clientes = Proveedores.objects.get(id_proveedor = id_proveedor)
    clientes.delete()

    return redirect("proveedores")