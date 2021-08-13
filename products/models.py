from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #image=models.FileField(upload_to ="static/images/Landing-images/%Y/%m/",validators=[FileExtensionValidator(['pdf','svg'])],blank=True,null=True)
    image=models.URLField(default=None, blank=True, null=True)
    price_amazon = models.DecimalField(max_digits=10, decimal_places=2, default=True, blank=True)
    price_ebay = models.DecimalField(max_digits=10, decimal_places=2,default=True, blank=True)
    condition = models.CharField(max_length=25)  #New or Refurbished
    amazon_url= models.URLField(blank=True,null=True, default='None')
    ebay_url= models.URLField(blank=True,null=True, default='None')
    slug = models.SlugField(max_length=255)
    class Meta:
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name
    