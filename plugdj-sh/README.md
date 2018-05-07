# Bash and JQ Song Search

This file was originally written with a find command until I recently decided to convert it to mostly jq reading the files, and bash parsing the output.
From what I've learned so far, jq is pretty powerful and I have yet to learn more.

If you don't give it a search term of some sort (i.e. if $1 is empty) then it will loop until you give it something. 
