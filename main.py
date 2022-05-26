import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui as pt




cap = cv2.VideoCapture(0)
wCam, hCam = 1280, 720

cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
ctime = 0
ptime = 0

wScr, hScr = pt.size()
frameR = 100

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        if fingers[1] == 1 and sum(fingers)==1:


            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            pt.moveTo(wScr - x3, y3, 0)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

        elif fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (255, 0, 255), cv2.FILLED)
            if length < 45:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pt.click()



    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, str(f'Fps: {int(fps)}'), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
