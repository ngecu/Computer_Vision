# import numpy library
import numpy as np
# import opencv
import cv2

# import matplotlib for plotting histogram
from matplotlib import pyplot as plt
#read the image and store it in a variable called image
image = cv2.imread("./images/panda.JPG")

# Plot a histogram
histogram_image = cv2.calcHist([image], [0], None, [256], [0,256])

plt.hist(histogram_image.ravel(), 256, [0,256])
plt.show()

#view color channels
color = ['b','g','r']

for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0.56])
plt.show ()