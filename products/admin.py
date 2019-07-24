from django.contrib import admin
from .models import Categories
from .models import Products
from .models import Pictures
from .models import Carts
from .models import Orders
from django.contrib.auth.models import Group

admin.site.site_header = "Admin Dashboard"

class CategoriesAdmin(admin.ModelAdmin):
    fields = ('name', 'perant_id', )
    list_display = ('name', 'perant_id', 'slug')
    list_filter = ('name', )

class PicturesInline(admin.TabularInline):
    model = Pictures

class ProductsAdmin(admin.ModelAdmin):
    fields = ('name', 'category_id', 'price', 'code', 'post')
    list_display = ('name', 'price', 'slug', 'code', 'category_id')
    list_filter = ('name', )
    inlines = [
        PicturesInline,
    ]

class OrdersInline(admin.TabularInline):
    model = Orders

class CartsAdmin(admin.ModelAdmin):
    list_display = ('name', 'addrress', 'phone_number', 'email', 'request')
    readonly_fields = ('name', 'addrress', 'phone_number', 'email', 'request')
    inlines = [
        OrdersInline,
    ]

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Carts, CartsAdmin)
# admin.site.register(Group)