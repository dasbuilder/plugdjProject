#!/usr/bin/env python3

import re
import os
import json
import requests
from time import sleep

# Global Vars
searchPath = "/Users/spencer.anderson/testing/plugdj/"
cachedir = searchPath + "cachedfiles/"

ua = {	'user-agent':
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
		}

def main():
	search_artist = input("Enter the artist you want to search for: ")
	sa = re.compile(search_artist, re.IGNORECASE)
	print("\n")

	playList_titles = []
	for fname in os.listdir(searchPath):
		if fname.endswith('.json'):
			playList_titles.append(searchPath + fname)
			playList_titles.sort()

	# Gets the list of everything and places it into one giant list
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
					print("\n{0} found in {1}\n{2}\n".format(r.status_code, json.loads(names)['meta']['name'], jsonData['title'].replace("&amp;", "&").replace("&apos;", "'")))
				else:
					print("{0}\n{1}\t{2}\n".format(json.loads(names)['meta']['name'], r.status_code, jsonData['title'].replace("&amp;", "&").replace("&apos;", "'")))
			elif jsonData['image'] is None and sa.findall(jsonData['title']):
				print("!!{0} found in {1}\n{2}\n".format(jsonData['image'], json.loads(names)['meta']['name'], jsonData['title'].replace("&amp;", "&").replace("&apos;", "'")))


#def cachefiles(main):
ytAPIkey = "AIzaSyAqDGpKsOw2b-8IBiOiZKWIrxm7fq4ug68"


try:
	main()
except KeyboardInterrupt:
	print(" detected, exiting")
	exit

"""
	for names in mega_FileList():
		print("Playlist:\t{name}".format(name=json.loads(names)['meta']['name']))
		print("Code\tTitle")
		print("===============================================================\n")
		for jsonData in json.loads(names)['data']:
			if jsonData['image'] is not None:
				if requests.get(jsonData['image']).status_code == 404:
					a =
					print(a)

playList_titles = []
for fname in os.listdir(searchPath):
	if fname.endswith('.json'):
		playList_titles.append(searchPath + fname)
		playList_titles.sort()

# Gets the list of everything and places it into one giant list
def mega_FileList():
	mega_FileList = []
	for rFiles in playList_titles:
		mega_FileList.append(open(rFiles, 'r').read())
	return mega_FileList

# Gets the list of filenames from the giant list using 'meta' and 'name'
def fileNames():
	fileNames = []
	for filename in mega_FileList():
		fileNames.append(json.loads(filename)['meta']['name'])
	return fileNames


Saved for backwards compatability
for names in mega_FileList():
	for jsonData in json.loads(names)['data']:
		if jsonData['image'] is not None and sa.findall(jsonData['title'], re.IGNORECASE):
				r = requests.get(jsonData['image'], headers=ua)
				sleep(.8)
				if r.status_code == 404:
					print("{0} detected in {1}\n{2}\n".format(r.status_code, json.loads(names)['meta']['name'], jsonData['title'].replace("&amp;", "&").replace("&apos;", "'")))
				else:
					print("{0}\n{1}\t{2}\n".format(json.loads(names)['meta']['name'], r.status_code, jsonData['title']))

for names in mega_FileList():
	print("Playlist:\t{name}".format(name=json.loads(names)['meta']['name']))
	print("Code\tTitle")
	print("===============================================================\n")
	for jsonData in json.loads(names)['data']:
		if jsonData['image'] is not None and sa.findall(jsonData['title']):
			print("{codes}\t{titles}\n".format(codes=requests.get(jsonData['image'], headers=ua).status_code, titles=jsonData['title']).replace("&amp;", "&").replace("&apos;", "'"))
			sleep(.8)
		elif jsonData['image'] is None and sa.findall(jsonData['title']):
			print("{codes}\t{titles}\n".format(codes=jsonData['image'], titles=jsonData['title']).replace("&amp;", "&").replace("&apos;", "'"))
"""

"""
The code needs to:
1. Create filename list
2. Create alphabet list
3.
2.
print("===================== Playlist Title =======================\n")
"""
