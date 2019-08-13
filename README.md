
# Face-detection-and-Recognition
A Face detection and recognition based on LBPH algorithm described in this paper(https://ieeexplore.ieee.org/document/8124508)

# Requirements

 - python 3.7.0
 - opencv version 4.0.0.21(pip install opencv-python)
 - tkinter module

#  Usage

 1. First Run dataset_genrator.py File.I have capture dataset using Mobile phone camera due to poor quality of laptop-cam so for that you can use [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN).Install on android device start the server and change the url of 8th line in dataset_genrator.py file
 2. This all image will be store in dataset folder after that run face_recognizer.py file this will create Yaml source file in reconizer folder
 3. At the end to detect face use face_detection.py here also you have to change 16th line (url =  'http://192.168.1.108:8080/shot.jpg') or just use comment 16th line and use the cv2.VideoCapture(0)
 
Or directly you can run graphics.pyw which is create using Tkinter,but before using that change the line I mention in step 1 and 3 otherwise it won't run 
