from . import views
from django.urls import path

app_name = 'ecommerce_app'

urlpatterns = [

    path('', views.allProductCategory, name='allProductCategory'),
    path('<slug:category_slug>/', views.allProductCategory, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.productDetail, name='product_category_detail')
]
