import config
import time
import RPi.GPIO as GPIO
import threading
import datetime
import os

shutdown_flag = False  # True if shutdown

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(config.REQUEST_SHUTDOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def shutdown_raspbery() -> None:
    os.system("sudo shutdown now")


def get_Shutdown_Flag() -> bool:
    return shutdown_flag


def stuff() -> None:
    global shutdown_flag
    if GPIO.input(config.REQUEST_SHUTDOWN_PIN) is config.SHUTDOWN_REQUEST:
        shutdown_flag = True


def check_shutdown() -> None:
    if GPIO.input(config.REQUEST_SHUTDOWN_PIN) is config.SHUTDOWN_REQUEST:
        print(datetime.datetime.now())
        threading.Timer(config.SHUTDOWN_DELAY, stuff).start()


if __name__ == '__main__':
    while True:
        check_shutdown()
        time.sleep(30)
