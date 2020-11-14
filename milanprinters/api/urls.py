from django.conf.urls import url
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name="api"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('owner/', include('api.owner.urls'))
]
