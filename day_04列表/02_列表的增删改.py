# 例如：表格文件，一行等于一个列表，每一行的一个单元格等于一个列表中的一个元素。
# Python操作excel表格文件的中间介质可以是列表。
# 办公自动化。

# 一、列表（元素）的增删改
# 列表这个容器可以存放任意数据。
stu_info = []
# 1. 增加
# append：追加，在末尾添加
# insert：插入，指定位置添加元素
stu_info.append('Java')
stu_info.append('Python')
stu_info.insert(1, 'HTML')
stu_info.append(['张三', 18])
print(stu_info)

# 2.修改
# 语法：有序容器[下标] = 新的值
# 给张三改名为：张伟
# 逻辑：对数据来说从外层到内层一层层递进；对代码来说从左向右正常执行
(stu_info[-1])[0] = '张伟'
print(stu_info)

# 3. 删除操作
# remove:根据元素删除,一次只删除一个，如果某元素不存在，报错。
# del:通过下标删除元素, del 有序容器[下标]
stu_info.remove('Java')
del stu_info[-1]
print(stu_info)

# 练习：生成100个学生的学号，学号为2023001、2023002、2023003等，
# 将所有学生的学号存储到列表中， [[2023001], [2023002], [2023003], [2023004]]

stu = []
for stu_id in range(2023001, 2023101):
    # print([stu_id], type([stu_id]))
    stu.append([stu_id])
print(stu)