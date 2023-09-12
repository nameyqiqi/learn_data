#for - in 循环
#一 .语法
'''
for 变量 in 容器：
    代码块
容器中有多少个元素
'''
'''
total =1
for i in range(1,101):
    total += i*total
    print(total)
'''

x = int(input('max:'))
for t in range(1,x):
    gw = t % 10
    sw = t // 10 % 10
    bw = t // 100
    if gw**3+sw**3+bw**3 == t:
        print("yes",t)



