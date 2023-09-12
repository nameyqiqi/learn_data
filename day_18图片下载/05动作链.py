from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# 1. 驱动打开浏览器
browser = webdriver.Chrome()
# 2.请求url
url = 'https://pvp.qq.com/'
browser.get(url)
# 3. 休眠等待数据加载
time.sleep(2)
# 引入动作链
action = ActionChains(browser)
# 4. 定位游戏资料 并把鼠标移动上去
game_info = browser.find_element(by=By.CSS_SELECTOR,value='a[title="游戏资料"]')
action.move_to_element(game_info).perform()
# 5. 定位游戏壁纸  并执行点击
game_img = browser.find_element(by=By.CSS_SELECTOR,value='a[title="游戏壁纸"]')
action.click(game_img).perform()
time.sleep(10)
# 6. 关闭浏览器
browser.close()