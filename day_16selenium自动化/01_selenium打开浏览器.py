from optparse import Option

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 打开浏览器
# 创建配置项对象
Options = webdriver.ChromeOptions()
# 设置selenium不自动关闭浏览器
Options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=Options)

# 请求地址
browser.get('https://www.baidu.com/')
# 休眠2s
time.sleep(2)
# 定位输入框
# iput输入框 id='kw' id选择器进行定位 find_element一个 加s使用
input_tag = browser.find_element(by=By.CSS_SELECTOR,value='#kw')
# 向输入框传递数据
input_tag.send_keys('分手快乐')

# 点击输入按钮
button = browser.find_element(By.CSS_SELECTOR,'#su')
button.click()
time.sleep(3)


# 关闭浏览器
#browser.close()
