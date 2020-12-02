## Part 1
d1Input = [int(i.strip()) for i in open('inputs/d1_p1.input')]
for j in d1Input:
    checkNum = 2020-j
    if checkNum in d1Input:
        print('The answer to part1 is {}'.format(j*checkNum))
    for i in d1Input: ## Part2
        checkNum2 = 2020-(j+i)
        if checkNum2 in d1Input:
            print('The answer to part2 is {}'.format(j*checkNum2*i))
            break
    

