from collections import defaultdict
inputD2 = 'inputs/d2_p1.input'
valid = 0
with open(inputD2) as inFile:
    for line in inFile:
       min_, max_, alph, pwd= line.strip().replace(':', '').replace('-', ' ').split(' ')
       strDict = defaultdict(int)
       for i in pwd:
           strDict[i]+=1
       if alph in strDict:
           getOcc = strDict.get(alph)
           if getOcc >= int(min_) and getOcc <= int(max_):
               valid += 1
print('the number of valid passwds {}'.format(valid))



