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

fileName = "/home/pi/Documents/StratoFlight-Camera/media/default_" + str(time.time())

def takePicture():
    camera.capture(fileName + ".jpg")


def recordVideo(_secondsToRecord):
    camera.start_preview()
    camera.start_recording(fileName + ".h264")
    camera.wait_recording(_secondsToRecord)
    camera.stop_recording()
    camera.stop_preview()


def main():
    takePicture()
    recordVideo(5)


if __name__ == "__main__":
    main()
