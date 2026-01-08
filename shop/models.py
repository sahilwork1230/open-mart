from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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


class Address(models.Model):
    categories = [("HM", "Home Address"), ("WK", "Work Address")]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "addresses"
    )
    address_type = models.CharField(
    max_length=2,
    choices=categories,
    default="HM"
    )
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null=False, blank=False,region="IN")
    pincode = models.CharField(max_length=6, blank=False)
    locality = models.TextField(blank=False)
    full_address = models.TextField()
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")

    def __str__(self):
        return f"{self.full_address}, {self.city}"
    


    
