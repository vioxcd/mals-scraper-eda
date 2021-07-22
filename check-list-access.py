import os
import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

ANIME_LINK = 'https://myanimelist.net/animelist/'
MANGA_LINK = 'https://myanimelist.net/mangalist/'
IN_FILE = f'{os.getcwd()}/data/sampled-username.list'
OUT_FILE = f'{os.getcwd()}/data/sampled-access-list.list'
USERS = []

def soupify(link):
	page = requests.get(link)
	return BeautifulSoup(page.content, 'html.parser')

def has_access(link):
	# 1. check if badresult, e.g. ryuu_zake
	# 2. check if data table exist, e.g. MisterJohnMan
	soup = soupify(link)
	
	# first check
	badresult = soup.find('div', {'class': 'badresult'})
	if badresult:
		print(f'Bad result on {link}')
		return 0

	# second check
	data_table = soup.find('tr', {'class': 'list-table-data'})
	if not data_table:
		print(f'Data table does not exist on {link}')
		return 0

	return 1

def load_users(PATH = IN_FILE):
	with open(PATH, 'r') as f:
		for line in f:
			USERS.append(line.strip())

	return USERS

if __name__ == '__main__':
	# load data here
	users = load_users()

	# prep out file
	with open(OUT_FILE, 'w') as f:
		headers = 'username,anime_access,manga_access'
		f.write(headers)

	# loop over
	for username in tqdm(users):
		access = {'animelist': None, 'mangalist': None}

		access['animelist'] = has_access(ANIME_LINK + username)
		time.sleep(2)

		# if got no access to anime, skip access to manga too
		if not access['animelist']:
			continue

		access['mangalist'] = has_access(MANGA_LINK + username)
		time.sleep(2)

		# if got no access to manga, skip dump
		if not access['mangalist']:
			continue
		
		# dump
		with open(OUT_FILE, 'a') as f:
			f.write(f"\n{username},{access['animelist']},{access['mangalist']}")
