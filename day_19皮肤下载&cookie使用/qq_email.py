'https://mail.qq.com/'
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#创建浏览器对象
browser = webdriver.Chrome()
#请求地址
url='https://mail.qq.com/'
browser.get(url)
time.sleep(1)
#内嵌窗口
frame1=browser.find_element(By.XPATH,'//*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe')
browser.switch_to.frame(frame1)
frame2=browser.find_element(By.XPATH,'//*[@id="ptlogin_iframe"]')
browser.switch_to.frame(frame2)
time.sleep(1)
#点击密码登录
switcher_plogin=browser.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()
time.sleep(1)
#获取用户名输入框
user_tag=browser.find_element(By.XPATH,'//*[@id="u"]')
user_tag.click()
time.sleep(2)
user_tag.send_keys('314584328')
#获取密码框
password_tag=browser.find_element(By.XPATH,'//*[@id="p"]')
password_tag.send_keys('yqq0706..')
time.sleep(3)
#点击登录按钮 点击
login_tag=browser.find_element(By.XPATH,'//*[@id="login_button"]').click()
time.sleep(10)
