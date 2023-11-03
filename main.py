import cv2
import numpy as np

from scipy import ndimage
from Quadrants.quadrants import *
from helper import *
from calibration import *
from webcam import *

picture = start()

(actual_area, calculated_area, calibrated_value, pixel_area) = calibrate(img=picture)
print(f"True Gauge Area:\n{round(actual_area, 4)}"
      f"\n\nPixel Area:\n{pixel_area}"
      f"\n\nCalculated Area:\n{round(calculated_area, 4)}"
      f"\n\nCalibration Factor:\n{calibrated_value}\n")
print(f"Calculated Valve Area (in mm^2):\n{calculateValveArea(calibrated_value, img=picture)}")

# (actual_area, calculated_area, calibrated_value, pixel_area) = calibrate()
# print(f"True Gauge Area:\n{round(actual_area, 4)}"
#       f"\n\nPixel Area:\n{pixel_area}"
#       f"\n\nCalculated Area:\n{round(calculated_area, 4)}"
#       f"\n\nCalibration Factor:\n{calibrated_value}\n")
# print(f"Calculated Valve Area (in mm^2):\n{calculateValveArea(calibrated_value, img=)}")

cv2.waitKey(0)
cv2.destroyAllWindows()
