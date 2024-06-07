from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models.customer import Customer
from ..serializers.customer import CustomerSerializer
from django.db import transaction
from django_filters import rest_framework as filters

class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.filter(deleted_at__isnull=True)
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class CustomerBulkUpdateView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        results = []
        is_valid = True

        with transaction.atomic():
            for customer in request.data:
                pk = customer.get('id', None)
                if pk:
                    instance = Customer.objects.get(id=pk)
                    serializer = CustomerSerializer(data=customer, instance=instance, partial=True)
                else:
                    serializer = CustomerSerializer(data=customer, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    results.append({**serializer.data, 'cookie': customer['cookie']})
                else:
                    is_valid = False
                    message_list = []
                    for messages in serializer.errors.values():
                        for message in messages:
                            message_list.append({"type": "error", "message": message})
                    results.append({**serializer.data, 'cookie': customer['cookie'], 'results': message_list})
            if is_valid:
                return Response(results, status=status.HTTP_200_OK)
            else:
                transaction.set_rollback(True)
                return Response(results, status=status.HTTP_400_BAD_REQUEST)
