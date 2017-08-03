from global_coords.data_structures import *
from common import filter_by_id

class Model():
    def __init__(self):
        self.events = []
        
    def add_event(self, ev):
        if ev in self.events:
            return False
        self.events.append(ev)
        return True
    
    def remove_event(self):
        pass
    
    def add_track(self, event_id):
        event = self.get_event(event_id)
        if not event:
            return None
        track_id = self.generate_track_id(event)
        event.add_track(Track(track_id=track_id, 
                              track_type="selected"))
        return True
    
    def remove_track(self, event_id, track_id):
        event = self.get_event(event_id)
        if not event:
            return None
        
        track = filter_by_id(event.tracks, track_id)
        if not track:
            return None
        
        event.tracks.remove(track)
        return True
        
    def add_hits(self, event_id, track_id, hit_indices):
        pass
    
    def remove_hits(self, event_id, track_id, hit_indices):
        pass
    
    def get_event(self, event_id):
        return filter_by_id(self.events, event_id)
        
    def generate_track_id(self, event):
        existing_ids = [tr.id for tr in event.tracks]
        if len(existing_ids) == 0:
            return 0
        return max(existing_ids) + 1 
        
        
        