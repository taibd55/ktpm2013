import sys
import itertools
import unittest
from input import *
from domainList import *
f = open('input.py','r')
class TestSequense(unittest.TestCase):
    pass
def test_generator(a, b):
    def test(self):
        self.assertEqual(main(*a),b)
    return test
if __name__ == '__main__':
    for line in f:
        if 'main' in line:#find main function
            x = line.index('(')#find value domain
            y = line.index(')')
            substring = line[x+1:y]
            #get number of parameters
            li = substring.split(',')
            length = len(li)#number of parameters
            domainList = [DomainList() for i in range(length)] 
            i = 0
            for keyline in f:
                if i < length+1 : #get values of parameters
                    if i != 0:#ignore '''
                        #print keyline
                        pairs = keyline.split('[')
                        pos = 0
                        for temp in pairs:#max 3
                            if pos > 0:
                                pair = str(pos)+'['+temp
                                domainList[i-1].setValues(pair)
                            pos=pos+1
                    i = i+1
            check = 0
            for k in range(len(domainList)):
                if domainList[k].checkDomainList() != 1:#input wrong
                    check = 1
            if check == 0:
                a = []
                lis = []
                for k in range (len(domainList)):
                    for j in range(3):
                        if domainList[k].getDomain(j-1).checkDomain()== 1:
                            a.append(domainList[k].getDomain(j-1).getValueLeft())
                    lis.append(a)
                    a = []
                for k in range(len(list(itertools.product(*lis)) )):
                    test_name = 'test_%s' % str (list(itertools.product(*lis))[k])
                    #print list(itertools.product(*lis))[k]
                    test = test_generator(list(itertools.product(*lis))[k], test_name)
                    setattr(TestSequense, test_name, test)
                unittest.main()
            else :
                raise Exception("wrong input")
f.close()
