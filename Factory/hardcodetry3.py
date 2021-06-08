import threading
import time

startablauf = time.time()

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starte run\n")
        if self.name == "m1":
            print(self.name)
            m1()    #sleep 5
        if self.name == "m2":
            print(self.name)
            m2()    #sleep 10
        print("Beende thread " + self.name + "\n")
        print("Gesamtablaufdauer: {}".format(time.time() - startablauf))


def m1():
        print("In M1")
        starttime = time.time()
        time.sleep(5)
        print('Dauer: {}'.format(time.time() - starttime))
        return

def m2():
        print("In M2")
        starttime = time.time()
        time.sleep(10)
        print('Dauer: {}'.format(time.time() - starttime))
        return


#lockm1 = threading.Lock()
#lockm2 = threading.Lock()
t1 = myThread("m1")
t2 = myThread("m2")

t1.start()
t2.start()

print("Beende main Thread")
