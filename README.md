# Django Customer Orders API

This Django project provides a RESTful API to manage and retrieve customer orders. It is designed to handle a growing number of orders efficiently, using caching, pagination, and database indexing.

## Features

- Fetch an order by order ID
- Fetch the average number of products in all the orders
- Fetch the average quantity of a single product from the orders using the product ID

## Prerequisites

- Python 3.8+
- Docker (optional)

## Setup

### With Docker

1. Clone the repository:

`git clone https://github.com/sbhardwaj7529/LovelyOrdersApp.git`
`cd LovelyOrdersApp`


2. Build the Docker image:

`docker build -t LovelyOrdersApp .`


3. Run the Docker container:

`docker run -p 8000:8000 LovelyOrdersApp`


The API should now be accessible at http://localhost:8000.

### Without Docker

1. Clone the repository:

`git clone https://github.com/sbhardwaj7529/LovelyOrdersApp.git`
`cd LovelyOrdersApp`


2. Create a virtual environment and activate it:

`python3 -m venv venv`
`source venv/bin/activate`

3. Install the required packages:

`pip install -r requirements.txt`


4. Run the Django development server:

`python manage.py runserver`


The API should now be accessible at http://localhost:8000.

## Usage

### Fetch an order by order ID

GET `http://localhost:8000/api/orders/<order_id>`

### Fetch the average number of products in all the orders

GET `http://localhost:8000/api/orders/average-products`

### Fetch the average quantity of a single product from the orders using the product ID

GET `http://localhost:8000/api/orders/average-quantity/<product_id>`

## Populate orders from the third-party API

You can use the provided management command to populate your database with orders from the third-party API:

`python manage.py populate_orders`


