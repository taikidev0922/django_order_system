from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.customer import CustomerViewSet
from .views.product import ProductViewSet
from .views.order import OrderViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
