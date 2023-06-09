
from .models import Data
from rest_framework import serializers



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=90)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    def create(self, validated_data):
        return Data.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance