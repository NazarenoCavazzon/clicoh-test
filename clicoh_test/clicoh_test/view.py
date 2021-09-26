from django.shortcuts import get_object_or_404
from ecommerce.models import Product, Order, OrderDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework import viewsets
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    #Get at /api/products/
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    #Get at /api/products/<pk>/
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        product = get_object_or_404(Product, pk=params.get('pk'))
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    #Put at /api/products/<pk>/
    def update(self, request, *args, **kwargs):
        product = self.get_object()
        product_data = request.data
        product.name = product_data.get('name')
        product.price = product_data.get('price')
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    #Post at /api/products/
    def create(self, request, *arg, **kwargs):
        product_data = request.data
        precio = float(product_data.get('price'))
        name = product_data.get('name')
        new_product = Product.objects.create(name=name, price=precio)
        new_product.save()
        serializer = ProductSerializer(new_product)
        return Response(serializer.data)

    #Delete at /api/products/<pk>/
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response({'message': 'Producto eliminado'})


class OrderViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        queryset = Order.objects.all()
        return queryset

    #Get at /api/orders/
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    #Get at /api/orders/<pk>/
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        order = get_object_or_404(Order, pk=params.get('pk'))
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    #Post at /api/orders/
    def create(self, request, *arg, **kwargs):
        new_order = Order.objects.create()
        new_order.save()
        serializer = OrderSerializer(new_order)
        return Response(serializer.data)
    
    #Put at /api/orders/<pk>/
    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.date_time = now()
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    #Delete at /api/orders/<pk>/
    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.delete()
        return Response({'message': 'Pedido eliminado'})

class OrderDetailsViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        queryset = OrderDetail.objects.all()
        return queryset

    #Get at /api/orderdetails/
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderDetailSerializer(queryset, many=True)
        return Response(serializer.data)
    
    #Get at /api/orderdetails/<pk>/
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        order_detail = get_object_or_404(OrderDetail, pk=params.get('pk'))
        serializer = OrderDetailSerializer(order_detail)
        return Response(serializer.data)
    
    #Post at /api/orderdetails/
    def create(self, request, *arg, **kwargs):
        order_detail_data = request.data
        product_id = order_detail_data.get('product_id')
        order_id = order_detail_data.get('order_id')
        try:
            OrderDetail.objects.get(order_id=order_id, product_id=product_id)
            return Response({'message': 'El producto ya esta en el pedido'})
        except OrderDetail.DoesNotExist:
            quantity = order_detail_data.get('quantity')
            if int(quantity) <= 0:
                return Response({'message': 'La cantidad debe ser mayor a 0'})
            product = get_object_or_404(Product, pk=product_id)
            price = float(product.price) * int(quantity)
            new_order_detail = OrderDetail.objects.create(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
            new_order_detail.save()
            serializer = OrderDetailSerializer(new_order_detail)
            return Response(serializer.data)
    
    #Put at /api/orderdetails/<pk>/
    def update(self, request, *args, **kwargs):
        order_detail_data = request.data
        order_detail = self.get_object()
        order_detail.quantity = order_detail_data.get('quantity') if order_detail_data.get('quantity') != None else order_detail.quantity
        order_detail.product_id = order_detail_data.get('product_id') if order_detail_data.get('product_id') != None else order_detail.product_id
        product = get_object_or_404(Product, pk=order_detail.product_id)
        order_detail.price = float(product.price) * int(order_detail.quantity)
        order_detail.save()
        serializer = OrderDetailSerializer(order_detail)
        return Response(serializer.data)
    
    #Delete at /api/orderdetails/<pk>/
    def destroy(self, request, *args, **kwargs):
        order_detail = self.get_object()
        order_detail.delete()
        return Response({'message': 'Detalle de pedido eliminado'})