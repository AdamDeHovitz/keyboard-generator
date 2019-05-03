from namedlist import namedlist

Key = namedlist('Key', ['row', 'finger'])
keys = [Key(0, 0) for i in range(26)]
for i in range(10):
	keys[i].row = 1
for i in range(10, 19):
	keys[i].row = 2
for i in range(19, 26):
	keys[i].row = 3
keys[0].finger = 1  #QWERTY q
keys[10].finger = 1 #a
keys[19].finger = 1 #z

keys[1].finger = 2  #w
keys[11].finger = 2 #s
keys[20].finger = 2 #x

keys[2].finger = 3 	#e
keys[12].finger = 3 #d
keys[21].finger = 3 #c

keys[3].finger = 4 	#r
keys[13].finger = 4 #f
keys[22].finger = 4 #v

keys[4].finger = 4 	#t
keys[14].finger = 4 #g
keys[23].finger = 4 #b

keys[5].finger = 5 	#y
keys[15].finger = 5 #h
keys[24].finger = 5 #n

keys[6].finger = 5 	#u
keys[16].finger = 5 #j
keys[25].finger = 5 #m

keys[7].finger = 6 	#i
keys[17].finger = 6 #k

keys[8].finger = 7 	#o
keys[18].finger = 7 #l

keys[9].finger = 8 	#p

def key_distances(num):
	keyDistances = [[] for _ in range(26)]
	if num == 0:
		for i in range(26):
			for j in range(26):
				keyDistances[i].append(0)
				if i == j:
					# Same Key
					keyDistances[i][j] = 1
				elif keys[i].finger == keys[j].finger:
					# Same finger used to type these keys
					if (keys[i].row == 1 and keys[j].row == 3) or (keys[i].row == 3 and keys[j].row == 1):
						keyDistances[i][j] = 2
					else:
						keyDistances[i][j] = 1
				else:
					# Different fingers type these keys. Base off row of j
					if keys[j].row == 1:
						# Top Row
						keyDistances[i][j] = 1
					elif keys[j].row == 3:
						# Bot Row
						keyDistances[i][j] = 1
					else:
						# Home Row
						keyDistances[i][j] = 0
	elif num == 1:
		for i in range(26):
			for j in range(26):
				keyDistances[i].append(0)
				if (keys[i].finger <=4 and keys[j].finger > 4) or (keys[j].finger <=4 and keys[i].finger > 4):
					#different hands
					keyDistances[i][j] = 1
				else:
					if keys[i].finger == keys[j].finger:
						#same finger
						keyDistances[i][j] = 6 + abs(keys[i].row - keys[j].row)
					else:
						keyDistances[i][j] = 4 + abs(keys[i].row - keys[j].row)
				finger_penalty = 0
				row_penalty = 0
				if keys[j].finger == 1 or keys[j].finger == 8:
					#pinky
					finger_penalty = 2
				elif keys[j].finger == 2 or keys[j].finger == 7:
					# ring
					finger_penalty = 1.6
				elif keys[j].finger == 3 or keys[j].finger == 6:
					# middle
					finger_penalty = 1.5
				elif keys[j].finger == 4 or keys[j].finger == 5:
					#pointer
					finger_penalty = 1.1

				if keys[j].row == 1:
					#top
					row_penalty = 1.5
				elif keys[j].row == 2:
					#home
					row_penalty = 1
				elif keys[j].row == 3:
					#bottom
					row_penalty = 1.8
				keyDistances[i][j] = keyDistances[i][j] * finger_penalty * row_penalty

	return keyDistances
