FROM tensorflow/tensorflow:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any additional Python dependencies if needed (e.g., imageio for loading images)
RUN pip install imageio

# Install core utilities to ensure tail command is available
RUN apt-get update && apt-get install -y coreutils

# Ensure the model directory exists
RUN mkdir -p /tmp/mnist_model
RUN mkdir -p /images

# Run train.py and keep the container running
CMD ["sh", "-c", "python train.py --model-path /tmp/mnist_model/mnist_model.keras && while true; do sleep 1000; done"]