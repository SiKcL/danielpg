# reservas/urls.py

from django.urls import path
from .views import lista_reservas, agregar_reserva, editar_reserva, eliminar_reserva

urlpatterns = [
    path('', lista_reservas, name='lista_reservas'),
    path('agregar/', agregar_reserva, name='agregar_reserva'),
    path('editar/<int:id>/', editar_reserva, name='editar_reserva'),
    path('eliminar/<int:id>/', eliminar_reserva, name='eliminar_reserva'),
]