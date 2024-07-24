# reservas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

def agregar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
        else:
            print(form.errors)  # Imprimir errores en la consola para depuración
    else:
        form = ReservaForm()
    return render(request, 'reservas/agregar_reserva.html', {'form': form})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/editar_reserva.html', {'form': form})

def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'reservas/eliminar_reserva.html', {'reserva': reserva})
