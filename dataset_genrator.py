import numpy as np
import cv2
import requests,time
class dataset_gen:
    def genrate(_id,name):    
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        #cap = cv2.VideoCapture(0)#TO use laptop cam comment next line and use this
        url = 'http://192.168.1.108:8080/shot.jpg'#add own server name using Ipwebcam android app
        sample=0
        font = cv2.FONT_HERSHEY_SIMPLEX
        while 1:
            #_,frame = cap.read()
            img_re = requests.get(url)
            img_arr = np.array(bytearray(img_re.content),dtype=np.uint8)
            frame = cv2.imdecode(img_arr,-1)
            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.2,6)
            for (x,y,w,h) in faces:
                sample+=1
                if sample == 20:
                    cv2.putText(frame,"change location",(50,50), font,1,255,2,cv2.LINE_AA)
                    time.sleep(5)
                if sample == 40:
                    cv2.putText(frame,"change location",(50,50), font,1,255,2,cv2.LINE_AA)
                    time.sleep(5)
                print("Capture ---> "+str(sample))
                cv2.imwrite("dataset/"+name+"."+str(_id)+"."+str(sample)+".jpg",gray[y:y+h,x:x+w])
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(frame,str(sample),(30,30), font,1,255,2,cv2.LINE_AA)
            cv2.imshow('gray',frame)
            cv2.waitKey(1)
            if sample>=60:
                break
        
        #cap.release()
        cv2.destroyAllWindows()
