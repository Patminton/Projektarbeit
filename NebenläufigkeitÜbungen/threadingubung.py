import threading
import time

class myThread(threading.Thread):
    def __init__(self, ID, name):
        threading.Thread.__init__(self)
        self.ID = ID
        self.name = name

    def run(self):
        lockMe.acquire()
        print ("Starte ", self.ID)
        time.sleep(self.ID*3)
        print("Beende ", self.ID)
        lockMe.release()

lockMe = threading.Lock()                   #Über definition von Threads schreiben
t1 = myThread(1, "t1")
t2 = myThread(2, "t2")

t1.start()
t2.start()
t1.join()                                 #wartet auf Ende des t1 Threads bis Hauptprogramm weiter ausgeführt wird
if t2.is_alive():
    time.sleep(1)

print("Main Thread beendet!")