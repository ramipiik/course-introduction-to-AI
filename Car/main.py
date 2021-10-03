# B(attery)
# R(adio)
# I(ignition)
# G(asoline)
# S(tarts)
# M(oves)

from random import random

#Returns BATTERY state
def pB():
    if random()<=0.9: #90% probability that battery full
        return 1
    else:
        return 0

#Returns RADIO state
def pR(B):
    if B==0: # no radio if battery empty 
        return 0
    elif B==1: 
        if random()<=0.9: #if battery, 90% chance that radio works
            return 1
        else: 
            return 0
    else:
        raise(TypeError)


#Returns IGNITION state
def pI(B):
    if B==0: # no ignition if battery empty 
        return 0
    elif B==1: 
        if random()<=0.95: #if battery, 95% chance that ignition works
            return 1
        else: 
            return 0
    else:
        raise(TypeError)

#Returns GASOLINE state
def pG():
    if random()<=0.95: #95% probability that gasoline in the tank
        return 1
    else:
        return 0

#Returns START state
def pS(I, G):
    if I==0 and G==0: # doesn't start
        return 0
    elif I==0 and G==1: # doesn't start
        return 0
    elif I==1 and G==0: # doesn't start
        return 0
    elif I==1 and G==1:
        if random()<=0.01:
            return 0
        else:
            return 1
    else:
        raise(TypeError)

#Returns MOVES state
def pM(S):
    if S==0: # doesn't move if doesnt start
        return 0
    elif S==1: 
        if random()<=0.99: #if starts, 99% chance that moves
            return 1
        else: 
            return 0
    else:
        raise(TypeError)


def create_n_car_states(n):
    counter=0
    states=[]
    while counter<n:
        B=pB()
        R=pR(B)
        I=pI(B)
        G=pG()
        S=pS(I, G)
        M=pM(S)
        state=(B,R,I,G,S,M)
        states.append(state)
        counter+=1

    return states

# P(B | R,G,¬S)
def estimate1(states):
    total_cases=0
    positive_cases=0
    for state in states:
        if state[1]==1 and state[3]==1 and state[4]==0:
            total_cases+=1
            if state[0]==1:
                positive_cases+=1
    if total_cases==0:
        total_cases=0.000000000001
    print("total_cases",total_cases)
    print("positive_cases",positive_cases)
    return (positive_cases/total_cases)


# P(S | R,I,G)
def estimate2(states):
    total_cases=0
    positive_cases=0
    for state in states:
        if state[1]==1 and state[2]==1 and state[3]==1:
            total_cases+=1
            if state[4]==1:
                positive_cases+=1
    if total_cases==0:
        total_cases=0.000000000001
    print("total_cases",total_cases)
    print("positive_cases",positive_cases)
    return (positive_cases/total_cases)

# P(S | ¬R,I,G)
def estimate3(states):
    total_cases=0
    positive_cases=0
    for state in states:
        if state[1]==0 and state[2]==1 and state[3]==1:
            total_cases+=1
            if state[4]==1:
                positive_cases+=1
    if total_cases==0:
        total_cases=0.000000000001
    print("positive_cases",positive_cases)
    print("total_cases",total_cases)
    return (positive_cases/total_cases)

simulated_states=create_n_car_states(100000)

# for state in simulated_states:
#     print (state)

print("Estimate 1:", estimate1(simulated_states))
print("------")
print("Estimate 2:", estimate2(simulated_states))
print("------")
print("Estimate 3:", estimate3(simulated_states))