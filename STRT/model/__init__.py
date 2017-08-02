from global_coords.data_structures import *

class Model():
    def __init__(self):
        self.events = []
        
    def add_event(self, ev):
        if ev not in self.events:
            self.events.append(ev)
            return True
        return False
    
    def remove_event(self):
        pass
    
    def add_hits(self, event, hit_indices):
        pass
    
    def remove_hits(self, event, hit_indices):
        pass
        