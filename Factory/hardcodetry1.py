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
        MyThread.m1("A")
        MyThread.m1("A")
        MyThread.m1("B")
        MyThread.m1("C")
        print("Zwischenzeit: {}".format(time.time() - startablauf))
        MyThread.m2("A")
        MyThread.m3("B")
        MyThread.m3("C")
        MyThread.Zusammenbauen([a, b, c])
        print("Beende ", self.name)
        lockMe.release()

    def m1(token):
        starttime = time.time()
        cap.pop(0)
        print("input: " + token + " output: " + token)
        time.sleep(10)
        cap.insert(0, "CAP")
        print('Dauer: {}'.format(time.time() - starttime))
        return (token)

    def m2(token):
        starttime = time.time()
        cap2 = 0
        print("input: " + token + " output: " + token)
        if token == "A":
            time.sleep(30)
        else:
            time.sleep(15)
        cap2 = 1
        print("Dauer: {}".format(time.time() - starttime))
        return (token)

    def m3(token):
        starttime = time.time()
        cap3 = 0
        print("input: " + token + " output: " + token)
        if token == "A" or token == "B":
            time.sleep(10)
        else:
            time.sleep(25)
        cap3 = 1
        print("Dauer: {}".format(time.time() - starttime))
        return (token)

    def Zusammenbauen(tokens):
        starttime = time.time()
        print("input: " + str(tokens) + " output: abc")
        prod = ["abc"]
        print("Dauer: {}".format(time.time() - starttime))
        print("Gesamtablaufdauer: {}".format(time.time() - startablauf))
        return (prod)

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t2.start()
t1.join()
t2.join()