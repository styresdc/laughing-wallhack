## pitch-hash

Create a hash value based on the pitch of a segment

**Problem**

Finding a way to compare songs in a reasonable time will involve the use of a database and a hashing funtion. Starting easily with this, we will need to hash a given segment of a song. Later we can try to make a hash table and observe via histogram how the buckets are organized


**Process**

We can retreive pitch data from a segment quite easily , all we need to do is pull track analysis from echonest and group it. For pitch analysis we will be using the circle of 5ths to froup chords. We will then convert this into a hash string. 


**Dependencies**

To use aqplayer.py, you will need:

      - pyaudio
      - ffmpeg

**Example**

Simply initialize the aqplayer with an 'echonest.remix.audio.LocalAudioFile'.
Then you can feed it any type of AudioQuantum to be played.
```python
import echonest.remix.audio as audio
from aqplayer import Player

audio_file = audio.LocalAudioFile("15 Sir Duke.m4a")
bars = audio_file.analysis.bars

aqplayer = Player(audio_file) #creates a Player given an 'echonest.remix.audio.LocalAudioFile'

for bar in bars:
    aqplayer.play(bar) #give play() any 'echonest.remix.audio.AudioQuantum' to be played (section, bar, beat, etc...)

aqplayer.closeStream() #close the audiostream when done
```

**Code Explanation**

In the initializer, aqplayer first creates a pyaudio object. It then retrieves the wave file associated with the 'echonest.remix.audio.LocalAudioFile' and opens it using the built in wave module. After opening the wave, a stream is opened using the pyaudio object. The parameters used to open the stream are retrieved from the wave file.
```python
    def __init__(self, audio_file):
        self.p = pyaudio.PyAudio()
        self.af = audio_file
        self.wf = wave.open(self.get_wav(), 'rb')
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                channels=self.af.numChannels, rate=self.af.sampleRate, output=True)
```
To find the start of the wave frames to be fed to the stream, aqplayer multiplies the starting time of the 'echonest.remix.audio.AudioQuantum' by the wave framerate. To calculate the number of frames, aqplayer multiplies the duration of the 'echonest.remix.audio.AudioQuantum' by the wave framerate. After these values are found, the position of the wave is set, and the frames read using wave's readframes method. These frames are written to the stream to be played.
```python
    def play(self, AudioQuantum, intro=True):
        """
        Accepts any echonest.remix.audio.AudioQuantum and audibly plays it for you.
        If the AudioQuantum is the first one present, it will play any frames before
        it's start time. To turn this off, set intro=False.
        """
        index = AudioQuantum.absolute_context()[0]
        if index == 0 and intro== True:
            numframes = int((AudioQuantum.duration + AudioQuantum.start) * self.wf.getframerate())
            startframe = 0
        else:
            numframes = int(AudioQuantum.duration * self.wf.getframerate())
            startframe = int(AudioQuantum.start * self.wf.getframerate())
        self.wf.setpos(startframe)
        self.stream.write(self.wf.readframes(numframes))
```
Make sure to close the pyaudio stream when you are done by calling the closeStream() method.
