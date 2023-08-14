from django.contrib import admin
from .models import Product, Category


class ProducAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


# Register your models here.
admin.site.register(Product, ProducAdmin)
admin.site.register(Category, CategoryAdmin)
