from django.contrib import admin
from django.urls import path
from shop import views # Або як ти імпортуєш views у своєму проєкті

urlpatterns = [
    path('admin/', admin.site.urls),
    # Головна сторінка
    path('', views.index, name='index'),
    # Сторінка фільтрації за категорією (наприклад: /category/1/)
    path('category/<int:category_id>/', views.index, name='category_detail'),
    # Сторінка конкретного товару (наприклад: /product/3/)
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]