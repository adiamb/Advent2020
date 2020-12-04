from collections import defaultdict, Counter
import re

def parseBatch(inputFile):
    pNo = 1
    passDict=defaultdict(lambda:defaultdict(str))
    with open(inputFile) as inFile:
        for line in inFile:
            if not line.strip():
                pNo += 1
            else:
                lineParse = line.strip().split(' ')
                for item in lineParse:
                    key, val=item.split(':')
                    passDict[pNo][key] = val
    return passDict

class passport(object):
    """
    passport object
    """
    def __init__(self, object):
        self.byr=int(object.get('byr'))
        self.iyr=int(object.get('iyr'))
        self.eyr=int(object.get('eyr'))
        self.hgt = object.get('hgt')
        self.ecl = object.get('ecl')
        self.hcl = object.get('hcl')
        self.pid = object.get('pid')
    
    def yearCheck(self):
        """
        year checks 
        """
        yearParam =[1920, 2002, 2010, 2020, 2020, 2030]
        byrSt, byrEnd, iyrSt, iyrEnd, eyrSt, eyrEnd = yearParam
        if self.byr >=byrSt and self.byr <=byrEnd and self.iyr >= iyrSt and self.iyr <= iyrEnd and self.eyr >= eyrSt and self.eyr <= eyrEnd:
            return True
        else:
            return False
    
    def passIdCheck(self):
        """Passport ID check
        """
        if self.pid.isdigit() and len(self.pid) == 9 and self.pid[:2] == '00':
            return True
        else:
            return False
    
    def hgtCheck(self):
        cmParams = [150, 193]
        inParams = [59, 76]
        if re.search('cm', self.hgt):
            hgt=int(re.sub('cm', '', self.hgt))
            if hgt >= cmParams[0] and hgt <= cmParams[1]:
                return True
        elif re.search('in', self.hgt):
            hgt = int(re.sub('in', '', self.hgt))
            if hgt >= inParams[0] and hgt <= inParams[1]:
                return True
        else:
            return False

    def eclCheck(self):
        params = ['amb', 'blu', 'brn' ,'gry', 'grn', 'hzl', 'oth']
        if self.ecl in params:
            return True
        else:
            return False

    def hclCheck(self):
        if self.hcl[0] == '#':
            totalLen = len(self.hcl)-1
            intChar = re.findall('[0-9]', self.hcl)
            alhChar = re.findall('[a-f]', self.hcl)
            if len(intChar) == totalLen:
                return True
            elif len(alhChar) == totalLen:
                return True
            elif len(intChar) + len(alhChar) == totalLen:
                return True
            else:
                return False
        else:
            return False
    
    def checkAll(self):
        boolCheck =[self.yearCheck(), 
        self.passIdCheck(),
        self.hgtCheck(),
        self.eclCheck(),
        self.hclCheck()]
        if all(boolCheck):
            return True
        else:
            return False

passDict = parseBatch(inputFile = 'inputs/d4_p1.input')

valid = 0
validCounter = Counter()
for k1, v1 in passDict.items():
    validCounter[len(v1)] += 1
    #for k2, v2 in  v1.items():
    if len(v1) >= 7:
        if 'cid' not in v1:
            validCounter['cid'] += 1
            passInst=passport(v1)
            if passInst.checkAll() == True:
                validCounter['valid'] += 1




print('The answerr to part 1 is {}'.format(validCounter.get(8)+validCounter.get('cid')))



#d=passport(passDict.get(1))
#d.yearCheck(yearParam =[1920, 2002, 2010, 2020, 2020, 2030])

