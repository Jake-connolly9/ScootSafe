import cv2
import mediapipe as mp
import base64
import time
import requests
import argparse
import xml.dom.minidom
import urllib.parse
from rdflib import Graph
import RPi.GPIO as GPIO
import pygame.mixer
    # GPIO pin number for the switch
SWITCH_PIN = 17
# WAV file path
WAV_FILE = "/home/taheryusuf/Desktop/350cc-bike-firing-32391.wav"
# Initialize pygame.mixer and the GPIO library
pygame.mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
num = 1
mp_drawing = mp.solutions.drawing_utils
mp_face = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
cap=cv2.VideoCapture(0)
width=640
height=480
Known_distance = 69.0
Known_width = 14.0
Distance = 0
a=[]
def Focal_Length_Finder(Known_distance, real_width, width_in_rf_image):

    focal_length = (width_in_rf_image * Known_distance) / real_width
    return focal_length

def obj_data(img):
    obj_width=0
    image_input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mp_face.process(image_input)
    if not results.detections:
       print("NO FACE")
    else: 
       for detection in results.detections:
           bbox = detection.location_data.relative_bounding_box
           x, y, w, h = int(bbox.xmin*width), int(bbox.ymin * height), int(bbox.width*width),int(bbox.height*height)
           cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
           a.append([x,y])
           obj_width=w
       return obj_width
def Distance_finder(Focal_Length, Known_width, obj_width_in_frame):
    distance = (Known_width * Focal_Length)/obj_width_in_frame
    return distance
def b64():
    with open("image.jpg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    return converted_string
def croneM2M():
    aePayld = "{ \"m2m:ae\": { \"rr\": true, \"api\": \"NR_AE001\", \"apn\": \"IOTApp\", \"csz\": [ \"application/json\" ], \"srv\": [ \"2a\" ], \"rn\": \""+"Image"+ "\" , \"poa\": [ \"http://100.64.12.153:8080\" ] } }" 
    cntPayld = "{ \"m2m:cnt\": { \"rn\": \"CNT001\", \"lbl\": [ \"key1\", \"key2\" ], \"mni\":10} }"

    # AE Create
    print ('AE Create Request')
    print ('*****************')
    print (aePayld)
    print ('*****************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'id-in'
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CImage','X-M2M-RVI': '3','Content-Type':'application/json;ty=2'}
    print (url)
    print (hdrs)
    r = requests.post(url, data=aePayld, headers=hdrs)
    print ('AE Create Response')
    print ('*****************\n')
    print (r.text)
    # Container Create
    print ('Container Create Request')
    print ('************************')
    print (cntPayld)
    print ('************************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'cse-in' + '/' + 'Image'
    print (url)
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CImage','X-M2M-RVI': '3','Content-Type':'application/json;ty=3'}
    r = requests.post(url, data=cntPayld, headers=hdrs)
    print ('Container Create Response')
    print ('*************************\n')
    print (r.text)
    return
def oneM2Mcm(string64):
    ciPayld = "{ \"m2m:cin\": { \"cnf\": \"application/text:0\", \"con\": \"" +  str(string64) + "\" } }"

    # CI Create
    print ('CI Create Request')
    print ('************************')
    print (ciPayld)
    print ('************************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'cse-in' + '/' + 'Image' + '/CNT001'
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CImage','X-M2M-RVI': '3','Content-Type':'application/json;ty=4'}
    r = requests.post(url, data=ciPayld, headers=hdrs)
    print ('CI Create Response')
    print ('*************************')
    print (r.text)
    return 
def dis_oneM2M():
    aePayld = "{ \"m2m:ae\": { \"rr\": true, \"api\": \"NR_AE001\", \"apn\": \"IOTApp\", \"csz\": [ \"application/json\" ], \"srv\": [ \"2a\" ], \"rn\": \""+"Distance"+ "\" , \"poa\": [ \"http://100.64.12.153:8080\" ] } }" 
    cntPayld = "{ \"m2m:cnt\": { \"rn\": \"CNT002\", \"lbl\": [ \"key1\", \"key2\" ], \"mni\":10} }"

    # AE Create
    print ('AE Create Request')
    print ('*****************')
    print (aePayld)
    print ('*****************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'id-in'
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CDistance','X-M2M-RVI': '3','Content-Type':'application/json;ty=2'}
    print (url)
    print (hdrs)
    r = requests.post(url, data=aePayld, headers=hdrs)
    print ('AE Create Response')
    print ('*****************\n')
    print (r.text)
    # Container Create
    print ('Container Create Request')
    print ('************************')
    print (cntPayld)
    print ('************************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'cse-in' + '/' + 'Distance'
    print (url)
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CDistance','X-M2M-RVI': '3','Content-Type':'application/json;ty=3'}
    r = requests.post(url, data=cntPayld, headers=hdrs)
    print ('Container Create Response')
    print ('*************************\n')
    print (r.text) 
    return
def oneM2Mdis(distance):
    ciPayld = "{ \"m2m:cin\": { \"cnf\": \"application/text:0\", \"con\": \"" +  str(distance) + "\" } }"

    # CI Create
    print ('CI Create Request')
    print ('************************')
    print (ciPayld)
    print ('************************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'cse-in' + '/' + 'Distance' + '/CNT002'
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CDistance','X-M2M-RVI': '3','Content-Type':'application/json;ty=4'}
    r = requests.post(url, data=ciPayld, headers=hdrs)
    print ('CI Create Response')
    print ('*************************')
    print (r.text)
    return 
def gps_oneM2M():
    aePayld = "{ \"m2m:ae\": { \"rr\": true, \"api\": \"NR_AE001\", \"apn\": \"IOTApp\", \"csz\": [ \"application/json\" ], \"srv\": [ \"2a\" ], \"rn\": \""+"GPS"+ "\" , \"poa\": [ \"http://100.64.12.153:8080\" ] } }" 
    cntPayld = "{ \"m2m:cnt\": { \"rn\": \"CNT003\", \"lbl\": [ \"key1\", \"key2\" ], \"mni\":10} }"

    # AE Create
    print ('AE Create Request')
    print ('*****************')
    print (aePayld)
    print ('*****************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'id-in'
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CGPS','X-M2M-RVI': '3','Content-Type':'application/json;ty=2'}
    print (url)
    print (hdrs)
    r = requests.post(url, data=aePayld, headers=hdrs)
    print ('AE Create Response')
    print ('*****************\n')
    print (r.text)
    # Container Create
    print ('Container Create Request')
    print ('************************')
    print (cntPayld)
    print ('************************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'cse-in' + '/' + 'GPS'
    print (url)
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CGPS','X-M2M-RVI': '3','Content-Type':'application/json;ty=3'}
    r = requests.post(url, data=cntPayld, headers=hdrs)
    print ('Container Create Response')
    print ('*************************\n')
    print (r.text) 
    return
def oneM2Mgps():
    ciPayld = "{ \"m2m:cin\": { \"cnf\": \"application/text:0\", \"con\": \"" +  '1' + "\" } }"

    # CI Create
    print ('CI Create Request')
    print ('************************')
    print (ciPayld)
    print ('************************\n')
    url = 'http://' + '100.64.12.153' + ':' + '8080' + '/' + 'cse-in' + '/' + 'GPS' + '/CNT003'
    hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CGPS','X-M2M-RVI': '3','Content-Type':'application/json;ty=4'}
    r = requests.post(url, data=ciPayld, headers=hdrs)
    print ('CI Create Response')
    print ('*************************')
    print (r.text)
    return 
def sound():
    if 50< Distance < 450:
        pygame.mixer.music.load(WAV_FILE)
        pygame.mixer.music.play()
    else:
        # Switch released, stop playing
        pygame.mixer.music.stop()
    return 
def switch_callback(channel):
    if GPIO.input(channel) == GPIO.LOW:
        # Switch pressed, play the WAV file
        pygame.mixer.music.load(WAV_FILE)
        pygame.mixer.music.play()
    else:
        # Switch released, stop playing
        pygame.mixer.music.stop()
    return   


Focal_length = 1030
# Add event detection for both rising and falling edges of the switch
GPIO.add_event_detect(SWITCH_PIN, GPIO.BOTH, callback=switch_callback, bouncetime=200)
croneM2M()
dis_oneM2M()
gps_oneM2M()
while True:
    #time.sleep(2)
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480)) 
    cv2.imwrite('image'+str(num)+'.jpg',frame)
    num=num+1
    obj_width_in_frame=obj_data(frame)
    if not obj_width_in_frame:
        print("NO FACE")
        Distance = 0
    else:
        Distance = Distance_finder(Focal_length, Known_width, obj_width_in_frame)
        for i in a:
            x1=i[0]
            y1=i[1]
          
        cv2.putText(frame, f"Distance: {round(Distance,2)} CM", (x1, y1),cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
    
    

    cv2.imshow("FRAME",frame)
    frame=cv2.resize(frame,(120,120)) 
    string64 = b64()
    sound()
    oneM2Mcm(string64)
    oneM2Mgps()
    oneM2Mdis(Distance)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()


