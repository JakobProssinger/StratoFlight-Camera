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

def startVideoPreview():
    camera.start_preview()
    while True:
        time.sleep(1)


def main():
    startVideoPreview()


if __name__ == "__main__":
    main()
