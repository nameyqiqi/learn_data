# 暴力破解 ’密码‘
# 1. 问题：密码由哪些符合组成
# 数字，字母，特殊符号(英文)

# 2. 假设密码是英文字母，数字组成
pwd=[]
for i in range(0,10):
    pwd.append(str(i))
for i in range(65,91):
    pwd.append(chr((i)))
    pwd.append(chr(i+32))
print(len(pwd),pwd)

#itertools --具有枚举功能的模块
#product 能实现具有重复元素的枚举方法
from itertools import product
for length in range(4,5):
    result=product(pwd,repeat=length)
    for i in result:
        pwd_result=''.join(i)
        print(pwd_result)




