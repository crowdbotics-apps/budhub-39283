from django.contrib import admin
from .models import Assets,Company,Company_type,Customers,Inventory,Orders,Product_catalog,Product_types,Products,Units
admin.site.register(Company)
admin.site.register(Inventory)
admin.site.register(Assets)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Product_types)
admin.site.register(Orders)
admin.site.register(Company_type)
admin.site.register(Product_catalog)
admin.site.register(Units)

# Register your models here.
