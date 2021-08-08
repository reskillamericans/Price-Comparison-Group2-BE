from django.db import models
from products.models import Product
from django.utils import timezone
from django.contrib.auth.models import User

class Like(models.Model):
    product=models.OneToOneField(Product, blank=True, on_delete=models.CASCADE)
    user=models.ManyToManyField(User,blank=True, related_name='likebutton')
     
    def __str__(self):
        return self.text


    def __str__(self):
        return f"{self.product.name} Likes"

    @property
    def total_likes(self):
        return self.user.count() 

    
