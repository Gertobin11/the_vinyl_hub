from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'brand',
        'category',
        'price',
        'rating',
        'image'
    ]

    ordering = ('name', 'brand')


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'friendly_name',
        'name'
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
