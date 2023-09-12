# 文件的复制，粘贴
# 类似于在电脑上复制某个文件，粘贴到另外一个位置

# 告知如何读
f = open('./发邮件.py','rb')
result = f.read()

# 二.在某个位置粘贴
f_1 = open('./test.py','wb')
f_1.write(result)
f.close()