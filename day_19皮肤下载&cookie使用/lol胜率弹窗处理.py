# 易错点  每一次回到有所有英雄的页面 重新获取所有的英雄
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 1. 驱动打开浏览器
browser = webdriver.Chrome()
# 2. 请求url
browser.get('https://101.qq.com/#/hero')
# 3. 时间休眠等待数据加载
time.sleep(2)
# 4. 获取所有的英雄
all_heros = browser.find_elements(by=By.CSS_SELECTOR,value='.hero-list>li')
# 5. 遍历每一个英雄 获取英雄名字
for i in range(0,len(all_heros)):
    hero = all_heros[i]
    hero_name = hero.find_element(by=By.CSS_SELECTOR,value='.hero-name').text
    print(hero_name)
    # 6. 点击英雄  获取胜率
    a_tag = hero.find_element(by=By.CSS_SELECTOR,value='a').click()
    time.sleep(2)
    # 处理弹框
    ul = browser.find_element(By.CSS_SELECTOR,value='.info-list')
    if '胜率' in ul.text:
        win_text =browser.find_element(by=By.CSS_SELECTOR,value='.info-list>li:nth-child(3)>div').text
        print(win_text)
        # 7. 回退
        browser.back()
        time.sleep(1)
    else:
        bcak_list=browser.find_element(by=By.CSS_SELECTOR,value='.solid-s').click()
        all_heros = browser.find_elements(by=By.CSS_SELECTOR, value='.hero-list>li')
        time.sleep(1)
    # 8. 重新获取英雄
    all_heros = browser.find_elements(by=By.CSS_SELECTOR, value='.hero-list>li')

# 关闭浏览器
browser.close()






