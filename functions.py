
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
    l=[]
    l1=[]
    l2=[]
    for i in range (len(AM)):
        for j in range (len(AM)):
            if AM[i][j]==1 :
                l.append([i,j])
    n=len(l)
    for i in range (n):
        l1.append( sorted(l[i]))
    l2=sorted(l1)
    for i in range (len(AM)):
        if l2[i]==l2[(i+1)]:
            l2.remove(l2[i])
    l3=np.zeros([len(AM),2])
    for i in range (len(AM)): 
        for j in range (2):
            if l2[i][j]==0:
                l3[i][j]=pi[0]
            if l2[i][j]==1:
                l3[i][j]=pi[1]
            if l2[i][j]==2:
                l3[i][j]=pi[2]
            if l2[i][j]==3:
                l3[i][j]=pi[3]
    AM0=np.zeros([len(AM),len(AM)])
    for i in range (len(l3)):
        a,b=l3[i]
        AM0[int(a),int(b)]= AM0[int(b),int(a)]=1
    return AM0

    


### composite two permutation using composite_permutition()

def composite_permutition(p,g):
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
    
