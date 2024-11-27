from django.shortcuts import render,redirect
from .models import Venta

# Create your views here.

def inicio_vistaVentas(request):
    lasventas = Venta.objects.all()

    return render(request,"gestionarVentas.html",{"misventas":lasventas})



def registrarVentas(request):
    id_venta = request.POST["txtidventa"]
    fecha_venta = request.POST["txtfechaventa"]
    id_cliente = request.POST["txtidcliente"]
    id_producto = request.POST["txtidproducto"]
    cantidad = request.POST["txtcantidad"]
    precio_unitario = request.POST["txtprecio"]
    forma_pago = request.POST["txtforma"]

    guardarventa = Venta.objects.create(id_venta=id_venta, fecha_venta=fecha_venta,
                                             id_producto=id_producto, id_cliente=id_cliente, 
                                              cantidad=cantidad, precio_unitario=precio_unitario, forma_pago=forma_pago)

    return redirect("ventas")

def seleccionarVenta(request, id_venta):
    ventas = Venta.objects.get(id_venta = id_venta)

    return render(request,"editarVentas.html",{"misventas":ventas})


def editarVentas(request):
    id_venta = request.POST["txtidventa"]
    fecha_venta = request.POST["txtfechaventa"]
    id_cliente = request.POST["txtidcliente"]
    id_producto = request.POST["txtidproducto"]
    cantidad = request.POST["txtcantidad"]
    precio_unitario = request.POST["txtprecio"]
    forma_pago = request.POST["txtforma"]

    venta = Venta.objects.get(id_venta = id_venta)
    venta.fecha_venta = fecha_venta
    venta.id_producto = id_producto
    venta.id_cliente = id_cliente
    venta.cantidad = cantidad
    venta.precio_unitario = precio_unitario
    venta.forma_pago = forma_pago

    venta.save()

    return redirect("ventas")


def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta = id_venta)
    venta.delete()

    return redirect("ventas")