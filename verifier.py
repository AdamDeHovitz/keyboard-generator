from key_timer import letters
print('Enter your corpus file path: ')
f = input()
s = set()

with open('corpora/great_expectations.txt') as g:
	for line in g:
		for i in range(len(line)-1):
			pair = (line[i], line[i+1])
			s.add(pair)

with open(f) as f:
	for line in f:
		for i in range(len(line)-1):
			pair = (line[i], line[i+1])
			if pair in s:
				s.remove(pair)
		if len(s) == 0:
			print('Corpus has all pairs')
			exit()
print('Corpus does not have all pairs')