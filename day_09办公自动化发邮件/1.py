import smtplib
from email.mime.text import MIMEText #导入无附件模块
username = '314584328@qq.com'
password = 'smgphjfkttwkbgfg'
server = smtplib.SMTP_SSL('smtp.qq.com',465) #协议 端口
result = server.login(username,password) # 发邮件用户
print(result)

content = 'this is a test'
msg = MIMEText(content,)