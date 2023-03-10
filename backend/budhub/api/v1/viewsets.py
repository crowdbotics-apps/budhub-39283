from rest_framework import authentication
from budhub.models import Assets,Company,Company_type,Customers,Inventory,Line_items,Orders,Product_catalog,Product_types,Products,Units
from .serializers import AssetsSerializer,CompanySerializer,Company_typeSerializer,CustomersSerializer,InventorySerializer,Line_itemsSerializer,OrdersSerializer,Product_catalogSerializer,Product_typesSerializer,ProductsSerializer,UnitsSerializer
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

class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Orders.objects.all()

class Company_typeViewSet(viewsets.ModelViewSet):
    serializer_class = Company_typeSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Company_type.objects.all()

class Product_catalogViewSet(viewsets.ModelViewSet):
    serializer_class = Product_catalogSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Product_catalog.objects.all()

class UnitsViewSet(viewsets.ModelViewSet):
    serializer_class = UnitsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Units.objects.all()

class Line_itemsViewSet(viewsets.ModelViewSet):
    serializer_class = Line_itemsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Line_items.objects.all()