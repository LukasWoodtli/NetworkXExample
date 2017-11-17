#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt
import os


def example1():
  lines = [["A",["B","C","G"]],
          ["B",["Q","G"]]]

  G=nx.DiGraph()

  for line in lines:
    for dep in line[1]:
      #print line[0], dep
      G.add_edge(line[0], dep)

  #print(G.nodes())

  nx.draw(G)
  plt.show()



WORKING_DIR = os.path.split(os.path.realpath(__file__))[0]

def parse_data(file):
  G = nx.DiGraph()
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      line = line.replace('\n','') # replace end of line sign
      line = line.split(";")
      data_node = line[0]
      G.add_node(data_node)
      dependent_data = line[1].split(",")
      for dep in dependent_data:
        if "" != dep:
          G.add_edge(data_node, dep)

  return G

def example2():
    data = parse_data(os.path.join(WORKING_DIR, 'data.txt'))

    nx.draw_random(data)
    #nx.draw_circular(data)
    #nx.draw_spectral(data)
    #nx.draw(data)
    plt.show()


if __name__ == '__main__':
  example1()
  example2()
