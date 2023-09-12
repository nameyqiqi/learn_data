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

# email模块
# MIMEText:构造没有附件的邮件的方法
from email.mime.text import MIMEText
#邮件包含发件人，收件人，主题，正文
#1.构造正文
content = '这是邮件里面显示内容'
#构建邮件（默认必须提供正文）
#MIMEText（邮件正文，邮件类型，编码方式）
#不包含附件的邮件对应的类型为plain
# utf-8 -->万国码unicode
msg = MIMEText(content,'plain','utf-8',)
# 给邮件消息添加:发送人，收件人，抄送人，主题
# 各种人的写法： 名字<邮箱地址> 部分邮箱列qq 要求 名字+空格+邮箱地址
# 如果多个各种人： 每个人用英文符号;隔开
msg['From'] = '=?utf-8?B?546L5LqM6bq75a2Q=?= <314584328@qq.com>'
msg['To'] = 'olaf <314584328@qq.com>;'
msg['Cc'] ='olaf <314584328@qq.com>'
msg['Subject'] = '今日干坏事'
#from： 发邮件； to：收件人 cc：抄送人； subject：主题

# 第三步发送
#借助已经联通，登录的服务发送
# sendmail（发件人，收件人，邮件消息字符串）
# 发件人必须保持登录账号一致
# 收件人：无论抄送人，密送人，收件人一律看作收邮件
while True:
    server.sendmail(username,['314584328@qq.com'],msg.as_string())
    print('send successful')