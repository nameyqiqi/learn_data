from selenium import webdriver
import time
# 打开浏览器
brower = webdriver.Chrome()
# 请求url
brower.get('http://taobao.com')
time.sleep(1)
# 请求jd
brower.get('http://jd.com')
time.sleep(1)
#请求豆瓣
brower.get('http://movie.douban.com')
time.sleep(1)
#回退
brower.back()
#前进
brower.forward()
#刷新
brower.refresh()