import numpy as np, multiprocessing, time
import random as rd
import re


def setship(ship, lock):
    if rd.randint(0, 1):  # 1 = horizontal; 0 = vertical
        (x, y) = (rd.randint(0, 9), rd.randint(0, 9 - ship))
        lock.acquire()
        if np.all(field[x, y:y + ship + 1] == 0):
            field[x, y:y + ship] = 1
        else:
            lock.release()
            setship(ship, lock)
    else:
        (x, y) = (rd.randint(0, 9 - ship), rd.randint(0, 9))
        lock.acquire()
        if np.all(field[x:x + ship + 1, y] == 0):
            field[x:x + ship, y] = 1
        else:
            setship(ship)
            lock.release()
    lock.release()


def game():
    counter = 0
    print("Bitte geben Sie eine Position ein auf die Sie schiessen moechten.\n"
          "Das Spielfeld hat 10 Reihen(A-J) und 10 Zeilen(1-10)."
          "\nGeben Sie die Position in diesem Format 'A1' ein\n")
    while not np.all((field == 0)):
        shot = re.search('([a-jA-J])+([1-9]|10)', input("Bitte Ziel eingeben: "))
        if shot:
            checkmarkhit((int(shot.group(2)) - 1, checkchar(shot.group(1))))
        else:
            print("Position nicht im Spielfeld. Erneut eingeben: ")
            continue
        counter = counter + 1
    else:
        print(f"Sie haben das Spiel mit {counter} Schuessen beendet")


def checkchar(char):
    converter = {chars: index for index, chars in enumerate('abcdefghij')}
    return converter[char.lower()]


def checkmarkhit(pos):
    if field[pos[0], pos[1]] == 1:
        print("Treffer")
        field[pos[0], pos[1]] = 0
    else:
        print("Daneben")


field = np.zeros((10, 10), dtype=int)


if __name__ == '__main__':
    starttime = time.time()
    processes = []
    lock = multiprocessing.Lock()
    for i in [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]:
        p = multiprocessing.Process(target=setship, args=(i, lock))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print()
    print('Zeit um Schiffe zu setzen = {} seconds'.format(time.time() - starttime))
    game()
