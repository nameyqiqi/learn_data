#列表的成员运算
#判断某个元素是否在列表中： in not in
# 成员运算结果为True，Flase
stu = ['zs','ls','ww',1]
print('zs'in stu)
print([1]in stu)
print(1 in stu)
#列表的比较大小
list1=[1,2,3]
list2=[1,2,4]
list3=[3,4]
#列表比较大小比较的是第一对不相同（下标相同，元素不同）元素的大小
print(list3>list2>list1)

#列表的循环遍历
#直接循环
for i in stu:
    print(i)

#间接循环
for i in range(0,len(stu)):
    print(i,stu[i])


na=input('need search:')
names=['zs','ls','ww','zl','xz','xh']
if na in names:
    for i in range(0,len(names)):
        if na == names[i]:
            print(names[i],i)
else:
    print('')
