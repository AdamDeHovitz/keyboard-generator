s = set()
letters = 'qwertyuiopasdfghjklzxcvbnm'

for l1 in letters:
	for l2 in letters:
		s.add((l1, l2))

def verify(pairs):
	return set(pairs) == s

def verify_with_missing(pairs):

	for pair in range(len(pairs)-1):
		if pair in s:
			s.remove(pair)
	if len(s) == 0:
		return True

	print('Corpus does not have all pairs, this is what\'s missing: ')
	print(s)

	return False

if __name__ == "__main__":
	print('Enter your corpus file path: ')
	f = input()
	with open(f) as f:
		for line in f:
			for i in range(len(line)-1):
				pair = (line[i].lower(), line[i+1].lower())
				if pair in s:
					s.remove(pair)
			if len(s) == 0:
				print('Corpus has all pairs')
				exit()
	print('Corpus does not have all pairs, this is what\'s missing: ')
	print(len(s))
	print(s)