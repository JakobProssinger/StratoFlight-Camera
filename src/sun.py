##############################################################################
# StratoFlight II - The flying Pi                                            #
# Test for the sunposition application                                       #
# File:     sun.py                                                           #
# Version:  0.0.1.0                                                          #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

from sunposition import sunpos
import time
from datetime import datetime

##############################################################################

LAT = 47.7919442
LON = 12.9783463
ELE = 0

def getSunposition():
    now = datetime.utcnow()
    az,zen = sunpos(now, LAT, LON, ELE)[:2]
    elev = 90 - zen
    return (az,elev)


def main():
    while True:
        az,elev = getSunposition()
        print(az, elev)
        time.sleep(15)


if __name__ == "__main__":
    main()
