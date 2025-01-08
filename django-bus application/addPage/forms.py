
from django import forms
from addPage.models import *


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_number', 'brand', 'no_of_seats', 'trip', 'trip_duration', 'conductor', 'driver']
