class Event():
    def __init__(self, id):
        self.id = id
        self.hits = []
        
    def add_hit(self, hit):
        self.hits.append(hit)
    

class Hit():
    def __init__(self, FEC, board, chip, xp, yp, value):
        self.FEC = FEC 
        self.board = board
        self.chip = chip
        self.xp = xp
        self.yp = yp
        self.value = value
        
    def __repr__(self):
        return "%d %d %d, Chip %d, Board %d, FEC %d" % (self.xp, self.yp, self.value, self.chip, self.board, self.FEC)
        
        
class Track():
    def __init__(self):
        pass
    
