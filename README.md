# Django Customer Orders API

This Django project provides a RESTful API to manage and retrieve customer orders. It is designed to handle a growing number of orders efficiently, using caching, pagination, and database indexing.

## Features

- Fetch an order by order ID
- Fetch the average number of products in all the orders
- Fetch the average quantity of a single product from the orders using the product ID

## Prerequisites
- Docker

## Setup

### Initial step

Clone the repository:

`git clone https://github.com/sbhardwaj7529/LovelyOrdersApp.git <br>
cd LovelyOrdersApp`
### Setup mongodb

Just run the shell script `setup_mongodb.sh` which would automatically download mongodb docker image, start its container, create database and credentials inside it. <br> Simply run: `./setup_mongodb.sh`

Note: if you want to stop and remove the spawned container later, then simply run: `docker stop mongo-server && docker rm mongo-server`

### Setup redis

Just run the shell script `setup_redis.sh` which would automatically download redis docker image, start its container, create database and credentials inside it. <br> Simply run: `./setup_redis.sh`

Note: if you want to stop and remove the spawned container later, then simply run: `docker stop redis-instance && docker rm redis-instance`
### Setup the Django app

1. Build the Docker image:

`docker build -t LovelyOrdersApp:latest .`


2. Run the Docker container:

`docker run -p 8000:8000 --name LovelyOrdersApp LovelyOrdersApp:latest`

3. Exec inside the container and run migrations

`docker exec -it bash <br>
python manage.py migrate`


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



