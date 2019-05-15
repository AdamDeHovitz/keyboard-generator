from key_timer import letters
s = set()

with open('corpora/great_expectations.txt') as g:
	for line in g:
		for i in range(len(line)-1):
			pair = (line[i], line[i+1])
			s.add(pair)

def verify(pairs):
	return set(pairs) == s

if __name__ == "__main__":
	print('Enter your corpus file path: ')
	f = input()
	with open(f) as f:
		for line in f:
			for i in range(len(line)-1):
				pair = (line[i], line[i+1])
				if pair in s:
					s.remove(pair)
			if len(s) == 0:
				print('Corpus has all pairs')
				exit()
	print('Corpus does not have all pairs, this is what\'s missing: ')
	print(s)