from django.contrib import admin
from .models import Category, Product

# Проста реєстрація для категорій
admin.site.register(Category)

# Просунута реєстрація для товарів (щоб було красиво)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available') # Колонки в таблиці
    list_filter = ('category', 'is_available')                   # Фільтри збоку
    search_fields = ('name', 'description')                      # Пошук по назві