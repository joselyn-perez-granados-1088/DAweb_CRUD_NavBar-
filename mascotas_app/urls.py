from django.urls import path
from mascotas_app import views

urlpatterns = [
    path('Mascota',views.inicio_vistaMascota,name="Mascota"),
    path("registrarMascota/",views.registrarMascota,name="registrarMascota"),
    path("seleccionarMascota/<codigo>",views.seleccionarMascota,name="seleccionarMascota"),
    path("borrarMascota/<codigo>",views.borrarMascota,name="borrarMascota"),
    path("editarMascota/",views.editarMascota,name="editarMascota"),
]
