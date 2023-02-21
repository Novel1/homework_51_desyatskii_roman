from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    category = models.ForeignKey(to='webapp.Category', verbose_name='Категория', null=False, blank=False,
                                 on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.TextField(max_length=200, null=True, blank=True, verbose_name='Картинка')

    def __str__(self):
        return f'{self.name} - {self.description} - {self.category} - {self.price} - {self.image}'


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} - {self.description}'
