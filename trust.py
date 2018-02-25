# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:59:35 2017

@author: User
"""

G = nx.read_edgelist('./trust.txt', nodetype=int,
  data=(('weight',float),), create_using=nx.DiGraph())
nx.draw(G)
plt.show()
a=nx.all_pairs_shortest_path(G,cutoff=None)
class Generator:
    def __init__(self, gen):
        self.gen = gen

    def __iter__(self):
        self.value = yield from self.gen

path=Generator(a)
for i in path:
    print(i)