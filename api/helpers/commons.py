# Encode to base64 and decode from base64
# base64_convert.py
import numpy as np
import base64
import cv2


def stringToRGB(base64_string):
    '''Decode base64 string to image'''
    im_bytes = base64.b64decode(base64_string)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img


def RGB2String(image):
    '''Encode image to base64'''
    _, im_arr = cv2.imencode('.jpg', image)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64

# im_bytes = base64.b64decode(str_bs64) ## b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\
# im_arr = np.frombuffer(im_bytes, dtype=np.uint8) # [255 216 255 ...  31 255 217]

def strToList(myStr):
    """Convert string to List(tupe, arr)"""
    myStr = myStr.replace("[","")
    myStr = myStr.replace("]","")
    return myStr.split()

def listToString(myList: list):
    """Convert List(tupe, arr) to String"""
    # Output: "[.235, .091024, .82235, .65803]"
    #  Input: [.235 .091024 .82235 .65803]
    # myStr = ' '.join(str(i) for i in myList)
    myStr = str(myList)
    return myStr
