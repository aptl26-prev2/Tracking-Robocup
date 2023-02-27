import cv2
import numpy as np

video = cv2.VideoCapture(0)

image = cv2.imread('./pic.png')

pink = []
blue = []

while(True):
      


    # print('shape', npframe.shape)
    # Capture the video frame
    # by frame
    ret, frame = video.read()
    npframe = np.array(frame)

    # Range for color detection
    # lower = [80, 80, 200]
    # # lower = [0, 0, 0]
    # upper = [140, 140, 240]
    b_lower = [190, 170, 0]
    b_upper = [255, 220, 150]

    b_lower = np.array(b_lower, dtype="uint8")
    b_upper = np.array(b_upper, dtype="uint8")

    # print(upper)

    b_mask = cv2.inRange(frame, b_lower, b_upper)

    bluecnts = cv2.findContours(b_mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]
    p_lower = [0, 0, 200]
    p_upper = [255, 255, 255]

    p_lower = np.array(p_lower, dtype="uint8")
    p_upper = np.array(p_upper, dtype="uint8")

    p_mask = cv2.inRange(frame, p_lower, p_upper)

    pinkcnts = cv2.findContours(p_mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

    for blue_area in bluecnts:
        if (cv2.contourArea(blue_area) < 100 or cv2.contourArea(blue_area) > 500): continue
        # blue_area = min(bluecnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
        print('xg: ', xg, ',    yg', yg, ',    wg', wg, ',    hg', hg)
        blue.append((xg, yg, wg, hg))


    for pink_area in pinkcnts:
        if (cv2.contourArea(pink_area) < 10 or cv2.contourArea(pink_area) > 5000): continue
        # blue_area = min(bluecnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(pink_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
        print('xg p: ', xg, ',    yg p', yg, ',    wg p', wg, ',    hg p', hg)

        pink.append((xg, yg, wg, hg))
    output = cv2.bitwise_and(frame, frame, mask = p_mask)
  
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