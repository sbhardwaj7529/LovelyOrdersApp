# models.py
from django.db import models

class Order(models.Model):
    """
    Order model representing a customer order.

    Attributes:
    - order_id (IntegerField): A unique identifier for the order. Indexed for faster querying.
    - products (JSONField): A JSON field containing an array of products in the order.

    Methods:
    - __str__(): Returns a string representation of the order.
    """

    order_id = models.IntegerField(unique=True, db_index=True)
    products = models.JSONField()

    def __str__(self):
        """
        Returns a string representation of the order.

        :return: A string in the format "Order {order_id}".
        """
        return f"Order {self.order_id}"

