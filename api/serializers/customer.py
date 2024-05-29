from ..models.customer import Customer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class CustomerSerializer(serializers.ModelSerializer):
    cookie = serializers.IntegerField(required=False)
    class Meta:
        model = Customer
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Customer.objects.all(),
                fields=('name', 'address'),
                message="得意先名と住所は重複しています"
            )
        ]

class CustomerListSerializer(serializers.ListSerializer):
    child = CustomerSerializer()

