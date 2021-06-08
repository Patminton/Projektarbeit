import threading
import time


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
                                                            #Serverantwort abwarten, Danach muss Token weitergegeben werden und Kapazität wieder eingefügt werden
    places.get("Zwischenprodukte").insert(0, token)
    places.get("Kapazität M1").insert(0,"CAP")
    return #Ergebnis von Antwort


def m2(token):                                              #sendet Befehl Transition M1 an MQTT Server und erhält Antwort nach bestimmter Zeit
    places.get("Zwischenprodukte").pop(0)                   #wenn antwort negativ, dann token wieder in Bestellungen einfügen
    places.get("Kapazität M2").pop(0)
                                                            #Serverantwort abwarten, Danach muss Token weitergegeben werden und Kapazität wieder eingefügt werden
    places.get("fertige Teilprodukte").insert(0, token)
    places.get("Kapazität M2").insert(0,"CAP")
    return #Ergebnis von Antwort

def m3(token):                                              #sendet Befehl Transition M1 an MQTT Server und erhält Antwort nach bestimmter Zeit
    places.get("fertige Teilprodukte").pop(0)                   #wenn antwort negativ, dann token wieder in Bestellungen einfügen
    places.get("Kapazität M3").pop(0)
                                                            #Serverantwort abwarten, Danach muss Token weitergegeben werden und Kapazität wieder eingefügt werden
    places.get("fertige Teilprodukte").insert(0, token)
    places.get("Kapazität M3").insert(0,"CAP")
    return #Ergebnis von Antwort


def Zusammenbauen():                                        #sendet Befehl Transition M1 an MQTT Server und erhält Antwort nach bestimmter Zeit
    for i in range(3):
            places.get("fertige Teilprodukte").pop(0)                   #wenn antwort negativ, dann token wieder in Bestellungen einfügen
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


check("A", "M1")