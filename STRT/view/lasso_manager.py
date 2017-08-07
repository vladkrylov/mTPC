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
        print("Callback called")
        p = path.Path(verts)
        self.ind = nonzero([p.contains_point(xy) for xy in self.xys])[0]
        print(self.ind)
        self.canvas.draw_idle()
        self.canvas.widgetlock.release(self.lasso)
        del self.lasso
        self.canvas.mpl_disconnect(self.cid)
        self.cid = self.canvas.mpl_connect('button_press_event', self.onpress)

    def onpress(self, event):
        print("LassoManager.onpress called")
        if self.canvas.widgetlock.locked():
            return
            print("Canvas is locked somehow")
        if event.inaxes is None:
            return
            print("Event is not in axes somehow")
        self.lasso = Lasso(event.inaxes,
                           (event.xdata, event.ydata),
                           self.callback)
        print("Lasso created")
        # acquire a lock on the widget drawing
        self.canvas.widgetlock(self.lasso)
        print("Seems everything is ok here")
        
        
        