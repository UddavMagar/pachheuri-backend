from django.contrib import admin

from product.models import Category,Inventory,\
    Discount

# Register your models here.
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(Discount)