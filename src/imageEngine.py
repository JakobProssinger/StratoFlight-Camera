##############################################################################
# StratoFlight II - The flying Pi                                            #
# Main application for testing the camera settings                           #
# File:     image_engine.py                                                  #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

import os
from systemStatus import getAvailableSpace
import time
from time import sleep
from picamera import PiCamera

##############################################################################

camera = PiCamera()
camera.rotation = -90
camera.resolution = camera.MAX_RESOLUTION
picture_folder = "/home/pi/Desktop/media/engine-images"
image_counter = 0

##############################################################################

def get_date_time():
    date_time = time.strftime("%Y%m%d_%H%M%S")
    return date_time


def images_lowlight() -> None:
    global image_counter
    iso = 300
    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ll-" + str(image_counter) + "-"

    while iso <= 800:
        camera.iso = iso
        shutter_speed = 300000
        while shutter_speed <= 6000000:
            camera.shutter_speed = shutter_speed
            brightness = 45
            while brightness <= 55:
                camera.brightness = brightness

                camera.capture(pre_file_name + "ISO=" + str(iso) + "ShSp=" \
                    + str(shutter_speed) + "BR=" + str(brightness) + ".jpg")
                image_counter += 1
                sleepCounter(2)

                brightness += 1
            shutter_speed += 300000
        iso += 50


def images_shuttspeed(shutsp_min: int, shutsp_step: int, shutsp_max: int) -> None:
    global image_counter
    if shutsp_max > 6000000 or shutsp_min < 500: return
    
    shutsp = shutsp_min
    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ll-" + str(image_counter) + "-"

    while shutsp <= shutsp_max:
        camera.shutter_speed = shutsp
        
        camera.capture(pre_file_name + "ISO=" + str(iso) + ".jpg")
        image_counter += 1
        
        shutsp += shutsp_step


def images_ISO(iso_min: int, iso_step: int, iso_max: int) -> None:
    global image_counter
    if iso_max > 800 or iso_min < 0: return
    
    iso = iso_min
    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ll-" + str(image_counter) + "-"

    while iso <= iso_max:
        camera.iso = iso

        camera.capture(pre_file_name + "ISO=" + str(iso) + ".jpg")
        image_counter += 1

        iso += iso_step


def images_brightness(brightness_min: int, brightness_step: int, brightness_max: int) -> None:
    global image_counter
    if brightness_max > 100 or brightness_min < 0: return
    
    brightness = brightness_min
    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ll-" + str(image_counter) + "-"

    while brightness <= brightness_max:
        camera.brightness = brightness

        camera.capture(pre_file_name + "BR=" + str(brightness) + ".jpg")
        image_counter += 1

        brightness += brightness_step


def sleepCounter(time_s: int) -> None:
    while(time_s != 0):
        os.system('clear')
        print("Waiting " + str(time_s) + " seconds...")
        print("Free space (mb): " + str(getAvailableSpace()))
        print("Current image counter: " + str(image_counter)
        sleep(1)
        time_s -= 1


def main():
    sleepCounter(120)


if __name__ == "__main__":
    main()
