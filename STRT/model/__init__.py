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
        event, track = self.get_event_and_track(event_id, track_id)
        if not track or not event:
            return False
        event.tracks.remove(track)
        return True
        
    def add_hits(self, event_id, track_id, hit_indices):
        event, track = self.get_event_and_track(event_id, track_id)
        if not track or not event:
            return False
        if not event.hit_indices_are_valid(hit_indices):
            return False
        
        track_index = event.tracks.index(track)
        
        track.hit_indices = set(track.hits).union(hit_indices)
        
        event.tracks[track_index] = track
        return True
    
    def remove_hits(self, event_id, track_id, hit_indices):
        pass
    
    def get_event(self, event_id):
        return filter_by_id(self.events, event_id)
        
    def generate_track_id(self, event):
        existing_ids = [tr.id for tr in event.tracks]
        if len(existing_ids) == 0:
            return 0
        return max(existing_ids) + 1 
        
    def get_event_and_track(self, event_id, track_id):
        event = self.get_event(event_id)
        track = None
        if event:
            track = filter_by_id(event.tracks, track_id)
        return event, track
        
        