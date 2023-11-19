from django.db import models

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

    def __str__(self):
        return f'{self.name} {self.description} {self.preview} {self.category} {self.price} {self.create_date} {self.last_change_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'



