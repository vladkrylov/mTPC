from unittest import TestCase
from random import randint
from controller import Controller
from model import Model, Event
from model_tests import generate_event


class TestControllerModelInterface(TestCase):
    
    def test_add_events(self):
        m = Model()
        c = Controller(m, None)
        
        event_ids = [4, 4, 8, 2, 4, 2, 3, 6, 7, 0, 10, 4, 0, 4, 4, 5, 2, 8, 10, 3]
        
        for ev_id in event_ids:
            ev = generate_event(None, ev_id)
            c.on_event_loaded(ev)
        
        loaded_events = [ev.id for ev in m.events]
        should_be = [4, 8, 2, 3, 6, 7, 0, 10, 5]
        self.assertEqual(should_be, loaded_events)

    def test_add_remove_track(self):
        m = Model()
        c = Controller(m, None)
        
        ev_id = 17
        ev = generate_event(None, ev_id)
        c.on_event_loaded(ev)
        
        c.on_add_track(ev_id)
        c.on_add_track(ev_id)
        c.on_add_track(ev_id)
        c.on_add_track(ev_id)
        
        c.on_remove_track(ev_id, 2)
        
        added_track_ids = [tr.id for tr in m.events[0].tracks]
        expected_track_ids = [0, 1, 3]
        self.assertEqual(added_track_ids, expected_track_ids)
        
        
