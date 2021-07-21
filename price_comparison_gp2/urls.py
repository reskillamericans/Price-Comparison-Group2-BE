from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from products.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="index"),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls'))

]
