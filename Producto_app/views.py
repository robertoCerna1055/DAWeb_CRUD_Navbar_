from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def inicio_vistaProductos(request):
    losproductos = Producto.objects.all()

    return render(request,"gestionarProductos.html",{"misproductos":losproductos})



def registrarProductos(request):
    id_producto = request.POST["txtidproducto"]
    nombre = request.POST["txtnombreproducto"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    categoria = request.POST["txtcategoria"]
    material = request.POST["txtmaterial"]
    stock = request.POST["txtstock"]
    id_proveedores = request.POST["txtidproveedores"]

    guardarproducto = Producto.objects.create(id_producto=id_producto, nombre=nombre, descripcion=descripcion,
                                              precio=precio, categoria=categoria, material=material, stock=stock, id_proveedores=id_proveedores)

    return redirect("productos")

def seleccionarProductos(request, id_producto):
    clientes = Producto.objects.get(id_producto = id_producto)

    return render(request,"editarProductos.html",{"misproductos":clientes})


def editarProductos(request):
    id_producto = request.POST["txtidproducto"]
    nombre = request.POST["txtnombreproducto"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    categoria = request.POST["txtcategoria"]
    material = request.POST["txtmaterial"]
    stock = request.POST["txtstock"]
    id_proveedores = request.POST["txtidproveedores"]

    productos = Producto.objects.get(id_producto = id_producto)
    productos.nombre = nombre
    productos.descripcion = descripcion
    productos.precio = precio
    productos.categoria = categoria
    productos.material = material
    productos.stock = stock
    productos.id_proveedores = id_proveedores

    productos.save()

    return redirect("productos")


def borrarProductos(request, id_producto):
    productos = Producto.objects.get(id_producto = id_producto)
    productos.delete()

    return redirect("productos")