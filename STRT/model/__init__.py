from global_coords.data_structures import *

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
        event = self.filter_by_id(self.events, event_id)
        if not event:
            return None
        event.add_track(Track(track_type="selected"))
    
    def remove_track(self, event_id, track_id):
        event = self.filter_by_id(self.events, event_id)
        if not event:
            return None
        
        track = self.filter_by_id(event.tracks, track_id)
        if not track:
            return None
        
        event.tracks.remove(track)
        return True
        
    def add_hits(self, event_id, track_id, hit_indices):
        pass
    
    def remove_hits(self, event_id, track_id, hit_indices):
        pass

    def filter_by_id(self, sequence, item_id):
        res = filter(lambda item: item.id == item_id, sequence)
        if len(res) != 0:
            return res[0]
        return None
        