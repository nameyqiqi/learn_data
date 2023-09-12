'''
1. https://pvp.qq.com/web201605/wallpaper.shtml
2. 鼠标移动到 游戏资料  点击 英雄资料
3. 窗口切换
4. 获取所有的英雄的名字
--------------------------------------------------------
5. 点击每一个英雄  新窗口
6. 获取每一个英雄的所有的皮肤  所有的图片的链接   链接不全  字符串的拼接  https:
7. wget 下载 保存的格式  名字-皮肤名字.jpg
'''
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import wget
import os

# 创建文件夹
if not(os.path.exists('./王者荣耀')):
    os.mkdir('./王者荣耀')

# 1. 驱动打开浏览器
browser= webdriver.Chrome()
# 2. 发送请求
url = 'https://pvp.qq.com/web201605/wallpaper.shtml'
browser.get(url)
# 3. 时间休眠等待数据加载
time.sleep(2)
# 4. 创建动作链对象
action = ActionChains(browser)
# 5. 定位 游戏资料 并把鼠标移动上去
game_info_tag = browser.find_element(by=By.CSS_SELECTOR,value='a[title="游戏资料"]')
action.move_to_element(game_info_tag).perform()
time.sleep(0.5)
# 6. 定位英雄资料  并执行点击操作
hero_info = browser.find_element(by=By.CSS_SELECTOR,value='a[title="英雄资料"]')
action.click(hero_info).perform()
time.sleep(1)
# 7. 把窗口切换到新打开的窗口
browser.switch_to.window(browser.window_handles[-1])
# 8. 获取所有的英雄
all_hero = browser.find_elements(by=By.CSS_SELECTOR,value='ul[class="herolist clearfix"]>li')
for hero in all_hero:
    a_tag = hero.find_element(by=By.CSS_SELECTOR,value='a')
    # 9. 遍历每一个英雄 获取英雄的名字  并找到 点击位置  执行点击操作  切换新窗口 最后一个
    hero_name = a_tag.text
    action.click(a_tag).perform()
    time.sleep(0.5)
    browser.switch_to.window(browser.window_handles[-1])
    # 10 获取所有的皮肤的链接 并进行下载
    all_li = browser.find_elements(by=By.CSS_SELECTOR,value='ul[data-imgname]>li')
    # 11 每一个英雄的皮肤下载完成之后 关闭 英雄的页面
    for li in all_li:
        skin_name = li.find_element(by=By.CSS_SELECTOR,value='img').get_attribute('data-title')
        skin_url = li.find_element(by=By.CSS_SELECTOR,value='img').get_attribute('data-imgname')
        skin_url = 'https:' + skin_url
        print(skin_name,skin_url)
        wget.download(skin_url,f'./王者荣耀/{hero_name}-{skin_name}.jpg')
    browser.close()
    # 12.回到具有所有英雄的页面  窗口切换  第二个  索引  1
    browser.switch_to.window(browser.window_handles[1])









