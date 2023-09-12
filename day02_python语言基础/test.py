# 1. 小明拿了30块钱去买菜，花了20，问还剩多少。
m=30
m-=20
print(m)
# 2. 任意给定三个边，判断能否组成三角形。
list =[]
a0=input("input bc1")
a1=input("input bc2")
a2=input("input bc3")
list.append(a0)
list.append(a1)
list.append(a2)
print(list)
if a0+a1 > a2 and a0+a2 > a1 and a1+a2 > a0 :
    print("yes")
else:
    print("no")
# 3. 给定一个半径，计算圆的面积和周长。
r=float(input('day01笔记:'))
s=3.14**r
c=3.14*2*r
print(s,c)