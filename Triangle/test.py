import unittest
import math
import decimal
from test import *

class TriangleTest(unittest.TestCase):
#kiem tra xem 3 canh co la 1 tam giac
    def testTriangle1(self):
        self.assertEqual(detect_triangle("1",2.0,3.0),"input khong hop le")
    def testTriangle2(self):
        self.assertEqual(detect_triangle(1.0,"2",3.0),"input khong hop le")
    def testTriangle3(self):
        self.assertEqual(detect_triangle(1.0,2.0,"3"),"input khong hop le")
    def testTriangle4(self):
        self.assertEqual(detect_triangle("1.0","2.0",3),"input khong hop le")
    def testTriangle5(self):
        self.assertEqual(detect_triangle("1.0",2.0,"3"),"input khong hop le")
    def testTriangle6(self):
        self.assertEqual(detect_triangle(1.0,"2.0","3"),"input khong hop le")
    def testTriangle7(self):
        self.assertEqual(detect_triangle("1.0","2.0","3"),"input khong hop le")
    def testTriangle8(self):
        self.assertEqual(detect_triangle(-1.0,2.0,3.0),"input khong hop le")
    def testTriangle9(self):
        self.assertEqual(detect_triangle(1.0,-2.0,3.0),"input khong hop le")
    def testTriangle10(self):
        self.assertEqual(detect_triangle(1.0,2.0,-3.0),"input khong hop le")
    def testTriangle11(self):
        self.assertEqual(detect_triangle(-1.0,-2.0,3.0),"input khong hop le")
    def testTriangle12(self):
        self.assertEqual(detect_triangle(1.0,-2.0,-3.0),"input khong hop le")
    def testTriangle13(self):
        self.assertEqual(detect_triangle(-1.0,2.0,-3.0),"input khong hop le")
    def testTriangle14(self):
        self.assertEqual(detect_triangle(1.0,2.0,3.0),"input khong hop le")
    def testTriangle15(self):
        self.assertEqual(detect_triangle(4.0,2.0,3.0),"tam giac binh thuong")
    def testTriangle16(self):
        self.assertEqual(detect_triangle(2,2.0,3.0),"input khong hop le")
    def testTriangle17(self):
        self.assertEqual(detect_triangle(2.0,2,3.0),"input khong hop le")
    def testTriangle18(self):
        self.assertEqual(detect_triangle(2.0,2.0,3),"input khong hop le")
#kiem tra 3 canh co la tam giac can..
    def testTGCan1(self):
        self.assertEqual(detect_triangle(2.0,2.0,3.0),"tam giac can")
    def testTGCan2(self):
        self.assertEqual(detect_triangle(3.0,2.0,2.0),"tam giac can")
    def testTGCan3(self):
        self.assertEqual(detect_triangle(2.0,3.0,2.0),"tam giac can")
    def testTGCan4(self):
        self.assertEqual(detect_triangle(2.0**32-1,2.0**32-1,3.0),"tam giac can")
#kiem tra tam giac vuong:
    def testTGVuong1(self):
        self.assertEqual(detect_triangle(3.0,4.0,5.0),"tam giac vuong")
#kiem tra tam giac vuong can:
    def testTGVuongCan1(self):
        self.assertEqual(detect_triangle(2.0,2.0,math.sqrt(8.0)),"tam giac vuong can")
#kiem tra tam giac deu:
    def testTGDeu1(self):
        self.assertEqual(detect_triangle(3.0,3.0,3.0),"tam giac deu")
if __name__ == '__main__':
    unittest.main()
