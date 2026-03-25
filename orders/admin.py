from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "price", "quantity")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price", "status", "is_paid", "created_at")
    list_filter = ("status", "is_paid", "created_at")
    search_fields = ("user__email", "user__username", "tracking_number")
    inlines = [OrderItemInline]
