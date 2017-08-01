class Event():
    def __init__(self, ev_id):
        self.id = ev_id
        self.hits = []
        
    def add_hit(self, hit):
        self.hits.append(hit)
    

class Hit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Hit at %f\t%f" % (self.x, self.y)
        
        
class Track():
    def __init__(self):
        pass
    
