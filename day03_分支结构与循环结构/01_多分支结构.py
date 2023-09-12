"""
语法：
if 条件1:
    代码块1
elif 条件2:
    代码块2
elif 条件3:
    代码块3
......
else:
    代码块N
"""
# 案例：给定一个成绩，如果在90-100之间等级A，
# 80-90之间等级B，依次类推C、D、E。
score = 67
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('E')

# 练习：BMI问题，输出标准、偏胖、偏瘦。
w = 80
h = 1.8
BMI = w / h ** 2
if 18.5 <= BMI <= 23.9:
    print('标准')
elif BMI < 18.5:
    print('偏瘦')
# elif BMI > 23.9:
else:
    print('偏胖')

# 总结：
# 1. else分支可以忽略不写
# 2. 分支结构最终只会走其中一条分支


# 练习：有一种数字叫做水仙花数，水仙花数一定是一个3位数。
# 请判断153是不是水仙花数： 1 ** 3 + 5 ** 3 + 3 ** 3 == 153
# 这个三位数各个位数的立方之和等于它本身。
# 153\370\371\407
num = 370
gw = num % 10
sw = num // 10 % 10
bw = num // 100
if gw ** 3 + sw ** 3 + bw ** 3 == num:
    print(num, '是水仙花数')