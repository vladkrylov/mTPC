from sets import Set
from model.common import filter_by_id


class Event():
    def __init__(self, data_file_path):
        self.path = data_file_path
        self.id = self.set_id()
        self.hits = []
        self.tracks = []
        
    def __repr__(self):
        return "Event %d with %d hits" % (self.id, len(self.hits))
    
    def __eq__(self, other):
        return self.path == other.path
    
    def __neq__(self, other):
        return not self.__eq__(other)
        
    def set_id(self):
        return 0
    
    def add_hit(self, hit):
        self.hits.append(hit)
        
    def add_track(self, new_track):
        self.tracks.append(new_track)
        
    def get_track(self, track_id):
        return filter_by_id(self.tracks, track_id)


class Hit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Hit at %f\t%f" % (self.x, self.y)
        
        
class Track():
    def __init__(self, track_id=0, track_type="selected"):
        self.hit_indices = Set()
        self.id = track_id
        self.type = track_type
        
    
