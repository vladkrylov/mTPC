from unittest import TestCase
from random import randint
from model import Model, Event

def generate_event(max_possible_id, ev_id=None):
    if ev_id is None:
        ev_id = randint(0, max_possible_id)
        
    ev = Event("/some/dummy/path%d" % ev_id)
    ev.id = ev_id
    return ev


class TestActions():
    def __init__(self):
        self.add_event = Model.add_event


class TestModelAPI(TestCase):
    
    def test_add_events(self):
        m = Model()
        event_ids = [4, 4, 8, 2, 4, 2, 3, 6, 7, 0, 10, 4, 0, 4, 4, 5, 2, 8, 10, 3]
        
        for ev_id in event_ids:
            ev = generate_event(None, ev_id)
            m.add_event(ev)
        
        loaded_events = [ev.id for ev in m.events]
        should_be = [4, 8, 2, 3, 6, 7, 0, 10, 5]
        self.assertEqual(should_be, loaded_events)