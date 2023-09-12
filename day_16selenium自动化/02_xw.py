from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 打开浏览器
# 创建配置项对象
Options = webdriver.ChromeOptions()
# 设置selenium不自动关闭浏览器
Options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=Options)

browser.get('https://v.qq.com/')
time.sleep(2)
input_tag=browser.find_element(By.CSS_SELECTOR,'#keywords')
input_tag.send_keys('鹊刀门传奇')
# 组合键send_keys(Keys.Ctrl,'a') -->Ctrl+a
# 等价于input_tag.send_keys(Keys.ENTER)
button = browser.find_element(By.CSS_SELECTOR,'.intro-wrapper__icon')
button.click()
