
from collections import Counter
def checkAdapter(arr):
    '''adapted from https://github.com/fogleman/AdventOfCode2020/blob/main/10.py'''
    valCounter = Counter()
    for i, j in zip(arr, arr[1:]):
        valCounter[j-i] +=1
    return valCounter


def adapterWay(arr, n, memo):
    '''from https://github.com/fogleman/AdventOfCode2020/blob/main/10.py'''
    print(n, memo)
    if n ==0:
        return 1
    if n in memo:
        return memo[n]
    if n not in arr:
        return 0
    memo[n] = sum((adapterWay(arr, n-i, memo)) for i in range(1, 4))
    return memo[n]

def main():
    inputFile = 'inputs/d10_p1.input'
    arr=[int(i.strip()) for i in open(inputFile)]
    arr.extend([0, max(arr)+3])
    arr.sort()
    a=checkAdapter(arr)
    p1=a.get(1)*a.get(3)
    memo ={}
    p2 = adapterWay(arr, arr[-1], memo)
    print('The Answer to part1 is {}'.format(p1))
    print('The Answer to part2 is {}'.format(p2))

if __name__ == "__main__":main()
