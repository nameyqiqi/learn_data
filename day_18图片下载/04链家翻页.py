from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 1. 驱动打开浏览器
browser = webdriver.Chrome()
# 2.发送请求
url = 'https://bj.lianjia.com/ershoufang/pg98/'
browser.get(url)
# 3.时间休眠等待数据加载
time.sleep(3)
# 窗口最大化
browser.maximize_window()
while True:
    # 4. 获取这一页的所有的房屋标签
    all_li = browser.find_elements(by=By.CSS_SELECTOR,value='.sellListContent>li')
    # 5. 遍历每一个房屋标签 获取的 名字
    for li in all_li:
        title = li.find_element(by=By.CSS_SELECTOR,value='div[class="info clear"]>.title>a').text
        print(title)
    # 6. 定位下一页 并执行点击
    # div 中的最后一个a标签  如果a标签中间的文本数据 为 下一页  代表 能点击    如果不是下一页 代表 当前页已经是最后一页   循环结束
    next_tag = browser.find_element(by=By.CSS_SELECTOR,value='div[class="page-box house-lst-page-box"]>a:last-child')
    if next_tag.text == '下一页':
        next_tag.click()
        time.sleep(3)
    else:
        break
# 7.关闭浏览器
browser.close()