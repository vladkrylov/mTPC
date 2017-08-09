import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from PyQt5 import QtWidgets
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from lasso_manager import LassoManager
from random import uniform

# def set_main_plot_widget(qt_ui):
class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
#         fig, ax = plt.subplots()
        
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        
        a, b = self.axes.margins()

#         self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass
    
    def test_plot(self):
        pass


class PlotCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
#         self.lasso = LassoManager(self.figure.canvas)
        
        # customize axes view
        self.axes.xaxis.set_visible(False)
        self.axes.yaxis.set_visible(False)
        self.figure.tight_layout()
        self.figure.subplots_adjust(left=0.00,
                                    right=1.00,
                                    top=1.00,
                                    bottom=0.00)
        self.figure.canvas.draw()
        self.figure.canvas.mpl_connect('pick_event', self.onpick)

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)
        
    def test_plot(self, k):
        t = arange(0.0, 3.0, 0.01)
        s = sin(k*pi*t)
        self.axes.plot(t, s)
        self.draw()
        
    def plot(self, x, y, *args):
        self.axes.plot(x, y, 'k.')
        # adjust the ranges
        self.axes.set_xlim([min(x), max(x)])
        self.axes.set_ylim([min(y), max(y)])
        self.draw()
        
    def select_points(self, points):
        self.lasso.set_points(self.axes, points)

    def add_line(self, track):
        x, y = track.line
        self.axes.hold(True)
        line, = self.axes.plot(x, y, color=track.color)
        line.set_visible(True)
        self.axes.hold(False)
        self.draw()
        return line
    
    def onpick(self, click_event):
        line = click_event.artist
        mouse_button = click_event.button
        return
        
class MatplotlibToolbar(NavigationToolbar):
    pass


        