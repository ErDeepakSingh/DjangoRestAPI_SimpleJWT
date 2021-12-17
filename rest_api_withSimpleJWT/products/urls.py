from django.urls import path
from .views import CreateProductAPIView,ProductListAPIView,ProductDetailAPIView


urlpatterns = [
    path('create/',CreateProductAPIView.as_view(),name='create_product'),
    path('list/',ProductListAPIView.as_view(),name='list_product'),
    path('detail/<int:pk>/',ProductDetailAPIView.as_view(),name='product_detail'),


]