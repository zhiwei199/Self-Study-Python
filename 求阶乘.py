"""
求阶乘
"""
def func2(n):
    if n == 1:
        result = 1
    else:
        result = (n * func2(n-1))
    return result

n = int(input("Input your number:"))
print("The result is :%d"%func2(n))
