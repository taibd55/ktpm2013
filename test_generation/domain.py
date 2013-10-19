class Domain:
    def __init__(self,l=None,r=None):
        self.left = None
        self.right = None
    def setValue(self,l,r):
        self.left = int(l)
        self.right = int(r)
    def setLeft(self,l):
        self.left = l
    def setRight(self,r):
        self.right = r
    def getValueLeft(self):
        return self.left
    def getValueRight(self):
        return self.right
    def checkDomain(self):
        if self.left != None and self.right != None:
            return 1
        else :
            return 0
