from django import forms
from .models import Reservation
from datetime import date, datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'es_ES')

class ReserveTableForm(forms.ModelForm):
    name = forms.CharField(required=True, label="Nombre")
    email = forms.EmailField(required=True, label="Email")
    phone = forms.IntegerField(required=True, label="Teléfono")
    number_of_persons = forms.IntegerField(required=True, label="¿Para cuántos?")

    dateList = [((datetime.today() + timedelta(days=x)).strftime("%Y-%m-%d"), "{} de {}".format((datetime.today() + timedelta(days=x)).strftime("%A %d").capitalize(), (datetime.today() + timedelta(days=x)).strftime("%B"))) for x in range(7)]
    timeList = [(('{}:00').format((8 + x)), ('{}:00').format((8 + x))) for x in range(11)]
    date = forms.ChoiceField(required=True, label="Día", widget=forms.Select(attrs={'class': 'custom-select'}), choices=dateList)
    time = forms.ChoiceField(required=True, label="Hora", widget=forms.Select(attrs={'class': 'custom-select'}), choices=timeList)    

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'number_of_persons', 'date', 'time']