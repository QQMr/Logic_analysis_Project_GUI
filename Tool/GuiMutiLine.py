#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Burton Huang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

# Debugging commands:
# $ picocom -c --omap crcrlf -b 115200 -f h /dev/ttyUSB0
#   DATE?

import sys
import numpy as np
from PyQt5 import QtGui, QtCore
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from pylab import setp
import matplotlib.pyplot as plt
from Burton_window import Ui_MainWindowBurton

class My_Axes(matplotlib.axes.Axes):
    name = "My_Axes"
    def drag_pan(self, button, key, x, y):
        matplotlib.axes.Axes.drag_pan(self, button, 'x', x, y) # pretend key=='x'

class GuiMutiLine():
    def __init__(self):
        matplotlib.projections.register_projection(My_Axes)
        self.fig, self.axList = self.CreateMatplob()
        print("GuiMutiLine INIT")

        t = np.arange(0.0, 20.0, 0.01)
        s1 = np.sin(2 * np.pi * t)
        self.PlotSignal(t,[s1,s1,s1,s1],["UART-RX","UART-TX","XXX","XXX"]);

    def PlotSignal(self,t,s,chanelName):

        for ax, signal, chName in zip(self.axList, s, chanelName):
            ax.clear()
            ax.plot(t, signal)
            ax.grid(True)
            ax.set_yticks([0, 1])
            ax.set_ylabel(chName)

    def CreateMatplob(self):
        t = np.arange(0.0, 2.0, 0.01)

        plt.style.use('dark_background')
        fig = plt.Figure()
        t = np.arange(0.0, 2.0, 0.01)

        yprops = dict(rotation=0,
                      horizontalalignment='right',
                      verticalalignment='center',
                      x=-0.01)

        axprops = dict(yticks=[0, 1])


        #Register Only X can move for Pan
        ax1 = fig.add_axes([0.1, 0.7, 0.8, 0.2], **axprops,projection="My_Axes")
        ax1.set_ylabel('S1', **yprops)
        axprops['sharex'] = ax1
        axprops['sharey'] = ax1
        # force x axes to remain in register, even with toolbar navigation
        ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.2], **axprops,projection="My_Axes")
        ax2.set_ylabel('S2', **yprops)

        ax3 = fig.add_axes([0.1, 0.3, 0.8, 0.2], **axprops,projection="My_Axes")
        ax3.set_ylabel('S3', **yprops)

        ax4 = fig.add_axes([0.1, 0.1, 0.8, 0.2], **axprops,projection="My_Axes")
        ax4.set_ylabel('S4', **yprops)

        # turn off x ticklabels for all but the lower axes
        for ax in ax1, ax2, ax3:
            setp(ax.get_xticklabels(), visible=False)

        return fig,[ax1,ax2,ax3,ax4]
