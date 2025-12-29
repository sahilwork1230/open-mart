from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products", null=True, blank=True
 )
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length = 500)
    long_description = models.TextField(default=None)
    price = models.FloatField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    # ForeignKey creates a 'belongs to' relation -->> Cart belongs to a perticular user 
    # related_name means a cart can be accessed from a user using .cart 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.email}"
