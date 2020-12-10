

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

def main():
    inputFile = 'inputs/d8_p1.input'
    consol=[]
    for line in open(inputFile):
        op=(line.strip().split(' ')[0], int(line.strip().split(' ')[1]))
        consol.append(op)
    a=console(consol)
    seenPoints = set()
    while a.pointer < len(consol):
        if a.pointer in seenPoints:
            break
        seenPoints.add(a.pointer)
        op, n = a.Instructions[a.pointer]
        #print('op-{} n-{} pointer-{} acc-{}'.format(op, n, a.pointer, a.acc))
        if op == 'jmp':
            a.pointer=a.jmpOP()
        elif op== 'acc':
            a.pointer = a.accOP()
        else:
            a.pointer = a.nOP()
    print('The Answer to part1 is {}'.format(a.acc))

if __name__ == "__main__":main()
    



    

