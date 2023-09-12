from pypdf import PdfWriter,PdfReader
# 1. 读取要加密的pdf
r_1=PdfReader('./pdf合集/1.pdf')

# 2. 加密是修改操作，必然要创建新的pdf
w_1= PdfWriter()

# 3. 将读到的pdf原封不动的转移到新的pdf
# 要一页一页转移
for i in r_1.pages:
    w_1.add_page(i)

# 4. 加密：encrypt
w_1.encrypt('1234')

# 5. 保存
with open('./pdf合集/jm1.pdf','wb') as f:
    w_1.write(f)

