from django.urls import path
from addPage.views import *

urlpatterns = [
    path('', bus_list, name="bus-list"),
    path('add/', add_bus, name="add-bus"),
    path('delete/<int:bus_id>/', delete_bus, name='delete-bus'),
    path('api/', bus1_list),
    path('less_than_31_seats/',fetch_bus_less_than_31_seats)
   
]
