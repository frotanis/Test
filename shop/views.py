from django.shortcuts import render, get_object_or_404
from .models import Category, Product, CartItem
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



# Головна сторінка (або сторінка конкретної категорії)
def index(request, category_id=None):
    categories = Category.objects.all()

    # Рахуємо скільки товарів у кошику поточного юзера для шапки сайту
    cart_items_count = 0
    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'cart_items_count': cart_items_count  #Передаємо в шаблон
    })


# Додавання товару в кошик (доступно тільки для авторизованих)
@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Шукаємо, чи є вже такий товар у кошику цього юзера
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        # Якщо товар уже був в кошику то просто збільшуємо кількість на 1
        cart_item.quantity += 1
        cart_item.save()

    return redirect('index')


# Сторінка самого кошика
@login_required(login_url='login')
def view_cart(request):
    # Беремо всі товари з кошика поточного юзера
    cart_items = CartItem.objects.filter(user=request.user)
    # Рахуємо загальну вартість всього кошика
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


# Видалення з кошика
@login_required(login_url='login')
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

# Сторінка одного товару
def product_detail(request, product_id):
    # Дістаємо категорії для меню
    categories = Category.objects.all()
    # Шукаємо конкретний товар
    product = get_object_or_404(Product, id=product_id)

    # Рахуємо товари в кошику для шапки
    cart_items_count = 0
    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()

    return render(request, 'product-page.html', {
        'product': product,
        'categories': categories,
        'cart_items_count': cart_items_count
    })


def register(request):
    if request.method == 'POST':
        # Якщо користувач відправив заповнену форму
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Зберігаємо юзера в базу
            login(request, user)  # Одразу автоматично його логінимо
            return redirect('index')  # Перекидаємо на головну
    else:
        # Якщо користувач просто відкрив сторінку - показуємо порожню форму
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def checkout(request):
    # Знаходимо і видаляємо всі товари з кошика поточного юзера
    CartItem.objects.filter(user=request.user).delete()

    # Перенаправляємо на сторінку подяки
    return render(request, 'checkout_success.html')