from django.contrib import admin
from .models import Product, PriceHistory


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name', 'current_price']


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['parent_product', 'price', 'created_at']
    readonly_fields = (
        'parent_product', 'price', 'created_at'
    )
