from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('accounts/', include('accounts.urls')),
    #path('shop/', include('shop.urls')),
    path('', views.index, name='index'),
]
