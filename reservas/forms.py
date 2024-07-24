# reservas/forms.py

from django import forms
from .models import Reserva

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'fono', 'fecha', 'hora', 'personas', 'estado', 'observaciones']
        
        widgets = {
            'fecha': DateInput(format='%d-%m-%Y'),
            'hora': forms.TimeInput(format='%H:%M'),
        }