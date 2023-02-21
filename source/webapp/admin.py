from django.contrib import admin

from webapp.models import Product


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'created_at', 'price')
    list_filter = ('id', 'name', 'description', 'category', 'created_at', 'price')
    search_fields = ('name', 'description', 'category', 'price')
    fields = ('name', 'description', 'category', 'created_at', 'price')
    readonly_fields = ('id', 'created_at')


admin.site.register(Product, ProductsAdmin)
