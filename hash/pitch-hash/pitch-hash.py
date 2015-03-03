#Programmer Dixon Styres
#Version 3-2-15
#pitch-hash

from pyechonest import track
import echonest.remix.audio as audio

fifths = []
run1 = []

def main():
    audio_file = audio.AudioAnalysis('TRKPXWQ145D2A22467')
    a = audio_file.segments.pitches
    fifths.append(a[0][0])
    fifths.append(a[0][7])
    fifths.append(a[0][2])
    fifths.append(a[0][9])
    fifths.append(a[0][4])
    fifths.append(a[0][11])
    fifths.append(a[0][6])
    fifths.append(a[0][1])
    fifths.append(a[0][8])
    fifths.append(a[0][3])
    fifths.append(a[0][10])
    fifths.append(a[0][5])
    
    hash(fifths)

def hash(five):
    
    if(five[0]> five[1]):
        run1.append(1)
    else:
        run1.append(0)
    if(five[2]>five[3]):
        run1.append(1)
    else:
        run1.append(0)
    if(five[4]> five[5]):
        run1.append(1)
    else:
        run1.append(0)
    if(five[6]>five[7]):
        run1.append(1)
    else:
        run1.append(0)
    if(five[8]> five[9]):
        run1.append(1)
    else:
        run1.append(0)
    if(five[10]>five[11]):
        run1.append(1)
    else:
        run1.append(0)


    print run1

if  __name__ =='__main__':
    main()
