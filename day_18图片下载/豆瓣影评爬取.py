from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#获取浏览器对象
browser= webdriver.Chrome()
#请求网址
browser.get('https://movie.douban.com/review/best/?start=0')
#时间休眠等待数据加载
time.sleep(1)
total_page=browser.find_element(By.CSS_SELECTOR,'#content > div > div.article > div.paginator > a:nth-child(6)').text
for i in range(1,int(total_page)+1):
    #获取所有的div
    all_mv = browser.find_elements(By.CSS_SELECTOR,'.review-list>div')
    #print(all_mv)
    for j in all_mv:
        content=j.find_element(By.CSS_SELECTOR,'.loaded hidden>main-bd>p')
        print(content)