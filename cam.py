import cv2
import numpy as np

video = cv2.VideoCapture(0)

image = cv2.imread('./pic.png')

pink = []
blue = []

while(True):
      
    
    check, frame = video.read()

    npframe = np.array(frame)
    # print('shape', npframe.shape)
    # Capture the video frame
    # by frame
    ret, frame = video.read()

    # Range for color detection
    lower = [80, 80, 200]
    # lower = [0, 0, 0]
    upper = [140, 140, 240]

    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # print(upper)

    mask = cv2.inRange(frame, lower, upper)

    bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(bluecnts)>0:
        blue_area = max(bluecnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
        print('xg: ', xg, ',    yg', yg, ',    wg', wg, ',    hg', hg)

    pink.append((xg, yg, wg, hg))
    output = cv2.bitwise_and(frame, frame, mask = mask)
  
    # Display the resulting frame
    # cv2.imshow("frames", frame)
    cv2.imshow("frames", np.hstack([frame, output]))
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)

video.release()