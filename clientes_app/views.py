from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarClientes.html',{"misclientes":losclientes})

def registrarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    numero=request.POST["txtnumero"]
    direccion=request.POST["txtdireccion"]
    interes=request.POST["txtinteres"]
    historial=request.POST["txthistorial"]
    email=request.POST["txtemail"]

    guardarcliente=Cliente.objects.create(codigo=codigo,nombre=nombre,numero=numero,direccion=direccion,interes=interes,historial=historial,email=email) 

    return redirect('Cliente')

def seleccionarCliente(request,codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    return render(request,"editarCliente.html",{"misclientes":cliente})

def editarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]    
    numero=request.POST["txtnumero"]
    direccion=request.POST["txtdireccion"]
    interes=request.POST["txtinteres"]
    historial=request.POST["txthistorial"]
    email=request.POST["txtemail"]

    cliente=Cliente.objects.get(codigo=codigo)

    cliente.numero=numero
    cliente.nombre=nombre
    cliente.direccion=direccion
    cliente.interes=interes
    cliente.historial=historial
    cliente.email=email
    cliente.save()

    return redirect('Cliente')

def borrarCliente(request,codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    cliente.delete()

    return redirect("Cliente")