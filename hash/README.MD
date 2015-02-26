# Problem
How can we quickly compare between multiple songs.

# Question
1. How can we store song data in such a way that they are quickly accesible?
2. How should we sort simaler songs?
3. Where to go from here?

# Resources
1. [Music Info Retrevial]
2. [The Infinite Jukebox]

### 1. Mini-abstract and relevance of [Music Info Retrevial]
Music information retrevial has been around for hundreds of years, from sheet music, to the modern mp3 player. It even extends to services such as shazam and others.
This slideshow gives a presentation of the history of music info retrevial, its purpose, and overviews of how its done.
Some sort of sorted database would be a quick an easy way to acess song data.

### 2. Mini-abstract and relevance of [The infinite jukebox]
The infinite jukebox provides away to evaluate sections of songs and rate them bases on similarity. 
It would be an interesting task to see if we could turn this into a hash function so that we can store songs in a DB
```javascript
function preprocessTrack(track) {
                trace('preprocessTrack');
                var types = ['sections', 'bars', 'beats', 'tatums', 'segments'];

                
                for (var i in types) {
                    var type = types[i];
                    trace('preprocessTrack ' + type);
                    for (var j in track.analysis[type]) {
                        var qlist = track.analysis[type]

                        j = parseInt(j)

                        var q = qlist[j]
                        q.track = track;
                        q.which = j;
                        if (j > 0) {
                            q.prev = qlist[j-1];
                        } else {
                            q.prev = null
                        }
                        
                        if (j < qlist.length - 1) {
                            q.next = qlist[j+1];
                        } else {
                            q.next = null
                        }
                    }
                }

                connectQuanta(track, 'sections', 'bars');
                connectQuanta(track, 'bars', 'beats');
                connectQuanta(track, 'beats', 'tatums');
                connectQuanta(track, 'tatums', 'segments');

                connectFirstOverlappingSegment(track, 'bars');
                connectFirstOverlappingSegment(track, 'beats');
                connectFirstOverlappingSegment(track, 'tatums');

                connectAllOverlappingSegments(track, 'bars');
                connectAllOverlappingSegments(track, 'beats');
                connectAllOverlappingSegments(track, 'tatums');


                filterSegments(track);
            }


```

### 3. Where to go from here?
We need to find a databse that suits are needs, and to create a python fucntion that like the infinte jukebox can hash a song and retunrn a value based on its attributes.
While looking for simaler songs to switch between, we can fingerprint it and compare it to to databse.


[Music Info Retrevial]: http://www.marsyas.info/acm2009_tutorial.pdf
[The Infinite Jukebox]: http://labs.echonest.com/Uploader/index.html
