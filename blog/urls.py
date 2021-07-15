from django.urls import path
from .import views 


urlpatterns = [
#    # path('', home, name="index"),
#     path('blog/', include('blog.urls')),
#     path('comments/', include('comments.urls'))
path("", views.comment_add, name="comments"),

]