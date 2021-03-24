import numpy as np, time
import random as rd
import re

import threading


class Setship(threading.Thread):
    #globalen Variablen field,ship
    field = np.zeros((10,10), dtype=int)
    ship = [5,4,4,3,3,3,2,2,2,2]

    def __init__(self,iD,name):
        threading.Thread.__init__(self)
        self.iD = iD 
        self.name = name
         
    def setship(ship):
        if rd.randint(0, 1):  # 1 = horizontal; 0 = vertical
            (x, y) = (rd.randint(0, 9), rd.randint(0, 9 - ship))
            if np.all(Setship.field[x, y:y + ship + 1] == 0):
                Setship.field[x, y:y + ship] = 1
            else:
                Setship.setship(ship)

        else:
            (x, y) = (rd.randint(0, 9 - ship), rd.randint(0, 9))
            if np.all(Setship.field[x:x + ship + 1, y] == 0):
                Setship.field[x:x + ship, y] = 1
            else:
                Setship.setship(ship)

    def run(self):
        for i in Setship.ship:
            time.sleep(1)
            lockMe.acquire()
            #print("\nStarte", self.iD)
            Setship.setship(i)
            Setship.ship.pop(0)
            lockMe.release()
            #print("\nBeende",self.iD)


lockMe = threading.Lock()

t1 = Setship(1,"t1")
t2 = Setship(2,"t2")

t1.start()
t2.start()
t1.join()
t2.join()

print("Beende Main")
print(Setship.field)

