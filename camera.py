#!/usr/bin/env python

import os
import imageio
import numpy as np
from time import sleep
import time
import datetime
from picamera import PiCamera
import RPi.GPIO as GPIO
import json
import pickle
from twisted.internet import reactor, protocol


# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    
    def connectionMade(self):
        path = "photosRasp/lebron.jpeg"
        imgC = imageio.imread(path)
        img = np.array(imgC)
        data = {"action":"recognition",
                "image":img.tolist()}
        self.transport.write(json.dumps(data).encode())
    
    def dataReceived(self,data):
        "As soon as any data is received, write it back."
        print("Server said:", data)
        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print("connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Disconnecting...")
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print("Disconnecting...")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("181.54.151.249", 9006, f)
    reactor.run()
    input()
 

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()

def photo(camera):
    os.environ.setdefault('XAUTHORITY', '/home/user/.Xauthority')
    os.environ.setdefault('DISPLAY', ':0.0')
    date = str(datetime.date.today())
    hrs = time.strftime("%H:%M:%S")
    
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    nameFile = "photosRasp/"+date + "-" + hrs + ".jpg"
    camera.capture(nameFile)
    print("save photo")
    camera.stop_preview()

def start():
    pin = 26
    camera = PiCamera()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.IN)
    while True:
        
        if(str(GPIO.input(pin))=="1"):
            photo(camera)
        else:
            print("---") #str(GPIO.input(pin))
        

start()
