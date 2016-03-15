
from bottle import static_file,route,run,request
import json
import os
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import math
import time
from PIL import Image
import random

@route('/')
def loadIndex():
    return static_file('index.html', root='./') #sets up web page
@route('/<filename:re:.*\..*>')#matches files
def sendWebFile(filename):
    return static_file(filename, root='./')
@route('/runScript',method = "POST")
def script():
    execfile('comparetest.py')
run(host='localhost',port=8080,debug=True)
