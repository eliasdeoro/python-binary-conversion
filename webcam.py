import cv2
from helper import*
import time

def display_captured_image(frame):
    cv2.imshow("output_image", frame)
    cv2.imwrite('image_example.png', frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def start():
    vid = cv2.VideoCapture(0)
    frame = None
    while True:
        ret, frame = vid.read()
        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
    return frame

# vid = cv2.VideoCapture(1)
# frame = None
#
# while True:
#     def display_captured_image(frame):
#         cv2.imshow("output_image", frame)
#         cv2.imwrite('image_example.png', frame)
#
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# vid.release()
# time.sleep(2)
# display_captured_image(frame)
# frame = start()
# display_captured_image(frame)