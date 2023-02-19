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


# class Drinks(models.Model):
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='salads')
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=5, decimal_places=0)
#     image = models.ImageField(upload_to='/img')
#     description = models.TextField()

#     class Meta:
#         verbose_name = ''
#         verbose_name_plural = 'Сеты'

#     def str(self):
#         return self.name
