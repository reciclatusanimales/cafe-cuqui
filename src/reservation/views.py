from django.shortcuts import render
from .models import Reservation
from .forms import ReserveTableForm

def reserve_table(request):
    form = ReserveTableForm()

    if request.method == 'POST':
        form = ReserveTableForm(request.POST)
        
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'reservation/reservation.html', context)
