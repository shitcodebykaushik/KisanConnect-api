from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/user_auth/', include('api.v1.user_auth.urls')),
    path('api/v1/market/', include('api.v1.market.urls')),
]
