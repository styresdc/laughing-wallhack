#Programmer Dixon Styres
#Version 2-9-14
#music sim

#working on xquartz, pretty sure it might need other things for xming


from pyechonest import track
import echonest.remix.audio as audio
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import numpy as np

def main():
#    timbre_list = []
#    pitch_list = []
#    t = track.track_from_id('TRKPXWQ145D2A22467')
#    t.get_analysis()
#    for i in range(0,len(t.segments)):
#    	a=t.segments[i]
#        timbre_list.append( a[u'timbre'])
#    for i in range(0,len(t.segments)):
#        a=t.segments[i]
#        pitch_list.append( a[u'pitches'])
#            #plot(timbre_list, "Timbre", t)
#            #plot(pitch_list, "Pitch", t)
    mplo()

'''
plots a line kida thingy not enabled
def plot(list, value, track):
    n = np.asarray(list)
    plt.xlabel("Time")
    plt.ylabel(value)
    plt.title(value +" Progression : " + track.meta[u'title'])
    plt.plot(n)
    plt.show()
'''


def mplo():
    dimlist = [(773, 773)]
    for d in dimlist:
        matshow(samplemat(d,'TRKPXWQ145D2A22467',"timbre"))
        matshow(samplemat(d,'TRKPXWQ145D2A22467',"pitches"))
    show()

def samplemat(dims, id, value):
    t = track.track_from_id(id)
    t.get_analysis()
    audio_file = audio.AudioAnalysis(id)
    if(value == "pitches"):
        a = audio_file.segments.pitches
    else:
        a = audio_file.segments.timbre
    n = np.asarray(a)
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = zeros(dims)
    print "Loading... (takes a while)" + t.meta[u'title'] + ": " + t.meta[u'artist']
    for i in range(0,len(n)):
        for j in range(0,len(n)):
            aa[i][j] = (sum(n[i])-sum(n[j]))

    return aa

if  __name__ =='__main__':
    main()
