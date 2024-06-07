from rest_framework import serializers
from ..models.customer import Customer
from rest_framework.validators import UniqueValidator

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'phone']
        extra_kwargs = {
            'name': {'validators': [UniqueValidator(queryset=Customer.objects.all(), message='得意先名が重複しています')]}
        }

