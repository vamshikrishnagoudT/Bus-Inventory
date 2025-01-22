from django.urls import path
from addPage.api.views import *

urlpatterns = [
    path('', bus_list, name="bus-list"),
    path('add/', add_bus, name="add-bus"),
    path('delete/<int:bus_id>/', delete_bus, name='delete-bus'),
    path('list/', bus1_list, name="bus1-list"),
    path('less_than_31_seats/',fetch_bus_less_than_31_seats),
    path('<int:pk>/', bus_details, name="bus-details"),
]
