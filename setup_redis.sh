#!/bin/bash

# Download the Redis Docker image
docker pull redis:latest

# Set up environment variables for Redis
REDIS_PORT=6379
REDIS_PASSWORD=iamsuperuser

# Run Redis container with specified port and password
docker run --name redis-instance -p $REDIS_PORT:6379 -d redis:latest redis-server --requirepass $REDIS_PASSWORD
