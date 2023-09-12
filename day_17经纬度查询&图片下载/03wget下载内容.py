#从互联网下载内容
import wget
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#驱动打开浏览器
brower=webdriver.Chrome()
#请求url
brower.get('https://pvp.qq.com/web201605/wallpaper.shtml')
#时间休眠等待数据加载
time.sleep(5)
all_img = brower.find_elements(By.CSS_SELECTOR,"#Work_List_Container_267733>div>img")
all_gqimg=brower.find_elements(By.CSS_SELECTOR,"#Work_List_Container_267733 > div > ul > li:nth-child(5)")
# 获取所有图片的img标签
#
# 遍历每一个的图片标签
for img in all_img:
    img_name = img.get_attribute('alt')
    img_src = img.get_attribute('src')
    print(img_name,img_src)
# wget.download(链接，位置)
    wget.download(img_src,f'./图片/{img_name}.jpg')

# 关闭浏览器
brower.close()