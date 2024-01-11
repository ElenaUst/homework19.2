from django.db import models
from config import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование', db_index=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена покупки')
    create_date = models.DateTimeField(verbose_name='дата создания')
    last_change_date = models.DateTimeField(verbose_name='дата последнего изменения')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='зарегистрированный пользователь')

    def __str__(self):
        return f'{self.name} {self.description} {self.preview} {self.category} {self.price} {self.create_date} {self.last_change_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(primary_key=True, verbose_name='Номер версии')
    name = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} (версия {self.number}) - {self.is_active}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        # constraints = [
        #     models.UniqueConstraint(fields=['number', 'product'], name='unique_number_version_for_product')]


