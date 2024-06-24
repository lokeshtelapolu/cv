import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\mslok\OneDrive\Desktop\istockphoto-1360554439-612x612.jpg")

channels = cv2.split(image)
colors = ('b', 'g', 'r')
channel_names = ('Blue', 'Green', 'Red')


plt.figure(figsize=(10, 5))
plt.title('Color Histogram')
plt.xlabel('Intensity Value')
plt.ylabel('Pixel Count')

    
    # Plot the histogram for each color channel
for channel,color,channel_names in zip(channels,colors,channel_names):
    histogram=cv2.calcHist([channel],[0],None,[256],[0,256])
    plt.plot(histogram, color=color)
    

plt.show()


