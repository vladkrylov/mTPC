from random import uniform
from model.common import filter_by_id
from model.color_set import get_color

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
    def __init__(self, track_id, track_type="selected", color=None):
        self.hit_indices = []
        self.id = track_id
        self.type = track_type
        self.line = None
        self.displayed = True
        if color:
            self.color = color
        else:
            try:
                self.color = get_color(self.id)
            except:
                self.color = '#00ff00'
        
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
        
    def set_random_line(self, xlims, ylims):
        x_min, x_max = xlims
        y_min, y_max = ylims
        
        if x_min > 0 and x_max > 0:
            length = x_max - x_min
            x_min += 0.1 * length
            x_max -= 0.1 * length
        elif x_min < 0 and x_max > 0:
            length = x_max - x_min
            x_min += 0.1 * length
            x_max -= 0.1 * length
        elif x_min < 0 and x_max < 0:
            length = x_min - x_max
            x_min -= 0.1 * length
            x_max += 0.1 * length
        else:
            # means x_min > x_max, nonsense
            pass 
        x = [x_min, x_max]
        y = [uniform(y_min, y_max)] * 2
        self.set_line(x, y)
    
    def set_line(self, xs, ys):
        self.line = (xs, ys)
    
    def has_line(self):
        return self.line is not None and len(self.line) == 2
    
    
