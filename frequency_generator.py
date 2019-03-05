import os
from collections import defaultdict

MAX_N = 3
CORPORA_PATH = './corpora/'

def make_freq():
	freqs = []
	for i in range(MAX_N):
		freqs.append(defaultdict(int))

	for file in os.listdir(CORPORA_PATH):
		if file.endswith(".txt"):
			with open(CORPORA_PATH + file, 'r') as f:
				contents = f.read()
				for i in range(len(contents)):
					for j in range(1, MAX_N+1):
						if i + j <= len(contents) and contents[i:i+j].isalpha():
							freqs[j-1][contents[i:i+j]] += 1
	return freqs

