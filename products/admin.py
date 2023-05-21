from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class BasketAdmin(admin.TabularInline):
    model = models.Basket
    fields = ('product', 'price', 'created_timestamp', 'quantity')
    readonly_fields = ('created_timestamp', 'price')
    extra = 0

    def price(self, instance):
        try:
            return instance.product.price
        except models.Product.DoesNotExist:
            return 'Unknown'
