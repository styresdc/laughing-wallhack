#Programmer Dixon Styres
#Version 3-17-15
#SOM.py

#Forms a Self-organizing map for a given track id

from pyechonest import track
import echonest.remix.audio as audio
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import numpy as np
import random

fifths = []
map = []
rand = []
w = np.random.uniform(0.0, 1.0, (30,12))
def main():
    audio_file = audio.AudioAnalysis('TRKPXWQ145D2A22467')
    a = audio_file.segments.pitches
    
    for i in range(0,len(a)):
        fifths = []
        fifths.append(a[i][0])
        fifths.append(a[i][7])
        fifths.append(a[i][2])
        fifths.append(a[i][9])
        fifths.append(a[i][4])
        fifths.append(a[i][11])
        fifths.append(a[i][6])
        fifths.append(a[i][1])
        fifths.append(a[i][8])
        fifths.append(a[i][3])
        fifths.append(a[i][10])
        fifths.append(a[i][5])
        map.append(fifths)

    sMake(map)

def sMake(vector):
    for s in range(0,1):
        for i in range(0, 24):
            dist = euc(vector)
            print dist

def euc(vector):
    rand = []
    index = 0
    maxDist = 0
    rand.append(random.choice(vector))
    for i in range(0,len(w)):
        a = w[i]
        b = rand
        dist = np.linalg.norm(a-b)
        if(dist>maxDist):
            maxDist = dist
            index = i
    return index

if  __name__ =='__main__':
    main()