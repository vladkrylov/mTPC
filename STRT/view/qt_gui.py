from PyQt5 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow

class QtGui(Ui_MainWindow):
    def __init__(self):
        super(QtGui, self).__init__()
        self.current_event = None
        
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.connect_signals_slots()
        
    def connect_signals_slots(self):
        self.action_load_event.triggered.connect(self.load_new_event)
        
        self.action_previous_event.triggered.connect(self.prev_event)
        self.action_next_event.triggered.connect(self.next_event)
        
        self.action_add_hits_to_track.triggered.connect(self.select_hits)
    
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
        self.current_event = event
        points = [(h.x, h.y) for h in event.hits]
        x = map(lambda point: point[0], points)
        y = map(lambda point: point[1], points)
        self.plotWidget.plot(x, y)
        self.handle_events_navigation(is_first, is_last)
        self.update_status_bar(event)
        self.update_track_list(event)
        
    def update_track_list(self, event):
        
    
    def handle_events_navigation(self, is_first, is_last):
        if is_first and is_last:
            self.action_previous_event.setEnabled(False)
            self.action_next_event.setEnabled(False)
        elif is_first:
            self.action_previous_event.setEnabled(False)
            self.action_next_event.setEnabled(True)
        elif is_last:
            self.action_previous_event.setEnabled(True)
            self.action_next_event.setEnabled(False)
        else:
            self.action_next_event.setEnabled(True)
            self.action_previous_event.setEnabled(True)
    
    def update_status_bar(self, event):
        self.statusbar.showMessage(str(event))
    
    def prev_event(self):
        self.controller.on_show_previous_event(self.current_event)
    
    def next_event(self):
        self.controller.on_show_next_event(self.current_event)
    
    def add_new_track(self):
        pass
    
    def remove_track(self):
        pass
        
    def select_hits(self):
        points = [(h.x, h.y) for h in self.current_event.hits]
        self.plotWidget.select_points(points)
    
    def remove_hits(self):
        pass
    

