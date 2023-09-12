# 定义变量
a1 = 10
a2 = 20
print(a1, a2)

# 函数的写法
# 函数的作用：把可能重复操作的内容封装成函数，避免代码的重复性
# 封装成函数  在需要的地方进行调用
'''
语法  

def 函数名(未知数，可以有多个):
    函数的功能体 【实现的功能】
    return 返回值  
    
求两个数的和   未知数 两个数   函数的功能  求和   把结果返回  

'''


# 封装函数
def get_sum(a1, a2):
    # 函数的功能体  求和  求  a1  a2
    res = a1 + a2
    # 把结果返回  返回到调用位置
    return res


# 调用函数   函数名(实际的值)
m = get_sum(10, 20)
print(m)

n = get_sum(30, 50)
print(n)

print(get_sum(100, 200))

# 求1-100的和
s = 0
for i in range(1, 101):
    s += i
print(s)


# 封装一个函数  求 1到某个数的和
# 未知数  某个数  函数的功能体  求 1到这个数的和    返回值抛出
def get_1_num_sum(num):
    s = 0
    for i in range(1, num + 1):
        s += i
    # 循环结束之后  抛出结果
    return s


print(get_1_num_sum(100))
print(get_1_num_sum(50))
print(get_1_num_sum(1000))


# 求某个数的阶乘   1*2*3*4****某个数
# 未知数  某个数  函数的功能体 求阶乘    返回的结果  乘积
def get_fac(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    # 所有的数据都已经×到结果上  输出结果
    return res


print(get_fac(10))
print(get_fac(200))


# 封装一个函数 未知量有两个 如果前者大于后者 返回1  如果前者小于后者 返回-1  否则 返回0
def get_compare(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


# 打印1-10
for i in range(1, 11):
    print(i)

a = 1
while a < 11:
    print(a)
    a += 1
