class Controller():
    def __init__(self, my_model, my_view):
        self.model = my_model
        self.view = my_view
        if self.view:
            self.view.add_listener(self)
        
    def on_event_loaded(self, event_id):
        return self.model.add_event(event_id)
    
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


