from django.contrib import admin
from django.urls import path, include # Додали include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Кажемо ядру: "Всі базові запити перенаправляй у додаток shop"
    path('', include('shop.urls')), 
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.index, name='category_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

# МАРШРУТИ ДЛЯ КОШИКА:
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # НОВИЙ МАРШРУТ ДЛЯ ОФОРМЛЕННЯ ЗАМОВЛЕННЯ:
    path('checkout/', views.checkout, name='checkout'),
]

# Обов'язково додаємо цей рядок для роботи з картинками:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

