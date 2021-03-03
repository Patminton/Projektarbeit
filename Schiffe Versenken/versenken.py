import numpy as np
import random as rd
import re


def setShip(ship):
    if rd.randint(0,1):                                                  # 1 = horizontal; 0 = vertical
        (x,y)=(rd.randint(0,9),rd.randint(0,9-ship))
        if np.all(field[x,y:y+ship+1]==0):
            field[x,y:y+ship]=1
        else:
            setShip(ship)
    else:
        (x,y)=(rd.randint(0,9-ship),rd.randint(0,9))
        if np.all(field[x:x+ship+1,y]==0):
            field[x:x+ship,y]=1
        else:
           setShip(ship)


def game():
    counter=0
    print("Bitte geben Sie eine Position ein auf die Sie schiessen moechten.\nDas Spielfeld hat 10 Reihen(A-J) und 10 Zeilen(1-10).\nGeben Sie die Position in diesem Format 'A1' ein\n")
    while not np.all((field==0)): 
        if re.search('([a-jA-J])+([1-9]|10)',input("Bitte Ziel eingeben: ")):
            checkMarkHit((int(shot.group(2))-1,checkChar(shot.group(1))))
        else:
            print("Position nicht im Spielfeld. Erneut eingeben: ")
            continue
        counter= counter+1
    else:
        print("Sie haben das Spiel mit {counter} Schuessen beendet")


def checkChar(char):
    converter = {chars: index for index, chars in enumerate('abcdefghij')}
    return converter[char.lower()]


def checkMarkHit(pos):
    if field[pos[0],pos[1]] == 1:
        print("Treffer")
        field[pos[0],pos[1]]=0
    else:
        print("Daneben")


schiffe = [5,4,4,3,3,3,2,2,2,2]
field = np.zeros((10,10),dtype = int)
for schiff in schiffe: setShip(schiff)
game()