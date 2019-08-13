# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:52:49 2019

@author: Light
"""
import os
import cv2
import numpy as np
from PIL import Image

class training:
    def train():
        reconizer = cv2.face.LBPHFaceRecognizer_create()
        path="dataset"
        def getImagewithId(path):
            imagePath=[os.path.join(path,i) for i in os.listdir(path)]
            print(imagePath)
            faces,Id=[],[]
            
            for impath in imagePath:
                faceImg = Image.open(impath).convert('L')
                faceNp = np.array(faceImg,'uint8')
                faces.append(faceNp)
                ID = int(impath.split('\\')[1].split('.')[1])
                print("training on "+str(ID))
                Id.append(ID)
                cv2.imshow("training image",faceNp)
                cv2.waitKey(10)
            return np.array(Id),faces
        
        Id,faces = getImagewithId(path)
        reconizer.train(faces,Id)
        reconizer.save('reconizer/traindata.yml')
        cv2.destroyAllWindows()