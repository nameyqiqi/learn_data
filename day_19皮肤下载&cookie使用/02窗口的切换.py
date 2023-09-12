from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# 1. 驱动打开浏览器
browser = webdriver.Chrome()
# 2. 请求url
url = 'https://lol.qq.com/main.shtml'
browser.get(url)
# 3. 等待数据加载  时间休眠
time.sleep(2)
# 创建鼠标对象
action = ActionChains(browser)
# 4. 鼠标移动到 游戏资料标签   1） 定位到游戏资料标签  2）鼠标的移动
game_info_tag = browser.find_element(by=By.CSS_SELECTOR,value='#J_headNav>li:first-child')
action.move_to_element(game_info_tag).perform()
time.sleep(3)
# 5. 定位资料库  并执行点击  休眠
info_cu = browser.find_element(by=By.CSS_SELECTOR,value='#J_headNavSub > li:nth-child(1) > a:nth-child(3)')
action.click(info_cu).perform()
time.sleep(2)
#切换窗口
browser.switch_to.window(browser.window_handles[-1])
# 6. 获取所有的英雄的名字
all_heros = browser.find_elements(by=By.CSS_SELECTOR,value='.hero-list>li')

# 7. 关闭浏览器
browser.close()

