##############################################################################
# StratoFlight II - The flying Pi                                            #
# Methods to get current system status                                       #
# File:     systemStatus.py                                                  #
# Author:   AblL / Leon Ablinger                                             #
##############################################################################

import os

##############################################################################

# getAvailableSpace determines the current disk space available on the system
# (path "/") and returns that value in full megabytes.
def getAvailableSpace() -> int:
    path = '/'
    st = os.statvfs(path)
    bytes_avail = (st.f_bavail * st.f_frsize)
    megabytes = bytes_avail / 1024 / 1024
    return int(megabytes)