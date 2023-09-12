#for-in循环是循环次数确定的循环
# while循环是循环次数不确定的循环
# 一.语法
'''
while 条件：
    代码块
'''
#while 循环开始执行前，先判断条件是否为真，如果条件为真循环执行，代码块执行；
#一次性循环完成，再回到while继续判断条件为真，再决定循环是否继续。

# 二、案例：
# 猜数字游戏，从1-100之间随机给定一个数字，一群人猜，
# 猜对的人接受惩罚，猜数字游戏停止；猜错了，缩小范围。
import random

# random模块（包）：python官方提供的实现了各种随机功能的模块
# randint:从指定范围（闭区间）随机产生一个整数

number = random.randint(1, 100)
# print(number)
flag = True
while flag:
    num = int(input('请输入你猜的数字：'))
    if num > number:
        print('再小一点')
    elif num < number:
        print('再大一点')
    else:
        print('恭喜猜对了，请接收惩罚！')
        # 当猜对了，要让循环结束，只需要手动让条件不成立
        flag = False