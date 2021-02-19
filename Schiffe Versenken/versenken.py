import numpy as np
import random as rd

schlachtschiff = [1,1,1,1,1]
kreuzer1 = kreuzer2 = [1,1,1,1]
zerstorer1 = zerstorer2 = zerstorer3 =[1,1,1]
uboot1 = uboot2 = uboot3 = uboot4 = [1,1]

def createField():
    return np.zeros((10,10),dtype = int)

def setship(ship,field):
    pos = createShipPos(field)
    if checkHorizontal(pos,ship,field):
        insertShipHorizontal(pos,ship,field)
    elif checkVertical(pos,ship,field):
        insertShipVertical(pos,ship,field)
    else:
        setship(ship,field)

def createShipPos(field):
    x = rd.randint(0,9)
    y = rd.randint(0,9)
    if checkPos(x,y,field):
        return (x,y)
    else: 
        return(createShipPos(field))

def checkPos(x,y,field):
    if x==0 and y==0:
        check = field[x:(x+2), y:(y+2)]
    elif x==0 and y==9:
        check = field[x:(x+2), (y-1):(y+1)]
    elif x==9 and y==0:
        check = field[(x-1):(x+1), y:(y+2)]
    elif x==9 and y==9:
        check = field[(x-1):(x+1),(y-1):(y+1)]
    elif x<0 or y<0 or x>9 or y>9:
        return False
    else:
         check = field[(x-1):(x+2),(y-1):(y+2)]
    return np.all((check==0))

def checkHorizontal(pos,ship,field):
    if (pos[1]+len(ship) > 9):
        return False
    else:
        return np.all((field[pos[0],pos[1]:pos[1]+len(ship)] == 0))

def checkVertical(pos,ship,field):
    if (pos[0]+len(ship) > 9):
        return False
    else:
        return np.all((field[pos[0]:pos[0]+len(ship),pos[1]] == 0))
    
def insertShipHorizontal(pos,ship,field):
    field[pos[0],pos[1]:pos[1]+len(ship)]=1
    
def insertShipVertical(pos,ship,field):
    field[pos[0]:pos[0]+len(ship),pos[1]] = 1

field = createField();setship(schlachtschiff,field);setship(kreuzer1,field)
setship(kreuzer2,field);setship(zerstorer1,field);setship(zerstorer2,field)
setship(zerstorer3,field);setship(uboot1,field);setship(uboot2,field)
setship(uboot3,field);setship(uboot4,field);print("Feld mit Schiffen\n", field)

def game(field):
    counter=0
    print("Bitte geben Sie eine Position ein auf die Sie schiessen moechten.\nDas Spielfeld hat 10 Reihen(A-J) und 10 Zeilen(1-10).\nGeben Sie die Position in diesem Format 'A1' ein\n")
    
    while not np.all((field==0)):
        shot = list(input("Ziel eingeben:"))
        if len(shot) == 3:
            if (shot[1]!= '1' or shot[2]!= '0'):
                shot = list(input("Bitte Position in richtigem Format('A1,J10,usw') eingeben:"))
            else:
                pos = (9,checkChar(shot))
                checkHit(pos,field)
                counter = counter+1
                print(field)
        else:
            while len(shot) != 2:
                shot = list(input("Bitte Position in richtigem Format('A1,J10,usw') eingeben:"))
            pos = (checkNum(shot),checkChar(shot))
            checkHit(pos,field)
            counter = counter+1
            print(field)
    else:
        print("Sie haben das Spiel mit {counter} Schuessen beendet")
    
def checkChar(shot):
    input_letter= shot[0]
    letters = 'abcdefghij'
    converter = {letter: index for index, letter in enumerate(letters)}
    if (input_letter.lower() in letters):
        return converter[input_letter.lower()]
    else:
        checkChar(list(input("Bitte Grossbuchstaben von A-J eingeben:")))

def checkNum(shot):
    if not shot[1].isdigit():
        shot = list(input("Bitte Zahl eingeben von 1-10:"))
        shot.insert(0,'x')  #Platzhalter einfügen
        checkNum(shot)
    else:
        return (int(shot[1]))-1

def checkHit(pos,field):
    if field[pos[0],pos[1]] == 1:
        print("Treffer");markAsHit(pos,field);return True
    else:
       print("Daneben");return False

def markAsHit(pos,field):
    field[pos[0],pos[1]]=0
    return

game(field)