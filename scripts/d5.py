import math

def recRowCol(colArr, ncolrow, col):
    if len(colArr) != 0:
        curR = colArr.pop(0)
        if curR == 'L' or curR =="F":
            ncolrow = math.ceil(min(ncolrow)), math.floor(sum(ncolrow)/2)
        else:
            ncolrow = math.ceil(sum(ncolrow)/2), math.floor(max(ncolrow))
        return recRowCol(colArr, ncolrow=ncolrow,col=col)
    else:
        if col is True:
            return max(ncolrow)
        else:
            return min(ncolrow)

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
            rowId=recRowCol(rowArr, nrows, col=False)
            colId=recRowCol(colArr, ncols, col=True)
            seatArray.append(rowId*8+colId)
    min_, max_ = min(seatArray), max(seatArray)
    mySeat=next(i for i in range(min_, max_) if i not in seatArray )
    print('The answer to part1 is {}'.format(max_))
    print('The answer to part2 is {}'.format(mySeat))

if __name__ == "__main__":main()
