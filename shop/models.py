from django.db import models


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
