# 1.读取为二进制与字符串的读
# with open ('./','rt'.encoding='utf-8') as f:
# 1. 使用rt（读字符串）结合utf-8编码打开文件
f=open('./文件的读取.py','rt',encoding='utf-8')

# 2. 从打开的文件中读内容
result=f.read()
print(result)

# 3.关闭操作
f.close()
#文件关闭不能再进行读写操作

# 以rb模式读取文件内容
f = open('./文件的读取.py','rb')
result=f.read()
print(result)
f.close()