from state import *
from agent import *
# import state
import numpy as np
import math


def main():
    deleteContent("r1.txt")
    deleteContent("r2.txt")
    deleteContent("r3.txt")
    deleteContent("r4.txt")
    gamma = 0.1
    alpha=0.2
    agent_1=agent([1,1])
    agent_2=agent([1,1])
    i=0
    L1=[]
    L2=[]
    L3 = []
    L4 = []
    while(i<100):
        a1=agent_action(agent_1.Q, gamma)
        a2 = agent_action(agent_2.Q, gamma)
        if(a1==a2):
            reward=0
        else:
            reward=1
        update_Q(reward, agent_1.Q, alpha, a1)
        update_Q(reward, agent_2.Q, alpha, a2)
        i+=1
        L1.append(agent_1.Q[0]/agent_1.Q[1])
        L2.append(probability(agent_1.Q,1,gamma))
        L3.append(agent_2.Q[0]/agent_2.Q[1])
        L4.append(probability(agent_2.Q, 1, gamma))
    print(L1)
    print("Hooray")
    print(L2)
    print("Hooray")
    print(L3)
    print("Hooray")
    print(L4)
    with open("r1.txt", "a") as myfile:
        myfile.write(str(L1)+ '\n')
    with open("r2.txt", "a") as myfile:
        myfile.write(str(L2) + '\n')
    with open("r3.txt", "a") as myfile:
        myfile.write(str(L3) + '\n')
    with open("r4.txt", "a") as myfile:
        myfile.write(str(L4) + '\n')





def agent_action(Q,gamma):
    p_1=math.exp(Q[0]/gamma)/(math.exp(Q[0]/gamma)+math.exp(Q[1]/gamma))
    p_2 = math.exp(Q[1] / gamma) / (math.exp(Q[0] / gamma) + math.exp(Q[1] / gamma))
    r=np.random.uniform(0,1)
    if(r<=(p_1)):
        return 0
    else:
        return 1

def probability(Q,i,gamma):
    return math.exp(Q[i]/gamma)/(math.exp(Q[0]/gamma)+math.exp(Q[1]/gamma))

def update_Q(reward,Q,alpha,i):
    Q[i]=Q[i]+alpha*(reward-Q[i])



def deleteContent(fName):
    with open(fName, "w"):
        pass

if __name__ == '__main__':
    main()


