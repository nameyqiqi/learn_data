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