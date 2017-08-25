import yaml
import os

from model import Event, Track, Hit
from numpy.distutils.fcompiler import none

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
            for e in events:
                evfile.write(self.dump_event(e))
        with open(self.track_file, 'w') as trfile:
            for e in events:
                for t in e.tracks:
                    trfile.write(self.dump_track(t))
                    trfile.write("---\n")
                        
    def load_all(self):
        with open(self.event_file, 'r') as evfile:
            data = evfile.read()
            events = []
        raw_events = data.split("# New Event")
        for e in raw_events:
            if len(e) > 0:
                ev_dict = yaml.load(e)
                ev_id = ev_dict["id"]
                new_event = Event(ev_id, self.directory)
                xhits = ev_dict["xhits"]
                yhits = ev_dict["yhits"]
                new_event.hits = [Hit(x, y) for x, y in zip(xhits, yhits)]
                events.append(new_event)
        
        with open(self.track_file, 'r') as trfile:
            data = trfile.read()
        raw_tracks = data.split("---")
        tracks = [yaml.load(t) for t in raw_tracks if t.split()]
        for t in tracks:
            event_id = t.event_id
            filt_events = filter(lambda ev: ev.id == event_id, events)
            if len(filt_events) > 0:
                event = filt_events[0]
                event.add_track(t)
        
        # assign tracks to events
        return events

    def dump_event(self, event):
        x = [hit.x for hit in event.hits]
        y = [hit.y for hit in event.hits]
        
        props_list = []
        # TODO generate the header accordingly
#         props_list.append("!!python/object:model.global_coords.data_structures.Event")
        props_list.append("# New Event")
        props_list.append("id: %d" % event.id)
#         props_list.append('path: "%s"' % event.path)
        props_list.append("xhits: %s" % x)
        props_list.append("yhits: %s" % y)
        return '\n'.join(props_list)

    def dump_track(self, track):
        props_list = []
        # TODO generate the header accordingly
        props_list.append("!!python/object:model.global_coords.data_structures.Track")
        props_list.append("id: %d" % track.id)
        props_list.append("event_id: %d" % track.event_id)
        props_list.append('color: "%s"' % track.color)
        props_list.append("hit_indices: %s" % track.hit_indices)
        props_list.append("line: !!python/tuple\n- %s\n- %s\n" % (track.line[0], track.line[1]))
        return '\n'.join(props_list)
    
if __name__ == "__main__":
    from model import Event, Track
    with open("../outdata/Run25/tracks.yaml", 'r') as tracks:
        data = tracks.read()
        for t in yaml.load_all(data):
            print t





    