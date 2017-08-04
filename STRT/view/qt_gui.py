from PyQt5 import QtCore
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
        test_file_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/STRT/indata/Run25/Event0.txt"  # TODO: add Qt file selection dialog here 
        self.controller.on_load_event(test_file_path)

    def update_with_event(self, event):
        points = [(h.x, h.y) for h in event.hits]
        x = map(lambda point: point[0], points)
        y = map(lambda point: point[1], points)
        self.plotWidget.plot(x, y)
    
    def prev_event(self):
        pass
    
    def next_event(self):
        pass
    
    def add_new_track(self):
        pass
    
    def remove_track(self):
        pass
        
    def select_hits(self):
        pass
    
    def remove_hits(self):
        pass
    

