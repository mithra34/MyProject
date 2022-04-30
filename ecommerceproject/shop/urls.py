from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import shop
from ecommerceproject import settings
from shop import views
app_name='shop'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]