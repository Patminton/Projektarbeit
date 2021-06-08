import snakes.plugins
from snakes.nets import *

snakes.plugins.load("gv", "snakes.nets", "nets")

n = PetriNet("N")
n.add_place(Place("Bestellung", [3]))
n.add_place(Place("Kran", [1]))
n.add_place(Place("Bauteile", [2]))
n.add_place(Place("freie Dollys"))
n.add_place(Place("volle Dollys"))
n.add_place(Place("Dolly in Presse", [2]))
n.add_place(Place("Kapazität Presse", [1]))

bestuecken = Transition("bestuecken")
dolly_entladen = Transition("Dolly Entladen")
in_presse_fahren = Transition("In Presse fahren")
n.add_transition(bestuecken)
n.add_transition(dolly_entladen)
n.add_transition(in_presse_fahren)
n.add_input("Bestellung", "bestuecken", Variable("x"))
n.add_input("Bauteile", "bestuecken", Variable("t"))
n.add_input("freie Dollys", "bestuecken", Variable("d"))
n.add_input("Kran", "bestuecken", Variable("k"))
n.add_input("Kran", "Dolly Entladen", Variable("k"))
n.add_input("volle Dollys", "In Presse fahren", Variable("d"))
n.add_input("Dolly in Presse", "Dolly Entladen", Variable("d"))
n.add_input("Kapazität Presse", "In Presse fahren", Variable("kapazitat"))
n.add_output("Kran", "bestuecken", Expression("k"))
n.add_output("volle Dollys", "bestuecken", Expression("d"))
n.add_output("Kran", "Dolly Entladen", Expression("k"))
n.add_output("freie Dollys", "Dolly Entladen", Expression("d"))
n.add_output("Kapazität Presse", "In Presse fahren", Variable("kapazitat"))
n.add_output("Dolly in Presse", "In Presse fahren", Variable("d"))

for engine in ("neato", "dot", "circo", "twopi", "fdp"):
    n.draw('_test-gv-%s.png' % engine, engine=engine)

s = StateGraph(n)
s.build()
s.draw('_test-gv-graph.png')
