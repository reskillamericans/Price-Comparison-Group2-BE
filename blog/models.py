from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# IMPLEMENT THE COMMENT MODELS HEREfrom django.db import models


# Create your models here.
'''class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text'''

class Product1(models.Model):
    product_name=models.CharField(max_length=255)
    price=models.IntegerField(null=True)
    description=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    likes= models.ManyToManyField(User,blank=True, related_name='blog_like')
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name + '      |     ' + str(self.likes.count())

    def total_likes(self):
        return self.likes.count()
