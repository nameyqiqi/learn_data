import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import wget
#如果文件不存在创建文件夹
if not os.path.exists('bqb'):
    os.mkdir('bqb')
driver=webdriver.Chrome()
driver.get('http://www.dbbqb.com/')
time.sleep(2)
# 填入输入框
input_tag=(driver.find_element(By.XPATH,'//*[@id="searchInput"]')).send_keys('蜡笔小新')
# 点击搜索
search_tag=driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/button[1]')
time.sleep(5)
#图片链接
img_tag=driver.find_elements(By.CSS_SELECTOR,'.lazyload-wrapper>a>img')

