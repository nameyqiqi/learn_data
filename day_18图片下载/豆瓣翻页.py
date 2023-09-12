from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#驱动打开浏览器
browser = webdriver.Chrome()
#加载指定url
browser.get('https://movie.douban.com/top250')
#时间休眠等待数据加载
time.sleep(3)
while True:
    #定位到这一页的所有电影信息 li标签
    all_li=browser.find_elements(By.CSS_SELECTOR,'.grid_view>li')
    #拿到每一页的电影信息
    for li in all_li:
        movie_name= li.find_element(By.CSS_SELECTOR,'.title').text
        print(movie_name)
    # 执行翻页操作
    try:
        next_tag=browser.find_element(By.CSS_SELECTOR,value='.next>a')
        next_tag.click()
        time.sleep(2)
    except:
        break


