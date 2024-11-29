from django.urls import path
from proveedor_app import views

urlpatterns = [
    path('Proveedor',views.inicio_vistaProveedor,name="Proveedor"),
    path("registrarProveedor/",views.registrarProveedor,name="registrarProveedor"),
    path("seleccionarProveedor/<codigo>",views.seleccionarProveedor,name="seleccionarProveedor"),
    path("borrarProveedor/<codigo>",views.borrarProveedor,name="borrarProveedor"),
    path("editarProveedor/",views.editarProveedor,name="editarProveedor")
]
