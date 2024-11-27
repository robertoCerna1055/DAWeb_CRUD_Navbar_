from django.shortcuts import render,redirect
from .models import Pedido

# Create your views here.

def inicio_vistaPedidos(request):
    lospedidos = Pedido.objects.all()

    return render(request,"gestionarPedidos.html",{"mispedidos":lospedidos})



def registrarPedidos(request):
    id_pedido = request.POST["txtidpedido"]
    fecha_pedido = request.POST["txtfechapedido"]
    id_cliente = request.POST["txtidcliente"]
    total_pedido = request.POST["txttotalpedido"]
    fecha_entrega = request.POST["txtfechaentrega"]
    direccion_entrega = request.POST["txtdireccion"]
    id_empleado = request.POST["txtidempleado"]

    guardarpedido = Pedido.objects.create(id_pedido=id_pedido, fecha_pedido=fecha_pedido, id_cliente=id_cliente,
                                              total_pedido=total_pedido, fecha_entrega=fecha_entrega, direccion_entrega=direccion_entrega, id_empleado=id_empleado)

    return redirect("pedidos")

def seleccionarPedidos(request, id_pedido):
    pedidos = Pedido.objects.get(id_pedido = id_pedido)

    return render(request,"editarPedidos.html",{"mispedidos":pedidos})


def editarPedidos(request):
    id_pedido = request.POST["txtidpedido"]
    fecha_pedido = request.POST["txtfechapedido"]
    id_cliente = request.POST["txtidcliente"]
    total_pedido = request.POST["txttotalpedido"]
    fecha_entrega = request.POST["txtfechaentrega"]
    direccion_entrega = request.POST["txtdireccion"]
    id_empleado = request.POST["txtidempleado"]

    pedidos = Pedido.objects.get(id_pedido = id_pedido)
    pedidos.fecha_pedido = fecha_pedido
    pedidos.id_cliente = id_cliente
    pedidos.total_pedido = total_pedido
    pedidos.fecha_entrega = fecha_entrega
    pedidos.direccion_entrega = direccion_entrega
    pedidos.id_empleado = id_empleado

    pedidos.save()

    return redirect("pedidos")


def borrarPedidos(request, id_pedido):
    pedidos = Pedido.objects.get(id_pedido = id_pedido)
    pedidos.delete()

    return redirect("pedidos")