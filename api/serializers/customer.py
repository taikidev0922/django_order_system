from ..models.customer import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    cookie = serializers.IntegerField(required=False)
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerListSerializer(serializers.ListSerializer):
    child = CustomerSerializer()

