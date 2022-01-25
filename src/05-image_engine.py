##############################################################################
# StratoFlight II - The flying Pi                                            #
# Main application for testing the camera settings                           #
# File:     image_engine.py                                                  #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

import time
from time import sleep
from picamera import PiCamera

##############################################################################

def get_date_time():
    date_time = time.strftime("%Y%m%d_%H%M%S")
    return date_time


def capture_consistent_images \
       (frame_rate, iso, number_images, image_counter, picture_folder):
    if(number_images<1):
        number_images = 1
    if(number_images>99):
        number_images = 99
    #
    camera = PiCamera()
    camera.led = True
    camera.rotation=-90
    #
    camera.resolution = camera.MAX_RESOLUTION #V2: (3280, 2464)
    camera.framerate = frame_rate # 1/10...15 with 3280x2464
    camera.iso = iso # automatic:0;60;daylight:100,200;night:400,800
    # wait for the automatic gain control to settle
    sleep(3)
    # now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    # take several photos with the fixed settings
    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        str(framerate.numerator) + "_" + str(framerate.denominator) + \
        "-" + str(iso) + "-" + str(image_counter)
    camera.capture_sequence([pre_file_name + '%02d.jpg' % i for i in range(number_images)])
    camera.led = False
    camera.close()
    image_counter = image_counter + number_images
    return image_counter


#Capturing consistent images, for timelapse photography day only
def sequence_of_consistent_images(number_images, image_counter, picture_folder):
    camera = PiCamera()
    camera.led = False
    camera.rotation=-90
    camera.resolution = camera.MAX_RESOLUTION
    camera.iso = 0
    # Wait for the automatic gain control to settle
    sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g

    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ci-" + str(image_counter) + "-"

    camera.led = True
    # Finally, take several photos with the fixed settings
    camera.capture_sequence([pre_file_name + '%04d.jpg' % i for i in range(number_images)])
    camera.led = False
    camera.close()

    image_counter = image_counter + number_images
    return image_counter


#Capturing consistent images, lowlight
def sequence_of_consistent_images_lowlight(number_images, image_counter, picture_folder):
    camera = PiCamera()
    camera.led = False
    camera.rotation=-90
    camera.resolution = camera.MAX_RESOLUTION
    camera.sensor_mode = 3
    camera.iso = 0
    camera.framerate_range = (0.167, 6)
    camera.exposure_mode = 'nightpreview'
    #raises the gains, and lowers the iso
    sleep(10)
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g

    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ll-" + str(image_counter) + "-"

    camera.led = True
    # Finally, take several photos with the fixed settings
    camera.capture_sequence([pre_file_name + '%04d.jpg' % i for i in range(number_images)])
    camera.led = False
    camera.close()

    image_counter = image_counter + number_images
    return image_counter


#Capturing consistent images, lowlight, for HDR
def sequence_of_consistent_images_lowlight_HDR(image_counter, picture_folder):
    camera = PiCamera()
    camera.led = False
    camera.rotation=-90
    camera.resolution = camera.MAX_RESOLUTION
    camera.sensor_mode = 3
    camera.iso = 0
    camera.framerate_range = (0.167, 6)
    camera.exposure_mode = 'nightpreview'
    #raises the gains, and lowers the iso
    sleep(10)
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    br = camera.brightness
    br0 = br

    pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
       "hdr-" + str(image_counter) + "-"

    camera.led = True
    camera.capture(pre_file_name + str(br) + "-" + "03.jpg")
    image_counter = image_counter + 1
    br = br - 10
    if br > 0:
         camera.brightness = br
         camera.capture(pre_file_name + str(br) + "-" + "02.jpg")
         image_counter = image_counter + 1
         br = br - 10
    if br > 0:
         camera.brightness = br
         camera.capture(pre_file_name + str(br) + "-" + "01.jpg")
         image_counter = image_counter + 1
         br = br + 30
    if br < 100:
         camera.brightness = br
         camera.capture(pre_file_name + str(br) + "-" + "04.jpg")
         image_counter = image_counter + 1
         br = br + 10
    if br < 100:
         camera.brightness = br
         camera.capture(pre_file_name + str(br) + "-" + "05.jpg")
         image_counter = image_counter + 1

    camera.led = False
    camera.close()
    return image_counter


def images_ISO():
    iso = 0
    while iso <= 800:
        camera.iso = iso
        
        pre_file_name = picture_folder + "/" + get_date_time() + "-" + \
        "ll-" + str(image_counter) + "-"
        
        camera.capture(pre_file_name + "ISO=" + str(iso) + "-" + ".jpg")
        iso += 100


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
    import os
    from time import sleep
    picture_folder = "/home/pi/Desktop/media/engine-images"
    image_counter = 0

    camera = PiCamera()
    camera.rotation = -90
    camera.resulotion = camera.MAX_RESOLUTION
    
    images_ISO()

    sleepCounter(10)
    print("Taking consistent images...")
    image_counter = sequence_of_consistent_images(5, image_counter, picture_folder)

    sleepCounter(120)
    print("Taking consistent low light images...")
    image_counter = sequence_of_consistent_images_lowlight(5, image_counter, picture_folder)

    sleepCounter(120)
    print("Taking consistent low light HDR images...")
    image_counter = sequence_of_consistent_images_lowlight_HDR(image_counter, picture_folder)

    sleepCounter(120)


if __name__ == "__main__":
    main()
