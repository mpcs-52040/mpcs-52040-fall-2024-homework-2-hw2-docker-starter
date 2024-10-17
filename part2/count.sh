IMAGE_NAME="word_count_image"

for i in {1..9}
do
  echo "Processing file number $i..."

  # Run the Docker container and execute the word count script with the current argument (1-9)
  docker run --rm -v "$(pwd)/counts:/app/counts" -v "$(pwd)/titles:/app/titles" $IMAGE_NAME python map.py $i
done

docker run --rm -v "$(pwd)/counts:/app/counts" -v "$(pwd)/titles:/app/titles" $IMAGE_NAME python /app/reduce.py

echo "All files processed."