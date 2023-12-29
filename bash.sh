#!/bin/bash

# Build the Docker image
docker build -t bst-container .

# Run the Docker container
docker run -it --rm bst-container
