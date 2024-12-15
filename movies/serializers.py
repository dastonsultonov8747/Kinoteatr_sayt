from .models import Serial, Serial_item, Kinolar, Multfilm
from rest_framework import serializers


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'


class SerialItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial_item
        fields = '__all__'


class KinolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kinolar
        fields = '__all__'


class MultfilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multfilm
        fields = '__all__'
