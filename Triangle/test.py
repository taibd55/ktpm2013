#kiem tra kieu float...
def checkType(x):
    if isinstance(x,float) == 1 :
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
            return "la tam giac"
        else :
            return "khong la tam giac"
    else :
        return "khong la tam giac"

#kiem tra 3 canh co la tam giac can khong
def checkTGCan(x,y,z):
    if checkTriangle(x,y,z) == "la tam giac" :
        if (x==y) | (y==z) | (z==x):
            return "la tam giac can"
        else :
            return "khong la tam giac can"
    else :
        return "khong la tam giac can"
    
#kiem tra 3 canh co la tam giac vuong khong
def checkTGVuong(x,y,z):
    if checkTriangle(x,y,z) == "la tam giac" :
        if (((x**2 + y**2)- z**2)<= 0.00003 ) | (((y**2+z**2)-x**2)<=0.00003) | (((z**2+x**2)-y**2)<=0.00003):
            return "la tam giac vuong"
        else :
            return "khong la tam giac vuong"
    else :
        return "khong la tam giac vuong"

#kiem tra 3 canh co la tam giac vuong can
def checkTGVuongCan(x,y,z):
    if checkTriangle(x,y,z) == "la tam giac" :
        if (((x**2 + y**2) - z**2) <= 0.00003) & (x==y):
            return "la tam giac vuong can"
        if (((y**2+z**2) - x**2) <= 0.00003) & (y==z):
            return "la tam giac vuong can"
        if (((z**2+x**2) - y**2) <= 0.00003) & (z==x):
            return "la tam giac vuong can"
    else :
        return "khong la tam giac vuong can"
    return "khong la tam giac vuong can"

#kiem tra 3 canh co la tam giac deu
def checkTGDeu(x,y,z):
    if checkTriangle(x,y,z) == "la tam giac" :
        if x==y==z:
            return "la tam giac deu"
        else :
            return "khong la tam giac deu"
    else :
        return "khong la tam giac deu"

