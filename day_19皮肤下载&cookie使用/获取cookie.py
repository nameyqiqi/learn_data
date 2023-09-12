# 1.进行登录 完全手动 获取cookie信息 失效性
# 2.自动的登录 携带cookie信息
# json数据 数据格式 常用的网络传输
# dump 将程序的对象[列表or字典]写到文件 变成字符串
# load 将文件的内容 读取到程序中 解析成程序的对象[列表or字典]
from  selenium import webdriver
import  time
import json
browser = webdriver.Chrome()
url= 'https://mail.qq.com/'
browser.get(url)
time.sleep(20)
# 获取cookie信息
all_cookie=browser.get_cookies()

#写入文件
with open('./qq.json','w',encoding='utf-8') as f:
    json.dump(all_cookie,f)

