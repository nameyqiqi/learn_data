from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='123456',
    database='trip_db'
)
# #创建cursor对象操作数据库
# mycursor = db.cursor()
# import MySQLdb
#
# db = MySQLdb.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     database='trip_db'
# )
mycursor = db.cursor()

mycursor.execute("CREATE TABLE trip (name VARCHAR(25), adress VARCHAR(50),"
                     "mark VARCHAR(10),remark_on VARCHAR(1500),reamke_it VARCHAR(25) )")

for i in range(1, 51): #i最大值可以是2330
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
            reamke_it = i.find_element(By.CSS_SELECTOR, '.rdetailbox>ul>li>a[rel="nofollow"]').text
        except:
            mark='null'
            remark_on='null'
            reamke_it='null'
        #print(name, adress, mark, remark_on, reamke_it)

        '''
        东方明珠 上海市浦东新区陆家嘴世纪大道1号 9.1 
        遇见美景，快乐欣赏点评：东方明珠位于上海市浦东新区陆家嘴世纪大道1号，地处黄浦江畔，
        背拥陆家嘴现代化建筑群，与外滩隔江相望，是集都市观光、时尚餐饮、购物娱乐等多功能于一
        体的上海市标志性建筑之一。 
        (145535条点评)
        '''
        time.sleep(1.5)
        # 数据库相关操作
        sql_insert = "INSERT INTO trip (name, adress,mark,remark_on,reamke_it) VALUES (%s,%s,%s,%s,%s)"
        value = (name, adress,mark,remark_on,reamke_it)
        try:
            mycursor.execute(sql_insert, value)
            db.commit()
        except:
            db.rollback()
        time.sleep(1)
db.close()
