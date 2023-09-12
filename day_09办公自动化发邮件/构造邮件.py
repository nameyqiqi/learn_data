# email模块
# MIMEText:构造没有附件的邮件的方法
from email.mime.text import MIMEText
#邮件包含发件人，收件人，主题，正文
#1.构造正文
content = '这是个测试邮件'
#构建邮件（默认必须提供正文）
#MIMEText（邮件正文，邮件类型，编码方式）
#不包含附件的邮件对应的类型为plain
# utf-8 -->万国码unicode
msg = MIMEText(content,'plain','utf-8',)
# 给邮件消息添加:发送人，收件人，抄送人，主题
# 各种人的写法： 名字<邮箱地址>
# 如果多个各种人： 每个人用英文符号;隔开
msg['from'] = 'olaf<314584328@qq.com>'
msg['to'] = 'olaf<314584328@qq.com>;sara<2507587835@qq.com>'
msg['cc'] ='olaf<314584328@qq.com>'
msg['subject'] = '今日干坏事'
#from： 发邮件； to：收件人 cc：抄送人； subject：主题
