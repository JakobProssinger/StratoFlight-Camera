##############################################################################
# StratoFlight II - The flying Pi                                            #
# SER0006 Servomotor-Testfile                                                #
# File:     servotest.py                                                     #
# Version:  0.0.1.0                                                          #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import RPi.GPIO as GPIO
import time

##############################################################################

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50
SERVO_DUTYCYCLE_MIN = 0x0CCC
SERVO_DUTYCYCLE_MAX = 0x1999

def main():
    pca.channels[0].duty_cycle = SERVO_DUTYCYCLE_MIN
    print("Default position reached.\n")

if __name__ == "__main__":
    main()
