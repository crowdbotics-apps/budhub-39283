from rest_framework import serializers
from budhub.models import Assets,Company,Company_type,Customers,Inventory,Orders,Product_catalog,Product_types,Products

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = "__all__"

class AssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assets
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"

class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = "__all__"

class Product_typesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_types
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = "__all__"

class Company_typeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company_type
        fields = "__all__"

class Product_catalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_catalog
        fields = "__all__"