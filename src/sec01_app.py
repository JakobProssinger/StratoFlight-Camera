##############################################################################
# StratoFlight II - The flying Pi                                            #
# Main application for managing the servo                                    #
# File:     servoapp.py                                                      #
# Version:  0.0.1.0                                                          #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

##############################################################################

DELAY_BETWEEN_STEP = 0.15
ANGLE_CURRENT = 90

##############################################################################

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)
pca.frequency = 50

servo = servo.Servo(pca.channels[0], actuation_range=180)
servo.angle = ANGLE_CURRENT
time.sleep(0.5)
servo.angle = None

stepDir = 0

def turnToAngle(_angle : int) -> None:
    global ANGLE_CURRENT

    servo.angle = ANGLE_CURRENT

    if _angle < servo.angle:
        stepDir = -1
    elif _angle > servo.angle:
        stepDir = 1
    else:
        return

    while stepDir == +1 and servo.angle <= _angle or \
          stepDir == -1 and servo.angle >= _angle:
        try:
            servo.angle += stepDir
        except ValueError:
            print("End reached.")
            break
        time.sleep(DELAY_BETWEEN_STEP)
        print(servo.angle)

    ANGLE_CURRENT = servo.angle
    servo.angle = None


def main() -> None:
    while True:
        temp = int(input("Angle: "))
        turnToAngle(temp)


if __name__ == "__main__":
    main()
    pca.deinit()
