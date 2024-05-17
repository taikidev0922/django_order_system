from rest_framework import viewsets
from ..models.order import Order
from ..serializers.order import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
