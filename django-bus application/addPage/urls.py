
from django.urls import path
from addPage.views import bus_list,add_bus
urlpatterns = [
    path('', bus_list, name='bus_list'),
    path('add/', add_bus, name='add_bus'),
]