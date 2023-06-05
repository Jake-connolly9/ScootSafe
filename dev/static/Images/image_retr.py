import base64
import requests
import urllib.parse
import cv2
from PIL import Image
from rdflib import Graph


def getResId(tag,r):

    try:

        resId = r.json()[tag]['ri']

    except:

        #allready created

        resId = ""

    return resId
# Container Retrieve

print ('ContentInstance Retrieve Request')
print ('************************\n')
url = 'http://' + "100.64.12.153" + ':' + '8080' + '/' + 'cse-in' + '/' + 'Image'+ '/CNT001/la'
print (url)
hdrs = {'X-M2M-RI':'xyz1','X-M2M-Origin':'CImage','X-M2M-RVI': '3','Accept':'application/json'}
r = requests.get(url, headers=hdrs, timeout=5000)
print ('Container Create Response')
print ('*************************\n')
print (r.text)
string = getResId('m2m:cin',r)
print("string")
imgdata = base64.b64decode(str(string))