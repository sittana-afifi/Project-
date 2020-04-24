def graph_isomorphism(P,V):
    message_list=[]
    prover_move=True
    while len(message_list)>0 and not message_list[-1] in {'accept','erject'}:
        if prover_move :
            message_list=P(message_list)
        else :
            message_list=V(message_list)
        prover_move= not prover_move
    return message_list
    
    
g0=generate_graph()
g1=generate_graph()
def test_isomorphism():
    pi=list(map(int, input('Enter pi:').split())) 
    V=lambda msg: honest_verifier(g0,g1,msg)
    P=lambda msg: honest_prover(g0,g1,pi,msg)
    graph_isomorphism(P,V)
test_isomorphism()



def honest_verifier():
    ch=random.choice(range(1))
    phi=message_list[2]
    H1=apply_permut(g0,phi)
    r=are_same(H,H1)
    if r==True:
        message_list[3]='accept'
    else:
        message_list[3]='reject'
        
    return message+[new_message]
    
    
    
    import math
def honest_prover():
    n=int(input('Enter the length of your graphs:'))
    i = random.choice(range(int(math.factorial(n-1)/2)))
    sigma=s_n(n)[i]
    a0=adj_mat()
    h=apply_permut(a0,sigma)
    H=generate_graph()
    ch=message_list[1]
    if ch==0:
        message_list[2]=sigma
    else:
        p=inv(pi)
        message_list[2]=composite_permut(p,sigma)
