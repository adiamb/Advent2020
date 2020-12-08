import re
from collections import defaultdict

def parseInput(inputFile):
    #inputFile = 'inputs/d7_p1.input'
    masterBagDict = defaultdict(list)
    with open(inputFile) as inFile:
        for line in inFile:
            lineParse = line.strip().split('contain')
            parent = re.sub('bags|bag', '', lineParse[0]).strip()
            childBags=re.sub('bags|bag', '', lineParse[1]).strip('.')
            for bag in childBags.split(','):
                if 'no other' in bag.strip():
                    numBag =0
                else:
                    numBag = int(re.findall('[0-9]',bag )[0])
                typeBag = re.sub('[0-9]','', bag).strip()
                if 'no other' not in typeBag:
                    masterBagDict[typeBag].append(parent)
    return masterBagDict


def recurseDict2(BagDict, keyList, keyCheck, traversal):
    print(len(keyList), keyCheck)
    if len(keyList)==0:
        return traversal
    else:
        keyCheck = keyList.pop(0)
        if keyCheck in BagDict:
            keyList.extend(BagDict.get(keyCheck))
            traversal.update(keyList)
        return(recurseDict2(BagDict, keyList, keyCheck, traversal))


def main():
    inputFile = 'inputs/d7_p1.input'
    masterBagDict = parseInput(inputFile)
    uniqClrs=recurseDict2(BagDict=masterBagDict, keyList=['shiny gold'], keyCheck='', traversal=set())
    print('Answer to part 1 is {}'.format(len(uniqClrs)))

if __name__ == "__main__":main()


# print(
# masterBagDict.get('shiny gold'),
# masterBagDict.get('faded orange'),
# masterBagDict.get('muted chartreuse'),
# masterBagDict.get('pale turquoise'),
# masterBagDict.get('dull brown'))