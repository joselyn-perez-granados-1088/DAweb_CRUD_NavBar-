from django.urls import path
from clientes_app import views

urlpatterns = [
    path('Cliente',views.inicio_vistaCliente,name="Cliente"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<codigo>",views.seleccionarCliente,name="seleccionarCliente"),
    path("borrarCliente/<codigo>",views.borrarCliente,name="borrarCliente"),
    path("editarCliente/",views.editarCliente,name="editarCliente")
]
