import ntpath

from model import Event, Track, Hit

class Controller():
    def __init__(self, my_model, my_view):
        self.model = my_model
        self.view = my_view
        if self.view:
            self.view.add_listener(self)
        
    def on_load_event(self, event_file_path):
        ev = self.load_event(event_file_path)
        self.model.add_event(ev)
        if self.view:
            self.view.update_with_event(ev)
    
    def load_event(self, file_path):
        with open(file_path) as infile:
            _, file_name = ntpath.split(file_path)
            ev_id = self.get_new_event_id(file_name, "Event", ".txt")
            ev = Event(ev_id, file_path)
            for line in infile:
                x, y = (float(n) for n in line.split())
                ev.add_hit(Hit(x, y))
        return ev
    
    def get_new_event_id(self, filename, ev_prefix, ev_suffix):
        if filename.startswith(ev_prefix) and filename.endswith(ev_suffix):
            try:
                return int(filename(len(ev_prefix), -len(ev_suffix)))
            except:
                if len(self.model.events) > 0:
                    return self.model.events[-1].id + 1
                else:
                    return 0
        return None
    
    def on_show_next_event(self):
        pass
    
    def on_previous_next_event(self):
        pass
    
    def on_add_track(self, event_id):
        return self.model.add_track(event_id)
    
    def on_remove_track(self, event_id, track_id):
        return self.model.remove_track(event_id, track_id)
    
    def on_add_hits(self, event_id, track_id, selection_data):
        hit_indices = self.selection2hits(selection_data)
        return self.model.add_hits(event_id, track_id, hit_indices)
    
    def on_remove_hits(self, event_id, track_id, selection_data):
        hit_indices = self.selection2hits(selection_data)
        return self.model.remove_hits(event_id, track_id, hit_indices)
    
    def selection2hits(self, selection_data):
        hits = [0]
        return hits


