import threading
import time

startablauf = time.time()

places = {
    "Bestellungen": ["A", "B", "C"],
    "Kapazität M1": ["CAP", "CAP"],
    "Kapazität M2": ["CAP"],
    "Kapazität M3": ["CAP"],
    "Zwischenprodukte": [],
    "fertige Teilprodukte": [],
    "Platz": []
}

class myThread(threading.Thread):
    def __init__(self, transition, token):
        threading.Thread.__init__(self)
        self.transition = transition
        self.token = token

class run_M1(myThread):
    def __init__(self, transition, token):
        self.transition = "M1"

class run_M2(myThread):
    def __init__(self, transition, token):
        self.transition = "M2"

class run_M3(myThread):
    def __init__(self, transition, token):
        self.transition = "M2"
class run_zusammenbauen(myThread):
    def __init__(self, transition, token):
        self.transition = "Zusammenbauen"

t1=myThread("A","M1")