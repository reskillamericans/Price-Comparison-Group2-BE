from django.urls import path
from .import views 
#from .views import index, ebayindex

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.ebayindex, name='ebayindex'),
]