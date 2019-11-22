# MedianNoise.py
# Written by: Amir Fried
#
# Description:
# This program adds noise and remove it using the median of the N8 neighbours of each pixel
#
# Requires:
# opencv, numpy, argparse, random
#
# How to use:
# python MedianNoise.py -f <image file path>
# Example:
# python MedianNoise.py -f cameraman.jpg

import argparse
import cv2
import random
import numpy as np

# Arguments management:
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="Path to the image file")
args = vars(ap.parse_args())
image_file = args["file"]

# Image load (in graycycle)
image = cv2.imread(image_file, 0)
height, width = image.shape

# Adding noise (making 100 random pixels black)
for i in range(100):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    image[y, x] = 0

# Creating a filtered image by using the median of the N8 neighbours of each pixel
filtered_image = np.uint8(np.zeros((height, width)))
for x in range(width):
    for y in range(height):
        xmin = 0 if x == 0 else x - 1
        xmax = width - 1 if y == width - 1 else x + 1
        ymin = 0 if y == 0 else y - 1
        ymax = height - 1 if y == height - 1 else y + 1
        neighbours_matrix = image[ymin:ymax, xmin:xmax]
        filtered_image[y, x] = int(round(np.median(neighbours_matrix)))

# Printing the noisy and filtered images
cv2.imshow("Noisy Image", image)
cv2.imshow("After Filter", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
