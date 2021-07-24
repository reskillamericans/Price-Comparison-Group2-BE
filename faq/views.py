from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def faq(request):
    return render(request, "faq/faq.html")