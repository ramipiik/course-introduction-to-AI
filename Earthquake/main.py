# E(arthquaka)
# B(urglar)
# A(larm)


from random import random

#Returns EARTHQUAKE state
def pE():
    if random()<=1/111: #earthquakes happen every 111th day
        return 1
    else:
        return 0

#Returns BURGLAR state
def pB():
    if random()<=1/365: #burglar breaks in once a year
        return 1
    else:
        return 0

#Returns ALARM state
def pA(E, B):
    if E==1 and B==0: # Earthquake, no burglar
        if random()<=0.81: # 81% probability of alarm
            return 1
        else:
            return 0

    elif E==0 and B==1: # Burglar, no earthquake
        if random()<=0.92: # 92% probability of alarm
            return 1
        else:
            return 0

    elif E==1 and B==1: # Burglar and earthquake
        if random()<=0.97: # 97% probability of alarm
            return 1
        else:
            return 0

    elif E==0 and B==0: # Nothing special going on
        if random()<=0.0095: # 0.0095 probability of a false alarm
            return 1
        else:
            return 0

    else:
        raise(TypeError)


def create_n_alarm_states(n):
    counter=0
    states=[]
    while counter<n:
        E=pE()
        B=pB()
        A=pA(E,B)
        state=(E,B,A)
        states.append(state)
        counter+=1

    return states

# P(B | A)
def estimate1(states):
    total_cases=0
    positive_cases=0
    for state in states:
        if state[2]==1:
            total_cases+=1
            if state[1]==1:
                positive_cases+=1
    if total_cases==0:
        total_cases=0.000000000001
    print("positive_cases",positive_cases)
    print("total_cases",total_cases)
    return (positive_cases/total_cases)


# P(B | A,E)
def estimate2(states):
    total_cases=0
    positive_cases=0
    for state in states:
        if state[0]==1 and state[2]==1:
            total_cases+=1
            if state[1]==1:
                positive_cases+=1
    if total_cases==0:
        total_cases=0.000000000001
    print("positive_cases",positive_cases)
    print("total_cases",total_cases)
    return (positive_cases/total_cases)


simulated_states=create_n_alarm_states(1000000)

# for state in simulated_states:
#     print (state)

print("Estimate 1:", estimate1(simulated_states))
print("------")
print("Estimate 2:", estimate2(simulated_states))