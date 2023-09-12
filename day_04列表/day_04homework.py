#已知⼀个队伍（列表），得到这个队伍的中间那个⼈。
names = ['⼩红', '⼩王', '⼩李', '⼩张', '⼩刚', '⼩华']
if len(names)%2==1:
    print(names[len(names)//2])
else:
    print(names[len(names)//2-1],names[len(names)//2])

#已知⼀个数字列表，输出所有奇数下标元素。
number = [1, 2, 3, 4, 5, 6]
for i in range(0,len(number)):
    if number[i] % 2==1:
        print('js：',number[i],i)

#已知⼀个数字列表，将其中所有的元素的值都乘2。
lb=[1,2,3]
lb1=[]
for i in range (0,len(lb)):
    lb1.append(lb[i]*2)  # lb[i] *= 2
print(lb1)               # print(lb[])

#学校举⾏运动会，问哪些同学参加了多个项⽬，找到并输出
football = ['张三', '李四', '王五', '赵六']
long_jump = ['张三', '王五']
set1=set(football)
set2=set(long_jump)
print(set1.intersection(set2))

#在⼀次歌唱⽐赛中，5位评委给歌⼿打了分数，现要求去掉⼀个最⾼分和⼀个最低
#分，请把最⾼分找到，然后删除，不能使⽤max⽅法。
list=[]
list1=[]
for ss in range(1,6):
    score=float(input('please give score:'))
    list.append(score)
    if len(list)==5:
       sorted(list)
       del list[-1]
       del list[0]

#数字组合：有四个数字：1、2、3、4，能组成多少个互不相同且⽆重复数字的三
#位数？各是多少？
num = (1, 2, 3, 4)

count = 0

for i in num:

    for j in num:

        for k in num:

            if i != j and i != k and j != k:

                count = count + 1

                print('result is : %d' % (i * 100 + j * 10 + k))

print('count is %d' % (count))

# 在期末考试中，考了数学、语⽂、英语、地理、历史、物理这些科⽬，现已经将
#每科⽬的第⼀名找到，问哪位同学获得第⼀名次数最多（不考虑同时多⼈获得第
#⼀名次数⼀样）。
names = ['⼩红', '⼩王', '⼩红', '⼩张', '⼩红', '⼩王']
# 先去重，查看有几个学生
new_name = []
for i in names:
    if i not in new_name:
        new_name.append(i)
print(new_name)
# 再获取每个学生获得第一的次数
max_count = 0
for i in new_name:
    Count = 0
    for j in names:
        if i == j:
            Count += 1
    # 次数进行比较
    if Count > max_count:
        max_count = Count
        name = i
print(name)


#判断⼀个数字是否是丑数
# 丑数定义把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但7、14不是，因为它们包含质因子7。）
n = eval(input("输入："))
while n % 2 == 0:
    n = n / 2
while n % 3 == 0:
    n = n / 3
while n % 5 == 0:
    n = n / 5
if n == 1:
    print('True')
else:
    print('False')


#A、B、C、D、E 五⼈在某天夜⾥合伙去捕⻥，到第⼆天凌晨时都疲惫不堪，于是
#各⾃找地⽅睡觉。⽇上三杆，A 第⼀个醒来，他将⻥分为五份，把多余的⼀条⻥
#扔掉，拿⾛⾃⼰的⼀份。 B 第⼆个醒来，也将⻥分为五份，把多余的⼀条⻥扔掉
#拿⾛⾃⼰的⼀份。 C、D、E依次醒来，也按同样的⽅法拿⻥。问他们⾄少捕了多
#少条⻥?
def five_fish(n,m):
    if n==1:
        return m
    else:
        return  five_fish(n-1,m)/0.8+1
x=int(input("shururenshu"))
y=x+1
while five_fish(x,y)!=int(five_fish(x,y)):
    y+=x
print("{}".format(five_fish(x,y)))

