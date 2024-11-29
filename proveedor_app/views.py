from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.

def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()
    return render(request,'gestionarProveedores.html',{"misproveedores":losproveedores})

def registrarProveedor(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    productos=request.POST["txtproductos"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    frecuencia=request.POST["txtfrecuencia"]
    pagos=request.POST["txtpagos"]

    guardarproveedor=Proveedor.objects.create(codigo=codigo,nombre=nombre,productos=productos,direccion=direccion,telefono=telefono,frecuencia=frecuencia,pagos=pagos) 

    return redirect('Proveedor')

def seleccionarProveedor(request,codigo):
    proveedor=Proveedor.objects.get(codigo=codigo)
    return render(request,"editarProveedor.html",{"misproveedores":proveedor})

def editarProveedor(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    productos=request.POST["txtproductos"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    frecuencia=request.POST["txtfrecuencia"]
    pagos=request.POST["txtpagos"]

    proveedor=Proveedor.objects.get(codigo=codigo)

    proveedor.nombre=nombre
    proveedor.productos=productos
    proveedor.direccion=direccion
    proveedor.telefono=telefono
    proveedor.frecuencia=frecuencia
    proveedor.pagos=pagos
    proveedor.save()

    return redirect('Proveedor')

def borrarProveedor(request,codigo):
    proveedor=Proveedor.objects.get(codigo=codigo)
    proveedor.delete()

    return redirect("Proveedor")