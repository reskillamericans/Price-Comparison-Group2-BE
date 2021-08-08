import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def home(requests):
    product = Product.objects.all()

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
    # print(product)
    context = { 'product' : product}
    return render(requests, 'products/Product.html', context)



def product_comparison(requests, id):
    product = Product.objects.get(id=id)
    # print(product)
    context = { 'product' : product}
    return render(requests, 'products/Item.html', context)


