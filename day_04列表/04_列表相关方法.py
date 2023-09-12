#1. max/min :获取最大、最小值
numlist=[10,15,0,6,9]
max_num=max(numlist)
print(max_num)

#2. sum:计算数字列表（一个列表所有元素都是数字）中所有数字的和
print(sum(numlist))

#3. index:查找某个元素第一次出现的位置，找不到报错
try:
    result= numlist.index(100)
    print(result)
except:
    print('cwcr')