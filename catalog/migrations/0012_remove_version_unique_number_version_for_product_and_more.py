# Generated by Django 4.2.7 on 2024-01-10 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0011_alter_version_number_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='version',
            name='unique_number_version_for_product',
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='зарегистрированный пользователь'),
        ),
    ]
