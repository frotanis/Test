from django.test import TestCase
from .models import Category, Product

class ShopTestCase(TestCase):
    def setUp(self):
        # Цей метод запускається ПЕРЕД кожним тестом.
        # Тут створюємо "віртуальну" базу даних спеціально для тестів
        self.category = Category.objects.create(name="Тестова категорія")
        self.product = Product.objects.create(
            category=self.category,
            name="Тестовий товар",
            description="Опис",
            price=150.00,
            is_available=True
        )

    def test_product_creation(self):
        # Перевіряємо, чи товар дійсно успішно зберігся в базу
        self.assertEqual(self.product.name, "Тестовий товар")
        self.assertEqual(self.product.price, 150.00)
        self.assertTrue(self.product.is_available)

    def test_homepage_status_code(self):
        # Перевіряємо, чи головна сторінка віддає статус 200 (ОК), а не помилку
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Перевіряємо, чи є на головній сторінці наш тестовий товар
        self.assertContains(response, "Тестовий товар")