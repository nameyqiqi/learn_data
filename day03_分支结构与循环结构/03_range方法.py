#range(start and step)
#1. start :起点 end终点 组成了[start,end)的区间
#2. range 中根据start，end，step生成有规律的整数序列
#3. step可以不写 默认为1； start也可以不写 ，表示从0开始
#4. 如果step写了，start必须写；如果step不写 start也可以不写
#5. 下一次获取数据= 本次获取数据 + step
#6. step必须为整数，如果step>=1, start<end; 如果step<=-1，start>end.

for i in range(1, 6, 2):
    print(i)
print('**************')
for i in range(1, -1, -1):
    print(i)
print('**************')
for i in range(3):
    print(i)
print('**************')
for i in range(0, 10, 1):
    print(i)


# 二、练习
# 不使用range的高级方法，求出100以内所有偶数
for i in range(0, 101):
    if i % 2 == 0:
        print(i, '是偶数')

for j in range(0, 101, 2):
    print(j, '是偶数')


# 三、len():查看容器中元素个数（容器的长度）
print(len(range(0, 101, 2)))
