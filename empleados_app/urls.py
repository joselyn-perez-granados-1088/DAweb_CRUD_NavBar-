from django.urls import path
from empleados_app import views

urlpatterns = [
    path('Empleados',views.inicio_vistaEmpleados,name="Empleados"),
    path("registrarEmpleado/",views.registrarEmpleado,name="registrarEmpleado"),
    path("seleccionarEmpleado/<codigo>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("borrarEmpleado/<codigo>",views.borrarEmpleado,name="borrarEmpleado"),
    path("editarEmpleado/",views.editarEmpleado,name="editarEmpleado")
]
