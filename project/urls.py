from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.product_list, name='list'),
 path('create/', views.create_product, name='create'),
]
