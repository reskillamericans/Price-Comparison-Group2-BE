from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from .models import Like

#from django.views.generic import ListView,DetailView
from products.models import Product
from .models import Like
from django.urls import reverse
import json

# IMPLEMENT THE COMMENT VIEWS HERE. THANKS

def get_product(request):
      productlist= Product.objects.all()
      user=request.user
      context={
          'products' : productlist,
          'user':user,
      }
      return render(request,'blog/homeview.html', context)

def details(request, id):
    product=Product.objects.get(id=id)
    user=request.user
    context={
        'product':product,
        'user':user,
    }
    return render(request,'blog/product_details.html', context)



def like_view(request):
    user =request.user.id
    like_objects=Like.objects.all()
    likes_list=[]
    print(likes_list)
    if (request.method=="POST"):
        if request.POST.get("operation") == "like_submit" and request.is_ajax():
            likes_id=request.POST.get("likes_id", None)
            like_object=get_object_or_404(Like,pk=likes_id)
            
           

            if like_object.user.filter(id=request.user.id): #already liked the product
                like_object.user.remove(request.user) #remove user from product 
                liked=False
            else:
                #Add user like to product
                like_object.user.add(request.user) 
                liked=True
            
            #create new context to fee back to AJAX call
            context={"likes_count":like_object.total_likes,
                        "user_like"   :liked,
                        "likes_id":likes_id
                    }
            print(like_object.total_likes)
            return HttpResponse(json.dumps(context), content_type='application/json')



#def compare_price(request):
#    product= Product.objects.all()
#    context={
#          'products' : product
        
#      }

    #return render(request, "products/Item.html")

def Modal(request):
    return render(request, 'blog/Modal.html')

