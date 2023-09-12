# 实现登录操作

import xlrd

# 1. 打开文件：open_workbook
wb = xlrd.open_workbook('./数据集/用户信息.xls')
# 2. 指定工作表
# sheet_by_name():通过表名指定工作表
# sheet_by_index()：通过表的下标指定工作表
ws_1 = wb.sheet_by_name('用户信息')
ws_2 = wb.sheet_by_index(0)
print(ws_1 == ws_2, ws_1, ws_2)

# 3. 读取表格内的数据
# cell:一次读一格
# row:一次读一行
# col:一次读一列

# 在判断账号、密码之前先输入信息
username = input('请输入账号：')
password = input('请输入密码：')

# 使用col获取某一列，这一列拿到是个列表，列表中每个元素依旧是单元格
userinfo = ws_1.col(0)
print(userinfo)
# 结论：在操作表格时尽可能使用下标进行单元格的操作
for i in range(0, len(userinfo)):
    # 通过下标获取到某个元素，这个元素是一个单元格，使用value获取这个单元格的值
    # if分支借助了逻辑运算符的中断机制
    if username == userinfo[i].value and password == ws_1.cell(i, 1).value:
        # 如何找到这个账号与之匹配的密码？
        print('登陆成功')
        break

# # 在容器中成员运算
# print('admin' in userinfo)

# xlrd、xlwt不重要！！！！