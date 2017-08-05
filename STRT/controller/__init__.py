import ntpath

from model import Event, Track, Hit

class Controller():
    def __init__(self, my_model, my_view):
        self.model = my_model
        self.view = my_view
        if self.view:
            self.view.add_listener(self)
        
    def on_load_events(self, event_file_paths):
        if len(event_file_paths) == 0:
            return
        first_loaded_event = None
        for event_file_path in event_file_paths:
            ev = self.load_event(event_file_path)
            loaded = self.model.add_event(ev)
            if loaded and first_loaded_event is None:
                first_loaded_event = ev
        if self.view and first_loaded_event:
            self.view.update_with_event(first_loaded_event, is_first=True, is_last=False)
    
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
    
    def on_show_next_event(self, current_event):
        i = self.model.events.index(current_event)
        is_last = i == len(self.model.events) - 1
        if is_last:
            return
        next_event = self.model.get_event(i+1)
        is_last = (i+1) == len(self.model.events) - 1
        self.view.update_with_event(next_event, is_first=False, is_last=is_last)
    
    def on_show_previous_event(self, current_event):
        i = self.model.events.index(current_event)
        is_first = i == 0
        if is_first:
            return
        prev_event = self.model.get_event(i-1)
        is_first = (i-1) == 0
        self.view.update_with_event(prev_event, is_first=is_first, is_last=False)
    
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

