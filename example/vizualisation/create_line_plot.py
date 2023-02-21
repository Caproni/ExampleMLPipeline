#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

import matplotlib.pyplot as plt


def create_line_plot(x, y):

    fig = plt.figure()
    plt.plot(x, y)
    fig.show()
