# Dubtrack.fm and Plug.dj playlist parser

**Disclaimer!**

I have not tested this on any plug.dj tracklists that you download using JTBrinkman's bookmarklet listed below. I'm not certain if their data output is the same as I'm unfamiliar with JS.

I made this to search through all my dubtrack.fm .json files and find the artist or track name; if the video or song was still online or not (return http response code) and the playlist name the track comes from.

## Version History
    Have worked on these platforms:
    Linux distros
    macOS High Sierra

### Current Version 1.1
---

####  Version 1.0
    Redesigned this program from song-search which was the original program but without jq

  This newer version is built with [jq](https://stedolan.github.io/jq/manual/) which is a JSON parser and is particularly useful in this case.
  The old grep-centered command i.e.
  `grep -ioHP '[^"\{\}]*"title":"([^"]+)"'` was very clunky and was difficult to read. JQ is far faster and more flexible.

#### Version 1.1 - Made changes to curl command
    Added -o /dev/null and required "%{http_code}" which is curl friendlier.
    Refer to plugdj/README.md for more information. 


You may still get use out of this, but you may need to tweak it. If you have any questions let me know.

Dubtrack.fm has no mass playlist search or filter. The following song-search script will only work if you use this bookmarklet managed by [JTBrinkmann](https://github.com/JTBrinkmann), their [Dubtrack-Playlist-Pusher](https://github.com/JTBrinkmann/Dubtrack-Playlist-Pusher) to first download all your dubtrack.fm playlists.
Here's an example of how things look when something is searched:

![arminsearch](https://xavierlight.s3.amazonaws.com/monosnap/2m55a_04-05-2018_20-33-43.png)


In order to get this working on your system, you must change the code to match the paths of your local environment.

E.g. *I have /Users/userfifty/testing/plugdj where my json files are. Change this to your own path to your json files.*

What I had to do to get this to work is as follows:
1. Install the bookmarklet from JTBrinkman, mentioned above.
2. Download all my Dubtrack.fm playlists following instructions on hits Github.
3. Set an alias to the bash file itself, e.g. in my `~/.bash_profile` (`~/.bashrc` on Linux and Unix variants) which allows me to call my program wherever I am: `alias AS='/home/userfifty/testing/plugdj/song-search'`
4. Store all .json files within a certain directory. Here's an output of what I have stored after unzipping my files:

```
138?.json
Deep-TechHouse.json
Driving Trance Vol. 15.json
Drum&Bass.json
Friday (Upbeat & Feeling Great!).json
Live DJ Sets.json
Markus.json
Melodic.json
Mixes.json
NBC (nothin but chill).json
PSY.json
Progressive Sets.json
Progressive.json
Pure Uplifting.json
Solarstone.json
song-search
Spark (Vocal Hits).json
Starter (Darker Shades of Trance).json
The Dump.json
The Thrillseekers Nightmusic Volume 2.json
Trouse.json
WTFriday.json
blurb.json
oldschool (The Classics, Vol. 1).json
oldschool (The Classics, Vol. 2).json
```
#### Let's talk jq:

I did not have this on my Macbook and thus used brew to install. Linux users - use your appropriate package manager for installation instructions on installing jq.

If you already have jq installed, skip passed this section.
To install jq on Mac using homebrew use:

`brew install jq`

Alternatively you could do a `git clone` for the [jq repo](https://github.com/stedolan/jq).
*If you don't have brew installed, check it out [here](https://brew.sh/). Run the above command once you have brew installed.*

After that is installed you'll be able to run jq.

---

**Looking at the command**

`jq -r '.data[]|"\(input_filename)%\(.image)%\(.title)"' "${songdir}"*.json`

1. Using jq in raw mode (-r) I'm taking the key .data, I strip it of its outer boundary to get to the rest.
2. I then use input_filename to print the filename
3. Afterwards, grabbing the image (YT or SoundCloud link)
4. Finally, the title with all three being separated by a % which comes int play later.

 - The above output is fed into the following via pipe which is then fed through another pipe that rewrites missing &, ', and ".

    *I'm using gsed because I prefer gnu-sed over BSD sed.*

```
grep -i "$songinfo" | gsed -r "s_(&amp;)_\\&_g; s_(&apos;)_\\'_g; s_(&quot;)_\"_g" |

while IFS='%' read -r filename responses titles; do
printf "%s\n%s %s\n\n"
"$(awk -F'/' '{ gsub(/.json/, "", $6); print $6 }' <<<"$filename")" \
"$(curl -sIL "$responses" -A "$ua" -w "%{http_code}" -o /dev/null)" \
"$titles";
sleep .5;

done;
```

5. This is then piped into a while loop where IFS is set to % thus, allowing me to split above output from jq.
6. The loop reads each variable set from the jq output then
  a. Prints the filename, minus .json file extension using the read value filename as herestring input.
  b. Curl the SC or YT URL for a response code, return that and nothing else
  c. pattern that was matched from search string.
7. Sleep for .05 seconds
