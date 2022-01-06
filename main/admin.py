from django.contrib import admin

# Register your models here.
from main.models import ProductCategory, Product, ImageProduct


class InlineImage(admin.TabularInline):
    model = ImageProduct


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineImage]


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
