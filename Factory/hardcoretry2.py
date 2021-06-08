import threading
import time

startablauf = time.time()

class myThread(threading.Thread):
    def __init__(self, transition, token):
        threading.Thread.__init__(self)
        self.transition = transition
        self.token = token


    def run(self):
        if self.transition == "M1":
            #TODO
            print("Transition M1 schalten")
            m1(self.token)
        if self.transition == "M2":
            #TODO
            print("Transition M2 schalten")
            m2(self.token)
        if self.transition == "M3":
            #TODO
            print("Transition M3 schalten")
            m3(self.token)
        if self.transition == "Zusammenbauen":
            #TODO
            print("Transition Zusammenbauen schalten")
            Zusammenbauen(self.token)



places = {
    "Bestellungen": ["A", "B", "C"],
    "Kapazität M1": ["CAP", "CAP"],
    "Kapazität M2": ["CAP"],
    "Kapazität M3": ["CAP"],
    "Zwischenprodukte": [],
    "fertige Teilprodukte": [],
    "Platz": []
}

def m1(token):                                              #sendet Befehl Transition M1 an MQTT Server und erhält Antwort nach bestimmter Zeit
    places.get("Bestellungen").pop(0)                       #wenn antwort negativ, dann token wieder in Bestellungen einfügen
    places.get("Kapazität M1").pop(0)

    starttime = time.time()
    time.sleep(2)
    print('Dauer: {}'.format(time.time() - starttime))
                                                            #Serverantwort abwarten, Danach muss Token weitergegeben werden und Kapazität wieder eingefügt werden
    places.get("Zwischenprodukte").insert(0, token)
    places.get("Kapazität M1").insert(0,"CAP")
    return #Ergebnis von Antwort


def m2(token):                                              #sendet Befehl Transition M1 an MQTT Server und erhält Antwort nach bestimmter Zeit
    places.get("Zwischenprodukte").pop(0)                   #wenn antwort negativ, dann token wieder in Bestellungen einfügen
    places.get("Kapazität M2").pop(0)

    starttime = time.time()
    if token == "A":
        time.sleep(30)
    else:
        time.sleep(15)
    print('Dauer: {}'.format(time.time() - starttime))
                                                            #Serverantwort abwarten, Danach muss Token weitergegeben werden und Kapazität wieder eingefügt werden
    places.get("fertige Teilprodukte").insert(0, token)
    places.get("Kapazität M2").insert(0,"CAP")
    return #Ergebnis von Antwort

def m3(token):                                              #sendet Befehl Transition M1 an MQTT Server und erhält Antwort nach bestimmter Zeit
    places.get("fertige Teilprodukte").pop(0)                   #wenn antwort negativ, dann token wieder in Bestellungen einfügen
    places.get("Kapazität M3").pop(0)

    starttime = time.time()
    if token == "C":
        time.sleep(20)
    else:
        time.sleep(10)


                                                            #Serverantwort abwarten, Danach muss Token weitergegeben werden und Kapazität wieder eingefügt werden
    places.get("fertige Teilprodukte").insert(0, token)
    places.get("Kapazität M3").insert(0,"CAP")
    return #Ergebnis von Antwort


def Zusammenbauen():                                        #sendet Befehl Transition M1 an MQTT Server und erhält Antwort nach bestimmter Zeit
    for i in range(3):
            places.get("fertige Teilprodukte").pop(0)                   #wenn antwort negativ, dann token wieder in Bestellungen einfügen
    
    time.sleep(20)
                                                            #Serverantwort abwarten, Danach muss Token weitergegeben werden und Kapazität wieder eingefügt werden
    places.get("Platz").insert(0, "abc")
    return #Ergebnis von Antwort


def check(token, trans):
    if trans == "M1":
        if places.get("Bestellungen") == [] or places.get("Kapazität M1") == []:
            return False
        elif (token in places.get("Bestellungen")):
            return True                                   #Antwort von Server abwarten
    elif trans == "M2":
        if places.get("Zwischenprodukte") == [] or places.get("Kapazität M2") == []:
            return False
        elif (token in places.get("Zwischenprodukte")):
            return True
    elif trans == "M3":
        if places.get("Zwischenprodukte") == [] or places.get("Kapazität M2") == []:
            return False
        elif (token in places.get("Zwischenprodukte")):
            return True
    elif trans == "Zusammmenbauen":
        if not(token in places.get("fertige Teilprodukte")):
            return False
        elif len(places.get("fertige Teilprodukte"))==3:
            return True
        else:
            return False
    else:
        raise Exception("Falsche Transition")

print(places)
t1 = myThread("M1", "A")
t2 = myThread("M1", "B")
t1.start()
t2.start()
t1.join()
t2.join()
print(places)