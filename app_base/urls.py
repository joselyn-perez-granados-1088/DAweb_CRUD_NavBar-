from django.urls import path
from app_base import views


urlpatterns = [
       #inicio mascotas
    path('', views.inicio),

]