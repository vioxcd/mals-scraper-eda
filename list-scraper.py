"""
LINK: animelist/{username}/load.json?status=7
opt: offset={int}

result:
	"status": 1,
	"score": 0,
	"anime_title": "Anime Himitsu no Hanazono",
	"anime_id": 2810,
"""

import json
import os

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# replace offset using str methods later
ANIME_LINK = 'https://myanimelist.net/animelist/USERNAME/load.json?OFFSET=NUM&status=7'
MANGA_LINK = 'https://myanimelist.net/mangalist/USERNAME/load.json?OFFSET=NUM&status=7'

IN_FILE = f'{os.getcwd()}/data/sampled-username-offset.csv'
OUT_FILE = f'{os.getcwd()}/data/sampled-lists.csv'

OFFSET = 300
DATA = []

def fetch(link):
	payload = requests.get(link)
	return payload.json()
	return BeautifulSoup(page.content, 'html.parser')

def load_data(PATH = IN_FILE):
	C = 0

	with open(PATH, 'r') as f:
		for line in f:
			data = line.strip().split(',') 
			DATA.append({
				'username': data[0],
				'total_anime': int(data[1]),
				'total_manga': int(data[2]),
			})
			C += 1

			if C == 5:
				break
	return DATA

if __name__ == '__main__':
	# load data
	data = load_data()

	# prep out file
	with open(OUT_FILE, 'w') as f:
		headers = 'username,anime_id,anime_title,score,status'
		f.write(headers)

	# loop over
	for d in tqdm(data):
		anime_link = ANIME_LINK.replace('USERNAME', d.username)
		manga_link = MANGA_LINK.replace('USERNAME', d.username)
