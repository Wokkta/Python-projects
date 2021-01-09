import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
# модель G(n, p)
def random_graph(n:int, p):
  graph = nx.Graph()
   
  N_range = range(n)
  graph.add_nodes_from(N_range)
   
  for pair in itertools.permutations(N_range, 2):
    if rnd.random() < p:
      graph.add_edge(*pair)
   
  return graph

graph = random_graph(7, 0.5)

nx.draw_circular(graph,
         node_color='y',
         node_size=1000,
         with_labels=True)
plt.show()