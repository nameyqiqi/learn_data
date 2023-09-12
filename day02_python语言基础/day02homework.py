#1.写出判断⼀个数是否能同时被2和5整除的条件语句, 并且打印对应的结果。
a=int(input("输入数："))
if a % 5 ==0 and a % 2 == 0:
    print('{0}能同时被2或5整除'.format(a))
else:
    print("{0}不能同时被2或5整除".format(a))

#2.写出判断⼀个数是否能够被2或者5整除，但是不能同时被2和5整除的条件语句， 并且打印对应。
b=int(input("输入数："))
#if (num_2 % 2 == 0 and num_2 % 5 != 0) or (num_2 % 2 != 0 and num_2 % 5 == 0):
if b % 5 ==0 or b% 2 == 0 :
    if b % 5 ==0 and b% 2 == 0 :
        print('{0}能被2或5整除：'.format(b))
    else:
        print('{0}不能被2和5同时整除：'.format(b))
else:
    print('{0}不能被2或5整除：'.format(b))



#3.假设今天的上课时间为15678秒，编程计算今天上课时间是多少⼩时，多少分钟，多少秒；以‘XX时XX分XX秒’的⽅式表⽰出来。
#例如：100秒表⽰成‘0时1分40秒’
total=15678
h=total // 3600
m=total % 3600 // 60
s=total  % 60
print("{0}时,{1}分,{2}秒".format(h,m,s))

#4.定义两个变量保存⼀个⼈的⾝⾼和体重，编程实现判断这个⼈的⾝材是否正常! 公式：体重(kg) / (⾝⾼(m)的平⽅) 在18.5 ~ 23.9之间属于正常。
#输出格式：是否正常：True / False
h =float(input("请输入身高cm："))
w =float(input("请输入体重kg："))
print(h/100)
bmi=w/(h/100**2)
if 18.5<=bmi<=23.9:
    print(True)
else:
    print(False)