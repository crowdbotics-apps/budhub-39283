from django.conf import settings
from django.db import models
class Company(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
class Inventory(models.Model):
    'Generated Model'
    product = models.OneToOneField("budhub.Products",on_delete=models.CASCADE,null=True,blank=True,related_name="inventory_product",)
class Assets(models.Model):
    'Generated Model'
    product = models.OneToOneField("budhub.Products",on_delete=models.CASCADE,related_name="assets_product",)
class Products(models.Model):
    'Generated Model'
    company = models.OneToOneField("budhub.Company",on_delete=models.CASCADE,null=True,blank=True,related_name="products_company",)
    type = models.OneToOneField("budhub.Product_types",on_delete=models.CASCADE,null=True,blank=True,related_name="products_type",)
class Customers(models.Model):
    'Generated Model'
    company = models.OneToOneField("budhub.Company",on_delete=models.CASCADE,related_name="customers_company",)
    name = models.CharField(max_length=256,null=True,blank=True,)
    date_added = models.DateField(null=True,blank=True,)
class Product_types(models.Model):
    'Generated Model'
    name = models.BigIntegerField()

# Create your models here.
