import cv2
import numpy as np
###i commenti per salvare il video proocessato
size =(320,320) ###per aum risoluz yolo 608 da pjreddie/darknet.com yolo
MIN_CONFIDENCE=0.3
TARGET_CLASSES = None

def load_yolo(yolo_path=""):

    net = cv2.dnn.readNet(yolo_path+"yolov3.weights",yolo_path+"yolo3.cfg")

    layers_name = net.getLayerNames()
    output_layers = [layers_name[i[0]-1] for i in net.getUnconnectedOutLayers()]

    classes = []

    with open(yolo_path+"coco.names","r")as f:
        classes = [line.strip() for line in f.readlines()]

    colors = np.random.uniform(0,255,size = (len(classes),3)).astype(int)

    return net, output_layers,classes, colors


def detect_objects(img,net,output_layers):

    img=cv2.resize(img,size)
    blob = cv2.dnn.blobFromImage(img,scalefactor=1/255,size=size)
    net.setInput(blob)
    outputs = net.forward(output_layers)
    return(outputs)
def get_boxes(outputs,height,width):
    
    boxes=[]
    class_ids=[]
    confs=[]
    
    for output in outputs:
        for detect in output:
            scores=detect[5:]
            class_id=np.argmax(scores)
            conf=scores[class_id]
            
            if (TARGET_CLASSES!=None and classes[class_id] not in TARGET_CLASSES):
                continue



            if(conf>=MIN_CONFIDENCE):

                center_x= int(detect[0]*width)
                center_y= int(detect[1]*height)
                w=int(detect[2]*width)
                h=int(detect[3]*height)
                x=int(center_x-w/2)
                y=int(center_y-h/2)

                boxes.append([x,y,w,h])
                class_ids.append(class_id)
                confs.append(conf)
            
    return boxes, class_ids, confs
def non_max_suppress ( boxes,confidences,min_confidence, thresold):
    boxes_max =[]
    boxesIds= cv2.dnn.NMSBoxes(boxes,confidences,min_confidence, thresold)

    for boxId in boxesIds:
        boxes_max.append(boxes[boxId[0]])
    
    return boxes_max

def draw_results(img,boxes,class_ids,confs=None):
    
    for i in range(len(boxes)):
        
        box=boxes[i]
        class_id=class_ids[i]

        x,y,w,h = box
        color = colors[class_id].tolist()

        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)

        label= classes[class_id]

        if(confs!=None):
            label+=" (%1.f%%)"% (confs[i]*100)
        cv2.putText(img,label,(x,y-5),cv2.FONT_HERSHEY_PLAIN,2,color,1)
    
    return img



net,output_layers,classes,colors =load_yolo()
##vid_path = input("scegli video : ")
##out_path = "video_det.avi")

cap =cv2.VideoCapture(0) ###da tetare con 1 con sua camera
ret,frame=cap.read()
##codec = cv2.VideoWriter_fourcc(*'MJPG') ##dipende da sistema operativo

##out = cv2.VideoWriter(out_path,codec,20.0,(frame.shape[1],frame.shape[0]))
##frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
##current_frame =1

if (not ret):
    exit(0)

while (cap.isOpened()):

    ret,frame =cap.read()

    if (not ret):
        break

   ## print("proces frame: %d di %d" %(current_frame,frame_count),end="")

    outputs = detect_objects(frame,net,output_layers)
    boxes,class_ids,confs =get_boxes(outputs,frame.shape[0],frame.shape[1])
    boxes= non_max_suppress(boxes,confs,MIN_CONFIDENCE,0.3) ###riduce numero di box riconosciuti
    frame=draw_results(frame,boxes,class_ids)

    ##out.write(frame)
    ##current_frame+=1


    cv2.imshow("video",frame) ##
    if(cv2.waitKey(1)==ord("q")):
        break

cap.release()
##out.release()
cv2.destroyAllWindows()
