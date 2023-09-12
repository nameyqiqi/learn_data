from  pypdf import  PdfWriter
file =['1.pdf','3.pdf']
# 1.创建新的空白pdf
w = PdfWriter()
# 2. pypdf提供了更简便的pdf拼接方式
for i in file:
    file_path='./pdf合集/'+i
    #空白的pdf中有一个append追加的方法，只需要提供需要拼接的文件名和路径
    w.append(file_path)
#3. 保存
with open('./pdf合集/pinjie.pdf','wb') as f:
    w.write(f)
