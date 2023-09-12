#打印出所有的⽔仙花数,所谓⽔仙花数是指⼀个三位数，其各位数字⽴⽅和等于该
#数本⾝。例如:153是⼀个⽔仙花数,因为 1³ + 5³ + 3³ 等于 153。
for i in range(100, 1000):   #遍历100~999
    baiwei = i // 100        #取出百位数字
    shiwei = i // 10 % 10    #取出十位数字
    gewei = i % 10           #取出个位数字
if baiwei ** 3 + shiwei ** 3 + gewei ** 3 == i:  #判断是否满足水仙花数
    print(i)                 #打印满足的结果

#数字组合：有四个数字：1、2、3、4，能组成多少个互不相同且⽆重复数字的三
#位数？各是多少？
num_count = 0
for x in range(1, 5):   #遍历1~4
    for y in range(1, 5):
        for z in range(1, 5):
            if x != y and x != z and y != z: #判断 x,y,z是否相等
                print(f'{x}{y}{z}')          #打印结果
                num_count += 1               #统计满足个数
print(num_count)                             #打印统计结果

#输⼊任意⼀个正整数，求他是⼏位数？
num = True          #赋予num初值True
count = 0           #赋予count初值0
while True:
    if bool(num):   #判断布尔类型
        num //= 10  #对10取整
        count += 1  #统计能被10整除次数
    else:
        break
print(count)        #打印能被10整除次数的结果

#输出9*9⼝诀。 程序分析：分⾏与列考虑，共9⾏9列，i控制⾏，j控制列。
for i in range(1, 10):             #控制行数改变
    for j in range(1, i + 1):      #控制列数改变
        print(f'{i} * {j} = {i * j}', end='\t') #打印结果
print()                            #换行输出

#以上为注释作业


#. 随便给定⼀⽤户名，判断⽤户名是否合法（⽤户名⻓度6~10位）
x=input("⽤户名:")
if 6<=len(x)<=10:
    print(True)
else:
    print(False)

#随便给定⼀个字符串，统计字符串中⾮数字⾮字⺟的字符的个数
zfc=input('please input:')
zf=0
for i in zfc:
    if i.isalnum(): # if '0'<=i<='9' or 'A'<=i<='Z' or 'a'<=i<='z':
        zf+=1
ts=len(zfc)-zf
print(ts)


#随便给定⼀⽤户名，判断⽤户名是否合法（⽤户名中只能由数字和字⺟组成）
user=input('plese input user:')
if user.isalnum():
    print(True)
else:
    print(False)

#将wto转为WTO（⼤⼩写字⺟转换）
str =('wto')
print(str.upper()) #输出大写
print(str.lower()) #输出小写
print(str.title()) #首字母大写

'''
凯撒加密的实现，在密码学中，恺撒密码（英语：Caesar cipher），或称恺撒加
密、恺撒变换、变换加密，是⼀种最简单且最⼴为⼈知的加密技术。它是⼀种替
换加密的技术，铭⽂中的所有字⺟都在字⺟表上向后（或向前）按照⼀个固定数
⽬进⾏偏移后被替换成密⽂。例如，当偏移量是3的时候，所有的字⺟A将被替换
成D，B变成E，以此类推。这个加密⽅法是以罗⻢共和时期恺撒的名字命名的，
当年恺撒曾⽤此⽅法与其将军们进⾏联系。
'''
pwd = 'ABC'
for i in pwd:
    pwd=chr(ord(i) + 3)
    pwd.replace(i,chr(ord(i)+3))
    print(pwd,end='')
