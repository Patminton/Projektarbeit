import snakes.plugins
snakes.plugins.load("gv", "snakes.nets", "nets")
from nets import *

#def factory (cons, prod, init=[1, 2, 3]) :


#net, trans, modes = factory(Value(1), Value(0))
#net.draw("value-0.png")
#print(modes)
#trans.fire(modes[0])
#net.draw("value-1.png")

n = PetriNet("N")
n.add_place(Place("src", [0]))
n.add_place(Place("tgt", []))
t = Transition("t")
n.add_transition(t)
n.add_input("src", "t", Variable('x'))
n.add_output("tgt", "t", Expression('x+1'))
#    return n, t, t.modes()

for engine in ("neato", "dot", "circo", "twopi", "fdp"):
    n.draw(',test-gv-%s.png' % engine, engine=engine)
s=StateGraph(n)
s.build()
s.draw(',test-gv-graph.png')