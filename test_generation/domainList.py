from domain import *
class DomainList:
    def __init__(self):
        self.domain = [Domain(),Domain(),Domain()]
    def getDomain(self,i):
        return self.domain[i]
    
    def setValues(self,pair):     
        string = pair.split('[')
        pos = int(string[0])
        x = pair.index(';')
        left = pair[pair.index('[')+1 : x]
        right = pair[x+1 : (pair.index(']'))]
        
        if pos == 1:
            self.domain[0].setValue(left,right)
        if pos == 2:
            self.domain[1].setValue(left,right)
        if pos == 3:
            self.domain[2].setValue(left,right)
    def sortDomainList(self):
        if self.domain[0].checkDomain()== 1:
            for i in range(len(self.domain)):
                for j in range(i+1, len(self.domain)):
                    if self.domain[i].getValueLeft() > self.domain[j].getValueLeft():
                        temp1 = self.domain[i].getValueLeft()
                        temp2 = self.domain[i].getValueRight()

                        self.domain[i].setLeft(self.domain[j].getValueLeft())
                        self.domain[i].setRight(self.domain[j].getValueRight())

                        self.domain[j].setLeft(temp1)
                        self.domain[j].setRight(temp2)
            return 1
        else :
            return 0
    def checkDomainList(self):
        if self.sortDomainList() == 1:
            for i in range(len(self.domain) - 1):
                if self.domain[i+1].getValueLeft() != None:
                    if self.domain[i].getValueRight() < self.domain[i+1].getValueLeft():
                        continue
                    else :
                        return 0
            return 1
    def printList(self):
        for i in range (len(self.domain)):
            print '['+str(self.domain[i].getValueLeft())+','+str(self.domain[i].getValueRight())+']'
        print 'end'
            
                        
