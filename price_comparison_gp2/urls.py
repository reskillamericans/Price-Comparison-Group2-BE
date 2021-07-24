from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('faq/', include('faq.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
