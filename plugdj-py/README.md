# Aritst or Song Search Using Python and JSON converted Dictionaries

- Loops through the directory and looks for files ending with .json.
- Then it creates a list by adding the searchPath above and the fname (filename)
from the loop and finally sorts the list.

- Makes a list and loops through the playList_titles list created above.
- Opens each file, and appends it to one mega list ;)
- Loops through mega_FileList (which is one giant list) function created above.
- Loads each string into a Python dictionary using the ['data'] field.
- Loops through results that do not return None and also match the search_artist input
from the start of this function found in ['data']['title'].

- Continues by running a request to the URL it finds in ['data']['image']
and passes the user-agent from above as header.

- In the future, I hope to directly retrieve this using both YouTube and SoundCloud's
respective APIs.

### Note

Under the conditions describe above, I then check if a video has a 404
and if it does, then print out the filename, which I get from the ['meta']['name']
dictionary values and say 404 found and the title.
Else, print filename, response code and title.
If the image does return None, but matches our search string, print same information
as listed above, but add "None found".

The steps above undergo string replacement from &amp; to & and &apos; to a single '


#### Future Builds
If you know how to work with YouTube's API send me a message. I'm looking
to get this information using their API. I'm wanting to know if the videos
have been removed or if they are still up on the site. The playlists I
have and the site they are on do not have a way to search all playlists
nor do they have the ability to see which ones have been removed from
their respective site. Yes, you can see the video thumbnail, but what
if a video has been region locked? You will still see the thumbnail
but when the video plays - nothing.
