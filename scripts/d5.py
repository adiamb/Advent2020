import math

def recRow(rowArr, nrows):
    if len(rowArr) != 0:
        curR = rowArr.pop(0)
        if curR == 'F':
            n2 = math.floor(sum(nrows)/2)
            n1 = math.ceil(min(nrows))
        else:
            n1 = math.ceil(sum(nrows)/2)
            n2 = math.floor(max(nrows))
        nrows =n1, n2
        return recRow(rowArr, nrows=nrows)
    else:
        return min(nrows)

def recCol(colArr, ncols):
    print(ncols)
    if len(colArr) != 0:
        curR = colArr.pop(0)
        if curR == 'L':
            n2 = math.floor(sum(ncols)/2)
            n1 = math.ceil(min(ncols))
        else:
            n1 = math.ceil(sum(ncols)/2)
            n2 = math.floor(max(ncols))
        ncols =n1, n2
        return recCol(colArr, ncols=ncols)
    else:
        return max(ncols)

def main():
    inputFile = 'inputs/d5_p1.input'
    seatArray=[]
    with open(inputFile) as inFile:
        for line in inFile:
            nrows = 0, 127
            ncols = 0, 7
            bHex = line.strip()
            rowArr=list(bHex[:7])
            colArr=list(bHex[7:])
            rowId=recRow(rowArr, nrows)
            colId=recCol(colArr, ncols)
            print(rowId, colId)
            seatArray.append(rowId*8+colId)
    min_, max_ = min(seatArray), max(seatArray)
    mySeat=next(i for i in range(min_, max_) if i not in seatArray )
    print('The answer to part1 is {}'.format(max_))
    print('The answer to part2 is {}'.format(mySeat))


if __name__ == "__main__":main()
# ncols = 0, 7
# colArr = list('RLL')
# recCol(colArr, ncols)