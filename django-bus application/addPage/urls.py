from django.urls import path
from addPage.views import bus_list, add_bus, delete_bus

urlpatterns = [
    path('', bus_list, name="bus-list"),
    path('add/', add_bus, name="add-bus"),
    path('delete/<int:bus_id>/', delete_bus, name='delete-bus'),
   
]
