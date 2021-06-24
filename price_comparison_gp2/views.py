import requests
from django.http import HttpResponse

def index(request):
    url = "https://amazon-products1.p.rapidapi.com/product"
    var_asin="B08BF4CZSV"
    querystring = {"country":"US","asin":var_asin}
    headers = {
        'x-rapidapi-key': "47b5c7199amshf6676988b53e987p14d46cjsn795c426ae547",
        'x-rapidapi-host': "amazon-products1.p.rapidapi.com"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    return HttpResponse(response)



def ebayindex(request):
    url="https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?" 
    
    querystring={"q" : "drone","limit":3}
    
    headers = {
    'X-EBAY-C-MARKETPLACE-ID': "EBAY_US",
    'X-EBAY-C-ENDUSERCTX': "contextualLocation=country=<2_character_country_code>,zip=<zip_code>,affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"
        }
        
    response = requests.request("GET", url, headers=headers, params=querystring)
    return HttpResponse(response)
