
### use generate_graph() to transform adjeceny matrix to graph
import numpy as np
from graph_tools import *    
def generate_graph():
#User input of entries in a single line separated by space 
    AM=adj_mat()
    d = Graph(directed=False)
    d.add_vertex(len(AM)-1)
    for i in range(len(AM)):
        for j in range(i,len(AM)):
            if AM[i][j]==1:
                d.add_edge(i,j)
    return d
    
    
### apply permutation to adjeceny matrix using apply_permut()

def apply_permute(AM,pi):
    n=len(AM)
    AM1=np.zeros((n,n))
    for i in range (n):
        for j in range (n):
            if AM[i][j]==1 :
                AM1[pi[i]][pi[j]]=1
    return AM1

    


### composite two permutation using composite_permutition()

from sympy.combinatorics import Permutation
def compose_permutation(p,g):
    p1=Permutation(p)
    q1=Permutation(g)
    return [(p1*q1)(i) for i in range(p1.size)]
   
   
  
   
   ## check if two Addjaceny Matrix are equal using are_equal()
   
   def are_equal(AM,AM1) :
    return np.array_equal(AM1,AM)


### find the inverse of permutation using inv()

def inv(perm):
    per=list(perm)
    inverse = [0] * len(per)
    for i, p in enumerate(per):
        inverse[p] = i
    return inverse



import csv
def get_graph_from_file(i):
    with open('matices.csv') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    l=[]
    l=content[i]
    matrix=[]
    l[i]
    n=int(np.sqrt(len(l)-2))
    for i in range(1,len(l)-1):
        matrix.append(l[i])
        
        
       
    
    def get_pi_from_file(i):
    with open('matices.csv') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    l=[]
    l=content[i]
    matrix=[]
    l[i]
    n=int(np.sqrt(len(l)-2))
    
    
    
    
    def equal(AM):
    a=np.zeros([len(AM),len(AM)])
    for i in range(len(AM)):
        for j in range(len(AM)):
            a[i][j]=AM[i,j]
    return a
    for i in range(1,len(l)-1):
        matrix.append(int(l[i]))
    return matrix
    s=np.reshape(matrix,(n,n))
    return s
    
    
    
    import networkx as nx
import matplotlib.pyplot as plt
def plot_graph(AM):
    G = nx.Graph()
    for i in range(len(AM)):
        for j in range(len(AM)):
            if AM[i][j]==1:
                G.add_edge(i, j)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
