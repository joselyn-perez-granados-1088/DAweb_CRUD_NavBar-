from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.

def inicio_vistaEmpleados(request):
    losempleados=Empleado.objects.all()
    return render(request,'gestionarEmpleados.html',{"misempleados":losempleados})

def registrarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    cargo=request.POST["txtcargo"]
    horario=request.POST["txthorario"]
    salario=request.POST["txtsalario"]
    experiencia=request.POST["txtexperiencia"]
    certificaciones=request.POST["txtcertificaciones"]

    guardarempleado=Empleado.objects.create(codigo=codigo,nombre=nombre,cargo=cargo,horario=horario,salario=salario,experiencia=experiencia,certificaciones=certificaciones) 

    return redirect('Empleados')

def seleccionarEmpleado(request,codigo):
    empleado=Empleado.objects.get(codigo=codigo)
    return render(request,"editarEmpleado.html",{"misempleados":empleado})

def editarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    cargo=request.POST["txtcargo"]
    horario=request.POST["txthorario"]
    salario=request.POST["txtsalario"]
    experiencia=request.POST["txtexperiencia"]
    certificaciones=request.POST["txtcertificaciones"]

    empleado=Empleado.objects.get(codigo=codigo)

    empleado.nombre=nombre
    empleado.cargo=cargo
    empleado.horario=horario
    empleado.salario=salario
    empleado.experiencia=experiencia
    empleado.certificaciones=certificaciones
    empleado.save()

    return redirect('Empleados')

def borrarEmpleado(request,codigo):
    empleado=Empleado.objects.get(codigo=codigo)
    empleado.delete()

    return redirect("Empleados")