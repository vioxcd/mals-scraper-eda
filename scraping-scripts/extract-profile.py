import os
import re
import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# SET SAMPLE OR NON-SAMPLE
PATH = f'{os.getcwd()}/data/link.list'
DUMP = f'{os.getcwd()}/data/dump-profile.list'
LINKS = []

def load_links():
	with open(PATH, 'r') as f:
		for line in f:
			LINKS.append(line.strip())

	return LINKS


if __name__ == '__main__':
	links = load_links()

	# load headers into dump
	headers = 'username,anime_days,manga_days,watching,anime_completed,anime_on_hold,anime_dropped,anime_planned,reading,manga_completed,manga_on_hold,manga_dropped,manga_planned,anime_total_entries,manga_total_entries,friends'
	with open(DUMP, 'w') as f:
		f.write(headers)

	for link in tqdm(links):
		page = requests.get(link)
		soup = BeautifulSoup(page.content, 'html.parser')
		
		# getting data
		username = link.split('/')[-1]

		"""
		anime_days, manga_days
		div		di-tc al pl8 fs12 fw-b

		watching, anime_completed, anime_on_hold, anime_dropped, anime_planned
		reading, manga_completed, manga_on_hold, manga_dropped, manga_planned
		span	di-ib fl-r lh10

		anime_total_entries, manga_total_entries
		ul		stats-data fl-r
		  span	  di-ib fl-r
		
		friend
		a		fl-r fs11 fw-n ff-Verdana
		"""
		days = soup.find_all('div', {'class': 'di-tc al pl8 fs12 fw-b'})

		try:
			# careful of 404 error (WEIRD!!)
			days = [ day.text.split(' ')[-1].replace(',', '') for day in days ]
		except:
			print(f'SKIPPED ONE ERROR ON {username}')
			time.sleep(3)
			continue

		stats = soup.find_all('span', {'class': 'di-ib fl-r lh10'})
		stats = [ stat.text.replace(',', '') for stat in stats ]

		entries = soup.find_all('ul', {'class': 'stats-data fl-r'})
		entries = [ entry.find('span', {'class': 'di-ib fl-r'}).text.replace(',', '') for entry in entries ]

		f_str = soup.find_all('a', {'class': 'fl-r fs11 fw-n ff-Verdana'})[0].text
		friend = re.findall(r'\d+', f_str)[0].replace(',', '')

		# dumping data
		with open(DUMP, 'a') as f:
			dump = [ username, *days, *stats, *entries, friend ]
			f.write('\n')
			f.write(','.join(dump))

		# sleep
		time.sleep(3)
