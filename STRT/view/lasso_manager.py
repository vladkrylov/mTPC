from matplotlib import path
from matplotlib.widgets import Lasso
from matplotlib.collections import RegularPolyCollection
from matplotlib.colors import colorConverter
from numpy import nonzero

class LassoManager(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.dummy_already_pressed = False  # single click bugfix
                                            # see the commit ... for details
        
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
        self.dummy_already_pressed = False

    def onpress(self, event):
        if self.canvas.widgetlock.locked():
            if self.dummy_already_pressed:
                self.canvas.widgetlock.release(self.lasso)
                del self.lasso
            else:
                print("Canvas is locked somehow")
                return
        if event.inaxes is None:
            return
        self.lasso = Lasso(event.inaxes,
                           (event.xdata, event.ydata),
                           self.callback)
        # acquire a lock on the widget drawing
        self.canvas.widgetlock(self.lasso)
        self.dummy_already_pressed = True
        
        
        