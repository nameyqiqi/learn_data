import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
# 打开浏览器
# 创建配置项对象
Options = webdriver.ChromeOptions()
# 设置selenium不自动关闭浏览器
Options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=Options)
browser.get('http://newstu.1000phone.net/login')
time.sleep(2)
# 账号输入
input_tag = browser.find_element(by=By.CSS_SELECTOR, value='.el-input__inner')
input_tag.send_keys('340321200107062459')
# 密码输入
password_tag=browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div/div[2]/div/input')
password_tag.send_keys('yqq0706..')
# 定位图片
image_tag=browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div/div[3]/img[1]')
ocr1 = ddddocr.DdddOcr(show_ad=False)
# 密码
code=ocr1.classification(image_tag.screenshot_as_png)
botton = browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div/div[3]/div/input')
time.sleep(2)
botton.send_keys(code)
send = browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div/div[5]/button/span')
send.click()
time.sleep(2)
#点击评价
pj_icon =browser.find_element(By.XPATH,'//*[@id="app"]/section/section/aside/div/div[2]/div[3]/ul/a[1]/li/span[1]')
pj_icon.click()
time.sleep(2)
#点击开始测评
start_icon =browser.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tr[2]/td[7]/a')
start_icon.click()
time.sleep(0.5)

#测评系列操作
for i in range(1,14):
    value = '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tbody[' + str(
        i) + ']/tr[2]/td/div/label[1]/span[2]'
    bott_c = browser.find_element(By.XPATH, value)
    bott_c.click()
    time.sleep(0.5)
#填写第14评价
val = '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tbody[14]/tr[2]/td/div/textarea'
bot = browser.find_element(By.XPATH, val)
bot.send_keys('  内容有趣生动 ')
time.sleep(2)
#填写第15评价
val1 = '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tbody[15]/tr[2]/td/div/textarea'
bot1 = browser.find_element(By.XPATH, val1)
bot1.send_keys(" 讲课内容有趣")
#点击提交
btn_4_16 = browser.find_element(by=By.XPATH,value='//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tr/td/button')
btn_4_16.click()
time.sleep(1)
if btn_4_16.click():
    #政务测评
    for i in range(1,8):
        value = '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tbody[' + str(
            i) + ']/tr[2]/td/div/label[1]/span[2]'
        bott_c = browser.find_element(By.XPATH, value)
        bott_c.click()
        time.sleep(0.5)
    #评价
    #填写第8评价
    val = '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tbody[8]/tr[2]/td/div/textarea'
    bot = browser.find_element(By.XPATH, val)
    bot.send_keys('  无 ')
    time.sleep(2)
    #填写第9评价
    val1 = '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tbody[9]/tr[2]/td/div/textarea'
    bot1 = browser.find_element(By.XPATH, val1)
    bot1.send_keys(" 无")
    #提交
    btn_4_17=browser.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/table/tr/td/button').click()

