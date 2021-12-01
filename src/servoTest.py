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

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits
# to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
pca.channels[0].duty_cycle = SERVO_DUTYCYCLE_MIN


def setServoAngleCont():
    print("null")


def setServoDutyCycle(_dutyCycle, _stepDirection):
    _dutyCycle += _stepDirection

    pca.channels[0].duty_cycle = _dutyCycle
    print(pca.channels[0].duty_cycle)
    time.sleep(0.05)
    if _dutyCycle >= SERVO_DUTYCYCLE_MAX:
        _stepDirection = -0x0010
    if _dutyCycle <= SERVO_DUTYCYCLE_MIN:
        _stepDirection = 0x0010
    setServoDutyCycle(_dutyCycle, _stepDirection)


def main():
    setServoDutyCycle(SERVO_DUTYCYCLE_MIN, 0x0010)


if __name__ == "__main__":
    main()
