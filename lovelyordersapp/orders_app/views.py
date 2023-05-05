from django.core.cache import cache
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderById(generics.RetrieveAPIView):
    """
    API view for retrieving an order by its order_id.

    Attributes:
    - queryset: All Order objects.
    - serializer_class: OrderSerializer for serializing order data.
    - lookup_field: Field name used for looking up an order, 'order_id'.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

class AverageProductsInOrders(generics.GenericAPIView):
    """
    API view for fetching the average number of products in all orders.

    Methods:
    - get(request): Returns a JSON response containing the average number
      of products in all orders.
    """

    def get(self, request):
        """Fetches the average number of products in all orders."""
        cache_key = "average_products"
        avg_products = cache.get(cache_key)

        if avg_products is None:
            orders = Order.objects.all()
            if len(orders) == 0:
                return Response({"error": "No orders available in database. So, no data to find average number of products in all orders."}, status=status.HTTP_404_NOT_FOUND)
            total_products = sum(len(order.products) for order in orders)
            avg_products = total_products / len(orders)
            cache.set(cache_key, avg_products, 60 * 5)  # Cache for 5 minutes

        return Response({"average_products": avg_products})

class AverageQuantityByProductId(generics.GenericAPIView):
    """
    API view for fetching the average quantity of a single product in all orders
    using the product_id.

    Methods:
    - get(request, product_id): Returns a JSON response containing the average
      quantity of the specified product in all orders.
    """

    def get(self, request, product_id):
        """Fetches the average quantity of a single product in all orders."""
        cache_key = f"average_quantity_{product_id}"
        avg_quantity = cache.get(cache_key)

        if avg_quantity is None:
            orders = Order.objects.all()
            total_quantity = 0
            orders_with_product = 0

            for order in orders:
                for product in order.products:
                    if product['id'] == product_id:
                        total_quantity += product['quantity']
                        orders_with_product += 1

            if orders_with_product:
                avg_quantity = total_quantity / orders_with_product
                cache.set(cache_key, avg_quantity, 60 * 5)  # Cache for 5 minutes
            else:
                return Response({"error": "Product not found in any order"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"average_quantity": avg_quantity})
