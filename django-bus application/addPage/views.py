from django.shortcuts import render, redirect
from addPage.models import Bus
from addPage.forms import *
# Create your views here.
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'home.html', {'buses': buses})

def add_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'add.html', {'form': form})