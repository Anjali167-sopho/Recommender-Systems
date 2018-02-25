import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
li=[]
df=pd.read_csv('trust.txt',sep='\s')
G = nx.read_edgelist('trust.txt', nodetype=int,
  data=(('weight',float),), create_using=nx.DiGraph())
nx.write_gml(G,'trust1.gml')
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
    i=list(i)
    print(i)
    for j in i:
        j=i[1]
        


out=sorted(G.out_degree(),key=lambda x: x[1])
ind=sorted(G.in_degree(),key=lambda x: x[1])

print("Minimum indegree:",ind[0][1]," Node:",ind[0][0])
print("Maximum indegree:",ind[-1][1]," Node:",ind[-1][0])

print("Minimum outdegree:",out[0][1]," Node:",out[0][0])
print("Maximum outdegree:",out[-1][1]," Node:",out[-1][0])



