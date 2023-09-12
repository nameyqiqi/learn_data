from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json
#创建浏览器对象
browser = webdriver.Chrome()
#请求地址
url='https://mail.163.com/'
browser.get(url)
time.sleep(20)
all_cookie=browser.get_cookies()

#写入文件
with open('./pf/163cookie.json','w',encoding='utf-8') as f:
    json.dump(all_cookie,f)