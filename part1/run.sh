#!/bin/bash

# Run the container in the background, mounting the images directory from the host
docker run -d --name mnist_container -v ./images:/app/images mnist_classifier
