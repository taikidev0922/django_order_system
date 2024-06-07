from django.urls import path
from .views.customer import CustomerListView, CustomerBulkUpdateView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/bulk-update/', CustomerBulkUpdateView.as_view(), name='customer-bulk-update'),
]
