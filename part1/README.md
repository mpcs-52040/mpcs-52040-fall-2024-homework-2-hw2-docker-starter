# MNIST Classifier with Docker

This project builds and runs a Docker container that trains an MNIST classifier using TensorFlow, then allows you to classify random images.

## Files

- `train.py`: Python script to train the MNIST model.
- `classify.py`: Python script to classify a given image using the trained model.
- `images`: A folder containing images for testing.

## Steps to Run

1. **Extract the images directory to the current directory:**
   ```bash
   tar xvf images.tar.gz

2. **Run the build.sh script:**
   ```bash
   ./build.sh

3. **Run the run.sh script:**
   ```bash
   ./run.sh

4. **Run the infer.sh script to make predictions:**
   ```bash
   ./infer.sh