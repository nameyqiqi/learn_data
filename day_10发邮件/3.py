import openpyxl

# 1. 创建并打开文件
wb = openpyxl.Workbook()

ws = wb['Sheet']

wb.save('mm.xlsx')