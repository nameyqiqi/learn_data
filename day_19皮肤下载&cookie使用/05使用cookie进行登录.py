# 1. 进行登录  完全手动   获取 cookie 信息   失效性
# 2. 自动的登陆   携带 cookie 信息
# json数据   数据格式  常用与网络传输
# dump  将程序中的对象【列表或者字典】写入到文件  变成的 字符串
# load  将文件中的内容 读取到程序中 解析成程序中的对象 【列表或者字典】
from selenium import webdriver
import time
import json

browser = webdriver.Chrome()
url='https://mail.qq.com/'
browser.get(url)
time.sleep(30)
# 获取cookie信息
all_cookie = browser.get_cookies()
# 把cookie信息保存到文件
with open('./qq.json','w',encoding='utf-8') as fp:
    json.dump(all_cookie,fp)



