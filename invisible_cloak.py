import cv2
import numpy as np
cap = cv2.VideoCapture(0)
back = cv2.imread("./image.jpg")

while cap.isOpened():
    # Take each Frame
    ret, frame = cap.read()
    if ret:
        # Convert RGB Image to HSV Image( Hue, Saturation, Value ) - HSV Image is image interpreted by our Eyes
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red = np.uint8([[[0, 0, 255]]])
        # Get HSV Value from BGR
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #ORANGE_MIN = np.array([5, 50, 50], np.uint8)
        #ORANGE_MAX = np.array([15, 255, 255], np.uint8)
        # Threshold the HSV Values to get only Red Colors
        lower_red = np.array([0,100, 100])
        upper_red = np.array([10, 255,255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        part1 = cv2.bitwise_and(back, back, mask = mask)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask = mask)
        opening = cv2.morphologyEx(part1 + part2, cv2.MORPH_OPEN, hsv_red)
        cv2.imshow("Cloaked Image", opening)
        if cv2.waitKey(5) == ord("Q"):
            break
cap.release()
cv2.destroyAllWindows()


