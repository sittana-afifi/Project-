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
        if message_list[-1]== 'Accept' or   message_list[-1]== 'Reject':
            return message_list
    return message_list
    
   



import math
def honest_prover(AM,AM1,pi,mess_list,s):
    n=len(AM)
    if len(mess_list)==0:
        np.random.seed(s)
        sigma =np.random.permutation(n)
        h=apply_permute(AM,sigma)
        mess_list.append(h)
    if len(mess_list)==2:
        np.random.seed(s)
        sigma =np.random.permutation(n)
        ch=mess_list[1]
        if ch==0:
            mess_list.append(sigma)
        else:
            p=inv(pi)
            mess_list.append(composite_permutition(p,list(sigma)))
    return mess_list



def honest_verifier(AM,AM1,mess_list):
    if len(mess_list)==1:
        ch=random.choice(range(2))
        mess_list.append(ch)
    if len(mess_list)==3: 
        phi=mess_list[2]
        ch=mess_list[1]
        H=mess_list[0]
        mess_list[0]=generate_graph(H)
        if ch==0 :
            H0=apply_permute(AM,phi)
        if ch==1:
            H0=apply_permute(AM1,phi)
        if are_equal(H,H0):
            mess_list.append('Accept')
        else:
            mess_list.append('Reject')
    return mess_list
    
    
def test_isomorphism(AM, AM1, pi): 
    s=random.choice(range(1000))
    V=lambda msg: honest_verifier(AM,AM1,msg)
    P=lambda msg: honest_prover(AM,AM1,pi,msg,s)
    return graph_isomorphism(P,V)
    
    


def protocol_dishonest_prover(AM, AM1):
    s=random.choice(range(1000))
    V=lambda msg: honest_verifier(AM,AM1,msg)
    P=lambda msg: cheating_prover(AM,AM1,msg,s)
    return graph_isomorphism(P,V)


    
    
    


    
 def cheating_prover(AM, AM1, mess_list,s):
    n=len(AM)
    if len(mess_list)==0:
        np.random.seed(s)
        sigma =np.random.permutation(n)
        h=apply_permute(AM,sigma)
        mess_list.append(h)
    if len(mess_list)==2:
        np.random.seed(s)
        sigma =np.random.permutation(n)
        ch=mess_list[1]
        if ch==0:
            mess_list.append(sigma)
        else:
            mess_list.append(np.random.permutation(n))
    return mess_list


def simulator(AM,AM1):
    mess_list=[]
    s=random.choice(range(1000))
    np.random.seed(s)
    sigma =np.random.permutation(len(AM))
    b=random.choice(range(2))
    if b==0:
        h=apply_permute(AM,sigma)
    if b==1:
        h=apply_permute(AM1,sigma)
    mess_list.append(generate_graph(h))
    ch=random.choice(range(2))
    mess_list.append(ch)
    if ch == b:
        mess_list.append(sigma)
        mess_list.append('Accept')
        return mess_list
    else :
        return simulator(AM,AM1)

    
    
