

keys = []
for i in range(10)
	keys[i] = 10
for i in range(10, 19)
	keys[i] = 20
for i in range(19, 26)
	keys[i] = 30

keys[0] += 1 #q
keys[10] += 1 #a
keys[19] += 1 #z

keys[1] += 2 #w
keys[11] += 2 #s
keys[20] += 2 #x

keys[2] += 3 #e
keys[12] += 3 #d
keys[21] += 3 #c

keys[3] += 4 #r
keys[13] += 4 #f
keys[22] += 4 #v

keys[4] += 4 #t
keys[14] += 4 #g
keys[23] += 4 #b

keys[5] += 5 #y
keys[15] += 5 #h
keys[24] += 5 #n

keys[6] += 5 #u
keys[16] += 5 #j
keys[25] += 5 #m

keys[7] += 6 #i
keys[17] += 6 #

keys[8] += 7 #o
keys[18] += 7 #l

keys[9] += 8 #p

keyDistances = [][]

for i in range(26)

	fingerI = keys[i] % 10
	rowI = (keys[i] - fingerI) / 10

	for j in range(26)

		fingerJ = keys[j] % 10
		rowJ = (keys[j] - fingerJ) / 10

		if i == j
			#Same Key
			keyDistances[i][j] = 0 
		elif fingerI == fingerJ
			#Same finger used to type these keys
			if (rowI == 1 and rowJ == 3) or (rowI == 3 and rowJ == 1)
				keyDistances[i][j] = 2
			else 
				keyDistances[i][j] = 1
		else
			#Different fingers type these keys. Base off row of j
			if rowJ == 1
				#Top Row
				keyDistances[i][j] = 1
			elif rowJ == 3
				#Bot Row
				keyDistances[i][j] = 1
			else
				#Home Row
				keyDistances[i][j] = 0
 

			

