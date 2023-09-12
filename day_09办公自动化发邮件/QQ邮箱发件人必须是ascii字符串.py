# 将汉字改为base64
import base64
import smtplib
from email.mime.text import MIMEText
# base64 能把二进制数据中字节串转为base64形式

name ='王二麻子'
# 1.字符串是人看的 字节串是给机器看的
byte_str = name.encode('utf-8')
print(byte_str)
# 字节串明显的标志， 在字符串基础上开头多一个b

# 2. 将字节串改为base64形式
base_str=base64.b64encode(byte_str)
print(base_str)

# 3.qq邮箱要求base64数据不是二进制形式，是base64的字符串形式
# 把base64二进制形式转为base64字符串形式
result=base_str.decode('utf-8')
print(result)

# 4.构造qq邮箱完整发件人
str_1='=?utf-8?B?'+result+'=?='+' <314584328@qq.com>'
print(str_1)