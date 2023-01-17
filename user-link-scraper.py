import os
import time

import requests
from bs4 import BeautifulSoup

MALS_LINK = 'https://myanimelist.net'
USERS_LINK = 'https://myanimelist.net/users.php'
DUMP = f'{os.getcwd()}/data/dump-link.txt'
REQ_COUNT = 600


if __name__ == '__main__':
	for counter in range(REQ_COUNT):
		page = requests.get(USERS_LINK)
		soup = BeautifulSoup(page.content, 'html.parser')

		divs = soup.find_all('div', {'class': 'picSurround'})
		links = [ MALS_LINK + div.find('a').get('href') for div in divs ]

		# add newline to the first list
		links[0] = f'\n{links[0]}'

		with open(DUMP, 'a') as f:
			f.write('\n'.join(links))

		print(f'{counter} iteration')

		time.sleep(10)  # wait before next requests
