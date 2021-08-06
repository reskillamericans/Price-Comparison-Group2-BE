from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,  max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Like(models.Model):
    product=models.OneToOneField(Product, blank=True, on_delete=models.CASCADE)
    user=models.ManyToManyField(User,blank=True, related_name='likebutton')
     
    def __str__(self):
        return f"{self.product.name} Likes"

    @property
    def total_likes(self):
        return self.user.count() 
