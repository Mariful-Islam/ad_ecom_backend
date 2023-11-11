from django.contrib import admin
from .models import *
# Register your models here.


class AccountModel(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(Account, AccountModel)

class ProductModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'price')

admin.site.register(Product,  ProductModel)

class CartModel(admin.ModelAdmin):
    list_display = ('username', 'product')

admin.site.register(Cart, CartModel)

class CartSummaryModel(admin.ModelAdmin):
    list_display = ('cart_total_number', 'cart_total_price')

admin.site.register(CartSummary, CartSummaryModel)