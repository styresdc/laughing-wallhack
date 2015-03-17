# Problem
We want to be able to hash two songs to see if they are simaler.

# Question
1. How much info do we need from one song (how many segments to analyze)?
2. What parts of segments will be usefull for our comparasin (pitch tambre tempo)?

# Resources
1. [The infinite jukebox]
2. [Million Song Dataset Code]

### 1. Mini-abstract and relevance of [The infinite jukebox]
The infinite jukebox does a comparasin between segments of songs. It highly values 'sections', 'bars', 'beats', 'tatums', and 'segments'. It looks at these aspects to determine if segemts are close enough to switch between. It seems to compare all segments in a song for its usage. It would be safe to say that in order to ensure good trasitions, we would need to so the same thing.

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

### 2. Mini-abstract and relevance of [Locality-sensitive hashing]
In deciding what to process as far as attributes of a song, most items are neccesary to compute in order to have good trasitions. One problem we will begin to face is that this analysis especially when being done over http connections via EN will take a considerable amount of time. The idead of Locality-sensitive hashing is to have as many collisions as possible LSH hashes input items so that similar items map to the same “buckets” with high probability (the number of buckets being much smaller than the universe of possible input items). This will help us not only to speed up time needed, but will also give more similarity between tracks.

### 3. Where to go from here
We need to develop a way to hash a song by its elements. We have looked into doing this at the start by comparing pitch values from segments and making a hash for a segment. We need to extend this to multiple songs, and compare items within these songs. Once we have a hash value for a song, we can compare multiple songs via their hash.


[The infinite jukebox]: http://labs.echonest.com/Uploader/index.html
[Locality-sensitive hashing]: http://en.wikipedia.org/wiki/Locality-sensitive_hashing
