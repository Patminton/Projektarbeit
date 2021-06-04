import threading
import time


cap = ["CAP", "CAP"]
cap2 = 1
cap3 = 1
lockMe = threading.Lock()
startablauf = time.time()


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        lockMe.acquire()
        print("Starte ", self.name)
        print("Beende ", self.name)
        lockMe.release()


def m1(token, thread):
    starttime = time.time()
    lockMe.acquire()
    cap.pop(0)
    print("input: " + token + " output: " + token)
    time.sleep(10)
    cap.insert(0, "CAP")
    lockMe.release()
    print('Dauer: {}'.format(time.time()-starttime))
    return(token)


def m2(token, thread):
    starttime = time.time()
    lockMe.acquire()
    cap2 = 0
    print("input: " + token + " output: " + token)
    if token == "A":
        time.sleep(30)
    else:
        time.sleep(15)
    cap2 = 1
    lockMe.release()
    print("Dauer: {}".format(time.time()-starttime))
    return(token)


def m3(token, thread):
    starttime = time.time()
    lockMe.acquire()
    cap3 = 0
    print("input: " + token + " output: " + token)
    if token == "A" or token == "B":
        time.sleep(10)
    else:
        time.sleep(25)
    cap3 = 1
    lockMe.release()
    print("Dauer: {}".format(time.time()-starttime))
    return(token)

def Zusammenbauen(tokens, thread):
    starttime = time.time()
    lockMe.acquire()
    print("input: " + str(tokens) + " output: abc")
    prod = ["abc"]
    lockMe.release()
    print("Dauer: {}".format(time.time() - starttime))
    print("Gesamtablaufdauer: {}".format(time.time() - startablauf))
    return(prod)

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t2.start()

a = m1("A", t1)
b = m1("B", t2)
c = m1("C", t2)
a = m2(a,t1)
b = m3(b, t2)
c = m3(c, t2)
abc = Zusammenbauen([a, b, c],t1)
