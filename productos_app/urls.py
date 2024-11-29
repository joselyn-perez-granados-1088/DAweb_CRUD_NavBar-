from django.urls import path
from productos_app import views

urlpatterns = [
    path('Producto',views.inicio_vistaProducto,name="Producto"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<codigo>",views.seleccionarProducto,name="seleccionarProducto"),
    path("borrarProducto/<codigo>",views.borrarProducto,name="borrarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto")
]
