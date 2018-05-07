#!/usr/bin/env python3

import re
import os
import json
import requests
from time import sleep

# Global Vars
searchPath = "/Users/userfifty/testing/plugdj/"

# User-Agent for the requester
# In the future this will be replaced with YouTube's API

ua = {	'user-agent':
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
		}

# Main function
#

def main():
	search_artist = input("Enter the artist you want to search for: ")
	sa = re.compile(search_artist, re.IGNORECASE)
	print("Remember, a 200 means the song or video is still online; a 404 means it's offline")
	print("\n")

	playList_titles = []
	for fname in os.listdir(searchPath):
		if fname.endswith('.json'):
			playList_titles.append(searchPath + fname)
		playList_titles.sort()

	def mega_FileList():
		mega_FileList = []
		for rFiles in playList_titles:
			mega_FileList.append(open(rFiles, 'r').read())
		return mega_FileList

	for names in mega_FileList():
		for jsonData in json.loads(names)['data']:
			if jsonData['image'] is not None and sa.findall(jsonData['title']):
				r = requests.get(jsonData['image'], headers=ua)
				sleep(.8)

				if r.status_code == 404:
					print("{0}! found in {1}\n{2}\n".format(r.status_code, json.loads(names)['meta']['name'], jsonData['title'].replace("&amp;", "&").replace("&apos;", "'")))
				else:
					print("{0}\n{1}\t{2}\n".format(json.loads(names)['meta']['name'], r.status_code, jsonData['title'].replace("&amp;", "&").replace("&apos;", "'")))
			elif jsonData['image'] is None and sa.findall(jsonData['title']):
				print("!!{0} found in {1}\n{2}\n".format(jsonData['image'], json.loads(names)['meta']['name'], jsonData['title'].replace("&amp;", "&").replace("&apos;", "'")))

try:
	main()
except KeyboardInterrupt:
	print(" detected, exiting")
