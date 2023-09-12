from pypdf import PdfWriter, PdfReader
# 1.读取加密文件
ws_1=PdfReader('./pdf合集/jm1.pdf')

# 2.判断是否加密
if ws_1.is_encrypted:
    ws_1.decrypt('1234')
    print('解密成功')
else:
    print('文件未加密')

# 3.解密之后保存新的pdf
# PdfReader方法只能读，不能写
# PdfWriter方法有改权限
ws_2 =PdfWriter()
for i in ws_1.pages:
    ws_2.add_page(i)
with open('./pdf合集/jmcg.pdf','wb') as f:
    ws_2.write(f)