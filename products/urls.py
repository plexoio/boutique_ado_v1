from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_datail, name='product_detail'),

]
