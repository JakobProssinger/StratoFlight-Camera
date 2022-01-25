##############################################################################
# StratoFlight II - The flying Pi                                            #
# Main application for testing the camera settings                           #
# File:     image_engine.py                                                  #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

import os
import time
from time import sleep
from picamera import PiCamera

##############################################################################

camera = PiCamera()
camera.rotation = -90
camera.resolution = camera.MAX_RESOLUTION
picture_folder = "/home/pi/Desktop/media/engine-images"

##############################################################################

def get_date_time():
    date_time = time.strftime("%Y%m%d_%H%M%S")
    return date_time


def images_ISO(image_counter):
    iso = 0

    while iso <= 800:
        camera.iso = iso

        pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ll-" + str(image_counter) + "-"

        camera.capture(pre_file_name + "ISO=" + str(iso) + "-" + ".jpg")
        image_counter += 1

        iso += 100

    return image_counter


def sleepCounter(time_s):
    while(time_s != 0):
        os.system('clear')
        print("Waiting " + str(time_s) + " seconds...")
        sleep(1)
        time_s -= 1


def getFreeSpace():
    path = '/'
    st = os.statvfs(path)
    bytes_avail = (st.f_bavail * st.f_frsize)
    megabytes = bytes_avail / 1024 / 1024


def main():
    image_counter = 0

    image_counter = images_ISO(image_counter)

    sleepCounter(10)

    sleepCounter(120)


if __name__ == "__main__":
    main()
