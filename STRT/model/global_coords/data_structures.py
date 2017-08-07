from model.common import filter_by_id

class Event():
    def __init__(self, ev_id, data_file_path):
        self.path = data_file_path
        self.id = ev_id
        self.hits = []
        self.tracks = []
        
    def __repr__(self):
        return "Event %d with %d hits" % (self.id, len(self.hits))
    
    def __eq__(self, other):
        return self.path == other.path
    
    def __neq__(self, other):
        return not self.__eq__(other)
        
    def add_hit(self, hit):
        self.hits.append(hit)
        
    def add_track(self, new_track):
        self.tracks.append(new_track)
        
    def get_track(self, track_id):
        return filter_by_id(self.tracks, track_id)
    
    def hit_indices_are_valid(self, hit_indices):
        out_of_range = filter(lambda i: i >= len(self.hits), hit_indices)
        if len(out_of_range) == 0:
            return True
        return False
            
            
class Hit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Hit at %f\t%f" % (self.x, self.y)
        
        
class Track():
    def __init__(self, track_id, track_type="selected", color='b'):
        self.hit_indices = []
        self.id = track_id
        self.type = track_type
        self.color = color
        
    def __repr__(self):
        return "Track %d with %d hits" % (self.id, len(self.hit_indices))
    
    def __eq__(self, other):
        return self.id == other.id
    
    def __neq__(self, other):
        return not self.__eq__(other)
    
    def add_hits_indices(self, hit_indices):
        self.hit_indices = list(set(self.hit_indices).union(set(hit_indices)))
        
    def remove_hits_indices(self, hit_indices):
        self.hit_indices = list(set(self.hit_indices) - set(hit_indices))
        
