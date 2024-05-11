from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    images = models.ImageField(upload_to="categories", null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    images = models.ImageField(upload_to="products", null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
