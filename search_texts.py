import pydot
import sys

g = pydot.graph_from_dot_file(sys.argv[1])[0]

for d in dir(g):
    if d.startswith('get_') and d[-1] == 's':
        print(d)

for e in g.get_edges():
    print(e.get_label())
for n in g.get_nodes():
    print(n.get_label())
