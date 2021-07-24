"""price_comparison_gp2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
#<<<<<<< backenddev1
from django.conf.urls.static import static

from accounts.views import (
    login_view,
    logout_view,
    register_view,
    
)
from faq.views import faq
#==========
from products.views import home, amazon, ebay
#>>>>>>> dev

urlpatterns = [
    
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('admin/', admin.site.urls),
#<<<<<<< backenddev1
    path('', include('accounts.urls')),
    path('', include('faq.urls')),
#=======
    path('', home, name="index"),
    path('blog/', include('blog.urls')),
    path('products/', include('products.urls'))
#>>>>>>> dev
]
