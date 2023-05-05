# Django Customer Orders API

This Django project provides a RESTful API to manage and retrieve customer orders. It is designed to handle a growing number of orders efficiently, using caching, pagination, and database indexing.

## Features

- Fetch an order by order ID
- Fetch the average number of products in all the orders
- Fetch the average quantity of a single product from the orders using the product ID

## Prerequisites
- Python 3
- Docker

## Setup

### Initial step

Clone the repository:

`git clone https://github.com/sbhardwaj7529/LovelyOrdersApp.git` <br>
`cd LovelyOrdersApp`
### Setup mongodb

Just run the shell script `setup_mongodb.sh` which would automatically download mongodb docker image, start its container, create database and credentials inside it. <br> Simply run: `./setup_mongodb.sh` <br>
(Please ignore console message `OCI runtime exec failed: exec failed: unable to start container process: exec: "mongo"` during this step.)
<br>
Note: if you want to stop and remove the spawned container later, then simply run: `docker stop mongo-server && docker rm mongo-server`

### Setup redis

Just run the shell script `setup_redis.sh` which would automatically download redis docker image, start its container, create database and credentials inside it. <br> Simply run: `./setup_redis.sh`

Note: if you want to stop and remove the spawned container later, then simply run: `docker stop redis-instance && docker rm redis-instance`
### Setup the Django app

2. Create a virtual environment and activate it:

`python3 -m venv venv` (or replace `python3` with `python` assuming that binary points to python 3 rather than python 2) <br>
`source venv/bin/activate # On Windows: venv\Scripts\activate`

2. Install the required packages:

`pip install -r requirements.txt`

3. Now, `cd` into the directory containing `manage.py` file, and run migrations:

`python manage.py showmigrations` <br>
`python manage.py migrate`

4. Run the Django development server:

`python manage.py runserver`


The API should now be accessible at http://localhost:8000

## Populate orders from the third-party API

You can use the provided management command to populate your database with orders from the third-party API (located at https://orders-staging-api-fc7lwmf3uq-el.a.run.app/orders/all ):

`python manage.py populate_orders`

## Usage

### Fetch an order by order ID

GET `http://localhost:8000/api/orders/<order_id>`

### Fetch the average number of products in all the orders

GET `http://localhost:8000/api/orders/average-products`

### Fetch the average quantity of a single product from the orders using the product ID

GET `http://localhost:8000/api/orders/average-quantity/<product_id>`

## Documentation

### Management command to populate orders in database (from third-party API)

The management commands invokes a utility function named `populate_orders()`. 
The populate_orders function serves to fetch order data from an external API and store it in a local Django database. By sending a GET request to the specified API endpoint and parsing the JSON response, the function extracts order information, including 'order_id' and 'products'. It then iterates over the orders, either retrieving existing Order objects with the corresponding 'order_id' or creating new ones. The 'products' field of the Order object is updated with the fetched data, and the object is saved to the local database. 
### API Endpoints
The code defines three API views for an order management system using Django and Django Rest Framework:

1. `OrderById`: This API view retrieves an order by its order_id. It inherits from the generics.RetrieveAPIView class provided by Django Rest Framework, which is specifically designed for handling single object retrieval. The view sets the following attributes:

- queryset: The dataset the view should use is all Order objects in the database.
- serializer_class: The OrderSerializer class is responsible for converting order data into a JSON format that can be sent as a response.
- lookup_field: The field name used for looking up an order is 'order_id'.
When a client sends a GET request to the endpoint associated with this view, the system will look for the order with the specified order_id and return its serialized data as a JSON response.

2. `AverageProductsInOrders`: This API view calculates the average number of products across all orders. It inherits from the generics.GenericAPIView class, which is a base class for creating custom API views in Django Rest Framework. The view defines a get method that does the following:

- Check if the average number of products is available in the cache using the cache key "average_products".
- If the cached value is not found, it retrieves all Order objects from the database.
- If there are no orders available in the database, it returns an error message with an HTTP 404 Not Found status.
- Otherwise, it calculates the total number of products in all orders and divides it by the number of orders to get the average.
- The calculated average is stored in the cache with a 5-minute expiration time.
- Finally, it sends the average number of products as a JSON response to the client.

3. `AverageQuantityByProductId`: This API view computes the average quantity of a specific product in all orders based on the product_id. Like AverageProductsInOrders, it also inherits from generics.GenericAPIView. The get method does the following:

- Build a cache key using the product_id, e.g., "average_quantity_1".
- Check if the average quantity for the specified product is available in the cache.
- If the cached value is not found, it retrieves all Order objects from the database.
- It initializes variables for the total quantity and the number of orders containing the specified product.
- For each order, it iterates through its products and checks if the product_id matches the requested product_id.
- If a match is found, it increments the total quantity and the number of orders containing the product.
- If there are orders containing the product, it calculates the average quantity by dividing the total quantity by the number of orders with the product and stores the result in the cache with a 5-minute expiration time.
- If the product is not found in any order, the view returns an error message with an HTTP 404 Not Found status.
- Finally, it sends the average quantity of the specified product as a JSON response to the client.



