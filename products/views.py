import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from blog.models import Like


def home(requests):
    #product = Product.objects.all()
    product= Product.objects.all()
    context={
          'products' : product
        
      }
    return render(requests, "products/index.html", context)

    

    #Search item
    product_name = requests.GET.get('product_name')
    if product_name !='' and product_name is not None:
        product = product.filter(name__icontains=product_name)
    return render(requests, "products/index.html")


def amazon(request):
    url = "https://amazon-products1.p.rapidapi.com/product"
    var_asin="B08XNY5WGV"
    querystring = {"country":"US","asin":var_asin}
    headers = {
        'x-rapidapi-key': "47b5c7199amshf6676988b53e987p14d46cjsn795c426ae547",
        'x-rapidapi-host': "amazon-products1.p.rapidapi.com"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    return JsonResponse(response.json(), safe=False)



def ebay(request):
    url="https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?" 
    
    querystring={"q" : "drone","limit":3}
    
    headers = {
    'X-EBAY-C-MARKETPLACE-ID': "EBAY_US",
    'X-EBAY-C-ENDUSERCTX': "contextualLocation=country=<2_character_country_code>,zip=<zip_code>,affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"
        }
        
    response = requests.request("GET", url, headers=headers, params=querystring)
    return JsonResponse(response.json(), safe=False)


def product_detail(requests, id):
    product = Product.objects.get(id=id)
    user=requests.user
    likes_list =Like.objects.filter(product_id=id)
    if user.is_authenticated:
        user_like=Like.objects.filter( user=requests.user, product_id=id)
    else:
        user_like=False

    context={
        'product':product,
        'user':user,
        'likes_list': likes_list,
        'user_like': user_like
    }
    return render(requests, 'products/Product.html', context)



def product_comparison(requests, id):
    product = Product.objects.get(id=id)
    user=requests.user
    likes_list =Like.objects.filter(product_id=id)
    if user.is_authenticated:
        user_like=Like.objects.filter( user=requests.user, product_id=id)
    else:
        user_like=False

    context={
        'product':product,
        'user':user,
        'likes_list': likes_list,
        'user_like': user_like
    }
    # print(product)
    return render(requests, 'products/Item.html', context)


