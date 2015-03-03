#Programmer Dixon Styres
#Version 3-2-15
#pitch-hash

from pyechonest import track
import echonest.remix.audio as audio

fifths = []

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


    print a[0] 
    print fifths


if  __name__ =='__main__':
    main()
