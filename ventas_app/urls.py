from django.urls import path
from ventas_app import views

urlpatterns = [
    path('Ventas',views.inicio_vistaVentas,name="Ventas"),
    path("registrarVenta/",views.registrarVenta,name="registrarVenta"),
    path("seleccionarVenta/<factura>",views.seleccionarVenta,name="seleccionarVenta"),
    path("borrarVenta/<factura>",views.borrarVenta,name="borrarVenta"),
    path("editarVenta/",views.editarVenta,name="editarVentar")
]
