#!/usr/bin/env python3

import networkx as nx

def ancestor_count(inp):
  g: nx.DiGraph = nx.read_edgelist(inp, delimiter=")", create_using=nx.DiGraph)
  return sum(len(nx.ancestors(g, n)) for n in g.nodes)

def shortest_distance(inp):
  g: nx.Graph = nx.read_edgelist(inp, delimiter=")", create_using=nx.Graph)
  return len(nx.shortest_path(g, "YOU", "SAN")) - 3

print(ancestor_count('day6_input.txt'))
print(shortest_distance('day6_input.txt'))