from .view import ProductViewSet, OrderViewSet, OrderDetailsViewSet
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderdetails', OrderDetailsViewSet, basename='orderdetails')