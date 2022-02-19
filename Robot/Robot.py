import cv2
import mediapipe as mp
import time
import math 

def GetHandCommand(cap):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    pTime = 0
    cTime = 0

    #while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
    ditaestese=[0,0,0,0,0]

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            memHand=[]
            for id, lm in enumerate(handLms.landmark):
                    #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                    #print(id, cx, cy)
                memHand.append([cx,cy])
                if id == 0:
                    cv2.circle(img, (cx, cy), 25,(255, 0, 255), cv2.FILLED)
                ####get length dito
                
            mano=[]
            manobase=[]
                ##pollice differente gli altrri lunghezza dito
            manobase.append(math.sqrt(pow((memHand[0][0]-memHand[2][0]),2)+pow((memHand[0][1]-memHand[2][1]),2)))
            lPollice=math.sqrt(pow((memHand[3][0]-memHand[11][0]),2)+pow((memHand[3][1]-memHand[11][1]),2))
            mano.append(lPollice)
            manobase.append(math.sqrt(pow((memHand[0][0]-memHand[5][0]),2)+pow((memHand[0][1]-memHand[5][1]),2)))
            lIndice=math.sqrt(pow((memHand[5][0]-memHand[8][0]),2)+pow((memHand[5][1]-memHand[8][1]),2))
            mano.append(lIndice)
            manobase.append(math.sqrt(pow((memHand[0][0]-memHand[9][0]),2)+pow((memHand[0][1]-memHand[9][1]),2)))
            lMedio=math.sqrt(pow((memHand[9][0]-memHand[12][0]),2)+pow((memHand[9][1]-memHand[12][1]),2))
            mano.append(lMedio)
            manobase.append(math.sqrt(pow((memHand[0][0]-memHand[13][0]),2)+pow((memHand[0][1]-memHand[13][1]),2)))
            lAnulare=math.sqrt(pow((memHand[13][0]-memHand[16][0]),2)+pow((memHand[13][1]-memHand[16][1]),2))
            mano.append(lAnulare)
            manobase.append(math.sqrt(pow((memHand[0][0]-memHand[17][0]),2)+pow((memHand[0][1]-memHand[17][1]),2)))
            lMignolo=math.sqrt(pow((memHand[17][0]-memHand[20][0]),2)+pow((memHand[17][1]-memHand[20][1]),2))
            mano.append(lMignolo)
                #print("pollice " + str(lPollice)+" indice "+str(lIndice)+" Medio "+str(lMedio)+" anulare "+str(lAnulare)+" Mignolo "+str(lMignolo))
            for dita in range(len(mano)):
                    #print("dito ref: "+str(lditoesteso))
                if mano[dita]>0.7*manobase[dita]:
                        #print("dito "+str(dita)+" esteso: "+ str(mano[dita]))
                    ditaestese[dita]=1
                else:
                        #print("dito "+str(dita)+" chiuso: "+ str(mano[dita]))
                    ditaestese[dita]=0
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        #print(ditaestese)
        #cTime = time.time()
        #fps = 1/(cTime-pTime)
        #pTime = cTime
        #time.sleep(0.1)
        #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
    return img,ditaestese
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(3 , wCam)
cap.set(4 , hCam)
while True:
    img,mano=GetHandCommand(cap)
    if mano==[0,0,0,0,0]:
        print("STOP")
    elif mano==[1,1,0,0,0]:
        print("SPARA!!!")
    elif mano==[0,1,0,0,0]:
        print("SEGUI")
    cv2.imshow("Image", img)
    if(cv2.waitKey(1)==ord("q")):
        break
    cv2.waitKey(1)
cap.release()
##out.release()
cv2.destroyAllWindows()
