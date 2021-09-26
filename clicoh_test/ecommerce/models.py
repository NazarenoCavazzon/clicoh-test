from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(default="", max_length=255)
    price = models.FloatField(default=0.0)

class Order(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        total = 0
        try:
            _orderDetails = OrderDetail.objects.filter(order=self.id)
            for orderDetail in _orderDetails:
                total += orderDetail.price
            return total
        except:
            return total

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)