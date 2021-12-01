##############################################################################
# StratoFlight II - The flying Pi                                            #
# SER0006 Servomotor-Testfile with Raspberry Pi Cam Module                   #
# File:     servoCamTest.py                                                  #
# Version:  0.0.1.0                                                          #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

from picamera import PiCamera
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import RPi.GPIO as GPIO
import time
import threading

##############################################################################

SERVO_DUTYCYCLE_MIN = 0x0CCC
SERVO_DUTYCYCLE_MAX = 0x1999
SERVO_STEPTIME_S    = 0.025

filePath   = "~/Documents/StratoFlight-Camera/media/"
fileName   = "FHD_F30_R-90"
#fileSufix  = str(SERVO_STEPTIME_S)
fileSufix  = str(time.time())
file = filePath + fileName + "_" + fileSufix

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50
pca.channels[0].duty_cycle = SERVO_DUTYCYCLE_MIN
camera = PiCamera()

##############################################################################

def setServoAngleCont():
    print("null")


def turnServoLoop(_stopEvent, _dutyCycle, _stepDirection):
    while not _stopEvent.is_set():
        _dutyCycle += _stepDirection

        pca.channels[0].duty_cycle = _dutyCycle
        #print(pca.channels[0].duty_cycle)
        time.sleep(SERVO_STEPTIME_S)
        if (_dutyCycle >= SERVO_DUTYCYCLE_MAX) or (_dutyCycle <= SERVO_DUTYCYCLE_MIN):
            _stepDirection = -_stepDirection


def startVideoRecWServo(_secondsToRecord):
    # Create threading event to opt out of event on video finish
    stopEvent = threading.Event()
    servoLoop = threading.Thread(target=turnServoLoop, args=(stopEvent, SERVO_DUTYCYCLE_MIN, 0x0010))

    # Camera settings
    camera.rotation = -90
    camera.framerate = 30
    camera.resolution = (1920, 1080)

    # Record video and show feed on desktop
    camera.start_preview()
    camera.start_recording(file)

    servoLoop.start() # Starts servo turning

    camera.wait_recording(_secondsToRecord) # Waits for _secondsToRecord seconds before continueing

    # Stop recording video
    camera.stop_recording()
    camera.stop_preview()

    # Set event to stop turn loop and to jump back to the main thread
    stopEvent.set()
    servoLoop.join()


def main():
    startVideoRecWServo(15)


if __name__ == "__main__":
    main()
