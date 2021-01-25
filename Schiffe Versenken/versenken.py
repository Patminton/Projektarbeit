import numpy as np
import random as rd

schlachtschiff = [1,1,1,1,1]
kreuzer1 = [1,1,1,1]
kreuzer2 = [1,1,1,1]
zerstorer1 = [1,1,1]
zerstorer2 = [1,1,1]
zerstorer3 = [1,1,1]
uboot1 = [1,1]
uboot2 = [1,1]
uboot3 = [1,1]
uboot4 = [1,1]

def createField():
    field = np.zeros((10,10),dtype = int)
    return field


def set(ship,field):
    pos = createShipPos(field)
   
    if checkHorizontal(pos,ship,field):
        insertShipHorizontal(pos,ship,field)
    elif checkVertical(pos,ship,field):
        insertShipVertical(pos,ship,field)
    else:
        set(ship,field)


def createShipPos(field):
    x = rd.randint(0,9)
    y = rd.randint(0,9)
    #print("Davor",x,y)
    if checkPos(x,y,field):
        #print("Suche",(x,y))
        return (x,y)
    else: 
        #print("suche2",x,y)
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
         #print(check)
    
    if np.all((check==0)):
        return True
    else:
        return False


def checkHorizontal(pos,ship,field):
    i=0
    while i< len(ship) :
        res = checkPos(pos[0],(pos[1]+i),field)               #horizontaler Check
        if res == False:
            return False
            break
        i=i+1
    return True

def checkVertical(pos,ship,field):
    i=0
    while i< len(ship) :
        res = checkPos((pos[0]+i),pos[1],field)             #vertikaler Check
        if res == False:
            return False                                    #wenn sowohl horizontal als auch vertikal nicht geht, dann neue Position für Schiff suchen
            break
        i=i+1
    return True

def insertShipHorizontal(pos,ship,field):
    i=0
    while i< len(ship) :
        field[pos[0],(pos[1]+i)] = 1
        i=i+1
    return

def insertShipVertical(pos,ship,field):
    i=0
    while i< len(ship):
        field[(pos[0]+i),pos[1]] = 1
        i=i+1
    return

#field = createField()
#set(schlachtschiff,field)
#set(kreuzer1,field)
#set(kreuzer2,field)
#set(zerstorer1,field)
#set(zerstorer2,field)
#set(zerstorer3,field)
#set(uboot1,field)
#set(uboot2,field)
#set(uboot3,field)
#set(uboot4,field)
#print("Feld mit Schiffen\n", field)


def games():
    field=createField()
    set(schlachtschiff,field)
    set(kreuzer1,field)
    set(kreuzer2,field)
    set(zerstorer1,field)
    set(zerstorer2,field)
    set(zerstorer3,field)
    set(uboot1,field)
    set(uboot2,field)
    set(uboot3,field)
    set(uboot4,field)
    counter=0
    print("Bitte geben Sie eine Position ein auf die Sie schießen möchten.\nDas Spielfeld hat 10 Reihen(A-J) und 10 Zeilen(1-10).\nGeben Sie die Position in diesem Format 'A1' ein\n")
    
    
    while not np.all((field==0)):
        shot = input("Ziel eingeben:")
        shot = list(shot)
        while len(shot) != 2:
            shot = input("Bitte Position in richtigem Format('A1,J10,usw') eingeben:")
            shot = list(shot)
        pos = (checkNum(shot),checkChar(shot))
        checkHit(pos,field)
        counter = counter+1
        print(field)
    else:
        print(f'Sie haben das Spiel mit {counter} Schüssen beendet')
    

def checkChar(shot):
    if shot[0]=='A':
        y=0
    elif shot[0]=='B':
        y=1
    elif shot[0]=='C':
        y=2
    elif shot[0]=='D':
        y=3
    elif shot[0]=='E':
        y=4
    elif shot[0]=='F':
        y=5
    elif shot[0]=='G':
        y=6
    elif shot[0]=='H':
        y=7
    elif shot[0]=='I':
        y=8
    elif shot[0]=='J':
        y=9
    else:
        shot = input("Bitte Großbuchstaben von A-J eingeben:")
        checkChar(list(shot))
    return y

def checkNum(shot):
    
    if not shot[1].isdigit():
        shot = list(input("Bitte Zahl eingeben von 1-10:"))
        shot.insert(0,'x')
        checkNum(shot)
    else:
        num = int(shot[1])
        x = num-1
        return x

def checkHit(pos,field):
    print(field[pos[0],pos[1]])
    if field[pos[0],pos[1]] == 1:
        print("Treffer")
        markAsHit(pos,field)
        return True
    else:
       print("Daneben")
       return False

def markAsHit(pos,field):
    field[pos[0],pos[1]]=0
    return

games()
