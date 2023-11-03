import cv2
import math
from helper import *


# High precision value to represent pi
PI = math.pi

# Calibrated value that we will obtain from the gauge
pixel_calibrated_value = 0

# Actual, measured diameter of the gauge in millimeter
gauge_actual_diameter = 5.49

# Actual area of gauge
gauge_actual_area = 0.25 * (gauge_actual_diameter * gauge_actual_diameter) * PI

# Calculated area of gauge
gauge_calculated_area = 0


def calibrate(filename='images/test10.jpg', img=None):
    binaryGaugeImgFilled = None
    # Convert the gauge image into binary, and fill it.
    if img is None:
        binaryGaugeImgFilled = binarizeImage(filename)
    else:
        binaryGaugeImgFilled = binarizeImage(filename=None,img=img)



    # Now we calculate the area
    imgArea = bwarea(binaryGaugeImgFilled)

    pixel_calibrated_value = gauge_actual_area / imgArea
    gauge_calculated_area = imgArea * pixel_calibrated_value

    return gauge_actual_area, gauge_calculated_area, pixel_calibrated_value, imgArea










