from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from products.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('faq/', include('faq.urls')),
    path('blog/',include('blog.urls'))
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
