import numpy as np
import cv2

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
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()
