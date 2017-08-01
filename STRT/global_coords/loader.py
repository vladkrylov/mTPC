from data_structures import Event, Hit

def load_event(file_path):
    with open(file_path) as infile:
        ev = Event(75)
        for line in infile:
            x, y = (float(n) for n in line.split())
            ev.add_hit(Hit(x, y))

    return ev

def display_event(event):
    for h in event.hits:
        print(h)


