from rest_framework import serializers
from .models import Client, Bills, Organization


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'


class OneEndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class TwoEndPointSerializer(serializers.Serializer):
    client = serializers.CharField(max_length=200)
    number = serializers.IntegerField()
    summa = serializers.IntegerField()


class ThreeEndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'

