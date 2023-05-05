from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:order_id>/', views.OrderById.as_view()),
    path('orders/average_products/', views.AverageProductsInOrders.as_view()),
    path('orders/average_quantity/<int:product_id>/', views.AverageQuantityByProductId.as_view()),
]
