# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect, Http404
# from addPage.models import Bus
# from datetime import timedelta, datetime
# from django.http import HttpResponse, JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# # Create your views here.
# def bus_list(request):
#     buses=Bus.objects.all()
#     return render(request,'home.html',{'buses':buses})


# def add_bus(request):
#     if request.method=='POST':
#         bus_number=request.POST.get('bus-number')
#         brand=request.POST.get('brand')
#         no_of_seats=request.POST.get('no-of-seats')
#         trip=request.POST.get('trip') 
#         trip_duration=request.POST.get('trip-duration')
#         conductor=request.POST.get('conductor')
#         driver=request.POST.get('driver')
        
#         if bus_number and brand and no_of_seats and trip and trip_duration and conductor and driver:
#             hours, minutes, seconds,=map(int, trip_duration.split(':'))
#             trip_duration=timedelta(hours=hours, minutes=minutes, seconds=seconds)
#             Bus.objects.create(
#                 bus_number=bus_number,
#                 brand=brand,
#                 no_of_seats=no_of_seats,
#                 trip=trip,
#                 trip_duration=trip_duration,
#                 conductor=conductor,
#                 driver=driver,
#             ) 
#             return redirect(bus_list)      
#     return render(request, 'add.html')
# def delete_bus(request, bus_id):
#     try:
#         bus = Bus.objects.get(id=bus_id)
#     except Bus.DoesNotExist:
#         raise Http404("Bus not found")

#     if request.method == 'POST':
#         bus.delete()
#         return redirect(bus_list)  # Ensure 'bus_list' is a valid URL name
#     return render(request, 'delete.html', {'bus': bus})

# @api_view()
# def bus1_list(request):
#     movies=Bus.objects.all()
#     list1={'data':list(movies.values())}

#     return JsonResponse(list1)

# @api_view()
# def fetch_bus_less_than_31_seats(request):
#     buses = Bus.objects.filter(no_of_seats__lt=31)
#     list1 = {"data": list(buses.values())}
#     return JsonResponse(list1)

# @csrf_exempt
# @api_view(['PUT'])
# def update_bus_data(request):
#     """
#     API endpoint to update bus data based on the provided input.
#     """
#     try:
#         data = JSONParser().parse(request)
#         buses_to_update = data.get("data", [])

#         for bus_data in buses_to_update:
#             bus_id = bus_data.get("id")
#             if bus_id is not None:
#                 bus = Bus.objects.filter(id=bus_id).first()
#                 if bus:
#                     bus.bus_number = bus_data.get("bus_number", bus.bus_number)
#                     bus.brand = bus_data.get("brand", bus.brand)
#                     bus.no_of_seats = bus_data.get("no_of_seats", bus.no_of_seats)
#                     bus.trip = bus_data.get("trip", bus.trip)
#                     bus.trip_duration = bus_data.get("trip_duration", bus.trip_duration)
#                     bus.conductor = bus_data.get("conductor", bus.conductor)
#                     bus.driver = bus_data.get("driver", bus.driver)
#                     bus.save()  # Save changes to the database
#                 else:
#                     return JsonResponse({"error": f"Bus with id {bus_id} does not exist."}, status=404)

#         return JsonResponse({"message": "Bus data updated successfully."}, status=200)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)
   
    
    
    
    
    
    