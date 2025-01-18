from django.shortcuts import render
from rest_framework.response import Response
from addPage.api.serializers import BusSerializer
# Create your views here.
from django.shortcuts import render, redirect, Http404
from addPage.models import Bus
from datetime import timedelta, datetime
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def bus_list(request):
    buses=Bus.objects.all()
    return render(request,'home.html',{'buses':buses})


def add_bus(request):
    if request.method=='POST':
        bus_number=request.POST.get('bus-number')
        brand=request.POST.get('brand')
        no_of_seats=request.POST.get('no-of-seats')
        trip=request.POST.get('trip') 
        trip_duration=request.POST.get('trip-duration')
        conductor=request.POST.get('conductor')
        driver=request.POST.get('driver')
        
        if bus_number and brand and no_of_seats and trip and trip_duration and conductor and driver:
            hours, minutes, seconds,=map(int, trip_duration.split(':'))
            trip_duration=timedelta(hours=hours, minutes=minutes, seconds=seconds)
            Bus.objects.create(
                bus_number=bus_number,
                brand=brand,
                no_of_seats=no_of_seats,
                trip=trip,
                trip_duration=trip_duration,
                conductor=conductor,
                driver=driver,
            ) 
            return redirect(bus_list)      
    return render(request, 'add.html')
def delete_bus(request, bus_id):
    try:
        bus = Bus.objects.get(id=bus_id)
    except Bus.DoesNotExist:
        raise Http404("Bus not found")

    if request.method == 'POST':
        bus.delete()
        return redirect(bus_list)  # Ensure 'bus_list' is a valid URL name
    return render(request, 'delete.html', {'bus': bus})

@api_view()
def bus1_list(request):
    buses=Bus.objects.all()
    data1=BusSerializer(buses, many=True)
    return Response(data1.data)

@api_view()
def fetch_bus_less_than_31_seats(request):
    bus = Bus.objects.filter(no_of_seats__lt=31)
    data1=BusSerializer(bus, many=True)
    return Response(data1.data)

    
    
    
    
    