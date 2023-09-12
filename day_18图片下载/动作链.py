from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 驱动打开浏览器
browser =webdriver.Chrome()
# 请求url
browser.get('https://pvp.qq.com/')
# 数据休眠等待数据加载
time.sleep(3)
# 引入动态链
action = ActionChains(browser)
# 定位游戏资料 ， 把鼠标移动上去
game_info = browser.find_element(By.CSS_SELECTOR,'a[title="游戏资料"]')
action.move_to_element(game_info).perform()
# 定位游戏壁纸 点击
game_img= browser.find_element(By.CSS_SELECTOR,value='a[title="游戏壁纸"]')
action.click(game_img).perform()
time.sleep(10)