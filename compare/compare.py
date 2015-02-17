#Programmer Dixon Styres
#Version 2-9-14
#music sim
#compares simple traits of given track id


from pyechonest import track
import os
def main():
    os.system('clear')
    t1 = track.track_from_id('TRFQZUR14B7B2B03E8')
    t2 = track.track_from_id('TRRXYRP1456A26E5AC')
    t1.get_analysis()
    t2.get_analysis()
    print "Song One Artist: " + t1.meta[u'artist']
    print "Song One Title: " + t1.meta[u'title'] + " \n"

    print "Song Two Artist: " + t2.meta[u'artist']
    print "Song Two Title: " + t2.meta[u'title'] + " \n"

    print "Song One BPM: " +str(t1.tempo)
    print "Song Two BPM: " +str(t2.tempo)

    if(t1.tempo<t2.tempo):
        decrease = t1.tempo-t2.tempo
        result = round(((decrease / t1.tempo) * 100),0)
        print str(result) + "% change in tempo"

    os.system('read')
if  __name__ =='__main__':
    main()
