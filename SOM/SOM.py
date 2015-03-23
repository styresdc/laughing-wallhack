#Programmer Dixon Styres
#Version 3-17-15
#SOM.py

#Forms a Self-organizing map for a given track id

from matplotlib.pylab import *
import matplotlib.pyplot as plt
import numpy as np
import random
from random import randrange

fifths = []
map = []
rand = []
random_index = 0
ecdist = 0
tht = 0
count = 0

w = np.random.uniform(0.0, 1.0, (20,20,12))

def_cm = [[0.51, 0.03, 0.12, 0.09, 0.30, 0.19, 0.07, 0.28, 0.09, 0.24, 0.06, 0.00],[0.47,0.06,0.07,0.39,0.03,0.28,0.00,0.30,0.25,0.10,0.06,0.10]]

shift = []

in_cm = []

#append to map
#circular shift
#append that

#or cminor
def app(vector):
    global in_cm
    for i in range(0,12):
        shift = np.roll(def_cm[0],i)
        in_cm.append(shift)
        shift = []
        shift = np.roll(def_cm[1],i)
        in_cm.append(shift)
        shift = []
    for i in range(0,24):
        shift.append(in_cm[i].tolist())
    in_cm = shift
    comp(shift)

def comp(vector):
    for s in range(1,30):
        for i in range(1,24):
          retInd = euc(vector)
          tht = theta(retInd[2],(retInd[0],retInd[1]),s)
          lst = last(retInd[2], (retInd[0],retInd[1]))
          global w
          w[retInd[0]][[retInd[1]]] = (w[retInd[0]][[retInd[1]]]) + (tht*0.02*lst)
        if(s % 10 == 0):
            print s
            plot()


def plot():
    n = def_cm[1]
    s = np.random.uniform(0.0, 1.0, (20,20))
    #calculate distance beween c major
    #create a 2d array fill with distance form each node to c major
    #have c major vector
    #fucntion takes in w and a vecotr, computes distance between input and nodes and fills 20*20 array and show
    
    for i in range(0,20):
        for j in range(0,20):
            a = n
            b = w[i][j]
            ecdist = np.linalg.norm(a-b)
            s[i][j] = ecdist
    plt.imshow(s, interpolation = 'nearest')
    plt.colorbar()
    plt.show()


def euc(vector):
    rand = []
    retInd = []
    index = 0
    maxDist = 2
    random_index = 0
    random_index = randrange(0,len(vector))
    rand.append(vector[random_index])
    for i in range(0,20):
        for j in range(0,20):
            a = rand
            b = w[i][j]
            ecdist = np.linalg.norm(a-b)
            if(maxDist>ecdist):
                maxDist = ecdist
                index = i
                index2 = j
    retInd = [index,index2,random_index]
    return retInd

def theta(u,v,s):
    aph = alpha(19,s,20)
    euc = tor(u,v)
    return (e**(-(euc**2)/(2*(aph))))

def alpha(r,s,c):
    
    return (0.3*(r-(s/c)))

def tor(u,v):
    global in_cm
    a = in_cm[u]
    b = w[v[0]][v[1]]
    ecdist = np.linalg.norm(a-b)
    return ecdist

def last(u,v):
    a = in_cm[u]
    b = w[v[0]][v[1]]
    return a-b

if  __name__ =='__main__':
    app(def_cm)
