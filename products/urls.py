from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', views.ProductsListView.as_view(), name='category'),

    path('basket/add/<int:product_id>/', views.basket_add, name='basket-add'),
    path('basket/remove/<int:basket_id>/', views.basket_remove, name='basket-remove'),
]
