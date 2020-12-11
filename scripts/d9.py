            
def sumSeek(arr, pointer, offset, lag):
    while pointer < len(arr)-lag:
        pr  = arr[pointer:offset+1]
        pointer += 1
        offset +=1
        query=pr.pop()
        querySet = set()
        for i in pr:
            if query-i in pr:
                querySet.add(True)
        if not querySet:
            return(query)

def rangeSeek(arr, p1):
    """bad complexity"""
    for i in range(0, len(arr)):
        for j in range(1, len(arr)-1):
            arrSub = arr[i:j]
            n=sum(arrSub)
            if n == p1:
                return sum([max(arrSub),min(arrSub)])
    
def main():
    inputFile = 'inputs/d9_p1.input'
    arr=[int(i.strip()) for i in open(inputFile)]
    p1=sumSeek(arr, pointer=0, offset=25, lag=25)
    p2=rangeSeek(arr, p1)
    print('The Answer to part1 is {}'.format(p1))
    print('The Answer to part2 is {}'.format(p2))

if __name__ == "__main__":main()
