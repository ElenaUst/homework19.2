from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contact, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contact, name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),

]