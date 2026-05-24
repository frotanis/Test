from django.db import models
from django.contrib.auth.models import User


# Таблиця категорій (наприклад: Чоловічий одяг, Сумки)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name


# Таблиця товарів
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    # blank=True дозволяє створювати товар поки що без фото
    image = models.ImageField(upload_to='products/', verbose_name="Зображення", blank=True, null=True)
    is_available = models.BooleanField(default=True, verbose_name="В наявності")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"