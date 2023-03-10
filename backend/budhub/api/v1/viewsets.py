from rest_framework import authentication
from budhub.models import Assets,Company,Customers,Inventory,Product_types,Products
from .serializers import AssetsSerializer,CompanySerializer,CustomersSerializer,InventorySerializer,Product_typesSerializer,ProductsSerializer
from rest_framework import viewsets

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Company.objects.all()

class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Inventory.objects.all()

class AssetsViewSet(viewsets.ModelViewSet):
    serializer_class = AssetsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Assets.objects.all()

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Products.objects.all()

class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Customers.objects.all()

class Product_typesViewSet(viewsets.ModelViewSet):
    serializer_class = Product_typesSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Product_types.objects.all()