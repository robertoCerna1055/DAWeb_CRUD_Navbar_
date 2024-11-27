from django.shortcuts import render,redirect
from .models import Empleado

# Create your views here.

def inicio_vistaEmpleados(request):
    losclientes = Empleado.objects.all()

    return render(request,"gestionarEmpleado.html",{"misempleados":losclientes})



def registrarEmpleado(request):
    id_empleado = request.POST["txtidempleado"]
    nombre = request.POST["txtnombreempleado"]
    apellido = request.POST["txtapellido"]
    cargo = request.POST["txtcargo"]
    telefono = request.POST["txttelefono"]
    c_electronico = request.POST["txtcorreo"]
    fecha_contratacion = request.POST["txtfechacontratacion"]

    guardarcliente = Empleado.objects.create(id_empleado=id_empleado, nombre=nombre, apellido=apellido,
                                              cargo=cargo, telefono=telefono, c_electronico=c_electronico, fecha_contratacion=fecha_contratacion)

    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleados = Empleado.objects.get(id_empleado = id_empleado)

    return render(request,"editarEmpleado.html",{"misempleados":empleados})


def editarEmpleado(request):
    id_empleado = request.POST["txtidempleado"]
    nombre = request.POST["txtnombreempleado"]
    apellido = request.POST["txtapellido"]
    cargo = request.POST["txtcargo"]
    telefono = request.POST["txttelefono"]
    c_electronico = request.POST["txtcorreo"]
    fecha_contratacion = request.POST["txtfechacontratacion"]

    empleado = Empleado.objects.get(id_empleado = id_empleado)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.cargo = cargo
    empleado.telefono = telefono
    empleado.c_electronico = c_electronico
    empleado.fecha_contratacion = fecha_contratacion

    empleado.save()

    return redirect("empleados")


def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado = id_empleado)
    empleado.delete()

    return redirect("empleados")