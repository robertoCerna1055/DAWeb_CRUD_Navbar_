from django.shortcuts import render,redirect
from .models import Clientes

# Create your views here.

def inicio_vistaClientes(request):
    losclientes = Clientes.objects.all()

    return render(request,"gestionarCliente.html",{"misclientes":losclientes})



def registrarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombrecliente"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    c_electronico = request.POST["txtcorreo"]
    fecha_nacimiento = request.POST["txtfechanacimiento"]

    guardarcliente = Clientes.objects.create(id_cliente=id_cliente, nombre=nombre, apellidos=apellidos,
                                              direccion=direccion, telefono=telefono, c_electronico=c_electronico, fecha_nacimiento=fecha_nacimiento)

    return redirect("clientes")

def seleccionarCliente(request, id_cliente):
    clientes = Clientes.objects.get(id_cliente = id_cliente)

    return render(request,"editarCliente.html",{"misclientes":clientes})


def editarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombrecliente"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    c_electronico = request.POST["txtcorreo"]
    fecha_nacimiento = request.POST["txtfechanacimiento"]

    cliente = Clientes.objects.get(id_cliente = id_cliente)
    cliente.nombre = nombre
    cliente.apellidos = apellidos
    cliente.direccion = direccion
    cliente.telefono = telefono
    cliente.c_electronico = c_electronico
    cliente.fecha_nacimiento = fecha_nacimiento

    cliente.save()

    return redirect("clientes")


def borrarCliente(request, id_cliente):
    clientes = Clientes.objects.get(id_cliente = id_cliente)
    clientes.delete()

    return redirect("clientes")