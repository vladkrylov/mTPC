from mainwindow import Ui_MainWindow
from global_coords import load_event

class QtGui(Ui_MainWindow):
    def __init__(self):
        super(QtGui, self).__init__()
        
    def add_listener(self, controller):
        self.controller = controller
        
    def load_new_event(self):
        test_file_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/STRT/indata/Run25/Event0.txt"  # TODO: add Qt file selection dialog here 
        ev = load_event(test_file_path)
        self.controller.on_event_loaded(ev)

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
    

