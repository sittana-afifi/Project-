def graph_isomorphism(P,V):
    message_list=[]
    prover_move=True
    while len(message_list)<4:
        if prover_move :
            message_list=P(message_list)
        else :
            message_list=V(message_list)
        prover_move= not prover_move
        print(message_list[-1])
        if message_list[-1]== 'accept' or   message_list[-1]== 'reject':
            return message_list
    return message_list
    
    
def test_isomorphism():
    AM=enter_adjMatrix()
    AM1=enter_adjMatrix()
    pi=list(map(int, input('Enter pi:').split())) 
    s = raw_input("Enter any number as aseed to generate random permutation : ") 
    V=lambda msg: honest_verifier(AM,AM1,msg)
    P=lambda msg: honest_prover(AM,AM1,pi,msg,s)
    graph_isomorphism(P,V)


    
import math


def honest_prover(AM,AM1,pi,mess_list,s):
    n=len(AM)
    if len(mess_list)==0:
        np.random.seed(s)
        sigma =np.random.permutation(n)
        h=apply_permut(AM,sigma)
        H=generate_graph(h)
        mess_list.append(H)
        #print(sigma)
    if len(mess_list)==2:
        np.random.seed(s)
        sigma =np.random.permutation(n)
        ch=mess_list[1]
        #print(sigma)
        if ch==0:
            mess_list.append(sigma)
        else:
            p=inv(pi)
            mess_list.append(composite_permutition(sigma,p))
    return mess_list

def honest_verifier(AM,AM1,mess_list):
    if len(mess_list)==1:
        ch=random.choice(range(2))
        mess_list.append(ch)
    if len(mess_list)==3: 
        phi=mess_list[2]
        H=Graph(directed=False)
        H=mess_list[0]
        H0=apply_permut(AM,phi)
        H1=generate_graph(H0)
        print(g0,g1)
        if are_same(H,H1):
            mess_list.append('accept')
        else:
            mess_list.append('reject')
        
    return mess_list
    
    
def test_isomorphism():
    AM=enter_adjMatrix()
    AM1=enter_adjMatrix()
    pi=list(map(int, input('Enter pi:').split())) 
    V=lambda msg: honest_verifier(AM,AM1,msg)
    P=lambda msg: honest_prover(AM,AM1,pi,msg,s)
    return graph_isomorphism(P,V)
    
    
def protocol_dishonest_prover(G0, G1):
    AM=enter_adjMatrix()
    AM1=enter_adjMatrix()
    pi=list(map(int, input('Enter pi:').split())) 
    V=lambda msg: honest_verifier(AM,AM1,msg)
    P=lambda msg: cheating_prover(AM,AM1,msg,s)
    return graph_isomorphism(P,V)
    
    
 def cheating_prover(AM, AM1, mess,s):
    n=len(AM)
    if len(mess_list)==0:
        sigma =np.random.seed(s)
        sigma =np.random.permutation(n)
        h=apply_permut(AM,sigma)
        H=generate_graph(h)
        mess_list.append(H)
        #print(sigma)
    if len(mess_list)==2:
        sigma =np.random.seed(s)
        sigma =np.random.permutation(n)
        ch=mess_list[1]
        if ch==0:
            mess_list.append(sigma)
        else:
            mess_list.append(np.random.permutation(n))
    return mess_list
