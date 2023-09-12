from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import wget
import os

if not(os.path.exists('./王者荣耀高清图')):
    os.mkdir('./王者荣耀高清图')

# 1. 驱动打开浏览器
browser = webdriver.Chrome()
# 2. 请求url
browser.get('https://pvp.qq.com/web201605/wallpaper.shtml')
# 3. 时间休眠等待数据加载
time.sleep(5)
# 4. 获取的是 所有的图片的内容
all_div= browser.find_elements(by=By.CSS_SELECTOR,value='#Work_List_Container_267733>div')
# 图片的链接 高清   图片的名字
for div in all_div:
    img_name = div.find_element(by=By.CSS_SELECTOR,value='img').get_attribute('alt')
    img_src = div.find_element(by=By.CSS_SELECTOR,value='ul>li:nth-child(5)>a').get_attribute('href')
    wget.download(img_src,f'./王者荣耀高清图/{img_name}.jpg')
# 7. 关闭浏览器
browser.close()



