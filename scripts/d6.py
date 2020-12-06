from collections import defaultdict, Counter

def yesCount(inputFile):
    QDict=defaultdict(lambda:defaultdict(int))
    groupC = 0
    groupCounter =Counter()
    for line in open(inputFile):
        line=line.strip()
        if not line:
            groupC += 1
        else:
            groupCounter[groupC] += 1
            for a in list(line):
                QDict[groupC][a] += 1
    YesCounter =sum([len(j) for i,j in QDict.items()])
    print('Answer to part 1 is {}'.format(YesCounter))
    return QDict, groupCounter

def commonYesCount(QDict, groupCounter):
    YesGroupCount = 0 
    for k1, v1 in QDict.items():
        groupNo = groupCounter.get(k1)
        for k2, v2 in v1.items():
            if v2 == groupNo:
                YesGroupCount += 1
    print('Answer to part 2 is {}'.format(YesGroupCount))

def main():
    inputFile = 'inputs/d6_p1.input'
    QDict, groupCounter = yesCount(inputFile)
    commonYesCount(QDict, groupCounter)

if __name__ == "__main__":main()
