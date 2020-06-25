"""
输出用户输入的英文字符串中大写字母和小写字母的个数
"""

def func1(str):
    result = [0, 0]
    for i in str:
        if i >= 'a' and i <= 'z':
            result[1] += 1
        elif i >= 'A' and i <= 'Z':
            result[0] += 1
    return result

str = input("Input your english string:")
print("result is :", func1(str))
