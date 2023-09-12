import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

#for page in tqdm(range(1, 11), desc='中国新闻网爬虫'):
    # print(f'-----------第{page}页-----------')
    # 中国新闻网即时新闻精选链接
rl ='https://www.chinanews.com/scroll-news/2023/0803/news.shtml'
URL = rl
print(URL)
    # 伪装爬虫，获取User-Agent
Headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    # 向网站所在服务器发送请求，拿到响应结果
response = requests.get(url=rl, headers=Headers)
    # 如果网页发生乱码，添加这一句代码,将响应结果中的内容转码
response.encoding = 'utf-8'
    # 判断状态码是否为200
result = response.text if response.status_code == 200 else response.status_code
    # print(result)

    # 使用bs4模块将网页源代码转为树结构
soup = BeautifulSoup(result, 'html.parser')
    # print(soup)
    # 按照网页结构（树结构）从外到内查询、提取数据
    # 先提取出所有新闻所在的li标签
liList = soup.find_all("a")
print(liList, len(liList))
