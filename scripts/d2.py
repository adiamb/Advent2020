from collections import defaultdict
inputD2 = 'inputs/d2_p1.input'
valid = 0
valid2 = 0
with open(inputD2) as inFile:
	for line in inFile:
		min_, max_, alph, pwd= line.strip().replace(':', '').replace('-', ' ').split(' ')
		getIndAlpha1 = pwd[int(min_)-1]
		getIndAlpha2 = pwd[int(max_)-1]
		strDict = defaultdict(int)
		for i in pwd:
			strDict[i]+=1
		if alph in strDict:
			getOcc = strDict.get(alph)
			if getOcc >= int(min_) and getOcc <= int(max_):
				valid += 1
		if getIndAlpha1 == alph and getIndAlpha2 != alph:
			valid2 += 1
		elif getIndAlpha1 != alph and getIndAlpha2 == alph:
			valid2 += 1
			#print(getIndAlpha1, getIndAlpha2, min_, max_, pwd)


print('PART1 >>> the number of valid passwds {}'.format(valid))
print('PART2 >>> the number of valid passwds {}'.format(valid2))



