# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:45:23 2017

@author: User
"""

import networkx as nx
import matplotlib.pyplot as plt
import csv
import pandas as pd
G=nx.Graph()
#G.add_node(1)
#G.add_nodes_from([2,3])
#H=nx.path_graph(10)
#G.add_node(H)
#G.add_edge(1,2)
#e=(2,3)
#G.add_edge(*e)
#G.add_edges_from([(1,2),(1,3)])
#G.add_edges_from(H.edges())
#G.remove_node(H)
#
#nx.draw(G)
#plt.show()




#df=pd.read_csv('ratings.txt',sep='\s')
#print(df)
g = nx.read_edgelist('ratings.txt', nodetype=int,
  data=(('weight',float),), create_using=nx.DiGraph())
gnode=g.node()

#print(g.edges(data=True))
nx.draw(g)
plt.show()
#degree distribution
print(nx.info(g))
wtmat=nx.to_numpy_matrix(g, weight='weight')
outdegrees=dict(g.out_degree())
indegrees=dict(g.in_degree())
max(outdegrees.items(), key = lambda x: x[1])
min(outdegrees.items(), key = lambda x: x[1])
max(indegrees.items(), key = lambda x: x[1])
min(indegrees.items(), key = lambda x: x[1])
degrees=g.degree()
degrees=dict(degrees)
max(degrees.items(), key = lambda x: x[1])
min(degrees.items(), key = lambda x: x[1])

