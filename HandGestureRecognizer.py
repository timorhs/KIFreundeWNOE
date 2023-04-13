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
        #print(lmlist[8][1])
        #print(lmlist[8][1] + lmlist[5][1] + lmlist[12][1] + lmlist[9][1] + lmlist[16][1] + lmlist[13][1] + lmlist[20][1] + lmlist[17][1])
        if (lmlist[16][1] > lmlist[14][1] and lmlist[20][1] > lmlist[18][1] and lmlist[8][1] < lmlist[6][1] and lmlist[12][1] < lmlist[10][1]) \
              or (lmlist[16][1] < lmlist[14][1] and lmlist[20][1] < lmlist[18][1] and lmlist[8][1] > lmlist[6][1] and lmlist[12][1] > lmlist[10][1]):
            print("PEACE")

        elif (lmlist[8][1] > lmlist[5][1] and lmlist[12][1] > lmlist[9][1] and lmlist[16][1] > lmlist[13][1] and lmlist[20][1] > lmlist[17][1]):
            print("FAUST")

        elif (lmlist[8][1] < lmlist[7][1] and lmlist[7][1] < lmlist[6][1] and lmlist[6][1] < lmlist[5][1] and
              lmlist[12][1] < lmlist[11][1] and lmlist[11][1] < lmlist[10][1] and lmlist[10][1] < lmlist[9][1] and
              lmlist[16][1] < lmlist[15][1] and lmlist[15][1] < lmlist[14][1] and lmlist[14][1] < lmlist[13][1] and
              lmlist[20][1] < lmlist[19][1] and lmlist[19][1] < lmlist[18][1] and lmlist[18][1] < lmlist[17][1] and
              lmlist[4][1] < lmlist[3][1] and lmlist[3][1] < lmlist[2][1] and lmlist[2][1] < lmlist[1][1]
        ):
            print("HAND")

       # if (lmlist[16][1] > lmlist[14][1]):
          #  print(print(lmlist[16][1]))
       # print(lmlist[0])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)