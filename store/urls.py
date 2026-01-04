from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path("aboutus/",include('aboutus.urls')),
    path("accunts/",include ('accounts.urls')),
   ]
