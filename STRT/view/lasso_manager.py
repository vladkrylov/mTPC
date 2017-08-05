from matplotlib import path
from matplotlib.widgets import Lasso
from matplotlib.collections import RegularPolyCollection
from matplotlib.colors import colorConverter
from numpy import nonzero

class LassoManager(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.cid = self.canvas.mpl_connect('button_press_event', self.onpress)
        
    def set_points(self, ax, data):
        self.xys = data
#         self.axes = ax
#         self.canvas = ax.figure.canvas
#         self.data = data
# 
#         self.Nxy = len(data)
# 
# #         facecolors = [d.color for d in data]
# #         self.xys = [(d.x, d.y) for d in data]
#         self.xys = data
#         facecolors = [colorConverter.to_rgba('blue') for _ in range(len(self.xys))]
#         self.ind = []
#         fig = ax.figure
#         self.collection = RegularPolyCollection(
#             fig.dpi, 6, sizes=(100,),
#             facecolors=facecolors,
#             offsets=self.xys,
#             transOffset=ax.transData)
# 
#         ax.add_collection(self.collection)


    def callback(self, verts):
        facecolors = [colorConverter.to_rgba('blue') for _ in range(len(self.xys))]
        p = path.Path(verts)
        ind = p.contains_points(self.xys)
        self.ind = nonzero([p.contains_point(xy) for xy in self.xys])[0]
        for i in range(len(self.xys)):
            if ind[i]:
                facecolors[i] = colorConverter.to_rgba('red')
#                print ind
            else:
                facecolors[i] = colorConverter.to_rgba('blue')

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
        
        
        