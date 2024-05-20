from rest_framework import viewsets
from ..models.customer import Customer
from ..serializers.customer import CustomerSerializer
from rest_framework.permissions import IsAuthenticated


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
