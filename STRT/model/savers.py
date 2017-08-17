import yaml
import os

from model import Track

class Saver():
    def __init__(self):
        self.file = None

    def is_open(self):
        pass

    def save_track(self, track):
        pass


class YamlSaver():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        if not os.path.exists(self.directory):
            raise Exception("Directory %s dos not exist" % self.directory)
        self.track_file = os.path.join(self.directory, "tracks.yaml")
        self.event_file = os.path.join(self.directory, "events.yaml")

    def save_track(self):
        pass

    def save_all(self, events):
        with open(self.event_file, 'w') as evfile:
            with open(self.track_file, 'w') as trfile:
                for e in events:
                    evfile.write(self.dump_event(e))
                    for t in e.tracks:
                        trfile.write(self.dump_track(t))

    def dump_event(self, event):
        x = [hit.x for hit in event.hits]
        y = [hit.y for hit in event.hits]
        return "%s(id=%d, xhits=%s, yhits=%s)" % (event.__class__.__name__, event.id, x, y)

    def dump_track(self, track):
        return "%s(id=%d, event_id=%d, hit_indices=%s)" % (track.__class__.__name__, track.id, track.event_id, track.hit_indices)
    
    
    