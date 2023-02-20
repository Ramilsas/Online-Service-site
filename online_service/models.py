from django.db import models

# Create your models here.
class Rolls(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rolls')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(upload_to='images',blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Роллы'
        verbose_name_plural = 'Роллы'

    def str(self):
        return self.name


class Burgers(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='burgers')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Бургер'
        verbose_name_plural = 'Бургеры'

    def str(self):
        return self.name


class Pizza(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pizza')
    name = models.CharField(max_length=100)
    price30 = models.DecimalField(max_digits=5, decimal_places=0)
    price36 = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    composition = models.TextField()

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    def str(self):
        return self.name


class Salads(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='salads')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    composition = models.TextField()

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'

    def str(self):
        return self.name


class Sets(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='salads')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Сет'
        verbose_name_plural = 'Сеты'

    def str(self):
        return self.name


class Drinks(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'

    def str(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.created_at)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

    def __str__(self):
        return f"{self.product} ({self.quantity})"





