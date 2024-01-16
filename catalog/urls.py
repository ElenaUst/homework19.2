from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contact, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, AccessDeniedView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contact, name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('versions/create/', VersionCreateView.as_view(), name='version_create'),
    path('denied/', AccessDeniedView.as_view(), name='access_denied'),

]