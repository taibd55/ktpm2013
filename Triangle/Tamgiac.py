import unittest
import math
from test import *

class TriangleTest(unittest.TestCase):
#kiem tra xem 3 canh co la 1 tam giac
    def testTriangle1(self):
        self.assertEqual(checkTriangle("1",2.0,3.0),"khong la tam giac")
    def testTriangle2(self):
        self.assertEqual(checkTriangle(1.0,"2",3.0),"khong la tam giac")
    def testTriangle3(self):
        self.assertEqual(checkTriangle(1.0,2.0,"3"),"khong la tam giac")
    def testTriangle4(self):
        self.assertEqual(checkTriangle("1.0","2.0",3),"khong la tam giac")
    def testTriangle5(self):
        self.assertEqual(checkTriangle("1.0",2.0,"3"),"khong la tam giac")
    def testTriangle6(self):
        self.assertEqual(checkTriangle(1.0,"2.0","3"),"khong la tam giac")
    def testTriangle7(self):
        self.assertEqual(checkTriangle("1.0","2.0","3"),"khong la tam giac")
    def testTriangle8(self):
        self.assertEqual(checkTriangle(-1.0,2.0,3.0),"khong la tam giac")
    def testTriangle9(self):
        self.assertEqual(checkTriangle(1.0,-2.0,3.0),"khong la tam giac")
    def testTriangle10(self):
        self.assertEqual(checkTriangle(1.0,2.0,-3.0),"khong la tam giac")
    def testTriangle11(self):
        self.assertEqual(checkTriangle(-1.0,-2.0,3.0),"khong la tam giac")
    def testTriangle12(self):
        self.assertEqual(checkTriangle(1.0,-2.0,-3.0),"khong la tam giac")
    def testTriangle13(self):
        self.assertEqual(checkTriangle(-1.0,2.0,-3.0),"khong la tam giac")
    def testTriangle14(self):
        self.assertEqual(checkTriangle(1.0,2.0,3.0),"khong la tam giac")
    def testTriangle15(self):
        self.assertEqual(checkTriangle(2.0,2.0,3.0),"la tam giac")
    def testTriangle16(self):
        self.assertEqual(checkTriangle(2.0,2.0,3.0),"la tam giac")
    def testTriangle17(self):
        self.assertEqual(checkTriangle(2,2.0,3.0),"khong la tam giac")
    def testTriangle18(self):
        self.assertEqual(checkTriangle(2.0,2,3.0),"khong la tam giac")
    def testTriangle19(self):
        self.assertEqual(checkTriangle(2.0,2.0,3),"khong la tam giac")
#kiem tra 3 canh co la tam giac can..
    def testTGCan1(self):
        self.assertEqual(checkTGCan(2.0,2.0,3.0),"la tam giac can")
    def testTGCan2(self):
        self.assertEqual(checkTGCan(4.0,2.0,3.0),"khong la tam giac can")
    def testTGCan3(self):
        self.assertEqual(checkTGCan(4.0,5.0,3.0),"khong la tam giac can")
    def testTGCan4(self):
        self.assertEqual(checkTGCan(3.0,3.0,3.0),"la tam giac can")
    def testTGCan4(self):
        self.assertEqual(checkTGCan(2.0**32-1,2.0**32-1,3.0),"la tam giac can")
#kiem tra tam giac vuong:
    def testTGVuong1(self):
        self.assertEqual(checkTGVuong(3.0,4.0,5.0),"la tam giac vuong")
    def testTGVuong2(self):
        self.assertEqual(checkTGVuong(4.0,4.0,5.0),"khong la tam giac vuong")
    def testTGVuong3(self):
        self.assertEqual(checkTGVuong(2.0,2.0,math.sqrt(8)),"la tam giac vuong")
#kiem tra tam giac vuong can:
    def testTGVuongCan1(self):
        self.assertEqual(checkTGVuongCan(3.0,4.0,5.0),"khong la tam giac vuong can")
    def testTGVuongCan2(self):
        self.assertEqual(checkTGVuongCan(2.0,2.0,math.sqrt(8.0)),"la tam giac vuong can")
    def testTGVuongCan3(self):
        self.assertEqual(checkTGVuongCan(2.0,(2.0**32-1),(2.0**32-1)),"khong la tam giac vuong can")
#kiem tra tam giac deu:
    def testTGDeu1(self):
        self.assertEqual(checkTGDeu(3.0,3.0,3.0),"la tam giac deu")
    def testTGCan2(self):
        self.assertEqual(checkTGDeu(3.0,4.0,5.0),"khong la tam giac deu")
if __name__ == '__main__':
    unittest.main()
