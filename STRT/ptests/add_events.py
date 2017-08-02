from random import randint
from controller import Controller
from model import Model, Event

def generate_event(max_possible_id):
    ev_id = randint(0, max_possible_id)
    ev = Event("/some/dummy/path%d" % ev_id)
    ev.id = ev_id
    return ev

def add_events():
    m = Model()
    c = Controller(m, None)
    
    max_possible_id = 20
    for i in range(10):
        ev = generate_event(max_possible_id)
        added = c.on_event_loaded(ev)
        
        if added:
            print("%s was added" % str(ev))
        else:
            print("%s was not added" % str(ev))
        



