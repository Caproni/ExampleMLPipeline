#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

import matplotlib.pyplot as plt
from math import sqrt, floor


def create_histogram(y):

    fig = plt.figure()
    plt.hist(y, bins=floor(sqrt(len(y))))
    fig.show()
