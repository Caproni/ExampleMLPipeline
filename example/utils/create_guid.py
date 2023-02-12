#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

import uuid
from datetime import datetime

from example.utils.get_npt_time import get_ntp_time
from example.utils.logger import logger as log


def create_guid() -> str:
    """
    Creates GUID
    :return: guid string
    """
    log.info("Calling create_guid")
    ntp_time = get_ntp_time(address=None)
    if ntp_time is None:  # if NTP time not available then use system time
        log.warning("Using system time as NTP time not available")
        ntp_time_int = int(round(datetime.now().timestamp()))
    else:
        ntp_time_int = int(ntp_time.timestamp())

    return str(uuid.uuid1(clock_seq=ntp_time_int))
