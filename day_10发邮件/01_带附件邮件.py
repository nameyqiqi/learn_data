# 3.正文，附件分别是一封邮件的组成部分
# 借助MIMEMultipart
# Multipart: 多部分

# 1. 借助MIMEMultipart进行邮件多部分的容器
from email.mime.multipart import MIMEMultipart
# 2. 借助MIMEText分别构造正文和附件
from  email.mime.text import MIMEText

# 3.如果邮件有附件，不能使用MIMEText，需要使用MIMEMultipart来存储各部分
msg = MIMEMultipart()

# 4.构造正文
content = 'this is a test'
msg_content = MIMEText(content,'plain','utf-8')

# 5.将正文添加到邮件中
msg.attach(msg_content)

# 6. 发件人，收件人，抄送人 正常写
msg['From'] = 'olaf <314584328@qq.com>'
msg['To'] = 'olaf <314584328@qq.com>'
msg['Subject'] = 'this is a text '

# 7. 添加附件
# a. 先把附件以二进制读出来
f = open('文件集/1.jpg', 'rb')
photo_data = f.read()
f.close()
# b -> bytes --> 字节
# 为什么数据传输要用二进制：字节算是最小单位
# 网络传输数据承载能力有限，发邮件时，有可能还在进行其他工作，
# 网络传输要求传输的数据必须以字节（二进制）传输

# b. 将附件添加到邮件中
# 先将附件包装成一个整体
# 附件的类型就是base64
file_1 = MIMEText(photo_data, 'base64', 'utf-8')
# 告知邮箱服务器这是一个附件
file_1['Content-Type'] = 'application/octet-stream'
# 在附件中以xxx名字的文件显示这个附件
# Content-Disposition ---> 想办法让网络支持
# attachment --> 附件
file_1.add_header('Content-Disposition', 'attachment', filename='test.png')
msg.attach(file_1)

f1 = open('文件集/1.txt', 'rb')
te1 = f1.read()
f.close()
file_2 = MIMEText(te1,'base64','utf-8')
file_2['Content-Type'] = 'application/octet-stream'
file_2.add_header('Content-Disposition', 'attachment', filename='te.txt')
msg.attach(file_2)

import smtplib

#发件人账号
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

server.sendmail(username,['314584328@qq.com'],msg.as_string())
