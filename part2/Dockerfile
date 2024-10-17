# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts into the container
COPY map.py /app/
COPY reduce.py /app/

# Copy the "counts" and "titles" directories into the container
COPY counts/ /app/counts/
COPY titles/ /app/titles/

# Default command to start a shell
CMD ["/bin/bash"]
