import math

def settle(a,b,c):
    d = b**2 - 4*a*c
    if a==0:
        print("DataError!")
    else :
        if d<0:
            print("DataError!")
        elif d >0:
            x1 = (-b+math.sqrt(d)) / (2*a)
            x2 = (-b-math.sqrt(d)) / (2*a)
        elif d==0:
            x1 = (-b) / (2*a)
            x2 = x1
        print("根一为%.2f"%x1,"根二为%.2f"%x2)

while True:
    a = float(input("请输入二次项系数："))
    b = float(input("请输入一次项系数："))
    c = float(input("请输入常数项系数："))
    print(settle(a,b,c))
