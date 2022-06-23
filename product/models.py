
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "product_category"
        ordering = ["-created_at"]


class Inventory(models.Model):
    "Inventory model"
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.quantity

    class Meta:
        verbose_name_plural = "product_inventory"
        ordering = ["-created_at"]


class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount_percent = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "product_discount"
        ordering = ["-created_at"]

        