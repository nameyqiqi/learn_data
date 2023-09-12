#一.整型int
#1.浮点型可以转整型，直接把小数部分省掉
#2.布尔类型（True，False）可以转整型，True==1,Flase==0
#3.字符串可以转整型，去掉引号就是整数的字符串可以转整型：“22”
a=1.1
#type()：专门用于查看数据类型的方法
print(type(a),type(int(a)),int(a))#浮点转
print(int(True),int(False)) #bool类型
print('100',int('100'),type(int('100')))

#二.浮点型（float）
#1.整型转浮点型，整数后面加 .0
#2.布尔类型（True，False）可以浮点型，True==1.0,Flase==0.0
#3.字符串（文本）可以转浮点型，去掉引号就是数字的字符串可以转整型
print(float(1),float('1'),float('.1'))

#三.布尔类型（bool）
#1.在python中所有数据都能转布尔类型
#2. 0 0.0 None(空值) ，[](空列表) ()空元组 set()空集合 {}空字典 表示为False
#3 除了能转成False，其余都是True

print(bool(.00),bool([]),bool(''))
print(bool(0.1),bool([1,2]))