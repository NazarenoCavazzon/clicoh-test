from rest_framework import serializers
import ecommerce.models as ecommerce_models

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ecommerce_models.Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ecommerce_models.OrderDetail
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ecommerce_models.Product
        fields = '__all__'