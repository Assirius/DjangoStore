from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductModelViewSet)
router.register(r'baskets', views.BasketModelViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),

]
