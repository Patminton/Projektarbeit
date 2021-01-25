import numpy as np
import random as rd 

FT = [1,1,1,1,1]
Kr = [1,1,1,1]
Zer = [1,1,1]
Uboot = [1,1]

#Spielfeld erstellen
def createBoard():
    board = np.zeros((10,10),dtype = int )
    return board

#horizontaler Check
def checkhorizontal(ship,board,pos):
   #print("ich bin in check horizontal")
    i=0
    if (pos[1]+len(ship)>10): 
        return False
    while (i < len(ship)):

        res = checkPos(pos[0],(pos[1]+i),board)

        if res == False: 
            return False 
            break
        i+=1
    return True

#vertikaler Check
def checkvertikal(ship,board,pos):
    i=0
    if (pos[0]+len(ship)>10):
        return False
    while (i < len(ship)):

        res = checkPos((pos[0]+i),pos[1],board)

        if res == False: 
            return False 
            break
        i+=1
    return True

#positions Check
def checkPosMT(x,y,board):
    #print("ich bin in checkpos")
    if ((board[x][y]) == 0):  #returned true wenn an der Stelle auf dem Board eine Null steht
        #print("ich returne True")
        return True
    else:
        return False
    
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

#schiff horinzontal einsetzten
def inserthorizontal(ship,board,pos):
    i=0
    while i<len(ship):
        board[pos[0]][(pos[1]+i)] = 1
        i +=1

    return

#schiff vertikal einsetzten
def insertvertikal(ship,board,pos):
    i=0
    while i<len(ship):
        board[pos[0]+i][pos[1]] = 1
        i+=1

    return

#Schiffe Ai setzten
def setship(ship,board): #random Startposition für Schiffe der AI erstellen
    x=rd.randint(0,9)
    y=rd.randint(0,9)

    if (checkPos(x,y,board) == False):
       setship(ship, board)
       return
    else: 
        pos=(x,y)
        #print(pos)

    if   checkhorizontal(ship,board,pos):
        inserthorizontal(ship,board,pos)
    elif checkvertikal(ship,board,pos):
        insertvertikal(ship,board,pos)
    else: 
        setship(ship,board)  #wenn Schiff nicht gesetzt werden kann neue Anfangswerte generieren
        

    return


#Char im shot checken
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

#nummer im shot checken
def checkNum(x):
    xt = (ord(x)-49)
    if ((xt<0) or (xt>9)):
        shot = input("X Koordinate zwischen 1 und 10")
        checkNum(shot)
    else:
        return xt


def checkHit(pos,board):
    if board[pos[0],pos[1]] == 1:
        print("Treffer\n")
        markAsHit(pos,board)
        return
    else:
       print("Daneben\n")
       return

def markAsHit(pos,board):
    board[pos[0],pos[1]]=0
    return




    #Player soll eigene Schiffe setzten
def getPlayerShipPos(ship,board):
    SP = input("Startkoordiante für das Schiff angeben(Format z.b. A1):")
    SP = list(SP)
    if len(SP)==3:
        if (SP[1]!='1' or SP[2]!='0'):
            SP = input("Richtiges Format beachten!:")
            SP = list(SP)
        else:
            pos = (9,checkChar(SP[0]))
        R = input("Bitte Richtung angeben, v für vertikales Platzieren, h für horizontales Platzieren:")

        if R == "v":
            if checkvertikal(ship,board,pos):
                insertvertikal(ship,board,pos)
            else:
                print("Platzieren vertikal nicht möglich")
                getPlayerShipPos(ship,board)
        else:
            if R=="h":
                if checkhorizontal(ship,board,pos):
                    inserthorizontal(ship,board,pos)
                else:
                    print("Platzieren horizontal nicht möglich")
                    getPlayerShipPos(ship,board)
    else:
#wenn len(SP) = 2 wird alles obendrüber übersprungen

        while len(SP)!= 2:
            SP = input("Richtiges Format beachten!:")
            SP = list(SP)

        pos = (checkNum(SP[1]),checkChar(SP[0]))
        R = input("Bitte Richtung angeben, v für vertikales Platzieren, h für horizontales Platzieren:")

        if R == "v":
            if checkvertikal(ship,board,pos):
                insertvertikal(ship,board,pos)
            else:
                print("Platzieren vertikal nicht möglich")
                getPlayerShipPos(ship,board)
        else:
            if R=="h":
                if checkhorizontal(ship,board,pos):
                    inserthorizontal(ship,board,pos)
                else:
                    print("Platzieren horizontal nicht möglich")
                    getPlayerShipPos(ship,board)
    return


def game(board,boardplayer):
  
    while (not (np.all(board == 0) or np.all(boardplayer == 0))):
        x = rd.randint(0,9)
        y = rd.randint(0,9)
        shotAi = (x,y)  #Zufälliger Schuss der Ki
        print("Gegner hat auf (" + str(x) + "," + str(y) + ") geschossen")
        checkHit(shotAi,boardplayer)               #Hit wird auf dem Board des Players getestet
        print("Ihr Spielfeld\n")
        print(boardplayer)
        print("\n")

        if np.all(boardplayer == 0 ):
            print("Sie haben verloren")
            return
        

#Eigener Schuss
        shot = input("Zielkoordinate für Schuss eingeben:")
        shot = list(shot)
        if (len(shot) == 3):
            if (shot[1]!='1' or shot[2]!='0'):
                shot = input("Richtiges Format beachten!:")
                shot = list(shot)
            else:
                pos=(9,checkChar(shot[0]))
                checkHit(pos,board)
                #print(board)
        else:
            while (len(shot) != 2):
                shot = input("Bitte Position in richtigem Format('A1,J10,usw') eingeben:")
                shot = list(shot)
            pos = (checkNum(shot[1]),checkChar(shot[0]))
            checkHit(pos,board)
            #print(board)

        if np.all(board == 0):
            print("Sie haben gewonnen")
            return
        




     





#Spielvorbereitung
board = createBoard()
#print(board)    leeres Board der Ai
boardplayer = createBoard()   #eignes Board
setship(FT,board)
#print(board)
setship(Kr,board)
#print(board)
setship(Zer,board)
#print(board)
setship(Uboot,board)
#print(board)board mit Schiffen des Gegners
#print("Ich bin hier 2")
print("KI hat ihre Schiffe gesetzt!")

print("eigenen Flugzeugträger setzen:(Länge 5)")
getPlayerShipPos(FT,boardplayer)
print(boardplayer)
print("eigenen Kreutzer setzen:(Länge 4)")
getPlayerShipPos(Kr,boardplayer)
print(boardplayer)
print("eigenen Zerstörer setzen:(Länge 3)")
getPlayerShipPos(Zer,boardplayer)
print(boardplayer)
print("eigenes Uboot setzen:(Länge 2)")
getPlayerShipPos(Uboot,boardplayer)
print(boardplayer)

#game ausführen
game(board,boardplayer)
