from django.contrib import admin

from auth_app.models import ShopUser, ShopUserProfile


class InlineShopUserProfile(admin.TabularInline):
    model = ShopUserProfile


class ShopUserAdmin(admin.ModelAdmin):
    inlines = [InlineShopUserProfile]


admin.site.register(ShopUser, ShopUserAdmin)
