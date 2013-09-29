import math
import decimal
#kiem tra kieu float...
def checkType(x):
    if type(x) in [int,float,long]:
        return 1
    else: 
        return 0
    
#kiem tra pham vi mien gia tri cua so
def checkLength(y):
    if checkType(y) == 1:
        if (y > 0.0) & (y <= (2.0**32-1)):
            return 1
    else :
        return 0

#kiem tra 3 canh co la mot tam giac
def checkTriangle(x,y,z):
    if (checkLength(x) == 1) & (checkLength(y) == 1) & (checkLength(z) == 1) :
        if ( (x+y) > z) & ( (y+z) > x) & ( (z+x) > y):
            return 1
        else :
            return 0
    else :
        return 0

#kiem tra 3 canh co la tam giac can khong
def checkTGCan(x,y,z):
    if checkTriangle(x,y,z) == 1 :
        if (x==y) | (y==z) | (z==x):
            return 1
        else :
            return 0
    else :
        return 0
    
#kiem tra 3 canh co la tam giac vuong khong
def checkTGVuong(x,y,z):
    if checkTriangle(x,y,z) == 1 :
        if (math.fabs((x**2+y**2)-z**2)<=(1e-10) )|(math.fabs((y**2+z**2)-x**2)<=(1e-10)) | (math.fabs((z**2+x**2)-y**2)<=(1e-10)):
            return 1
        else :
            return 0
    else :
        return 0

#kiem tra 3 canh co la tam giac vuong can
def checkTGVuongCan(x,y,z):
    if checkTriangle(x,y,z) == 1 :
        if ( math.fabs( (x**2 + y**2) - z**2) <= (1e-10)) & (x==y):
            return 1
        if ( math.fabs( (y**2+z**2) - x**2) <= (1e-10)) & (y==z):
            return 1
        if ( math.fabs( (z**2+x**2) - y**2) <= (1e-10)) & (z==x):
            return 1
    else :
        return 0

#kiem tra 3 canh co la tam giac deu
def checkTGDeu(x,y,z):
    if checkTriangle(x,y,z) == 1 :
        if x==y==z:
            return 1
        else :
            return 0
    else :
        return 0

#kiem tra tong quan:
def detect_triangle(a,b,c):
    if checkTriangle(a,b,c) == 0 :
        return "input khong hop le"
    else :
        if checkTGDeu(a,b,c) == 1:
            return "tam giac deu"
        else :
            if checkTGVuongCan(a,b,c) ==1:
                return "tam giac vuong can"
            else :
                if checkTGCan(a,b,c) == 1:
                    return "tam giac can"
                else :
                    if checkTGVuong(a,b,c) == 1:
                        return "tam giac vuong"
                    else :
                        return "tam giac binh thuong"
    
