import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    if len(lmlist) != 0:

       # if (lmlist[16][1] > lmlist[14][1] and lmlist[20][1] > lmlist[18][1] and lmlist[8][1] < lmlist[6][1] and lmlist[12][1] < lmlist[10][1]) \
          #      or (lmlist[16][1] < lmlist[14][1] and lmlist[20][1] < lmlist[18][1] and lmlist[8][1] > lmlist[6][1] and lmlist[12][1] > lmlist[10][1]):
          #  print("Schere")
        if (lmlist[16][1] > lmlist[14][1]):
            print(print(lmlist[16][1]))
      #  print(lmlist[0])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)