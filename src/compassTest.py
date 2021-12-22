##############################################################################
# StratoFlight II - The flying Pi                                            #
# GY-271 Compass module test with QMC5883L IC                                #
# File:     compassTest.py                                                   #
# Version:  0.0.1.0                                                          #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

from board import SCL, SDA
import busio
import RPi.GPIO as GPIO
import time
import threading
import py_qmc5883l

##############################################################################

i2c_bus = busio.I2C(SCL, SDA)
compass = py_qmc5883l.QMC5883L()

##############################################################################

def getCompassMagn():
    m = compass.get_bearing()
    print(m)


def main():
    while True:
        getCompassMagn()
        time.sleep(2)


if __name__ == "__main__":
    main()
