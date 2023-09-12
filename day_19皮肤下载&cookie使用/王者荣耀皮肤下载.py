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
#创建文件夹
if not (os.path.exists('./pf')):
    os.mkdir('./pf')
# 1. 驱动打开浏览器
browser = webdriver.Chrome()
# 2. 请求url
url = 'https://pvp.qq.com/web201605/wallpaper.shtml'
browser.get(url)
# 3. 等待数据加载  时间休眠
time.sleep(1)
# 创建鼠标对象
action = ActionChains(browser)
# 4. 鼠标移动到 英雄资料标签   1） 定位到游戏资料标签  2）鼠标的移动
game_info_tag = browser.find_element(by=By.CSS_SELECTOR,value='#header > div.header-nav > div.header-inner > ul > li:nth-child(1) > a')
action.move_to_element(game_info_tag).perform()
time.sleep(1)
#点击游戏资料
hero_info=browser.find_element(By.XPATH,'//*[@id="header"]/div[1]/div[1]/ul/li[1]/a').click()
time.sleep(1)
#切换到英雄名字窗口
browser.switch_to.window(browser.window_handles[-1])
#获取所有英雄li
hero_names=browser.find_elements(By.CSS_SELECTOR,'body > div.wrapper > div > div > div.herolist-box > div.herolist-content > ul>li')
print(len(hero_names))
for i in hero_names:
    #点击每个英雄的窗口
    hero_a=i.find_element(By.CSS_SELECTOR,'a')
    name=hero_a.text
    print(name)
    hero_a.click()
    #browser.switch_to.window(browser.window_handles[-1])
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
    all_img_li=browser.find_elements(By.CSS_SELECTOR,'ul[data-imgname]>li')
    for j in all_img_li:
        src=j.find_element(By.CSS_SELECTOR,'img').get_attribute('src')
        pf_name=j.find_element(By.CSS_SELECTOR,'img').get_attribute('data-title')
        print(src,pf_name)
        wget.download(src,f'./pf/{pf_name}.jpg')
    browser.close()
    browser.switch_to.window(browser.window_handles[1])

