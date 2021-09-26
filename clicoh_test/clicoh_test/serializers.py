from rest_framework import serializers
from ecommerce.models import Order, OrderDetail, Product

class OrderSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = Order
        fields = ['id', 'date_time', 'total']
        
    total = serializers.SerializerMethodField('get_total')
    def get_total(self, Order):
        total = 0
        try:
            _orderDetails = OrderDetail.objects.filter(order_id=Order.id)
            for orderDetail in _orderDetails:
                total += orderDetail.price
            return total
        except:
            return total

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'