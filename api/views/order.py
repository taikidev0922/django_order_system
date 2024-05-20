from rest_framework import viewsets
from ..models.order import Order
from ..serializers.order import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
