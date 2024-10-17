# Word Count MapReduce with Docker

## Overview
This project demonstrates a MapReduce word count using Docker containers. It processes multiple text files using mapper and reducer containers.

## Steps to Run

1. **Extract the titles zip to the current directory and make a new counts directory:**
   ```bash
   tar xvf titles.tar.gz
   mkdir -p counts

2. **Run the build.sh script:**
   ```bash
   ./build.sh

3. **Run the count.sh script:**
   ```bash
   ./count.sh

## Top 16 Words

This document provides a summary of the top 16 most frequently used words:

| Word | Count |
|---|---|
| to | 16474 |
| a | 11191 |
| how | 9858 |
| in | 9424 |
| the | 7761 |
| on | 5587 |
| of | 5224 |
| and | 5094 |
| with | 4934 |
| is | 4510 |
| i | 4081 |
| for | 3753 |
| file | 3662 |
| from | 3652 |
| not | 3176 |
| linux | 2960 |

## Known Issues

No known issues are found yet, this works well for Mac 