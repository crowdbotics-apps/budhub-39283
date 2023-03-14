from django.conf import settings
from django.db import models
class Company(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    type = models.OneToOneField("budhub.Company_type",null=True,blank=True,on_delete=models.CASCADE,related_name="company_type",)
    status = models.CharField(null=True,blank=True,max_length=256,)
class Inventory(models.Model):
    'Generated Model'
    product = models.OneToOneField("budhub.Products",null=True,blank=True,on_delete=models.CASCADE,related_name="inventory_product",)
    source = models.OneToOneField("budhub.Inventory",null=True,blank=True,on_delete=models.CASCADE,related_name="inventory_source",)
    status = models.CharField(null=True,blank=True,max_length=256,)
    qty = models.FloatField(null=True,blank=True,)
    unit = models.OneToOneField("budhub.Units",null=True,blank=True,on_delete=models.CASCADE,related_name="inventory_unit",)
class Assets(models.Model):
    'Generated Model'
    product = models.OneToOneField("budhub.Products",on_delete=models.CASCADE,related_name="assets_product",)
    source = models.OneToOneField("budhub.Assets",null=True,blank=True,on_delete=models.CASCADE,related_name="assets_source",)
    status = models.CharField(null=True,blank=True,max_length=256,)
    qty = models.FloatField(null=True,blank=True,)
    unit = models.OneToOneField("budhub.Units",null=True,blank=True,on_delete=models.CASCADE,related_name="assets_unit",)
class Products(models.Model):
    'Generated Model'
    company = models.OneToOneField("budhub.Company",null=True,blank=True,on_delete=models.CASCADE,related_name="products_company",)
    type = models.OneToOneField("budhub.Product_types",null=True,blank=True,on_delete=models.CASCADE,related_name="products_type",)
    source = models.CharField(null=True,blank=True,max_length=256,)
    catalog = models.OneToOneField("budhub.Product_catalog",null=True,blank=True,on_delete=models.CASCADE,related_name="products_catalog",)
    status = models.CharField(null=True,blank=True,max_length=256,)
class Customers(models.Model):
    'Generated Model'
    company = models.OneToOneField("budhub.Company",on_delete=models.CASCADE,related_name="customers_company",)
    name = models.CharField(null=True,blank=True,max_length=256,)
    date_added = models.DateField(null=True,blank=True,)
    status = models.CharField(null=True,blank=True,max_length=256,)
class Product_types(models.Model):
    'Generated Model'
    name = models.BigIntegerField()
class Orders(models.Model):
    'Generated Model'
    customer = models.OneToOneField("budhub.Customers",on_delete=models.CASCADE,related_name="orders_customer",)
    status = models.CharField(null=True,blank=True,max_length=256,)
class Company_type(models.Model):
    'Generated Model'
    type = models.CharField(max_length=256,)
class Product_catalog(models.Model):
    'Generated Model'
    catalog = models.CharField(max_length=256,)
class Units(models.Model):
    'Generated Model'
    unit = models.CharField(max_length=256,)
    abbreviation = models.CharField(max_length=10,)
    qty_unit = models.FloatField()
class Line_items(models.Model):
    'Generated Model'
    order = models.OneToOneField("budhub.Orders",on_delete=models.CASCADE,related_name="line_items_order",)

# Create your models here.
