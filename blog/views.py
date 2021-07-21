from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Product1
from django.urls import reverse
import json

# IMPLEMENT THE COMMENT VIEWS HERE. THANKS

def get_product(request):
      productlist= Product1.objects.all()
      user=request.user
      context={
          'products' : productlist,
          'user':user,
      }
      return render(request,'homeview.html', context)

def details(request, id):
    product=Product1.objects.get(id=id)
    user=request.user
    context={
        'product':product,
        'user':user,
    }
    return render(request,'product_details.html', context)


def like_view(request):
    #user =request.user
    if (request.method=="POST"):
       if request.POST.get("operation") == "like_submit" and request.is_ajax():
         content_id=request.POST.get("content_id",None)
         content=get_object_or_404(Product1,pk=content_id)
         if content.likes.filter(id=request.user.id): #already liked the content
            content.likes.remove(request.user) #remove user from likes 
            liked=False
         else:
             content.likes.add(request.user) 
             liked=True
         ctx={"likes_count":content.total_likes(),"liked":liked,"content_id":content_id}
         return HttpResponse(json.dumps(ctx), content_type='application/json')

    contents=Product1.objects.all()
    already_liked=[]
    id=request.user.id
    for content in contents:
        if(content.likes.filter(id=id).exists()):
            already_liked.append(content.id)
    ctx={"contents":contents,"already_liked":already_liked }
    return render(request,"product_details.html",ctx)
