import threading
import numpy as np
import random as rd
import time

ships = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]
field = np.zeros((10, 10), dtype=int)


def setship(ship):
    time.sleep(1)
    if rd.randint(0, 1):  # 1 = horizontal; 0 = vertical
        (x, y) = (rd.randint(0, 9), rd.randint(0, 9 - ship))
        if np.all(field[x, y:y + ship + 1] == 0):
            field[x, y:y + ship] = 1
        else:
            setship(ship)
    else:
        (x, y) = (rd.randint(0, 9 - ship), rd.randint(0, 9))
        if np.all(field[x:x + ship + 1, y] == 0):
            field[x:x + ship, y] = 1
        else:
            setship(ship)

lockMe = threading.Lock()
threads = []
starttime = time.time()

for s in ships:
    t = threading.Thread(target=setship, args=[s])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print(field)
print('Zeit um Schiffe zu setzen = {} seconds'.format(time.time() - starttime))
