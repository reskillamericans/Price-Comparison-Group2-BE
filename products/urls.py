from django.urls import path
from .import views 
from blog.views import like_view
app_name='products'

urlpatterns = [

    path('amazon', views.amazon, name='amazon'),
    path('ebay', views.ebay, name='ebay'),
    path('<int:id>/', views.product_detail, name="product_detail"),
    path('product_comparison/<int:id>/',views.product_comparison,name="product_comparison")


]