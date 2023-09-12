from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 1.驱动打开浏览器
browser = webdriver.Chrome()
# 2. 发送请求
url = 'https://map.yanue.net/'
browser.get(url)
# 3. 时间休眠等待数据加载
time.sleep(2)
# 4. 定位清空输入按钮 并执行点击
# clear_tag = browser.find_element(by=By.CSS_SELECTOR,value='#clearLatLng')
# clear_tag.click()
# time.sleep(1)
# 5. 定位经纬度输入框  并输入内容
input_tag = browser.find_element(by=By.CSS_SELECTOR,value='#latLng')
# 清空
input_tag.clear()
input_tag.send_keys('115.2,32')
time.sleep(0.5)
# 6. 定位解析经纬度 按钮  并执行点击
button_tag = browser.find_element(by=By.CSS_SELECTOR,value='#toAddressBtn')
button_tag.click()
time.sleep(5)
# <div id="showResults">115.2,32：河南省信阳市潢川县<br></div>
# 7. 获取到解析内容
# 定位到包含内容的标签   内容为标签之间的文本数据
res = browser.find_element(by=By.CSS_SELECTOR,value='#showResults').text.split('：')[-1]
print(res)
# 8. 关闭浏览器
browser.close()




















