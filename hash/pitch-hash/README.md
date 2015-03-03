## pitch-hash

Create a hash value based on the pitch of a segment

**Problem**

Finding a way to compare songs in a reasonable time will involve the use of a database and a hashing funtion. Starting easily with this, we will need to hash a given segment of a song. Later we can try to make a hash table and observe via histogram how the buckets are organized


**Process**

We can retreive pitch data from a segment quite easily , all we need to do is pull track analysis from echonest and group it. For pitch analysis we will be using the circle of 5ths to froup chords. We will then convert this into a hash string. 


**Dependencies**

To use pitch-hash.py, you will need:

      -pyechonest

**Example**

Simply call python with the script, it uses a track id for now.

```python
python pitch-hash.py
```

**Code Explanation**

We start by getting a track analysis and getting one segment from it. We then get that one segment and arrange it in a way correspoding to the circle of 5ths
```python
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
```
Our hash funcitons checks the values and assigns a 1 or 0 to give us an idea of pitch at a point
```python
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
```
 We then print the hash for now
