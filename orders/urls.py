from django.urls import path
from .views import (
    OrderListView,
    OrderCreateView,
    OrderDetailView,
    CancelOrderView
)

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/cancel/', CancelOrderView.as_view(), name='order_cancel'),
]