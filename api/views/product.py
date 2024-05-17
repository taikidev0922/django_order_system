from rest_framework import viewsets
from ..models.product import Product
from ..serializers.product import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
