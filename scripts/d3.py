from collections import defaultdict, Counter
inputFile='inputs/d3_p1.input'

def parseCoords(inputFile):
    mapDict =defaultdict(str)
    y =0
    with open(inputFile) as inFile:
        for line in inFile:
            y += 1
            x =0
            for coord in line.strip():
                x +=1
                mapDict[(x, y)] = coord
    return x, y, mapDict

def parseMap(mapDict, xIncre, yIncre, x, y):
    x_ =1
    y_ =1
    treeCounter = 0
    while y_ <= y:
        print(x_, y_)
        x_+= xIncre
        y_ += yIncre
        if x_ > x:
            x_ =  abs(x-x_)
        getItem = mapDict.get((x_, y_))
        if getItem == '#':
            treeCounter += 1
    return treeCounter

x, y, mapDict = parseCoords(inputFile)
part1=parseMap(mapDict, x=x, y=y,xIncre=3, yIncre=1)

## part 2
params=[(1, 1),(3, 1), (5, 1), (7, 1), (1, 2)]
treeMapper = 1
for xIncre, yIncre in params:
    print(xIncre, yIncre)
    treeMapper *= parseMap(mapDict, x=x, y=y,xIncre=xIncre, yIncre=yIncre)

print('The answer to part 1 is {}'.format(part1))
print('The answer to part 2 is {}'.format(treeMapper))