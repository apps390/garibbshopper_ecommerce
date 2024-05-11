from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    ordered_date = models.DateField(auto_now=True)
    address = models.TextField()
    phone = models.BigIntegerField()
    delivery_status = models.CharField(max_length=200, default='pending')
    order_status = models.CharField(max_length=200, default='pending')




class Account(models.Model):
    account_no=models.BigIntegerField(default=123456)
    acc_type=models.CharField(max_length=500,default='savings')
    amount=models.IntegerField(default=1000)
    def __str__(self):
        return str(self.account_no)

