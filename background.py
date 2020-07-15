import cv2
# 0 Indicates my Laptop's Cam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    # Read the Image from Capture from Cam
    # back is what camera reads
    # Ret Tells whether what we were reading, was it successful or not!
    ret, back = cap.read()
    if ret:
        cv2.imshow("Background Image", back)
        if cv2.waitKey(5) == ord("Q"):
            # Save the Background Image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()