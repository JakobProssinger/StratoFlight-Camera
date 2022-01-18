import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)
pca.frequency = 50

servo = servo.Servo(pca.channels[0], actuation_range=180)

servo.angle = 95

pca.deinit()
