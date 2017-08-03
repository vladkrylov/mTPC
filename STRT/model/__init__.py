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
    
    def add_track(self, event_id):
        pass
    
    def remove_track(self, event_id, track_id):
        pass
    
    def add_hits(self, event_id, track_id, hit_indices):
        pass
    
    def remove_hits(self, event_id, track_id, hit_indices):
        pass
