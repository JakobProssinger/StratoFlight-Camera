##############################################################################
# StratoFlight II - The flying Pi                                            #
# SER0006 Servomotor-Testfile                                                #
# File:     camTest.py                                                       #
# Version:  0.0.1.0                                                          #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

import time
from picamera import PiCamera
import threading

##############################################################################

camera = PiCamera()
camera.rotation=-90

fileName = "/home/pi/Desktop/media/default"

def takePicture():
    camera.capture(fileName + ".jpg")


def recordVideo(_secondsToRecord):
    camera.start_preview()
    camera.start_recording(fileName + ".h265")
    camera.wait_recording(_secondsToRecord)
    camera.stop_recording()
    camera.stop_preview()


def main():
    #takePicture()
    recordVideo(10)


if __name__ == "__main__":
    main()
