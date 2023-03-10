
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AssetsViewSet,CompanyViewSet,CustomersViewSet,InventoryViewSet,Product_typesViewSet,ProductsViewSet
router = DefaultRouter()
router.register('company', CompanyViewSet )
router.register('inventory', InventoryViewSet )
router.register('assets', AssetsViewSet )
router.register('products', ProductsViewSet )
router.register('customers', CustomersViewSet )
router.register('product_types', Product_typesViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
