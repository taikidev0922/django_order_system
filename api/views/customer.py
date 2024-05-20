from rest_framework import viewsets
from ..models.customer import Customer
from ..serializers.customer import CustomerSerializer,CustomerListSerializer
from base.views import BulkUpdateModelViewSet
from django_filters import rest_framework as filters


class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerViewSet(BulkUpdateModelViewSet):
    queryset = Customer.objects.filter(deleted_at__isnull=True)
    serializer_class = CustomerSerializer
    bulk_update_serializer_class = CustomerListSerializer  # bulk_update用のシリアライザー
    bulk_update_fields = ['title', 'description', 'price', 'deleted_at']  # bulk_updateで更新するフィールド
    filterset_class = CustomerFilter
