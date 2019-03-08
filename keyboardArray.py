from namedlist import namedlist

Key = namedlist('Key', ['row', 'finger'])
keys = [Key(0, 0) for i in range(26)]
for i in range(10):
	keys[i].row = 1
for i in range(10, 19):
	keys[i].row = 2
for i in range(19, 26):
	keys[i].row = 3
keys[0].finger = 1 #q
keys[10].finger = 1 #a
keys[19].finger = 1 #z

keys[1].finger = 2 #w
keys[11].finger = 2 #s
keys[20].finger = 2 #x

keys[2].finger = 3 #e
keys[12].finger = 3 #d
keys[21].finger = 3 #c

keys[3].finger = 4 #r
keys[13].finger = 4 #f
keys[22].finger = 4 #v

keys[4].finger = 4 #t
keys[14].finger = 4 #g
keys[23].finger = 4 #b

keys[5].finger = 5 #y
keys[15].finger = 5 #h
keys[24].finger = 5 #n

keys[6].finger = 5 #u
keys[16].finger = 5 #j
keys[25].finger = 5 #m

keys[7].finger = 6 #i
keys[17].finger = 6 #

keys[8].finger = 7 #o
keys[18].finger = 7 #l

keys[9].finger = 8 #p

keyDistances = [[] for _ in range(26)]

for i in range(26):
	for j in range(26):
		keyDistances[i].append(0)
		if i == j:
			#Same Key
			keyDistances[i][j] = 0 
		elif keys[i].finger == keys[j].finger:
			#Same finger used to type these keys
			if (keys[i].row == 1 and keys[j].row == 3) or (keys[i].row == 3 and keys[j].row == 1):
				keyDistances[i][j] = 2
			else :
				keyDistances[i][j] = 1
		else:
			#Different fingers type these keys. Base off row of j
			if keys[j].row == 1:
				#Top Row
				keyDistances[i][j] = 1
			elif keys[j].row == 3:
				#Bot Row
				keyDistances[i][j] = 1
			else:
				#Home Row
				keyDistances[i][j] = 0
