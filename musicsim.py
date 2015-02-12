#Programmer Dixon Styres
#Version 2-9-14
#music sim

#working on xquartz, pretty sure it might need other things for xming
#also not exaclty sure what im looking at, pretty sure it is time vs value (i.e. pitches looks weird)

from pyechonest import track
import matplotlib.pyplot as plt
import numpy as np

def main():
    timbre_list = []
    pitch_list = []
    t = track.track_from_id('TRKPXWQ145D2A22467')
    t.get_analysis()
    for i in range(0,len(t.segments)):
    	a=t.segments[i]
        timbre_list.append( a[u'timbre'])
    for i in range(0,len(t.segments)):
        a=t.segments[i]
        pitch_list.append( a[u'pitches'])
    plot(timbre_list, "Timbre", t)
    plot(pitch_list, "Pitch", t)

def plot(list, value, track):
    n = np.asarray(list)
    plt.xlabel("Time")
    plt.ylabel(value)
    plt.title(value +" Progression : " + track.meta[u'title'])
    plt.plot(n)
    plt.show()


if  __name__ =='__main__':
    main()
