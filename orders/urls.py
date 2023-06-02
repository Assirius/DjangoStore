from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('order-create', views.OrderCreateView.as_view(), name='order-create'),
    path('', views.OrderListView.as_view(), name='orders-list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order-success', views.SuccessTemplateView.as_view(), name='order-success'),
    path('order-cancel', views.CancelTemplateView.as_view(), name='order-cancel'),
]
