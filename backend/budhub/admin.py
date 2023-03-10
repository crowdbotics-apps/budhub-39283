from django.contrib import admin
from .models import Assets,Company,Customers,Inventory,Product_types,Products
admin.site.register(Company)
admin.site.register(Inventory)
admin.site.register(Assets)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Product_types)

# Register your models here.
