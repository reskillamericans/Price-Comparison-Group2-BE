from os import name
from django.urls import path, include
from . import views


urlpatterns = [

    path('faq/', views.faq, name="faq"),

]