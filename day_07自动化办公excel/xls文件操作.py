# 方法一: 使用工具wps，excel打开这个文件，另存为的方式改为xlsx，再使用openpyxl
# 方法二： 使用xlrd(只读)与xlwt(只写)结合，读和写xls文件。
# 命令安装
# pip install xlrd
# pip install xlwt

# 案例： 实现注册功能（写）
import xlwt
import xlrd
# 1. 新建一个文件
# Workbook() 不给路径创建 给了打开已存在的
# openpyxl的Workbook()是没用路径参数
# openpyxl创建会生成一个为sheet的工作表
# 【 xlwt创建的工作簿 不会生成一个工作表 】
wb=xlwt.Workbook()
ws=wb.add_sheet('用户信息')
#向单元格写入数据
# 1.写入表头
col_name=['账号','密码']
# xlwt,以及xlrd认为行从0开始
for i in range(0,len(col_name)):
    #工作表.write(行号，列号，需要写入的内容)
    ws.write(0,i,col_name[i])

 # 2.写入账号，密码
user_name=input("please input name:")
pass_word=input("please input password:")
ws.write(1,0,user_name)
ws.write(1,1,pass_word)
wb.save('./数据集/用户信息.xls')