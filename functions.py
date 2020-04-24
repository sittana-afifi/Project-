
### use generate_graph() to transform adjeceny matrix to graph
import numpy as np
from graph_tools import *
def adj_mat():
    n = int(input("Enter the size of the matrix:"))  
    print("Enter the entries in a single line (separated by space): ") 
    entries = list(map(int, input().split())) 
    AM = np.array(entries).reshape(n, n) 
    return AM
    
    
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



### get the two graphs from prover as adjecny matrix and print them using recive_graph()
def recive_graph():
    g0=generate_graph()
    print(g0)
    g1=generate_graph()
    print(g1)
    
    
    
### apply permutation to adjeceny matrix using apply_permut()

def apply_permut(AM,p):
    M=np.array(AM)
    s=min(p)
    for i in range(len(p)):
        p[i]=p[i]-s
    for i in range(len(p)):
        M[:,i] = M[p,i]
    for i in range(len(p)):
        M[i,:] = M[i,p]
    return M    
    


### composite two permutation using composite_permutition()

def composite_permutition(p,g):
    g1=[0]*len(p)
    s=min(g)
    if len(p)==len(g):
        for i in range(len(p)):
            g1[i]=g[((p[i]-s)%len(p))]
        pass
    return g1
        
   
   
  
   
   ## check if two graphs are equal using are_same()
   
   def are_same(g0,g1):
    s=len(g0.vertices())
    q=len(g1.vertices())
    a=0
    for e in g0.edges():
        for f in g1.edges():
            if e==f :
                a=a+1
                break
    if a==q and s==q :
        return True
    else :
        return False
        
        
        
 ###tansform permutation to cyclic graph to deal easy with it
 
 def tran_permu_to_graph(g):
    d = Graph(directed=False)
    d.add_vertex(len(g))
    for i in range(len(g)):
        d.add_edge(g[(i)],g[(i+1)%len(g)])
    return d
    
    
    
### generate permutation those produce different graphs using s_n() 

def s_n(n):
    from itertools import permutations 
    l = list(permutations(range(1, n+1)))
    l1=[]
    l2=[]
    l3=[]
    for i in range(len(l)):
        if l[i][0]==1:
            l1.append(l[i])
    l2=To_list(l1)
    for i in range(len(l2)):
        for j in range(i+1,len(l2)):
            i1=Graph()
            j1=Graph()
            i1=tran_permu_to_graph(l2[i])
            j1=tran_permu_to_graph(l2[j])
            if are_same(i1,j1)==True :
                l3.append(l2[i])
    return l3



### find the inverse of permutation using inv()

def inv(perm):
    s=min(perm)
    inverse = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse[p-s] = i+s
    return inverse
    
    
    
### transform the permutation to list of list using
 
 def To_list(l):
    l1=[]
    for i in l:
        l1.append(list(i))
    return l1