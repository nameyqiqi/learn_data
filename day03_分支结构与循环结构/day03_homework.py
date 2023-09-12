#1.根据输⼊的成绩，判断是否及格，成绩范围只允许在0~100之间，输⼊错误给提⽰。
while True:
    grade =float(input("输入成绩："))
    if grade<0 or grade>100:
        print('error')
        break
    if grade<60:
        print("bjg")
        break
    else:
       print('jg')
       break

#2.2.根据输⼊的年纪范围打印 成年 或者 未成年 ，如果年龄不在正常范围内(0~150)打印不是人
age = int(input('输入年龄'))
while True:
    if age<0 or age>150:
        print('不是人')
        break
    if age<18:
        print('未成年')
        break
    else:
        print('成年')
        break

#输⼊两个整数a和b，若a-b的结果为奇数，则输出该结果，否则输出提⽰信息a-b结果不是奇数
a = int(input('输入数1：'))
b = int(input('输入数2：'))
result = a - b
while result >0:
    print('a-b结果不是奇数')
    if result % 2 != 0:
        print(result)
    else:
        print('a-b结果不是奇数')
        break

#4.使⽤while循环输出 0~100内所有3的倍数。
for i in range(1,101):
    while i % 3 ==0:
        print(i)
        break

#统计100以内个位数是2并且能够被3整除的数的个数
for k in range(1,101):
    while k %10 ==2 and k % 3==0:
        print('k',k)
        break

#使⽤循环计算 1*2*3*4*...*10 的结果。
jg=1
for j in range(1,11):
    jg *=j
    if j ==10:
        print(jg)

#打印出所有的⽔仙花数,所谓⽔仙花数是指⼀个三位数，其各位数字⽴⽅和等于该
#数本⾝。例如:153是⼀个⽔仙花数,因为	等于 153。
for sxh in range(100,1000):
    gw = sxh % 10
    sw = sxh // 10 % 10
    bw = sxh // 100
    if gw ** 3 + sw ** 3 + bw ** 3 == sxh:
        print(sxh, '是水仙花数')

#输⼊任意⼀个正整数，求他是⼏位数？
zs = input('输入')
total=0
while True:
    if zs==0:
        break
    else:
        zs //10
        total+=1



#.输出9*9⼝诀。 程序分析：分⾏与列考虑，共9⾏9列，i控制⾏，j控制列。
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()

#这是经典的"百⻢百担"问题，有⼀百匹⻢，驮⼀百担货，⼤⻢驮3担，
# 中⻢驮2 担，两只⼩⻢驮1担，问有⼤，中，⼩⻢各⼏匹？（可以直接使⽤穷举法）
for a in range(1,100//3 + 1):
     for b in range(1,100//2):
         c = 100 - (a + b)
         if a + b + c ==100 and 3*a + 2*b + c/2 == 100:
             print(f'大马{a}匹，中马{b}匹，小马{c}匹。')

#2.判断指定的数是否是素数（素数就是质数，即除了1和它本⾝以外不能被其他的数整除的数）
a=int(input('输入数：'))
if a <= 1:
    print(f"{a}不是素数")
else:
    for i in (2, a + 1):
        if a % i == 0:
            break
    if i >= a:
        print(f"{a}是素数")
    else:
        print(f"{a}不是素数")



# 求斐波那契数列列中第n个数的值:1，1，2，3，5，8，13，21，34.	（这⼉的n
#可以是任意正整数，可以通过输⼊来确定）
n = int(input('请输入要一个整数：'))
n_2 = 0
n_1 = 1
current = 1
for x in range(2, n+1):
    current = n_2 + n_1
    n_2 = n_1
    n_1 = current
print('第%d个数是%d' % (n, current))
