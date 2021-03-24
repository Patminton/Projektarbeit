import threading
import numpy as np
import random as rd
import time

class myThread(threading.Thread):
    Ergebnis = [0,1]
    ships = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]
    field = np.zeros((10, 10), dtype=int)
    def __init__(self, ID, name):
        threading.Thread.__init__(self)
        self.ID = ID
        self.name = name

    def setship(ship):
        if rd.randint(0, 1):  # 1 = horizontal; 0 = vertical
            (x, y) = (rd.randint(0, 9), rd.randint(0, 9 - ship))
            if np.all(myThread.field[x, y:y + ship + 1] == 0):
                myThread.field[x, y:y + ship] = 1
            else:
                myThread.setship(ship)
        else:
            (x, y) = (rd.randint(0, 9 - ship), rd.randint(0, 9))
            if np.all(myThread.field[x:x + ship + 1, y] == 0):
                myThread.field[x:x + ship, y] = 1
            else:
                myThread.setship(ship)

    def run(self):
        for i in myThread.ships:
            time.sleep(1)
            lockMe.acquire()
            myThread.setship(i)
            myThread.ships.pop(0)
            lockMe.release()


lockMe = threading.Lock()
t1 = myThread(1, "t1")
t2 = myThread(2, "t2")

starttime = time.time()
t1.start()
t2.start()
t1.join()
t2.join()

print(myThread.field)
print('Zeit um Schiffe zu setzen = {} seconds'.format(time.time() - starttime))