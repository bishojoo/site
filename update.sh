#!/bin/bash

# Stop and remove the existing Docker container (if it exists)
docker stop bishojo_website || true
docker rm bishojo_website || true

# Remove the existing Docker image (if it exists)
docker rmi bishojo_website || true

# Pull the latest changes from the Git repository
git pull

# Change directory to src
cd src

# Build the Docker image
docker build -t bishojo_website .

# Run the Docker container
docker run -d -p 4888:4888 --name=bishojo_website --restart=unless-stopped bishojo_website
