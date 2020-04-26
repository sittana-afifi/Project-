def graph_isomorphism(P,V):
    message_list=[]
    prover_move=True
    while len(message_list)>0 and not message_list[-1] in {'accept','reject'}:
        if prover_move :
            message_list=P(message_list)
        else :
            message_list=V(message_list)
        prover_move= not prover_move
    return message_list
    
    
def test_isomorphism():
    AM=enter_adjMatrix()
    AM1=enter_adjMatrix()
    pi=list(map(int, input('Enter pi:').split())) 
    V=lambda msg: honest_verifier(AM,AM1,msg)
    P=lambda msg: honest_prover(AM,AM1,pi,msg)
    graph_isomorphism(P,V)


    
 import math
def honest_prover(AM,AM1,pi,mess_list):
    if len(mess_list)==0:
        n=len(AM)
        sigma = np.random.permutation(range(0,n))
        h=apply_permut(AM,sigma)
        H=generate_graph(h)
        mess_list.append(H)
        #print(H)
    if len(mess_list)==1:
        if ch==0:
            mess_list.append(sigma)
            print(sigma)
        else:
            p=inv(pi)
            message_list.append(composite_permut(p,sigma))
            print(composite_permut(p,sigma))
    return mess_list



def honest_verifier(AM,AM1,mess_list):
    if mess_list==1:
        ch=random.choice(range(1))
        message_list.append(ch)
        H1=apply_permut(AM,phi)
    r=are_same(H,H1)
    if r==True:
        mess_list.append('accept')
    else:
        mess_list.append('reject')
        
    return mess_list
    
    
    
