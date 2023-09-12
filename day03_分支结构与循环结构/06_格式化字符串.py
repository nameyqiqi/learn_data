name = '李华'
age= 18
edu = '清华'
print(age,"age",name,"school",edu)

#一.旧式字符串格式化方法
# %i %s占位符， %i 对应的是整型（int --> integer) %s 对应的是字符串（str -->string）
string = '%iage%sschool%s'%(age,name,edu)
print(string)

#二.format方法
string2=('{}age{}school{}'.format(age,name,edu))
print(string2)

#三.f-string  f'{}{}{}'
string3=f'{age}age{name}school{edu}'
print(string3)
