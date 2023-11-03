import cv2
import glob
import numpy as np
from scipy import ndimage
from skimage.measure import regionprops
from Quadrants.quadrants import *

WIDTH = 720
HEIGHT = 480

file_name = input("Enter the file name for this jpg image: ")


def areaFormula(nq1, nq2, nq3, nq4, nqd):
    res = 0.25 * (nq1 + (2 * nq2) + (3 * nq3) + (4 * nq4) + (2 * nqd))
    return res

# Takes a string filename to an image file to binarize, returns filled binary image of original input image
def binarizeImage(filename, img=None):
    if img is None:
        img = cv2.imread(filename, 2)

    #resized = cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)

    # Converting the image into binary. The second argument is an integer representing the cutoff intensity for a pixel
    # If a pixel's intensity is above 150, set it to 0. If below 150, set to 1
    ret, bw_image = cv2.threshold(img, 150, 1, cv2.THRESH_BINARY_INV)
    imgArray = np.asarray(bw_image)

    # Fill the image to get rid of stray black pixels
    imgArrayFilled = np.array(ndimage.binary_fill_holes(imgArray), dtype=np.uint8) * 255
    return imgArrayFilled


def bwarea(img):
    properties = regionprops(img)
    return properties[0].area


def calculateValveArea(calibrated_value, targetFile='images/tv12.jpg', img=None):  #enter picture name to find values here
    if img is None:
        img = cv2.imread(targetFile, 2)

  #  file_name = input("Enter the file name for this jpg image: ")

    resized = cv2.resize(img, (720, 480), interpolation=cv2.INTER_AREA)
    ret, bw_image = cv2.threshold(img, 125, 1, cv2.THRESH_BINARY_INV)
    imgArray = np.asarray(bw_image)
    imgArrayFilled = np.array(ndimage.binary_fill_holes(imgArray), dtype=np.uint8) * 255
    cv2.imshow("output", imgArrayFilled)

    #Save the image
    cv2.imwrite("images/" + file_name + "saved.jpg", imgArrayFilled)

    valve_pixel_area = bwarea(imgArrayFilled)
    return calibrated_value * valve_pixel_area

# Returns the bwarea of a binary image
# def bwarea(img):
#     nq0, nq1, nq2, nq3, nq4, nqd = (0, 0, 0, 0, 0, 0)
#     for i in range(1, len(img) - 1):
#         for j in range(1, len(img[i]) - 1):
#             neighborhood = [img[i - 1][j - 1], img[i - 1][j + 1], img[i + 1][j - 1], img[i + 1][j + 1]]
#             quadrant_match = matchPattern(neighborhood)
#             if quadrant_match == 0:
#                 nq0 += 1
#             elif quadrant_match == 1:
#                 nq1 += 1
#             elif quadrant_match == 2:
#                 nq2 += 1
#             elif quadrant_match == 3:
#                 nq3 += 1
#             elif quadrant_match == 4:
#                 nq4 += 1
#             else:
#                 nqd += 1
#     return areaFormula(nq1, nq2, nq3, nq4, nqd)