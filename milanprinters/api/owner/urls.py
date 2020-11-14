from django.urls import path, include
from rest_framework import urlpatterns
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.OwnerViewset)

urlpatterns = [
    path('', include(router.urls))
]
