#!/usr/bin/env python

import os
from time import sleep
import time
import datetime
from picamera import PiCamera
import RPi.GPIO as GPIO

def photo():
    os.environ.setdefault('XAUTHORITY', '/home/user/.Xauthority')
    os.environ.setdefault('DISPLAY', ':0.0')
    date = str(datetime.date.today())
    hrs = time.strftime("%H:%M:%S")
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    camera.capture("photosRasp/"+date + "-" + hrs + ".jpg")
    print("save photo")
    camera.stop_preview()

def start():
    pin = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.IN)
    while True:
        if GPIO.input(pin) == 1:
            print(GPIO.input(pin))
        time.sleep(0.1)        
        

start()
        
    
