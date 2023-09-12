from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#创建浏览器对象
browser = webdriver.Chrome()
#请求地址
url='https://mail.163.com/'
browser.get(url)
time.sleep(1)
frame1=browser.find_element(By.CSS_SELECTOR,'iframe[scrolling]')
browser.switch_to.frame(frame1)
time.sleep(1)
#输入账号
use_tag=browser.find_element(By.CSS_SELECTOR,'input[data-loginname="loginEmail"]').send_keys('18226403152')
time.sleep(1)
#输入密码
pass_tag=browser.find_element(By.CSS_SELECTOR,'.dlpwd').send_keys('yqq0706..')
#点击登录
login_tag=browser.find_element(By.XPATH,'//*[@id="dologin"]').click()
time.sleep(5)