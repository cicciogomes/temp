import cv2
from datetime import datetime

def contains(r1,r2): 
    return r1[0]<r2[0]<r2[0]+r2[2]<r1[0]+r1[2] and r1[1]<r2[1]<r2[1]+r2[3]<r1[1]+r1[3]

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'MJPG')
out = None
bg_mode = False
dt_mode = False
rec = False
ret, _ = cap.read()


if not(ret):
    print("not connected")
    exit(0)

#face_cascade=cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
#smile_cascade=cv2.CascadeClassifier("data/haarcascade_smile.xml")

##webcam get img
#cv2.imshow("cam",frame)
#cv2.imwrite("cam.jpg",frame)
#cv2.waitKey(0)

##live

while (cap.isOpened()):

    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if (bg_mode): ######bianco nero
        frame = gray
    if (dt_mode): ###### data live
        now=datetime.now()
        str_now=now.strftime("%d/%m/%Y %H:%M:%S")
        cv2.putText(frame,str_now,(20,frame.shape[0]-20),cv2.FONT_HERSHEY_PLAIN,1.5,(255,255,255),2)
    if (rec): ########video
        out.write(frame)
        cv2.circle(frame,(frame.shape[1]-30,frame.shape[0]-30),10,(0,0,255),cv2.FILLED)
    
    #faces=face_cascade.detectMultiScale(gray,1.1,8)
    #smile=smile_cascade.detectMultiScale(gray,1.45,50)
   # for f in faces:
   #     cv2.rectangle(frame,(f[0],f[1]),(f[0]+f[2],f[1]+f[3]),(0,0,200),2)
   #     for s in smile:
   #         if (contains(f,s)):
   #             cv2.rectangle(frame,(s[0],s[1]),(s[0]+s[2],s[1]+s[3]),(250,0,0),2)
   
    cv2.imshow("web",frame)
    k=cv2.waitKey(1)
   
    if (k==ord("b")):
        bg_mode = not bg_mode
        print("bianco/nero è : %s" %bg_mode)

    elif (k==ord("t")):
        dt_mode = not dt_mode
        print("Printato data è : %s" %dt_mode)

    elif (k==ord("c")): #####salva frame
        now=datetime.now()
        filen=now.strftime("%Y%m%d%H%M%S")+".jpg"
        cv2.imwrite(filen,frame)
        print("saved data è : %s" %filen)
    elif (k==ord("v")):
        if (out==None):
            out= cv2.VideoWriter('outpweb.avi',codec,20.,(640,480)) ####video
        rec = not rec
    elif (k==ord("q")):
        break

if (out!=None):
    out.release()

cap.release()
cv2.destroyAllWindows()
        

