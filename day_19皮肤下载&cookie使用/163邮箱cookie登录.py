from selenium import webdriver
import time
import json

from selenium.webdriver.common.by import By

#创建浏览器对象
browser=webdriver.Chrome()
#请求地址
url='https://mail.163.com/'
browser.get(url)
time.sleep(1)
#读取cookie
with open('./pf/163cookie.json','r',encoding='utf-8') as f:
    all_cookie=json.load(f)

#遍历cookie 添加到浏览器
for cookie in all_cookie:
    browser.add_cookie(cookie)
#刷新页面
browser.refresh()
time.sleep(2)
#点击写信
w_tag=browser.find_element(By.CSS_SELECTOR,'.js-component-component.ra0.mD0').click()
time.sleep(2)

#点击收件人 输入内容
s_tag=browser.find_element(By.CSS_SELECTOR,'input[aria-label="收件人地址输入框，请输入邮件地址，多人时地址请以分号隔开"]')
s_tag.send_keys('314584328@qq.com')
time.sleep(2)
#点击主题 添加内容
title_tag=browser.find_element(By.CSS_SELECTOR,'div[aria-label="邮件主题输入框，请输入邮件主题"]>input')
title_tag.send_keys('this is a test')
time.sleep(2)
#定位到内嵌窗口
frame1=browser.find_element(By.CSS_SELECTOR,'.APP-editor-iframe')
browser.switch_to.frame(frame1)
browser.find_element(By.CSS_SELECTOR,'p[style="margin:0;"]').send_keys("hello 你好")
time.sleep(5)
#回到当前窗口
browser.switch_to.default_content()
#点击提交
browser.find_element(By.CSS_SELECTOR,'.nui-mainBtn-hasIcon').click()



