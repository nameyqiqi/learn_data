#python操作pdf有很多模块：pypdf2，pypdf3，pypdf4
#pypdf正主，pypdf2\3\4分身。
#pypdf4上次更新是18年，3和2上次更新是22年，正主说pypdf2不会维护了，pypdf3不知道

from pypdf import PdfReader
#PdfReader('文件名')
re = PdfReader('./pdf合集/1.pdf')
#指定页面
first_page = re.pages[0]
#extract_text()提取文本方法
content=first_page.extract_text()
#使用 len方法能知道有多少页
for i in range(0,len(re.pages)):
    page=re.pages[i]
    content=page.extract_text()
    print(content)
#print(content)
