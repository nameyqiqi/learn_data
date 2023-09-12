# 1. replace:替代, 如果某些符号没有，自动跳过
# 王者荣耀不文明用语屏蔽。
sample_txt = ['垃圾', '辣鸡', '草泥马', '滚']
content = '你可真菜，你个小垃圾，快滚回家'
for i in sample_txt:
    # 针对content做替换，是copy了content的内容做替换，没修改原数据
    content = content.replace(i, '*' * len(i))
print(content)

# 用法一：字符串.replace(old_str, new_str)
# 使用new_str将字符串中的old_str全部替换。

# 用法二：字符串.replace(old_str, new_str, count)
# 使用new_str将字符串中的old_str替换指定的count次。


# 2. join:拼接，将字符串容器（容器中所有元素都是字符串）按照指定符号进行元素拼接
str_list = ['1', '2', '3', '4']
result = '+'.join(str_list)
print(result)

# 3. str(): 将数据转为字符串，所有数据都可以转为字符串
print(''.join([str(1), str(2), str(3)]))
print(len(str(9999)))

# 4. strip(): 可以将字符串头尾空白符号或指定的符号去掉。
# 如果不给strip指定符号，默认去除空白符号；如果指定了特殊符号，去除该符号。
str_1 = '   你是个   好人*    ****'
print(str_1)
print(str_1.strip())
print(str_1.strip('*'))

# replace:默认全局替换，strip指定替换头尾。

# 5. split:切割，按照指定符号对字符串进行切割，切割点之外的符号放入到列表中
# 如果切割点在开头或末尾，会切分出空白符号。
str_1 = '1,2,3,4,5,'
print(str_1.split(','))


# 计算房子的总价
# 2室1厅 | 400平 | 南 | 陆家嘴 | 20层 | 20000元/平
# 1. 使用split --> 指定切割 |
# 结果： ['2室1厅 ',' 400平 ',' 南 ',' 陆家嘴 ',' 20层'，‘ 20000元/平’]
# 2. 去除无关符号strip或者replace去掉 空格
# 结果： ['2室1厅','400平','南',' 陆家嘴','20层'， ‘20000元/平’]