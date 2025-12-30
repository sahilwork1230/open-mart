from django.db import models
from django.conf import settings
from shop.models import Product

class Cart(models.Model):
    # ForeignKey creates a 'belongs to' relation -->> Cart belongs to a perticular user 
    # related_name means a cart can be accessed from a user using .cart 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.email}"
    

class cartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name = "items")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("cart", "product")

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"

    def subtotal(self):
        return self.quantity * self.price

