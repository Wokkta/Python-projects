# https://shwanoff-ru.turbopages.org/shwanoff.ru/s/networkx-part1/
# Создание простого графа
import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt

graph = nx.Graph()
'''
graph.add_node('A')# добавление вершины
graph.add_node('B')# добавление вершины
graph.add_node('C')# добавление вершины

graph.nodes()'''
'''метод add_edge, забегая наперёд, соединяет
 первую вершину со второй, но не наоборот'''
 #напишем свою функцию для добавления рёбер.
'''def add_edge(f_item, s_item, graph=None):
  graph.add_edge(f_item, s_item)
  graph.add_edge(s_item, f_item) 
# add some edges
add_edge('A', 'B', graph=graph)
add_edge('B', 'C', graph=graph)
add_edge('B', 'D', graph=graph)
add_edge('D', 'E', graph=graph)
# draw graph
nx.draw_circular(graph,
         node_color='red',
         node_size=1000,
         with_labels=True)
plt.show()
'''
'''Также мы можем создать вершины графа, воспользовавшись методом add_nodes_from(),
 передав туда итерируемый объект.
 Также работает и с методом add_edges_from(),
  где аргумент должен содержать кортежи с вершинами.'''
'''cities = {'A':(0, 20),
     'B':(15, 24),
     'C':(16, 41),
     'D':(10, 40)}

graph = nx.Graph()
graph.add_nodes_from(cities)'''
#Теперь добавим рёбра с весами (в нашем случае это расстояние между городами А, В, С и D):
'''kilometres = {('A', 'B', 15),
              ('B', 'C', 16),
              ('B', 'D', 25),
              ('C', 'D', 14),
              ('D', 'A', 18)}

graph.add_weighted_edges_from(kilometres)'''
# draw graph
'''snx.draw_circular(graph,
         node_color='red',
         node_size=1000,
         with_labels=True)
plt.show()
'''

'''Создание полносвязного графа

Полносвязный граф — граф, где каждая вершина соединена с каждой другой. Свойства полносвязного графа мы разберём попозже, а тем временем реализуем функцию для его построения.'''

def complete_graph(N: int) -> nx.Graph:
  graph = nx.Graph()
   
  N_range = range(N)
   
  all_pairs = itertools.permutations(N_range, 2)
   
  graph.add_nodes_from(N_range)
  graph.add_edges_from(all_pairs)
   
  return graph

'''itertools.permutations(arr[, len], n) — возвращает все возможные перестановки элементов arr длиной n'''

# Визуализируем полносвязный граф с 15-ю вершинами:
'''graph = complete_graph(15)

nx.draw_circular(graph, 
         node_color='y',
         node_size=750,
         with_labels=True)
plt.show()'''

