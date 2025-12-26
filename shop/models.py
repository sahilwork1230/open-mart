from django.db import models



categories = [("DR", "Drones"), ("RB", "Robots"), ("CM", "Camera"), ("SP", "Spare Parts")]
class Product(models.Model):
    category = models.CharField(choices=categories, default='DR')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length = 500)
    long_description = models.TextField(default=None)
    price = models.FloatField()
    image = models.ImageField(upload_to='featured-brand')

    def __str__(self):
        return self.name
