"""
LINK: animelist/{username}/load.json?status=7
opt: offset={int}

result:
	"status": 1,
	"score": 0,
	"anime_title": "Anime Himitsu no Hanazono",
	"anime_id": 2810,
"""

import csv
import json
import os
import time

import requests
from tqdm import tqdm

# replace offset using str methods later
ANIME_LINK = 'https://myanimelist.net/animelist/USERNAME/load.json?offset=OFFSET&status=7'
MANGA_LINK = 'https://myanimelist.net/mangalist/USERNAME/load.json?offset=OFFSET&status=7'

IN_FILE = f'{os.getcwd()}/data/sampled-username-offset.csv'
OUT_FILE = f'{os.getcwd()}/data/sampled-lists.csv'

OFFSET = 300
USERS_OFFSET = []

def fetch(link):
	payload = requests.get(link)
	return payload.json()

def load_user_offset(PATH = IN_FILE):
	with open(PATH, 'r') as f:
		for line in f:
			data = line.strip().split(',') 
			USERS_OFFSET.append({
				'username': data[0],
				'total_anime': int(data[1]), # used for comparison operation
				'total_manga': int(data[2]),
			})
	return USERS_OFFSET

if __name__ == '__main__':
	# load data
	user_offset = load_user_offset()

	# prep out file
	with open(OUT_FILE, 'w') as f:
		headers = 'username,type,id,title,score,status'
		f.write(headers)
		f.write('\n')

	# loop over all users
	for u in tqdm(user_offset):
		dump = []  # lists of data dumped to file

		# get data from anime
		offset = 0
		while offset < u['total_anime']:
			# format link & fetch
			anime_link = ANIME_LINK.replace('USERNAME', u['username']).replace('OFFSET', str(offset))
			payload = fetch(anime_link)
			
			# store data
			for data in payload:
				dump.append((
					u['username'],
					'anime',
					data['anime_id'],
					data['anime_title'],
					data['score'],
					data['status']
				))

			# increase offset for next turn
			offset += OFFSET
			time.sleep(2)

		# get data from manga
		offset = 0
		while offset < u['total_manga']:
			manga_link = MANGA_LINK.replace('USERNAME', u['username']).replace('OFFSET', str(offset))
			payload = fetch(manga_link)
			
			for data in payload:
				dump.append((
					u['username'],
					'manga',
					data['manga_id'],
					data['manga_title'],
					data['score'],
					data['status']
				))

			offset += OFFSET
			time.sleep(2)

		# dump to file
		with open(OUT_FILE, 'a') as f:
			w = csv.writer(f, delimiter=',', quotechar='"')
			w.writerows(dump)
