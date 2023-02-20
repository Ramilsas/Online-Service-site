from django.contrib import admin

# Register your models here.
from .models import Salads, Rolls, Burgers, Pizza, Drinks, Product, Cart, CartItem

class RollsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'description', )
    list_display_links = ('name',)
    list_editable = ('price',)


class BurgerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'description', )
    list_display_links = ('name',)
    list_editable = ('price',)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price30', 'price36', 'image', 'composition', )
    list_display_links = ('name',)
    list_editable = ('price30', 'price36',)


class SaladsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'composition', )
    list_display_links = ('name', )
    list_editable = ('price',)


class DrinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'description', )
    list_display_links = ('name',)
    list_editable = ('price',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'description', )
    list_display_links = ('name',)
    list_editable = ('price',)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]



admin.site.register(Rolls, RollsAdmin)
admin.site.register(Burgers, BurgerAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Salads, SaladsAdmin)
admin.site.register(Drinks, DrinksAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
