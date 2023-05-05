#!/bin/bash

# Set variables for MongoDB
MONGO_DB_NAME="lovelyordersapp"
MONGO_USER="superuser"
MONGO_PASSWORD="iamsuperuser"
MONGO_PORT=27017
MONGO_CONTAINER_NAME="mongo-server"

# Pull the MongoDB Docker image
docker pull mongo

# Start a new MongoDB container with the specified credentials
docker run -d \
  --name $MONGO_CONTAINER_NAME \
  -p $MONGO_PORT:27017 \
  -e MONGO_INITDB_DATABASE=$MONGO_DB_NAME \
  -e MONGO_INITDB_ROOT_USERNAME=$MONGO_USER \
  -e MONGO_INITDB_ROOT_PASSWORD=$MONGO_PASSWORD \
  mongo

# Wait for MongoDB to start
echo "Waiting for MongoDB to start..."
sleep 10

# Create the database and user for the Django project
echo "Creating the '$MONGO_DB_NAME' database and user '$MONGO_USER'..."
docker exec -it $MONGO_CONTAINER_NAME mongo -u $MONGO_USER -p $MONGO_PASSWORD --authenticationDatabase admin --eval "db=db.getSiblingDB('$MONGO_DB_NAME');db.createUser({user:'$MONGO_USER',pwd:'$MONGO_PASSWORD',roles:[{role:'readWrite',db:'$MONGO_DB_NAME'}]});"

# Show success message
echo "MongoDB container is set up and ready to use!"
