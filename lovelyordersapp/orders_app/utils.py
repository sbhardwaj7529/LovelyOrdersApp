import requests
from .models import Order

def populate_orders():
    url = "https://orders-staging-api-fc7lwmf3uq-el.a.run.app/orders/all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get('success'):
            orders = data.get('data', [])
            for order_data in orders:
                order_id = order_data.get('order_id')
                products = order_data.get('products')

                if order_id and products:
                    order, created = Order.objects.get_or_create(order_id=order_id)
                    order.products = products
                    order.save()
