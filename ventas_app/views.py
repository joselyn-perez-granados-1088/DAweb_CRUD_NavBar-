from django.shortcuts import render,redirect
from .models import Venta
# Create your views here.

def inicio_vistaVentas(request):
    lasventas=Venta.objects.all()
    return render(request,'gestionarVentas.html',{"misventas":lasventas})

def registrarVenta(request):
    factura=request.POST["txtfactura"]
    idcliente=request.POST["txtidcliente"]
    producto=request.POST["txtproducto"]
    empleado=request.POST["txtempleado"]
    fecha=request.POST["txtfecha"]
    cantidad=request.POST["txtcantidad"]
    metodo=request.POST["txtmetodo"]

    guardarventa=Venta.objects.create(factura=factura,idcliente=idcliente,producto=producto,empleado=empleado,fecha=fecha,cantidad=cantidad,metodo=metodo) 

    return redirect('Ventas')

def seleccionarVenta(request,factura):
    venta=Venta.objects.get(factura=factura)
    return render(request,"editarVenta.html",{"misventas":venta})

def editarVenta(request):
    factura=request.POST["txtfactura"]
    idcliente=request.POST["txtidcliente"]
    producto=request.POST["txtproducto"]
    empleado=request.POST["txtempleado"]
    fecha=request.POST["txtfecha"]
    cantidad=request.POST["txtcantidad"]
    metodo=request.POST["txtmetodo"]

    venta=Venta.objects.get(factura=factura)

    venta.factura=factura
    venta.idcliente=idcliente
    venta.producto=producto
    venta.empleado=empleado
    venta.fecha=fecha
    venta.cantidad=cantidad
    venta.metodo=metodo
    venta.save()

    return redirect('Ventas')

def borrarVenta(request,factura):
    venta=Venta.objects.get(factura=factura)
    venta.delete()

    return redirect("Ventas")