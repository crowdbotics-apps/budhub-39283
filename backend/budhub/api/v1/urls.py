
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AssetsViewSet,CompanyViewSet,Company_typeViewSet,CustomersViewSet,InventoryViewSet,OrdersViewSet,Product_typesViewSet,ProductsViewSet
router = DefaultRouter()
router.register('company', CompanyViewSet )
router.register('inventory', InventoryViewSet )
router.register('assets', AssetsViewSet )
router.register('products', ProductsViewSet )
router.register('customers', CustomersViewSet )
router.register('product_types', Product_typesViewSet )
router.register('orders', OrdersViewSet )
router.register('company_type', Company_typeViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
