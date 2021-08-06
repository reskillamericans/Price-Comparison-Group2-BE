from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    price_amazon = models.DecimalField(max_digits=10, decimal_places=2, default=True, blank=True)
    price_ebay = models.DecimalField(max_digits=10, decimal_places=2,default=True, blank=True)
    condition = models.CharField(max_length=25)  #New or Used
    image_amazon= models.CharField(max_length=300, default='')
    image_ebay= models.CharField(max_length=300, default='')
    # price = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField(max_length=255)
    class Meta:
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name
    