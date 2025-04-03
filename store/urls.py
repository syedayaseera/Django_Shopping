from django.urls import path
from . import views
from .views import product_detail, product_list, upload_product



urlpatterns = [
    path('upload_product/', upload_product, name='upload_product'),
    path('product_list/',product_list, name='product_list'),
     path('product/<int:pk>/', product_detail, name='product_detail'),
]
