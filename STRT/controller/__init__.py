class Controller():
    def __init__(self, my_model, my_view):
        self.model = my_model
        self.view = my_view
        self.view.add_listener(self)
        
    def on_event_loaded(self, ev):
        self.model.add_event(ev) 