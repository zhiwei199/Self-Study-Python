"""
该程序为判断用户输入字符串是否具有“回文”性质，即字符串前后部分完全对称
"""
def backstr(str):
     for i in range(len(str) // 2):
          if str[i] == str[-i-1]:
               return True
          else:
               return False
     return True

str = str(input("请输入字符串:"))
if backstr(str):
     print("该字符串是回文字符")
else:
     print("该字符串不是回文字符串")
     
     

