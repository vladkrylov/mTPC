from PyQt5 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow

class QtGui(Ui_MainWindow):
    def __init__(self):
        super(QtGui, self).__init__()
        
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.connect_signals_slots()
        
    def connect_signals_slots(self):
        self.action_load_event.triggered.connect(self.load_new_event)
    
    def add_listener(self, controller):
        self.controller = controller
    
    def load_new_event(self):
        test_file_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/STRT/indata/Run25"
        filenames = QtWidgets.QFileDialog.getOpenFileNames(self.centralwidget, "QFileDialog.getOpenFileNames()", test_file_path, "All Files (*)")
        self.controller.on_load_events(filenames[0])
#         if filenames:
#             for fn in filenames[0]:
#                 self.controller.on_load_event(fn)
    
    def update_with_event(self, event, is_first=False, is_last=False):
        points = [(h.x, h.y) for h in event.hits]
        x = map(lambda point: point[0], points)
        y = map(lambda point: point[1], points)
        self.plotWidget.plot(x, y)
    
    def on_prev_event(self):
        pass
    
    def on_next_event(self):
        pass
    
    def add_new_track(self):
        pass
    
    def remove_track(self):
        pass
        
    def select_hits(self):
        pass
    
    def remove_hits(self):
        pass
    

