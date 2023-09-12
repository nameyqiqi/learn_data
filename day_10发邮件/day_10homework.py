from  pypdf import PdfWriter,PdfReader,Transformation
import random
import openpyxl
import smtplib #邮箱登录
from email.mime.multipart import MIMEMultipart #带附件 容器模块
from  email.mime.text import MIMEText #构造文件正文

r_1 = PdfReader('./文件集/绝密文件.pdf')
r_2 = PdfReader('./文件集/water.pdf')
w_1=PdfWriter()
for i in range(0,len(r_1.pages)):
    page=r_1.pages[i]
    page.merge_transformed_page(r_2.pages[0], Transformation())
    w_1.add_page(page)
# 5.保存
with open('./文件集/secret.pdf', 'wb') as f:
    w_1.write(f)

# 加密操作
r_3 = PdfReader('./文件集/secret.pdf')
w_2 = PdfWriter()
for i in r_3.pages:
    w_2.add_page(i)
#for j in range(4,5):
enc=random.randrange(1000,9999)
print(enc)
w_2.encrypt(str(enc))

# 写入excel
wb = openpyxl.Workbook()
ws = wb['Sheet']
ws.cell(1,1).value=enc
wb.save('./文件集/mm.xlsx')
# 保存
with open('./文件集/secret_1.pdf','wb') as f:
    w_2.write(f)

# 发邮件
username='314584328@qq.com'
#发送人授权码
pwd = 'smgphjfkttwkbgfg'
# 连接邮箱服务器（qq邮箱为例）
server = smtplib.SMTP_SSL('smtp.qq.com',465)
#联通成功不报错
print(f'邮箱服务联通结果{server}')
#登录
result=server.login(username,pwd)
print(f'登录结果：{result}')
msg = MIMEMultipart() #创建msg带附件容器

content = 'asdfghjk' #正文
msg_content = MIMEText(content,'plain','utf-8')
msg['From'] = 'olaf <314584328@qq.com>'
msg['To'] = 'TeacherFu <1766935706@qq.com>'
msg['Subject'] = 'aoaoGu_homework '
f = open('文件集/secret_1.pdf', 'rb')
photo_data = f.read()
f.close()

file_1 = MIMEText(photo_data, 'base64', 'utf-8')
# 告知邮箱服务器这是一个附件
file_1['Content-Type'] = 'application/octet-stream'
file_1.add_header('Content-Disposition', 'attachment', filename='test.pdf')
msg.attach(file_1)

f1 = open('文件集/mm.xlsx', 'rb')
te1 = f1.read()
f.close()
file_2 = MIMEText(te1,'base64','utf-8')
file_2['Content-Type'] = 'application/octet-stream'
file_2.add_header('Content-Disposition', 'attachment', filename='mm_1.xlsx')
msg.attach(file_2)
server.sendmail(username,['314584328@qq.com'],msg.as_string())
