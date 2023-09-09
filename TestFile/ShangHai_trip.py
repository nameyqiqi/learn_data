import mysql.connector
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
# 创建数据库对象
db = mysql.connector.connect(
    # 端口默认localhost 代表本地
    host="localhost",
    # 用户名
    user='root',
    # 密码
    passwd='123456',
    # 数据库名
    database='shanghai_trip'
)
# 创建cursor对象操作数据库
cursor = db.cursor()
# 创建名为shanghai_trip的数据库
#cursor.execute("CREATE DATABASE shanghai_trip")
#使用shanghai_trips数据库
#cursor.execute("Use shanghai_trip")
# 创建字段trip的表
#cursor.execute("CREATE TABLE trip (name VARCHAR(25), adress VARCHAR(50),"
#                       "mark VARCHAR(10),remark_on VARCHAR(1500),remark_it VARCHAR(25) )")
# 提交至数据库
db.commit()
for i in tqdm(range(13, 51),'上海旅游'): #i最大值可以是2330
    url = 'https://you.ctrip.com/sight/Shanghai2/s0-p' + str(i) + '.html#sightname'
    wb = webdriver.Chrome()
    wb.get(url)
    time.sleep(2)
    # 景点div
    all_div = wb.find_elements(By.CSS_SELECTOR, '.list_mod2')
    # print(all_div) 打印正常
    for i in all_div:
        # 地名
        name = i.find_element(By.CSS_SELECTOR, '.rdetailbox>dl>dt>a').text
        # 地址
        adress = i.find_element(By.CSS_SELECTOR, '.rdetailbox>dl>dd').text
        try:
            # hotmark
            mark = i.find_element(By.CSS_SELECTOR, 'b[class="hot_score_number"]').text
            # 点评
            remark_on = i.find_element(By.CSS_SELECTOR, '.bottomcomment').text
            # 点评条数
            remark_it = i.find_element(By.CSS_SELECTOR, '.rdetailbox>ul>li>a[rel="nofollow"]').text
        except:
            #无内容给空
            mark='null'
            remark_on='null'
            remark_it='null'
        #print(name, adress, mark, remark_on, reamke_it)
        time.sleep(1.5)
        # 数据库相关操作
        sql_insert = "INSERT INTO trip (name, adress,mark,remark_on,remark_it) VALUES (%s,%s,%s,%s,%s)"
        value = (name, adress,mark,remark_on,remark_it)
        try:
            cursor.execute(sql_insert, value)
            db.commit()
        except:
            db.rollback()
        time.sleep(1)
# 关闭数据库
db.close()

