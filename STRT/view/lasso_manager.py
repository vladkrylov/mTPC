from matplotlib import path
from matplotlib.widgets import Lasso
from matplotlib.collections import RegularPolyCollection
from matplotlib.colors import colorConverter
from numpy import nonzero

class LassoManager(object):
    def __init__(self, canvas):
        self.canvas = canvas
        
    def set_points(self, ax, data):
        self.xys = data
        self.cid = self.canvas.mpl_connect('button_press_event', self.onpress)

    def callback(self, verts):
        p = path.Path(verts)
        self.ind = nonzero([p.contains_point(xy) for xy in self.xys])[0]
        print(self.ind)
        self.canvas.draw_idle()
        self.canvas.widgetlock.release(self.lasso)
        del self.lasso

    def onpress(self, event):
        if self.canvas.widgetlock.locked():
            return
        if event.inaxes is None:
            return
        self.lasso = Lasso(event.inaxes,
                           (event.xdata, event.ydata),
                           self.callback)
        # acquire a lock on the widget drawing
        self.canvas.widgetlock(self.lasso)
        
        
        