#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Daniel Sangorrin
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
from Burton_window import Ui_MainWindowBurton
from Tool.GuiMutiLine import GuiMutiLine
import serial
import glob
import time
from PyQt5 import QtWidgets as qtw

class Main(qtw.QMainWindow, Ui_MainWindowBurton):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        # add a figure to the canvas with a navigation toolbar
        self.fig = Figure()
        self.ax1f1 = self.fig.add_subplot(111)
        self.GuiMutiLine = GuiMutiLine()
        #self.fig = self.CreateMatplob()
        self.fig =self.GuiMutiLine.fig
        #self.ax1f1.set_autoscalex_on(False)
        self.canvas = FigureCanvas(self.fig)
        self.matplot_vlayout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas,
                self.matplot_widget, coordinates=True)
        self.matplot_vlayout.addWidget(self.toolbar)
        self.ch1_wave = None
        self.interval = None
        self.points = None


    def CreateMatplob(self):
        t = np.arange(0.0, 2.0, 0.01)
        s1 = np.sin(2 * np.pi * t)
        s2 = np.exp(-t)
        s3 = np.sin(2 * np.pi * t) * np.exp(-t)
        s4 = np.sin(2 * np.pi * t) * np.cos(4 * np.pi * t)

        fig = Figure()
        t = np.arange(0.0, 2.0, 0.01)

        yprops = dict(rotation=0,
                      horizontalalignment='right',
                      verticalalignment='center',
                      x=-0.01)

        axprops = dict(yticks=[-1, 0, 1])

        ax1 = fig.add_axes([0.1, 0.7, 0.8, 0.2], **axprops)
        ax1.plot(t, s1)
        ax1.set_ylabel('S1', **yprops)

        axprops['sharex'] = ax1
        axprops['sharey'] = ax1
        # force x axes to remain in register, even with toolbar navigation
        ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.2], **axprops)

        ax2.plot(t, s2)
        ax2.set_ylabel('S2', **yprops)

        ax3 = fig.add_axes([0.1, 0.3, 0.8, 0.2], **axprops)
        ax3.plot(t, s4)
        ax3.set_ylabel('S3', **yprops)

        ax4 = fig.add_axes([0.1, 0.1, 0.8, 0.2], **axprops)
        ax4.plot(t, s4)
        ax4.set_ylabel('S4', **yprops)

        # turn off x ticklabels for all but the lower axes
        for ax in ax1, ax2, ax3:
            setp(ax.get_xticklabels(), visible=False)

        return fig

    def Acquire(self, show_plot=True):

        self.points = 100
      

        tdiv = float(0.1);
        self.interval = (tdiv * 10) / self.points # sample_rate = 1/interval
        x = np.arange(0, self.interval * self.points, self.interval)

        if show_plot:
            self.ax1f1.clear()
            self.ax1f1.set_xlim([0, max(x)])

        self.ax1f1.clear()
        self.ax1f1.set_xlim([0, max(x)])
            



        self.ch1_wave = np.random.randint(7, size=self.points);
        if show_plot:
            self.ax1f1.plot(x, self.ch1_wave)
        self.ax1f1.plot(x, self.ch1_wave)


        self.canvas.draw()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

