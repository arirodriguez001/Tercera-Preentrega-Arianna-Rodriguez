from django.shortcuts import render, redirect, get_object_or_404
from .models import Habitacion, Cliente, Reserva
from .forms import HabitacionForm, ClienteForm, ReservaForm, BuscarReservaForm


# Create your views here.

def listar_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'reservasa/listar_habitaciones.html', {'habitaciones': habitaciones})

def detalle_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    return render(request, 'reservas/detalle_habitacion.html', {'habitacion': habitacion})

def crear_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_habitaciones')
    else:
        form = HabitacionForm()
    return render(request, 'reservas/crear_habitacion.html', {'form': form})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'reservas/listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'reservas/detalle_cliente.html', {'cliente': cliente})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'reservas/crear_cliente.html', {'form': form})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reservas/detalle_reserva.html', {'reserva': reserva})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})

def buscar_reserva(request):
    if request.method == 'POST':
        form = BuscarReservaForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            reservas = Reserva.objects.filter(cliente__nombre__icontains=cliente,
                                               fecha_inicio__lte=fecha_inicio,
                                               fecha_fin__gte=fecha_fin)
            return render(request, 'reservas/resultados_busqueda.html', {'reservas': reservas})
    else:
        form = BuscarReservaForm()
    return render(request, 'reservas/buscar_reserva.html', {'form': form})
