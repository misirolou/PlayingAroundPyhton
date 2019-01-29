#Trying out OpenCV following this video: https://www.youtube.com/watch?v=eLTLtUVuuy4
#OpenCV is an open source library around "computer vision" to understand what is happening in certain images,videos,...
#40:25 lesson 7 still to do

import cv2
import numpy as np 
import matplotlib.pyplot as plt 


def canny(image): 
#Converting image to gray scaled image
    grayImage = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
#Heps to remove noise of image, bluring image utilizing the Gaussian blur on the gray image, optional as canny does this already
    blur = cv2.GaussianBlur(grayImage, (5,5), 0)
#Helps to verify different gradients to determine edges in the image
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interests(image):
    height = image.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
#Computing the bitwise & of both images, masks the image according to the region specified in the polygons
    masked_image = cv2.bitwise_and(image, mask)
#Just to understand where the mask is plotted, this is fixed position, need to figure out how to do dynamically
#    plt.imshow(mask)
#    plt.show()
    return masked_image

#Showing the image, no alterations
image  = cv2.imread('OpenCV/test_image.jpg')
lane_image = np.copy(image)
cannyImage = canny(lane_image)
cropt_image = region_of_interests(cannyImage)
cv2.imshow("result", cropt_image)
cv2.waitKey(0)