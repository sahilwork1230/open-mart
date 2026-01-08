from django.contrib import admin
from .models import Product

from .models import Category, Address

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    prepopulated_fields = {"slug": ("name",)}

    
admin.site.register(Product)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "phone_number",
        "city",
        "state",
        "country",
        "address_type",
    )
    list_filter = ("address_type","state","country")
    
    search_fields = (
        "name",
        "phone_number",
        "city",
        "state",
        "user__email", #reference-->> we used __ for traversal purpose
        "user__username",
    )
    ordering = ("-id",)

