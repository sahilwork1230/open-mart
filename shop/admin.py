from django.contrib import admin
from .models import Product

from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    prepopulated_fields = {"slug": ("name",)}

    
admin.site.register(Product)

