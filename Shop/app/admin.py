from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, ShippingAddress, Review


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'created', 'updated', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Category, CategoryAdmin)

# ---------------------------------------------------------------------


class ProductAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'created', 'updated', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Product, ProductAdmin)

# ---------------------------------------------------------------------


class CustomerAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'created', 'updated', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Customer, CustomerAdmin)

# ---------------------------------------------------------------------


class OrderAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'created', 'updated', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Order, OrderAdmin)

# ---------------------------------------------------------------------


class OrderItemAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'created', 'updated', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(OrderItem, OrderItemAdmin)

# ---------------------------------------------------------------------


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'created', 'updated', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(ShippingAddress, ShippingAddressAdmin)

# ---------------------------------------------------------------------


class ReviewAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'created', 'updated', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


admin.site.register(Review, ReviewAdmin)
