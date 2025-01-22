from rest_framework import serializers
from addPage.models import Bus

class BusSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    bus_number = serializers.CharField(max_length=50)
    brand = serializers.CharField(max_length=100)
    no_of_seats = serializers.IntegerField(min_value=1)
    trip = serializers.CharField(max_length=200)
    trip_duration = serializers.DurationField()
    conductor = serializers.CharField(max_length=100)
    driver = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
       return Bus.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.bus_number = validated_data.get('bus_number')
        instance.brand = validated_data.get('brand')
        instance.no_of_seats = validated_data.get('no_of_seats')
        instance.trip = validated_data.get('trip')
        instance.trip_duration = validated_data.get('trip_duration')
        instance.conductor = validated_data.get('conductor')
        instance.driver = validated_data.get('driver')
        instance.save()
        return instance