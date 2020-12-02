## Part 1
d1Input = [int(i.strip()) for i in open('inputs/d1_p1.input')]
for j in d1Input:
    checkNum = 2020-j
    if checkNum in d1Input:
        print('The answer is {}'.format(j*checkNum))
        break
## Part2
