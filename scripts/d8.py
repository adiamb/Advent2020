

class console(object):
    """
    console object
    """
    def __init__(self, object):
        self.Instructions = object
        self.acc = 0
        self.pointer = 0
    
    def printCon(self):
        print(self.pointer, self.acc)

    def nOP(self):
        '''NO operation advance the op'''
        self.pointer += 1
        return self.pointer
    
    def accOP(self):
        acc=self.Instructions[self.pointer][1]
        self.acc += acc
        self.pointer += 1
        return self.pointer
    
    def jmpOP(self):
        op = self.Instructions[self.pointer][1]
        self.pointer += op
        return self.pointer


def runConsole(consol):
    a=console(consol)
    seenPoints = set()
    while a.pointer < len(consol):
        if a.pointer in seenPoints:
            return a.acc, False
        seenPoints.add(a.pointer)
        op, n = a.Instructions[a.pointer]
        #print('op-{} n-{} pointer-{} acc-{}'.format(op, n, a.pointer, a.acc))
        if op == 'jmp':
            a.pointer=a.jmpOP()
        elif op== 'acc':
            a.pointer = a.accOP()
        else:
            a.pointer = a.nOP()
    return a.acc, True

def swapIns(consol):
    opChDict = {'nop':'jmp', 'jmp':'nop'}
    for i in range(len(consol)):
        op, n = consol[i]
        if op in opChDict:
            p = list(consol)
            p[i] = (opChDict.get(op), n)
            #print(consol[i])
            acc, okay = runConsole(p)
            if okay:
                return acc
        

def main():
    inputFile = 'inputs/d8_p1.input'
    consol=[]
    for line in open(inputFile):
        op=(line.strip().split(' ')[0], int(line.strip().split(' ')[1]))
        consol.append(op)
    p1=runConsole(consol)[0]
    p2=swapIns(consol)
    print('The Answer to part1 is {}'.format(p1))
    print('The Answer to part2 is {}'.format(p2))


if __name__ == "__main__":main()
    



    

