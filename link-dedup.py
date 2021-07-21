import os

LIST_PATH = f'{os.getcwd()}/data/dump-link.list'
DEDUP_PATH = f'{os.getcwd()}/data/link-dedup.list'

data = set()

with open(LIST_PATH, 'r') as f:
	for line in f:
		if line in data:
			tmp = line.strip().split('/')[-1]  # for printing purpose
			print(f'duplicate on {tmp}')
		else:
			data.add(line)

	print(len(data))

# store dedup data
with open(DEDUP_PATH, 'w') as f:
	for line in data:
		f.write(f"{line}")
