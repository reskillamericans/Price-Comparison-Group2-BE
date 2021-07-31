from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    # price = models.DecimalField(max_digits=4, decimal_places=2)
    price_amazon = models.DecimalField(max_digits=4, decimal_places=2)
    price_ebay = models.DecimalField(max_digits=4, decimal_places=2)
    condition = models.CharField(max_length=25)  #New or Used
    # image = models.CharField(max_length=300, default='DEFAULT VALUE')
    image = models.ImageField(upload_to='images/product-images')
    slug = models.SlugField(max_length=255)
    class Meta:
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name
    