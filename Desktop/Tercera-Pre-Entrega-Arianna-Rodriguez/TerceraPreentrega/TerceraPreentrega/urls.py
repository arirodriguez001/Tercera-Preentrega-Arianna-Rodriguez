"""TerceraPreentrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservas import views


urlpatterns = [
    path('', views.listar_habitaciones, name='home'),
    path('habitaciones/<int:pk>/', views.detalle_habitacion, name='detalle_habitacion'),
    path('habitaciones/crear/', views.crear_habitacion, name='crear_habitacion'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/<int:pk>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/buscar/', views.buscar_reserva, name='buscar_reserva'),
    path('reservas/resultados_busqueda/', views.resultados_busqueda, name='resultados_busqueda'),
]
