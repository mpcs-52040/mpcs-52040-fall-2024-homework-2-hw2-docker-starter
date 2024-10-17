#!/bin/bash

# Randomly select an image from the images directory
IMAGE=$(ls images | shuf -n 1)

# Output the chosen image
echo "Classifying image: $IMAGE"

# Run inference inside the Docker container
docker exec mnist_container python classify.py --input //app/images/${IMAGE}
