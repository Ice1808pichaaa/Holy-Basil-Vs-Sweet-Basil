import numpy as np
import cv2
img_counter = 0
video_capture = cv2.VideoCapture('http://IP:81/stream')
#video_capture = cv2.VideoCapture('http://IP/capture')
while(True):
    # Capture frame-by-frame
    #ret, frame = cap.read()
    #video_capture = cv2.VideoCapture('http://IP/capture')
    ret, frame = video_capture.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()
