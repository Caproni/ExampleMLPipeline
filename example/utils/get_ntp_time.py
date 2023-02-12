#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from typing import Optional
from socket import socket, AF_INET, SOCK_DGRAM
from struct import unpack
from datetime import datetime

import example.utils.logger as log


def get_ntp_time(address: str = None) -> Optional[datetime]:
    if address is None:
        log.logger.error("No NTP server address provided")
        return None

    ref_time_1970 = 2208988800

    client = socket(AF_INET, SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (address, 123))
    response, response_address = client.recvfrom(1024)
    if response:
        t = unpack('!12I', response)[10]
        return datetime.fromtimestamp(t - ref_time_1970)
    log.logger.error("No NTP server response returned")
    return None
