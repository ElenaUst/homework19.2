from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'product', 'number', 'name',)
    list_filter = ('product',)
