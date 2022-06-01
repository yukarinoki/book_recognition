import sys
import cv2
import util
from matplotlib import pyplot as plt

for i, grayscale_image_file in enumerate(util.grayscale_image_files):
    if i == 0: 
        img = cv2.imread(grayscale_image_file)
        edges = cv2.Canny(img, 100, 200)
        
        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()

