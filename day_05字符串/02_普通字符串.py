# ASCII码表  --> 最原始的电脑用的码表
# ASCII码表的拓展表Unicode码表（万国码）

# 1. 记范围
# 计算机不懂十进制，计算机规定使用二进制，计算机只能看懂0和1
# 符号A~Z : 65~90
# 符号a-z : 97~122
# 符号0~9 : 48~57
# 汉字范围 : 十六进制 \u4e00~\u9fa5
# 十六进制：0~9、A、B、C、D、E、F

# \u是十六进制的标志

# ord():将符号转为十进制, 一次转一个符号
# chr()：将十进制转为符号
# int():int方法默认将数据转整型，同时int还可以将其他进制转为十进制
print(ord('A'), chr(65))
print(int('4e00', 16), int('9fa5', 16))

# for i in range(19968, 40869 + 1):
#     print(chr(i), end='')


# 2. 字符串比较大小
print('二' > '三', ord('二'), ord('三'), ord('四'), ord('一'))
# 电脑操作系统同类型文件按名称排序以编码值做排序，发现一、二、三、四没有按照unicode编码排序，大概率因为在中国，需要遵守国内的规范。
# unicode编码 也是 utf-8编码， 中国有一个自主研发的编码gbk编码。
# Python使用的时UTF-8（unicode）

print('123' > '12b')
print([1, 2, 3, '4a'] > [1, 2, 3, 'ab'])
# 字符串比较大小比较的是编码值，
# 字符串也是比较第一对不相同元素的大小

# 3. 字符串也是有序容器（下标）
# 字符串的下标、切片与列表的下标、切片一模一样
string = 'abcde'
# c的下标：2、-3
# 语法：有序容器[下标]
print(string[2])
# 从string切出 ： ace
print(string[0::2])

# 字符串的长度
string1 ='abc123\t'
print(len(string1))
# 有特殊作用的转义字符长度为1，转义作用消失长度为几就是几

# 就近原则
str_1="'abc'de'"
print(str_1)

# \的使用
# \将特殊符号的作用取消掉
str_2='ab\\tcd'
print(str_2)

# 字符串的循环遍历
# 直接遍历
game ='王者荣耀'

for i in game:

    print(i)
# 间接遍历
for i in range(0,len(game)):
    print(i,game[i])

# 字符串的拼接（+）与重复（*）
game1='lol'
game1=game1*2
print(game1+game,game1)

print(ord('A'))

