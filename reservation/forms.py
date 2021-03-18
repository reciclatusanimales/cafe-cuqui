from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    name = forms.CharField(required=True, label="Nombre")
    email = forms.EmailField(required=True, label="Email")
    phone = forms.IntegerField(required=True, label="Teléfono")
    number_of_persons = forms.IntegerField(required=True, label="¿Para cuántos?")
    date = forms.DateField(required=True, label="Día")
    time = forms.TimeField(required=True, label="Hora")

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'number_of_persons', 'date', 'time']