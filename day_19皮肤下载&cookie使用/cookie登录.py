from selenium import webdriver
import time
import json
browser = webdriver.Chrome()
url= 'https://mail.qq.com/'
browser.get(url)

#读取cookie信息
with open('qq.json','r',encoding='utf-8') as f:
    all_cookie=json.load(f)
print(all_cookie)
for cookie in all_cookie:
    browser.add_cookie(cookie)

browser.refresh()
time.sleep(15)